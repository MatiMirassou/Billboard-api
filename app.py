from fastapi import FastAPI, Query
from get_billboard import get_top_songs  # ✅ updated import

app = FastAPI()

@app.get("/top-songs")
def fetch_top_songs(language: str = Query("en")):
    try:
        return get_top_songs(language)
    except Exception as e:
        return {"error": str(e)}
