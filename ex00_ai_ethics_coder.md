# Exercise 00: Learning to Use AI Ethically as a Coder

## Part A: The Critical Distinction

### How have you used AI for coding so far?

<!-- TODO: Write your honest answer here. Example ideas:
- I asked AI to write whole functions for me
- I used it to debug my code when I got stuck
- I copied solutions without really reading them carefully
- I used it to understand concepts I didn't know
-->

### Do you ask AI for solutions before trying yourself?

<!-- TODO: Be honest. Example ideas:
- Yes, most of the time I ask AI first because its faster
- Sometimes I try first but if it takes more than 5 minutes I ask AI
- I usually try myself first but when deadline is close I just ask AI
- No, I always try first then use AI to improve my solution
-->

### Can you explain code you've submitted without AI's help?

<!-- TODO: Write your reflection. Example ideas:
- Sometimes I can explain it, sometimes not really
- I understand the general idea but not all the details
- Yes, because I always make sure to understand before submitting
- Honestly, some code I submitted I couldn't explain without looking at AI again
-->

### What would happen if AI was suddenly unavailable during an exam or interview?

<!-- TODO: Think about this scenario. Example ideas:
- I would struggle a lot because I rely on AI for syntax and logic
- I could probably do basic stuff but complex problems would be hard
- I think I would be okay because I try to learn and not just copy
- I would panic because I'm used to having AI help me
-->

### Which learner are you now?

**Learner A: "AI is my answer generator"**
- Asks: "Write a function that does X"
- Copies code without reading carefully
- Moves on once it works
- Cannot explain how the code works

**Learner B: "AI is my learning amplifier"**
- Attempts the problem first
- Asks: "Why does this approach work? What are the trade-offs?"
- Tests understanding by explaining concepts
- Uses AI to explore deeper, not to avoid thinking

<!-- TODO: Write where you are now and where you want to be. Example:
Right now I am mostly Learner A because I used AI a lot in go-reloaded project to get quick answers. I want to become Learner B because I want to actually understand what I am doing and not just copy code. I realize that if I keep being Learner A I will not learn anything real and will be replaceable.
-->

---

## Part B: The Wrong Way vs. The Right Way

### Challenge: Implement a function to check if a string is a palindrome

**Track B - The Right Way (DO THIS):**

#### Step 1: Attempt independently

**My pseudocode:**
<!-- TODO: Write your pseudocode first. Example:
1. Remove spaces and make all lowercase
2. Compare first character with last character
3. Move inward and keep comparing
4. If all match then its palindrome
5. If any dont match then its not palindrome
-->

**My implementation:**
<!-- TODO: Write your Python code here. Try it yourself first!
Example structure:
def is_palindrome(s):
    # your code here
    pass
-->

**Test cases I tried:**
<!-- TODO: List the test cases you tried. Examples:
- "racecar" - should return True
- "hello" - should return False
- "A man a plan a canal Panama" - should return True (if ignoring spaces and case)
- "" - should return ? (edge case to think about)
-->

**Issues I debugged myself:**
<!-- TODO: What problems did you face and how did you fix them? Examples:
- At first I forgot to handle uppercase letters
- I had trouble with spaces in the string
- I wasn't sure how to handle empty strings
-->

**My comments explaining the logic:**
<!-- TODO: After writing your code, add comments explaining WHY each part works -->

#### Step 2: Strategic AI use (AFTER you have a working solution)

**Questions I asked AI:**
<!-- TODO: Write the questions you would ask AI after your solution works. Examples:
- "I wrote a function to check palindromes. Here's my code: [paste code]. What's the time complexity?"
- "What edge cases am I missing in my palindrome function?"
- "Are there alternative approaches to check palindromes? What are the trade-offs?"
-->

**What AI taught me:**
<!-- TODO: What did you learn from AI that you didn't know before? Examples:
- I learned about O(n) time complexity
- I found out about edge cases like numbers and special characters
- I discovered you can also reverse the string and compare but that uses more memory
-->

#### Step 3: Reflection

**What did you learn by struggling first?**
<!-- TODO: Reflect on the struggle. Examples:
- I learned how to think through the problem step by step
- I understood the logic better because I had to figure it out myself
- I made mistakes but fixing them taught me more than just seeing the right answer
-->

**How is your understanding different than if you'd just asked for the solution?**
<!-- TODO: Compare the two approaches. Examples:
- If I just asked for solution I would have code that works but no idea why
- By doing it myself first I understand every line and can modify it easily
- I feel more confident now that I know I can solve similar problems
-->

**Can you now implement similar functions without AI?**
<!-- TODO: Be honest about your abilities now. Examples:
- Yes, I think I could do reverse string or find duplicates because I understand the pattern
- Maybe simple ones, but complex ones I would still need help
- I understand the concept so I could try, might not be perfect but I could start
-->

---

## Part C: Testing Your Understanding

### Variations I completed without using AI:

#### 1. Ignore spaces and punctuation
<!-- TODO: Modify your palindrome function to handle spaces and punctuation
Write your code here
-->

#### 2. Make it case-insensitive
<!-- TODO: Make sure "Racecar" is recognized as palindrome
Write your code here
-->

#### 3. Return the position where the string stops being a palindrome
<!-- TODO: If not a palindrome, return at which position it fails
Write your code here
Example: "racecxr" should return position 4 where 'x' doesn't match
-->

