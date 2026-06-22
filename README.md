# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and now the game is unplayable.

- You can't win.
- The hints lie to you.
- The secret number seems to have commitment issues.

## 🛠️ Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the broken app: `python -m streamlit run app.py`

## 🕵️‍♂️ Your Mission

1. **Play the game.** Open the "Developer Debug Info" tab in the app to see the secret number. Try to win.
2. **Find the State Bug.** Why does the secret number change every time you click "Submit"? Ask ChatGPT: _"How do I keep a variable from resetting in Streamlit when I click a button?"_
3. **Fix the Logic.** The hints ("Higher/Lower") are wrong. Fix them.
4. **Refactor & Test.** - Move the logic into `logic_utils.py`.
   - Run `pytest` in your terminal.
   - Keep fixing until all tests pass!

## 📝 Document Your Experience

- Describe the game's purpose. — A number guessing game where you guess a secret number within limited attempts, receiving higher/lower hints each round if you choose to receive them.
- Detail which bugs you found. — New Game didn't reset game status, hints gave wrong directions due to a string/int comparison bug, and the difficulty range was hardcoded.
- Explain what fixes you applied. — Reset status to "playing" on New Game, moved check_guess to logic_utils.py with proper type conversion, and used dynamic low/high values for the range.

## 📸 Demo Walkthrough

1. User enters a guess of 23 → "Go HIGHER!"
2. User enters a guess of 50 → "Go LOWER!"
3. User enters a guess of 45 → "Correct!" — game ends with final score
4. Score updates correctly after a guess is made every time
5. User clicks New Game → game resets and accepts new input

## 🧪 Test Results

```
# Paste your pytest output here, e.g.:
# pytest tests/
# ========================= X passed in 0.XXs =========================
```

## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, describe the Enhanced UI changes here — a screenshot is optional]
