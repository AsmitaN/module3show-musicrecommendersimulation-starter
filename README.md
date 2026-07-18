# 🎵 Music Recommender Simulation

## Project Summary

In this project you will build and explain a small music recommender system.

Your goal is to:

- Represent songs and a user "taste profile" as data
- Design a scoring rule that turns that data into recommendations
- Evaluate what your system gets right and wrong
- Reflect on how this mirrors real world AI recommenders

Replace this paragraph with your own summary of what your version does.

---

## How The System Works

Explain your design in plain language.

Some prompts to answer:

- What features does each `Song` use in your system\
  genre, mood, energy, acousticness
- What information does your `UserProfile` store\
  favorite_genre: str\
  favorite_mood: str\
  target_energy: float\
  likes_acoustic: bool
- How does your `Recommender` compute a score for each song\
  The app compares the genre, mood, energy, and acousticness fields of each song in the CSV file against the corresponding inputs the user entered.\
  If the genres and moods match, two points and one point, respectively, will be added to the score. \
  If the song is acoustic and the user likes acoustic (acousticness must be > 0.5) or if the song is not acoustic and the user doesn't like acoustic, 0.5 points will be added. \
  If either of these values don't match, no points will be added.\
  If the song's energy is very far from the target energy (0.5 < difference < 1.0), 1 point will be deducted from the score. \
  If the song's energy is a little far from the target energy (0.2 < difference <= 0.5), no points will be added to the score. \
  If the song's energy is very close to the target energy (0 <= difference <= 0.2), 1 point will be added to the score.\
  Potential bias: This system might over-prioritize genre, ignoring great songs that match user's acousticness preferences.

- How do you choose which songs to recommend\
  I will suggest the three songs with the highest scores generated from the described algorithm.

You can include a simple diagram or bullet list if helpful.

---

## Getting Started

### Setup

1. Create a virtual environment (optional but recommended):

   ```bash
   python -m venv .venv
   source .venv/bin/activate      # Mac or Linux
   .venv\Scripts\activate         # Windows

2. Install dependencies

```bash
pip install -r requirements.txt
```

3. Run the app:

```bash
python -m src.main
```

### Running Tests

Run the starter tests with:

```bash
pytest
```

You can add more tests in `tests/test_recommender.py`.

---

## Sample Recommendation Output

Paste a sample of your recommender's output here as a text block so a reader can see what it produces:

```
Loaded songs: 18

User Profile: Genre=pop, Mood=happy, Energy value=0.8, Likes acoustic=False
Top recommendations:
1. Sunrise City
   Score: 4.5
   Reasons:
     • genre match (+2.0)
     • mood match (+1.0)
     • energy close match (+1.0)
     • acousticness match (+0.5)

2. Open Road
   Score: 4.0
   Reasons:
     • genre match (+2.0)
     • mood match (+1.0)
     • energy close match (+1.0)

3. Gym Hero
   Score: 3.5
   Reasons:
     • genre match (+2.0)
     • energy close match (+1.0)
     • acousticness match (+0.5)

4. Rooftop Lights
   Score: 2.5
   Reasons:
     • mood match (+1.0)
     • energy close match (+1.0)
     • acousticness match (+0.5)

5. Digital Sunrise
   Score: 2.5
   Reasons:
     • mood match (+1.0)
     • energy close match (+1.0)
     • acousticness match (+0.5)
