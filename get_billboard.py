import billboard  # this is the external billboard.py library, not your file

def get_chart_id(lang_code: str) -> str:
    lc = lang_code.strip().lower()
    if lc in ("es", "spanish"):
        return "latin-songs"
    elif lc in ("fr", "french"):
        return "france-songs-hotw"
    elif lc in ("pt", "portuguese"):
        return "billboard-brasil-hot-100"
    else:
        return "hot-100"

def get_top_songs(lang_code: str):
    chart_id = get_chart_id(lang_code)
    chart = billboard.ChartData(chart_id)
    top_songs = []
    for entry in chart:
        top_songs.append({
            "rank": entry.rank,
            "title": entry.title,
            "artist": entry.artist
        })
    return {
        "chart": chart.title,
        "language": lang_code,
        "songs": top_songs
    }