### Strategic AI use after variations:

**Questions I asked AI:**
<!-- TODO: After completing the variations yourself, what did you ask AI? Examples:
- "I modified my palindrome to ignore punctuation using this approach: [code]. Did I miss any edge cases?"
- "Is there a more efficient way to handle case-insensitivity than converting the whole string?"
-->

**What I learned:**
<!-- TODO: What additional insights did AI provide? -->

---

## Part D: The Fairness Contract

### My Personal Code of Ethics for AI Use in Learning

**I will use AI when:**
<!-- TODO: Write your rules. Examples:
- After I've tried solving the problem for at least 20-30 minutes myself
- To understand why my solution works or doesn't work
- To explore alternative solutions after I have my own working solution
- To learn about concepts I don't know yet but want to understand deeply
-->

**I will NOT use AI when:**
<!-- TODO: Write your rules. Examples:
- I haven't attempted the problem myself first
- I'm taking an exam or assessment
- I need to build fundamental skills that I should know by heart
- I'm feeling lazy and just want a quick answer without learning
-->

**I know I'm using AI fairly when:**
<!-- TODO: Write your criteria. Examples:
- I can explain every line of my code without looking at AI's response
- I could solve similar problems without AI's help
- I feel more confident and knowledgeable after using AI
- I'm asking "why" and "how" questions, not just "give me the answer"
-->

**Signed:** ___________________________

**Date:** ___________________________

---

## Part E: Real-World Scenario Analysis

### Scenario 1: Interview - "Explain how you'd implement a caching system"

**If I always relied on AI, what would happen?**
<!-- TODO: Think about this honestly. Examples:
- I wouldn't be able to answer because I never actually understood the code I wrote
- I might remember some words but couldn't explain the actual logic
- I would freeze and realize I don't actually know what I'm doing
-->

### Scenario 2: Production bug at 2 AM - AI is unavailable

**Can I debug code I don't fully understand?**
<!-- TODO: Be honest. Examples:
- No, if I just copied code without understanding it I would be lost
- Maybe I could try but it would take very long and I might make it worse
- Yes, if I learned properly I would know how to debug step by step
-->

### Scenario 3: New technology with little documentation

**If I never learned to read docs and experiment, what happens?**
<!-- TODO: Think about this scenario. Examples:
- I would be stuck because AI might not know about very new tech
- I would struggle because I'm not used to learning from official docs
- I would have to learn these skills anyway, better to learn them now
-->

### How does using AI fairly NOW prepare me for these scenarios?

<!-- TODO: Write a paragraph connecting fair AI use to real-world readiness. Example:
If I use AI the right way now - as a learning tool not a replacement for thinking - I will build the skills I need for real situations. In interviews I can explain my code because I understand it. When there's a bug at night I can debug it because I know how the code works. When new technology comes I can read docs and experiment because I practiced learning, not just copying. Using AI fairly makes me stronger, not weaker.
-->

---

## Part F: Building Irreplaceable Skills

### Skills Self-Assessment (Rate 1-5, where 1=weak, 5=strong)

**1. Problem decomposition** (breaking big problems into small steps)
<!-- TODO: Rate yourself and explain why. Example:
Rating: 3/5
Why: I can break down simple problems but complex ones I still struggle with. I need more practice thinking through problems step by step before coding.
-->

**2. Systems thinking** (understanding how pieces fit together)
<!-- TODO: Rate yourself and explain. Example:
Rating: 2/5
Why: I often focus on single functions without thinking about the whole system. I need to learn how different parts of code interact with each other.
-->

**3. Critical evaluation** (judging if a solution is good or bad)
<!-- TODO: Rate yourself and explain. Example:
Rating: 2/5
Why: I usually just check if code works, not if its the best solution. I need to learn about performance, readability, and trade-offs.
-->

**4. Debugging mindset** (finding and fixing problems systematically)
<!-- TODO: Rate yourself and explain. Example:
Rating: 3/5
Why: I can fix simple bugs but when problems are complex I get frustrated. I need to be more patient and systematic with debugging.
-->

**5. Conceptual understanding** (knowing the "why" not just the "how")
<!-- TODO: Rate yourself and explain. Example:
Rating: 2/5
Why: I often know HOW to write code but not WHY it works that way. I need to go deeper and understand the concepts behind the code.
-->

### My Lowest Area: _________________

### Action Plan: 3 specific actions this week to improve

**Action 1:**
<!-- TODO: Be specific. Example:
This week I will solve 3 problems by writing pseudocode first before any actual code. This will help me practice breaking down problems into steps.
-->

**Action 2:**
<!-- TODO: Be specific. Example:
When I write code this week I will spend 10 minutes after each solution writing comments explaining WHY each part works, not just WHAT it does.
-->

**Action 3:**
<!-- TODO: Be specific. Example:
I will read the official Python documentation for 15 minutes each day to practice learning from docs instead of always asking AI.
-->

---

## Summary

This exercise is about becoming self-aware of how I use AI and committing to use it as a learning amplifier, not as a replacement for thinking. By being honest about where I am now and making a plan to improve, I am taking the first step toward becoming an irreplaceable developer.

The key lesson: **AI can write code, but only I can build judgment, understanding, and the ability to think through complex problems. These skills make me irreplaceable.**
