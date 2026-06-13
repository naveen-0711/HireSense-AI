import streamlit as st
import fitz
import sys
import os
import zipfile
import io
import uuid

sys.path.append(
    os.path.abspath(
        os.path.join(
            os.path.dirname(__file__),
            "..",
            ".."
        )
    )
)

from backend.utils.gemini_parser import (
    parse_resume_with_gemini
)

from backend.services.candidate_service import (
    save_candidate
)

from backend.services.embedding_service import (
    generate_embedding
)

from backend.services.chroma_service import (
    store_candidate_embedding
)

from backend.services.duplicate_service import (
    check_duplicate
)

from backend.utils.resume_parser import (
    extract_email,
    extract_phone,
    extract_name,
    extract_skills
)

st.title("📄 Resume Analyzer")

uploaded_files = st.file_uploader(
    "Upload Resume(s)",
    type=["pdf"],
    accept_multiple_files=True
)

zip_file = st.file_uploader(
    "Upload ZIP Folder",
    type=["zip"]
)


def extract_text_from_pdf(pdf_file):

    text = ""

    pdf = fitz.open(
        stream=pdf_file.read(),
        filetype="pdf"
    )

    for page in pdf:
        text += page.get_text()

    return text


# -----------------------------
# ZIP Processing
# -----------------------------

if zip_file:

    with zipfile.ZipFile(
        io.BytesIO(zip_file.read()),
        "r"
    ) as zip_ref:

        pdf_files = [
            file
            for file in zip_ref.namelist()
            if file.endswith(".pdf")
        ]

        st.success(
            f"Found {len(pdf_files)} resumes"
        )

        for pdf_name in pdf_files:

            st.markdown("---")

            st.write(
                f"### Processing: {pdf_name}"
            )

            pdf_bytes = zip_ref.read(
                pdf_name
            )

            uploaded_pdf = io.BytesIO(
                pdf_bytes
            )

            text = extract_text_from_pdf(
                uploaded_pdf
            )

            with st.spinner(
                f"AI is analyzing {pdf_name}..."
            ):
                candidate = parse_resume_with_gemini(
                    text
                )

            candidate_profile = f"""
Skills:
{candidate.get("skills", [])}

Projects:
{candidate.get("projects", [])}

Experience:
{candidate.get("experience", [])}

Education:
{candidate.get("education", [])}

Certifications:
{candidate.get("certifications", [])}
"""

            embedding = generate_embedding(
                candidate_profile
            )

            is_duplicate, score = (
                check_duplicate(
                    embedding
                )
            )

            if is_duplicate:

                st.warning(
                    f"Duplicate Resume Detected ({score:.2f}%)"
                )

                continue

            save_candidate(
                candidate,
                text
            )

            candidate_id = str(uuid.uuid4())

            store_candidate_embedding(
                candidate_id=candidate_id,
                candidate_name=candidate.get(
                    "name",
                    "Unknown"
                ),
                resume_text=candidate_profile,
                embedding=embedding
            )

            st.success(
                f"{candidate.get('name', 'Unknown Candidate')} saved"
            )

            st.subheader(
                "🤖 AI Candidate Profile"
            )

            st.json(candidate)


# -----------------------------
# Multiple PDF Processing
# -----------------------------

if uploaded_files:

    for uploaded_file in uploaded_files:

        st.markdown("---")

        st.write(
            f"### Processing: {uploaded_file.name}"
        )

        text = extract_text_from_pdf(
            uploaded_file
        )

        with st.spinner(
            f"AI is analyzing {uploaded_file.name}..."
        ):
            candidate = parse_resume_with_gemini(
                text
            )

        candidate_profile = f"""
Skills:
{candidate.get("skills", [])}

Projects:
{candidate.get("projects", [])}

Experience:
{candidate.get("experience", [])}

Education:
{candidate.get("education", [])}

Certifications:
{candidate.get("certifications", [])}
"""

        embedding = generate_embedding(
            candidate_profile
        )

        is_duplicate, score = (
            check_duplicate(
                embedding
            )
        )

        if is_duplicate:

            st.warning(
                f"Duplicate Resume Detected ({score:.2f}%)"
            )

            continue

        save_candidate(
            candidate,
            text
        )

        candidate_id = str(uuid.uuid4())

        store_candidate_embedding(
            candidate_id=candidate_id,
            candidate_name=candidate.get(
                "name",
                "Unknown"
            ),
            resume_text=candidate_profile,
            embedding=embedding
        )

        st.success(
            f"{candidate.get('name', 'Unknown Candidate')} saved"
        )

        st.subheader(
            "🤖 AI Candidate Profile"
        )

        st.json(candidate)

        st.markdown("---")

        col1, col2 = st.columns(2)

        with col1:

            st.subheader("Extracted Details")

            st.write(
                f"**Name:** {extract_name(text)}"
            )

            st.write(
                f"**Email:** {extract_email(text)}"
            )

            st.write(
                f"**Phone:** {extract_phone(text)}"
            )

        with col2:

            st.subheader("Skills")

            skills = extract_skills(text)

            if skills:

                for skill in skills:
                    st.success(skill)

            else:

                st.warning(
                    "No skills found"
                )

        with st.expander(
            f"View Full Resume Text - {uploaded_file.name}"
        ):
            st.write(text)