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
        # TODO: Implement recommendation logic
        return self.songs[:k]

    def explain_recommendation(self, user: UserProfile, song: Song) -> str:
        # TODO: Implement explanation logic
        return "Explanation placeholder"

def load_songs(csv_path: str) -> List[Dict]:
    """Load and parse songs from a CSV file, converting attributes to appropriate types."""
    import csv
    songs = []

    with open(csv_path, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            song = {
                'id': int(row['id']),
                'title': row['title'],
                'artist': row['artist'],
                'genre': row['genre'],
                'mood': row['mood'],
                'energy': float(row['energy']),
                'tempo_bpm': int(row['tempo_bpm']),
                'valence': float(row['valence']),
                'danceability': float(row['danceability']),
                'acousticness': float(row['acousticness'])
            }
            songs.append(song)

    return songs

def score_song(user_prefs: Dict, song: Dict) -> Tuple[float, List[str]]:
    """Calculate a score for a song based on how well it matches user preferences."""
    score = 0.0
    reasons = []

    # Genre match: 2 points
    if user_prefs.get('favorite_genre', '').lower() == song.get('genre', '').lower():
        score += 2.0
        reasons.append("genre match (+2.0)")

    # Mood match: 1 point
    if user_prefs.get('favorite_mood', '').lower() == song.get('mood', '').lower():
        score += 1.0
        reasons.append("mood match (+1.0)")

    # Energy: penalize or reward based on difference from target
    target_energy = user_prefs.get('target_energy', 0.5)
    song_energy = song.get('energy', 0.5)
    energy_diff = abs(target_energy - song_energy)

    if energy_diff > 1.0:
        score -= 1.0
        reasons.append("energy very far (-1.0)")
    elif 0.2 < energy_diff <= 1.0:
        reasons.append("energy somewhat off (0.0)")
    elif 0 <= energy_diff <= 0.2:
        score += 1.0
        reasons.append("energy close match (+1.0)")

    # Acousticness: reward if preference matches
    song_acousticness = song.get('acousticness', 0.0)
    user_likes_acoustic = user_prefs.get('likes_acoustic', False)

    if (song_acousticness > 0.5 and user_likes_acoustic) or (song_acousticness <= 0.5 and not user_likes_acoustic):
        score += 0.5
        reasons.append("acousticness match (+0.5)")

    return (score, reasons)

def recommend_songs(user_prefs: Dict, songs: List[Dict], k: int = 5) -> List[Tuple[Dict, float, str]]:
    """Score all songs and return the top k recommendations ranked by score."""
    # Score all songs and format explanations
    scored_songs = [
        (song, score, " | ".join(reasons))
        for song in songs
        for score, reasons in [score_song(user_prefs, song)]
    ]

    # Return top k sorted by score (highest first)
    return sorted(scored_songs, key=lambda x: x[1], reverse=True)[:k]
