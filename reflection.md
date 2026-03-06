# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the secret number kept changing" or "the hints were backwards").

---
- The game looked like a typical simple interactive game

- Hard is meant to have a more broader range
- The hint is not accurate
- The Normal range is meant to be for the Hard range
## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

--- 
Answer:
- I used Copilot as my AI teammate
- This was what the AI suggested:
  "If you compare the three branches you can see the logical error:

  Easy → 1–20 (narrow)
  Normal → 1–100 (wide)
  Hard → 1–50 (narrower than Normal)
  …it should have been something like 1–200 (or otherwise “broader than Normal”).
  Changing the “Hard” return value (and renaming “Normal” to “Medium” if you prefer)
  fixes the glitch."

- In this part, I was trying to run the pytest. I asked copilot for help but this was kind of misleading:
"
# activate whatever venv/conda you’re using first if needed
pytest -q               # “-q” gives a concise output
# or for full detail:
pytest"

- I verified the result by checking other AI systems for suggestions on how i can run the file

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

---
Answer:
- I made a comparision on the actual code and the fixed code and saw that the bugs were successfully corrected

- When i ran the code, i chose the easy level ranging from 1-20. After my first attempt, the hint that was suggested was accurate with what the guess was leading up to. I was able to guess the right number on the second trial.

- No, AI did not help me to design or understand any test cases because it was pretty straight forward and clear

## 4. What did you learn about Streamlit and state?

- In your own words, explain why the secret number kept changing in the original app.
- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
- What change did you make that finally gave the game a stable secret number?

---
- The range values were wrong and every submit/reset triggered a new 'random.randint() call.

- I would say .."Every interaction causes the app to restart from scratch, and session state is the special storage that survives those restarts."

- I changed the initialization so that the secret number is only generated once. Specifically, I wrapped the `random.randint` call in a check `if "secret" not in st.session_state:`. That meant reruns no longer replaced the secret, giving the game a stable number.

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.

Answer:
- The act of modularity is one habit that I would want to continue integrating whether it it for a large project or solo project. It makes debugging very easy

- I think more precised prompting is something I would do differently. With AI, you do not get accurate answers so precised prompting is one thing that I would try to learn and do differently next time

1. Not all AI codes are 100% correct. AI makes mistakes too. 
2. Although AI makes mistakes, with good prompting and directions, it can also really be a very helpful tool for debugging