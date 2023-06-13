from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import music_bubbles

app = FastAPI()

# CORS middleware to allow requests from any origin
app.add_middleware(
    CORSMiddleware,
    allow_methods=["GET"],
    allow_headers=["*"],
    allow_credentials=True,
)


@app.get("/canvas_coordinates")
async def canvas_coordinates(notes: str) -> list[dict]:
    notes_list = notes.split("-")
    return music_bubbles.parse_notes_list(notes_list, 1782, 1260)
