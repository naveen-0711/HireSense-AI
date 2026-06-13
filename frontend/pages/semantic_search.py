import streamlit as st
import sys
import os

sys.path.append(
    os.path.abspath(
        os.path.join(
            os.path.dirname(__file__),
            "..",
            ".."
        )
    )
)

from backend.services.embedding_service import (
    generate_embedding
)

from backend.services.chroma_service import (
    search_candidates
)

st.title("🔍 Semantic Candidate Search")

st.write(
    "Search candidates using natural language."
)

query = st.text_area(
    "Describe the candidate you are looking for",
    placeholder="""
Example:

Machine Learning Engineer with Python, Deep Learning,
TensorFlow, RAG and LLM experience
"""
)

if st.button("Search Candidates"):

    if not query.strip():

        st.warning(
            "Please enter a search query."
        )

    else:

        with st.spinner("Searching candidates..."):

            query_embedding = generate_embedding(
                query
            )

            results = search_candidates(
                query_embedding,
                top_k=10
            )

            candidate_count = len(
                results["ids"][0]
            )

            st.success(
                f"Found {candidate_count} candidates"
            )

            if candidate_count == 0:

                st.warning(
                    "No matching candidates found."
                )

            else:

                for i in range(candidate_count):

                    st.markdown("---")

                    candidate_name = (
                        results["metadatas"][0][i]
                        .get("name", "Unknown")
                    )

                    candidate_profile = (
                        results["documents"][0][i]
                    )

                    distance = (
                        results["distances"][0][i]
                    )

                    similarity = round(
                        (1 - distance) * 100,
                        2
                    )

                    similarity = max(  
                        0,
                        min(similarity, 100)
                    )

                    st.subheader(
                        candidate_name
                    )

                    st.metric(
                        "Match Score",
                        f"{similarity}%"
                    )

                    with st.expander(
                        "View Candidate Profile"
                    ):

                        st.write(
                            candidate_profile
                        )

                    st.caption(
                        f"Distance Score: {round(distance, 4)}"
                    )