```

**Screenshot or video** *(optional)*: <!-- Insert a screenshot or demo video link here -->

---

## Experiments You Tried

Use this section to document the experiments you ran. For example:

- What happened when you changed the weight on genre from 2.0 to 0.5
- What happened when you added tempo or valence to the score
- How did your system behave for different types of users
  ### High energy, sad mood
  ```
  Loaded songs: 18

  User Profile: Genre=lofi, Mood=sad, Energy value=0.85, Likes acoustic=True
  Top recommendations:
  1. Autumn Memories
    Score: 3.5
    Reasons:
      • genre match (+2.0)
      • mood match (+1.0)
      • energy somewhat off (+0.0)
      • acousticness match (+0.5)

  2. Midnight Coding
    Score: 2.5
    Reasons:
      • genre match (+2.0)
      • energy somewhat off (+0.0)
      • acousticness match (+0.5)

  3. Library Rain
    Score: 2.5
    Reasons:
      • genre match (+2.0)
      • energy somewhat off (+0.0)
      • acousticness match (+0.5)

  4. Focus Flow
    Score: 2.5
    Reasons:
      • genre match (+2.0)
      • energy somewhat off (+0.0)
      • acousticness match (+0.5)

  5. Midnight Lament
    Score: 1.5
    Reasons:
      • mood match (+1.0)
      • energy somewhat off (+0.0)
      • acousticness match (+0.5)
  ```
  ### Intense mood, wants acoustic
  ```
  Loaded songs: 18

  User Profile: Genre=rock, Mood=intense, Energy value=0.9, Likes acoustic=True
  Top recommendations:
  1. Storm Runner
    Score: 4.0
    Reasons:
      • genre match (+2.0)
      • mood match (+1.0)
      • energy close match (+1.0)

  2. Gym Hero
    Score: 2.0
    Reasons:
      • mood match (+1.0)
      • energy close match (+1.0)

  3. Urban Heat
    Score: 2.0
    Reasons:
      • mood match (+1.0)
      • energy close match (+1.0)

  4. Sunrise City
    Score: 1.0
    Reasons:
      • energy close match (+1.0)

  5. Night Drive Loop
    Score: 1.0
    Reasons:
      • energy close match (+1.0)
  ```
  ### Jazz, high-energy, non-acoustic
  ```
  Loaded songs: 18

  User Profile: Genre=jazz, Mood=happy, Energy value=0.85, Likes acoustic=False
  Top recommendations:
  1. Sunrise City
    Score: 2.5
    Reasons:
      • mood match (+1.0)
      • energy close match (+1.0)
      • acousticness match (+0.5)

  2. Rooftop Lights
    Score: 2.5
    Reasons:
      • mood match (+1.0)
      • energy close match (+1.0)
      • acousticness match (+0.5)

  3. Digital Sunrise
    Score: 2.5
    Reasons:
      • mood match (+1.0)
      • energy close match (+1.0)
      • acousticness match (+0.5)

  4. Coffee Shop Stories
    Score: 2.0
    Reasons:
      • genre match (+2.0)
      • energy somewhat off (+0.0)

  5. Midnight Lament
    Score: 2.0
    Reasons:
      • genre match (+2.0)
      • energy somewhat off (+0.0)
  ```
  ### Wants extremely low energy
  ```
  Loaded songs: 18

  User Profile: Genre=ambient, Mood=chill, Energy value=0.1, Likes acoustic=True
  Top recommendations:
  1. Spacewalk Thoughts
    Score: 4.5
    Reasons:
      • genre match (+2.0)
      • mood match (+1.0)
      • energy close match (+1.0)
      • acousticness match (+0.5)

  2. Moonlit Sonata
    Score: 3.5
    Reasons:
      • genre match (+2.0)
      • energy close match (+1.0)
      • acousticness match (+0.5)

  3. Midnight Coding
    Score: 1.5
    Reasons:
      • mood match (+1.0)
      • energy somewhat off (+0.0)
      • acousticness match (+0.5)

  4. Library Rain
    Score: 1.5
    Reasons:
      • mood match (+1.0)
      • energy somewhat off (+0.0)
      • acousticness match (+0.5)

  5. Coffee Shop Stories
    Score: 0.5
    Reasons:
      • energy somewhat off (+0.0)
      • acousticness match (+0.5)
  ```
---

## Limitations and Risks

Summarize some limitations of your recommender.

Examples:

- It only works on a tiny catalog
- It does not understand lyrics or language
- It might over favor one genre or mood

You will go deeper on this in your model card.

---

## Reflection

Read and complete `model_card.md`:

[**Model Card**](model_card.md)

Write 1 to 2 paragraphs here about what you learned:

- about how recommenders turn data into predictions
- about where bias or unfairness could show up in systems like this



