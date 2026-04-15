# 🎵 Music Recommender Simulation

## Project Summary

This is an app that recommends songs. You give it your preferred genre, mood, and energy level, and it gives you back the best 5 options along with a little explanation of why each one was chosen.

---

## How The System Works

The system works with a score system, where each variable receives more points as it matches the user's preferences and less if it doesn't.

**Each Song has these features:**
- genre, mood, energy, tempo_bpm, valence, danceability, acousticness

**The UserProfile stores:**
- favorite_genre, favorite_mood, target_energy, likes_acoustic

**Algorithm Recipe:**
- +2.0 points if the song's genre matches the user's preferred genre
- +1.0 point if the song's mood matches
- Up to +1.0 point based on how close the song's energy is to the user's target (calculated as 1 - absolute difference)

The algorithm assigns a lot of weight if the song matches genre and mood, but very little if it only has energy closeness. This means a song from the "wrong" genre will rarely appear in the top results, even if it matches the user's energy and mood perfectly.

**Data flow:**

Input (User Preferences) → Process (score every song in the catalog) → Output (Top K ranked recommendations with explanations)

---

## Getting Started

### Setup

1. Create a virtual environment (optional but recommended):

   ```bash
   python -m venv .venv
   source .venv/bin/activate      # Mac or Linux
   .venv\Scripts\activate         # Windows
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Run the app:

   ```bash
   python -m src.main
   ```

### Running Tests

```bash
pytest
```

---

## Experiments You Tried

Three distinct user profiles were tested:

- **High-Energy Pop** → Sunrise City scored 3.92 (genre + mood + energy match)
- **Chill Lofi** → Library Rain scored 3.95 (genre + mood + energy match)
- **Intense Rock** → Storm Runner scored 3.96 (genre + mood + energy match)

The pattern was clear: the algorithm assigns a lot of weight when a song matches both genre and mood, but very little when it only has energy closeness. Songs from the "wrong" genre rarely appear in the top results, even if their mood and energy are a perfect fit. This revealed that genre is by far the dominant factor in the scoring system.

---

## Limitations and Risks

- The catalog only has 10 songs — it still needs to grow significantly
- The genre list is limited: no jazz, no reggaeton, no latin music, no classical
- The genre weight (2.0) dominates scoring — a great song in the wrong genre will almost never surface
- The system has no memory: it doesn't learn from what the user skips or repeats
- No collaborative filtering — it only looks at song attributes, not at what similar users enjoy

---

## Reflection

Read and complete `model_card.md`:

[**Model Card**](model_card.md)

Building this showed that what feels like "magic" in apps like Spotify is, at its core, a list of songs, some weights, and a sort. A simple system like this can actually work surprisingly well. I would imagine that more sophisticated algorithms like Spotify's have a lot more variables, but in principle, something very simple can work very well. The biggest surprise was seeing how much the genre weight dominated everything else — it made me think differently about how real recommenders might create filter bubbles without anyone intending it.