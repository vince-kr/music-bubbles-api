from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import music_bubbles

app = FastAPI()

# CORS middleware to allow requests from any origin
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["GET"],
)


@app.get("/canvas_coordinates")
async def canvas_coordinates(notes_list: str):
    notes_json = music_bubbles.parse_notes_list(notes_list)
    return {"notes": notes_json}
