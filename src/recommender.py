import csv
from typing import List, Dict, Tuple, Optional
from dataclasses import dataclass

@dataclass
class Song:
    """
    Represents a song and its attributes.
    Required by tests/test_recommender.py
    """
    id: int
    title: str
    artist: str
    genre: str
    mood: str
    energy: float
    tempo_bpm: float
    valence: float
    danceability: float
    acousticness: float

@dataclass
class UserProfile:
    """
    Represents a user's taste preferences.
    Required by tests/test_recommender.py
    """
    favorite_genre: str
    favorite_mood: str
    target_energy: float
    likes_acoustic: bool

class Recommender:
    """
    OOP implementation of the recommendation logic.
    Required by tests/test_recommender.py
    """
    def __init__(self, songs: List[Song]):
        self.songs = songs

    def recommend(self, user: UserProfile, k: int = 5) -> List[Song]:
        user_prefs: Dict = {
            "genre": user.favorite_genre,
            "mood": user.favorite_mood,
            "energy": user.target_energy,
        }

        scored: List[Tuple[Song, float]] = []
        for song in self.songs:
            song_dict = _song_to_dict(song)
            score, _reasons = score_song(user_prefs, song_dict)
            if user.likes_acoustic and song.acousticness > 0.7:
                score += 0.5
            scored.append((song, score))

        scored.sort(key=lambda item: item[1], reverse=True)
        return [song for song, _ in scored[:k]]

    def explain_recommendation(self, user: UserProfile, song: Song) -> str:
        user_prefs: Dict = {
            "genre": user.favorite_genre,
            "mood": user.favorite_mood,
            "energy": user.target_energy,
        }
        song_dict = _song_to_dict(song)
        score, reasons = score_song(user_prefs, song_dict)
        total = score
        if user.likes_acoustic and song.acousticness > 0.7:
            total += 0.5
            reasons = reasons + [
                "acoustic-friendly track matches your taste (+0.5)"
            ]
        parts = "; ".join(reasons) if reasons else "general fit with your profile"
        return (
            f"This song fits your profile (score {total:.2f}): {parts}."
        )

def _song_to_dict(song: Song) -> Dict:
    return {
        "id": song.id,
        "title": song.title,
        "artist": song.artist,
        "genre": song.genre,
        "mood": song.mood,
        "energy": song.energy,
        "tempo_bpm": song.tempo_bpm,
        "valence": song.valence,
        "danceability": song.danceability,
        "acousticness": song.acousticness,
    }


def load_songs(csv_path: str) -> List[Dict]:
    """
    Loads songs from a CSV file.
    Required by src/main.py
    """
    rows: List[Dict] = []
    with open(csv_path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            row["energy"] = float(row["energy"])
            row["valence"] = float(row["valence"])
            row["danceability"] = float(row["danceability"])
            row["acousticness"] = float(row["acousticness"])
            row["tempo_bpm"] = int(row["tempo_bpm"])
            rows.append(row)
    return rows


def score_song(user_prefs: Dict, song: Dict) -> Tuple[float, List[str]]:
    """
    Scores a single song against user preferences.
    Required by recommend_songs() and src/main.py
    """
    score = 0.0
    reasons: List[str] = []

    if song.get("genre") == user_prefs.get("genre"):
        score += 2.0
        reasons.append("genre match (+2.0)")

    if song.get("mood") == user_prefs.get("mood"):
        score += 1.0
        reasons.append("mood match (+1.0)")

    target_energy = float(user_prefs["energy"])
    song_energy = float(song["energy"])
    energy_points = 1.0 - abs(song_energy - target_energy)
    score += energy_points
    reasons.append(f"energy closeness (+{energy_points:.2f})")

    return score, reasons


def recommend_songs(user_prefs: Dict, songs: List[Dict], k: int = 5) -> List[Tuple[Dict, float, str]]:
    """
    Functional implementation of the recommendation logic.
    Required by src/main.py
    """
    ranked: List[Tuple[Dict, float, str]] = []
    for song in songs:
        score, reasons = score_song(user_prefs, song)
        explanation = "; ".join(reasons)
        ranked.append((song, score, explanation))

    ranked.sort(key=lambda item: item[1], reverse=True)
    return ranked[:k]
