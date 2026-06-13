from backend.utils.supabase_client import supabase

result = supabase.table(
    "candidates"
).select("*").execute()

print(result)