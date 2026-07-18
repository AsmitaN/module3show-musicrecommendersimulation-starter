# 🎧 Model Card: Music Recommender Simulation

## 1. Model Name  

Give your model a short, descriptive name.  
Example: **VibeFinder 1.0**  

---

## 2. Intended Use  

Describe what your recommender is designed to do and who it is for. 

Prompts:  

- What kind of recommendations does it generate  
- What assumptions does it make about the user  
- Is this for real users or classroom exploration  

---

## 3. How the Model Works  

Explain your scoring approach in simple language.  

Prompts:  

- What features of each song are used (genre, energy, mood, etc.)  
- What user preferences are considered  
- How does the model turn those into a score  
- What changes did you make from the starter logic  

Avoid code here. Pretend you are explaining the idea to a friend who does not program.

---

## 4. Data  

Describe the dataset the model uses.  

Prompts:  

- How many songs are in the catalog  
- What genres or moods are represented  
- Did you add or remove data  
- Are there parts of musical taste missing in the dataset  

---

## 5. Strengths  

Where does your system seem to work well  

Prompts:  

- User types for which it gives reasonable results  
- Any patterns you think your scoring captures correctly  
- Cases where the recommendations matched your intuition  

---

## 6. Limitations and Bias 

Where the system struggles or behaves unfairly. 

Prompts:  

- Features it does not consider  
- Genres or moods that are underrepresented  
- Cases where the system overfits to one preference  
- Ways the scoring might unintentionally favor some users\
    The system over-prioritizes the lofi genre and happy mood because 22% of the dataset is lofi and happy music each.\
    This is equivalent to 4 songs that are lofi and 4 songs that are happy.\
    There are also more acoustic-leaning songs (acousticness > 0.5) than low-acoustic songs, which are 56% (10 songs) and 44% (8 songs), respectively.\
    This unintentionally favors listeners who like to listen to music that falls into lofi, happy, and acoustic categories.  
---

## 7. Evaluation  

How you checked whether the recommender behaved as expected. 

Prompts:  

- Which user profiles you tested  
- What you looked for in the recommendations  
- What surprised you  
- Any simple tests or comparisons you ran  

No need for numeric metrics unless you created some.\

I tested three different user profiles: high-energy pop, chill lofi, and deep intense rock. I then tested three additional edge cases and adversarial user profiles based on these ones as well as others of varying attributes (terminal output included in README.md). Below is the terminal output for each of the three user profiles.\

## High-energy pop
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
### Chill lofi
```
Loaded songs: 18

User Profile: Genre=lofi, Mood=chill, Energy value=0.4, Likes acoustic=True
Top recommendations:
1. Midnight Coding
   Score: 4.5
   Reasons:
     • genre match (+2.0)
     • mood match (+1.0)
     • energy close match (+1.0)
     • acousticness match (+0.5)

2. Library Rain
   Score: 4.5
   Reasons:
     • genre match (+2.0)
     • mood match (+1.0)
     • energy close match (+1.0)
     • acousticness match (+0.5)

3. Focus Flow
   Score: 3.5
   Reasons:
     • genre match (+2.0)
     • energy close match (+1.0)
     • acousticness match (+0.5)

4. Autumn Memories
   Score: 3.5
   Reasons:
     • genre match (+2.0)
     • energy close match (+1.0)
     • acousticness match (+0.5)

5. Spacewalk Thoughts
   Score: 2.5
   Reasons:
     • mood match (+1.0)
     • energy close match (+1.0)
     • acousticness match (+0.5)
```
### Deep intense rock
```
Loaded songs: 18

User Profile: Genre=rock, Mood=intense, Energy value=0.91, Likes acoustic=False
Top recommendations:
1. Storm Runner
   Score: 4.5
   Reasons:
     • genre match (+2.0)
     • mood match (+1.0)
     • energy close match (+1.0)
     • acousticness match (+0.5)

2. Gym Hero
   Score: 2.5
   Reasons:
     • mood match (+1.0)
     • energy close match (+1.0)
     • acousticness match (+0.5)

3. Urban Heat
   Score: 2.5
   Reasons:
     • mood match (+1.0)
     • energy close match (+1.0)
     • acousticness match (+0.5)

4. Sunrise City
   Score: 1.5
   Reasons:
     • energy close match (+1.0)
     • acousticness match (+0.5)

5. Night Drive Loop
   Score: 1.5
   Reasons:
     • energy close match (+1.0)
     • acousticness match (+0.5)
```
Comments: High-energy pop prefers less acoustic songs while chill lofi favors more acoustic songs.\
Chill lofi likes low-energy songs while deep intense rock leans toward high-energy songs.\
Deep intense rock prefers songs with an intense mood while high-energy pop likes songs with a happy mood. Note that both of these profiles like music that is high in energy and less acoustic.
---

## 8. Future Work  

Ideas for how you would improve the model next.  

Prompts:  

- Additional features or preferences  
- Better ways to explain recommendations  
- Improving diversity among the top results  
- Handling more complex user tastes  

---

## 9. Personal Reflection  

A few sentences about your experience.  

Prompts:  

- What you learned about recommender systems  
- Something unexpected or interesting you discovered  
- How this changed the way you think about music recommendation apps  
