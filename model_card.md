# 🎧 Model Card: Music Recommender Simulation

## 1. Model Name

VibeFinder 1.0

---

## 2. Intended Use

This recommender suggests songs from a small catalog based on a user's preferred genre, mood, and energy level. It is designed for learning and exploration — to understand how content-based filtering works in principle. It is not intended for real users or production use.

---

## 3. How the Model Works

The system works with a score system. Every song in the catalog gets evaluated against the user's preferences. A song earns more points the more it matches: genre is worth the most (+2.0), mood comes second (+1.0), and energy closeness adds up to +1.0 depending on how close the song's energy level is to what the user wants. The songs are then ranked by total score and the top results are returned with a plain-language explanation of why each was chosen.

---

## 4. Data

The catalog contains 10 songs in CSV format. Each song has: title, artist, genre, mood, energy, tempo_bpm, valence, danceability, and acousticness. The genres represented are pop, lofi, and rock. Moods include happy, chill, intense, and melancholic. The dataset is small and does not represent the full diversity of musical taste — genres like jazz, reggaeton, latin, and classical are completely absent.

---

## 5. Strengths

The system is transparent and explainable — every recommendation comes with a clear reason. It works well when the user's preferred genre and mood are both present in the catalog. For the three profiles tested (High-Energy Pop, Chill Lofi, Intense Rock), the top results matched intuition well.

---

## 6. Limitations and Bias

The genre weight dominates scoring. A song from the "wrong" genre will rarely appear in the top results even if its mood and energy are a perfect match for the user. The catalog still needs to grow — it only has 10 songs and is missing entire genres like jazz, reggaeton, and latin music. This creates a filter bubble: users whose taste falls outside the represented genres get poor recommendations. The system also has no memory — it doesn't learn from what the user skips or repeats.

---

## 7. Evaluation

Three user profiles were tested: High-Energy Pop, Chill Lofi, and Intense Rock. In every case, the top-scoring song had both a genre and mood match. Songs that only matched on energy clustered at the bottom of the list with scores under 1.0. This confirmed that genre is the strongest signal in the current scoring logic — which is a design choice that could disadvantage users whose favorite genre isn't well represented in the catalog.

---

## 8. Future Work

- The system needs to consider more variables like release year or beat/tempo ranges
- The catalog needs to grow significantly in both number of songs and genre diversity
- The most meaningful improvement would be adding the ability to learn from user behavior — what they skip, what they repeat, what they save — which is closer to how real recommenders like Spotify actually work


---

## 9. Personal Reflection

Building this showed that what feels like magic in apps like Spotify is, at its core, a list of songs, some weights, and a sort. I would imagine that more sophisticated algorithms have a lot more variables, but in principle, something very simple can work surprisingly well. The biggest learning moment was seeing how much the genre weight dominated everything else —it made me realize how easy it is for a simple algorithm to create bias without anyone intending it.