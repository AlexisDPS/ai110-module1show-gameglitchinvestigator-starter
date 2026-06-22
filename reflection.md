# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
  The visuals looked correct, but the game was unplayable because the features don't seem to work as intended.
- List at least two concrete bugs you noticed at the start  
  -The hints didn't match the secret number
  -The Enter key doesn't submit your guess

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input                    | Expected Behavior                                            | Actual Behavior                                          | Console Output / Error |
| ------------------------ | ------------------------------------------------------------ | -------------------------------------------------------- | ---------------------- |
| NewGame                  | Accept new inputs to submit                                  | Won't start over if all attempts from last game are used | None                   |
| Changed difficulty       | Changes the number range                                     | Numbers range not changed in the blue text bar           | None                   |
| Enter key                | Submits the answer you have typed                            | does not submit your answer                              | None                   |
| number in range of hints | Game ends when your guess is between an upper and lower hint | hints go to decimals                                     | None                   |
| hint                     | matches the value of the secret number                       | doesn't match the secret number                          | None                   |

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
  I used Claude Sonnet 4.6.
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
  Claude told me the New Game button wasn't resetting st.session_state.status back to "playing", which caused st.stop() to keep blocking the page. I checked the code myself and confirmed status was never touched in the New Game block. Adding that one line fixed it.
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).
  Claude suggested using Streamlit's AppTest framework to write a test for the New Game bug. When I ran pytest the test timed out every time and never passed. The AI didn't account for a Python 3.14 compatibility issue with Streamlit. I confirmed it by reading the error in the terminal and we had to replace it with a different test.

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
  First I went over the code to make sure that the changes made sense to me. Then I started the app.py and manually tested to check that what was implemented actually worked as intended. Lastly, I asked AI to confirm with me that the code and output worked correctly and used the pytest to also confirm alongside it.
- Describe at least one test you ran (manual or using pytest)
  One simple test that I ran was using the new game button since it just needed me to run a quick game guessing and then press new game. I noticed that everything was gettting reset as it should and took note of anything that could be wrong. That way I was sure that everything was working as it should.
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?
  Yes, the AI helped me design understand the tests by giving me clarifying questions to make sure that I knew what was going on. I also asked it questions for things that I was confused about which made it simple to go back and forth. Ultimately ending up with the correct understanding of what was happening.

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
  When you click a button in Streamlit the apps entire script reruns. Normal variables get reset/wiped. Session state saves values so that they don't get lost in reruns.

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
    One habit from this that I want to reuse in the future is trying to avoid using AI to do the logical thinking for me but letting it help guide me. Also using it to get the right git commands without taking too long.
- What is one thing you would do differently next time you work with AI on a coding task?
  Next time I think I will review the code on my own to get a feel and understand of it through my own perspective. Using Ai too much can make it easy to skip over certain logical errors that you would otherwise have been able to catch easily.
- In one or two sentences, describe how this project changed the way you think about AI generated code.
  This project actually made me realize how much things AI can actually achieve. I haven't really used AI for coding and this showed me how much I could do in much less time.
