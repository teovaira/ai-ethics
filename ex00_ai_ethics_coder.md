# Exercise 00: Learning to Use AI Ethically as a Coder

## Part A: The Critical Distinction

### How have you used AI for coding so far?

I used AI a lot in go-reloaded project. Sometimes I asked it to write functions and generally implement the next step for me when I didn't know how to continue. I also use it for debugging when code is not working the way i want it to work. I always aks it to get into full teacher mode and explain everything in great detail. I nevel leave questions and inquiries of mine, unanswered!

### Do you ask AI for solutions before trying yourself?

This has been the case a lot of times. Recently, i started asking it for hints and quidelines with me trying first to tackle the task i' ve been given. It's going a lot slower but i have noticed that i can reproduce the knowledge achieved this way, a lot faster than by just asking AI to explain me concepts and reading through it's explanations.

### Can you explain code you've submitted without AI's help?

Always!!

### What would happen if AI was suddenly unavailable during an exam or interview?

I would struggle for sure if the topic was complicated or advanced. If it was easy-medium level most probably i would be able to address it.

### Which learner are you now?

I am totally a Learner B but there are some traces inside me of Learner A. I am pretty confident that in the future i will be 100% only Learner B.

## Write a brief paragraph: Where are you now, and where do you want to be?

Currently i learn everyday scores of things and in general learning is one of the things i love. I want to be able to see and read something and understand the how and why and at the same time be able to explain it, teach it and reproduce it! And i am 100% sure that this will be the case for me in my future steps because i am thirsty of knowledge and the excitement and joy this procedure brings to my heart and mind.

---

## Part B: The Wrong Way vs. The Right Way

### Challenge: Implement a function to check if a string is a palindrome

**Track B - The Right Way (DO THIS):**

#### Step 1: Attempt independently

**My pseudocode:**
1. First I remove all the spaces and convert all letters to lowercase.
2. Then I compare the first character with the last one.
3. If they are the same, I move to the next set and compare second from left with second from right.
4. Keep doing this until I reach the middle of the string.
5. If all characters match then it is a palindrome.
6. If any don't match, then it's not.

**My implementation:**
```python
def is_palindrome(s):
    # Convert to lowercase and remove spaces
    s = s.lower().replace(" ", "")

    # Compare from both ends
    left = 0
    right = len(s) - 1

    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1

    return True
```

**Test cases I tried:**
- "racecar" - should return True (it works!)
- "hello" - should return False (it works!)
- "A man a plan a canal Panama" - should return True (it works!)
- "" - empty string returns True (My logic says this is correct!)
- "Racecar" - should return True (it works because I made lowercase)

**Issues I debugged myself:**
- At first I forgot to handle spaces so "A man a plan a canal Panama" was not working.
- I added .replace(" ", "") to fix spaces.
- Also I forgot about uppercase letters first time, then I added .lower()
- I was thinking about punctuation but didn't add it yet.

**My comments explaining the logic:**
```python
def is_palindrome(s):
    # First clean the string - make everything lowercase and remove spaces
    # This way "Racecar" and "race car" both work
    s = s.lower().replace(" ", "")

    # Use two pointers, one from start and one from end
    left = 0
    right = len(s) - 1

    # Keep comparing characters moving closer to the middle of the argument
    while left < right:
        # If any characters don't match, not a palindrome
        if s[left] != s[right]:
            return False
        # Move pointers closer to middle
        left += 1
        right -= 1

    # If we reached here, all characters matched
    return True
```

#### Step 2: Strategic AI use (AFTER you have a working solution, ask AI)

**Questions I asked AI:**

"I wrote a function to check palindromes. Here is my approach: [my code above].     
- "What is the time complexity?"
- "What edge cases am I missing?"
- "What are the alternatives and trade-offs?
- "How does it perform on very long strings?"

**What AI taught me:**
- I learned that my solution is O(n) time complexity which is good.
- AI told me I should handle punctuation too, not just spaces.
- I found out I can also reverse the string and compare but that uses more memory.
- AI showed me edge case with numbers and special characters that I didn't think about

#### Step 3: Reflection

**What did you learn by struggling first?**
I learned how to think about the problem step by step. When I tried myself first I had to understand what palindrome really means and how to check it. I made mistakes with spaces and uppercase but fixing them made me understand better. If I had just asked AI for answers I would not have learnt any of this.

**How is your understanding different than if you'd just asked for the solution?**
Now I really understand how the two pointer technique works. If I just asked for the solution I would have functional code but without know why it works. Because I did it myself I can explain every line and I know why I chose this way. I feel more confident.

**Can you now implement similar functions without AI?**
Yes I think so. I could do reverse string because it is a similar idea. I could also try finding and bypassing duplicates. I understand the pattern of checking from both ends and comparing at the same time and how efficient it is. Yes, i am pretty confident that if similar tasks were given to me i would be able to tackle them or at least, give me best effort.

---

## Part C: Testing Your Understanding

### Variations I completed without using AI:

#### 1. Ignore spaces and punctuation
```python
def is_palindrome_ignore_punctuation(s):
    # Remove all non-alphanumeric characters and make lowercase
    cleaned = ""
    for char in s.lower():
        if char.isalnum():
            cleaned += char

    # Same two pointer logic
    left = 0
    right = len(cleaned) - 1

    while left < right:
        if cleaned[left] != cleaned[right]:
            return False
        left += 1
        right -= 1

    return True
```

#### 2. Make it case-insensitive
```python
def is_palindrome_case_insensitive(s):
    # Just convert to lowercase before checking
    s = s.lower()

    left = 0
    right = len(s) - 1

    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1

    return True
```

#### 3. Return the position where the string stops being a palindrome
```python
def palindrome_fail_position(s):
    # Clean the string first
    s = s.lower().replace(" ", "")

    left = 0
    right = len(s) - 1

    while left < right:
        if s[left] != s[right]:
            # Return the position where it fails
            return left
        left += 1
        right -= 1

    # Is palindrome, return -1
    return -1
```

### Strategic AI use after variations:

**Questions I asked AI:**
- "I modified my palindrome function to handle these cases: [code above]. Did I miss any edge cases?"
- "How could I make this more efficient?"

**What I learned:**
- AI told me I could use list comprehension or join to be more pythonic.
- There is a regex way to remove punctuation which is faster.
- For very long strings my way is slower and thus less performant, because strings are immutable in Python and a lot of allocations will take place.

---

## Part D: The Fairness Contract

### My Personal Code of Ethics for AI Use in Learning

**I will use AI when:**
- After I tried solving a problem myself for at least 20-30 minutes.
- To understand why my code works or why it doesn't work.
- To learn about different approaches after I have my own working solution.
- To check if I missed edge cases or more optimized ways to implement something.
- To learn new concepts that I don't know yet but want to understand deeply.

**I will NOT use AI when:**
- I haven't tried the problem myself first.
- I am in exam or test or interview.
- I need to build basic skills that I should know without any help.
- I am just feeling lazy and want quick answers without using my mind.
- The code is something I should understand by myself to learn properly.

**I know I'm using AI fairly when:**
- I can explain all my code without looking at AI responses.
- I could solve same problem again without AI help.
- I feel more confident after using AI, not more confused
- I am asking "why this works" and "what are the trade-offs" not just "give me code".
- After using AI I learned something new that I will remember forever.

**Signed:** Theodore Vairaktaris

**Date:** November 2025

---

## Part E: Real-World Scenario Analysis

### Scenario 1: Interview - "Explain how you'd implement a caching system"

**If I always relied on AI, what would happen?**
I would not be able to answer at all. Maybe I will remember some words like "cache" and "hash map" but I would not be able to explain the actual logic or why we do the things we do. I would freeze and realize I don't actually know what I did in my projects. The interviewer would understand that I just copied code..

### Scenario 2: Production bug at 2 AM - AI is unavailable

**Can I debug code I don't fully understand?**
No, if I just copied code without understanding I would be completely lost. I wouldn't know where to start looking for the bug. Maybe I could try random things but probably make it worse and create more bugs along the way. If I learned properly I would know how to debug step by step and find the problem.

### Scenario 3: New technology with little documentation

**If I never learned to read docs and experiment, what happens?**
I would be stuck because AI might not know about very new and fresh technology. I I would not know how to learn from official docs or experiment myself. I need to practice learning from docs now so when new things come I can figure it out myself.

### How does using AI fairly NOW prepare me for these scenarios?

If I use AI the right way now - to learn not to replace my thinking - I build the skills for real situations. In interview I can explain because everything i will be asked, because I will understand the code. When bug happens at night, i can debug it, because I know how my code works. When new technology arrives, i can read docs and try things because I practiced learning properly. Using AI fairly makes me a stronger and irreplaceable programmer.

---

## Part F: Building Irreplaceable Skills

### Skills Self-Assessment (Rate 1-5, where 1=weak, 5=strong)

**1. Problem decomposition** (breaking big problems into small steps)
Rating: 3/5
Why: I can break down simple problems but complex ones are still out of my league. I need more practice thinking through problems step by step before I start coding. Usually I jump to coding too fast without planning ahead and because of that i get disappointed when i reach the first obstacles and impostor syndrome is activated and i address the AI to do the work..

**2. Systems thinking** (understanding how pieces fit together)
Rating: 3/5
Why: I would say i am pretty decent in this section, but when a problem gets bigger and more complex, i loose some connections between the different parts of my program.

**3. Critical evaluation** (judging if a solution is good or bad)
Rating: 3/5
Why: Even though i lack the experience to implement from the start optimized code, the last filters i give to my AI assistant before submitting any code, are these of performance, optimization and implementation of best practices. I have always these concepts in my mind.

**4. Debugging mindset** (finding and fixing problems systematically)
Rating: 2/5
Why: I can fix simple bugs but when the problem is complex, I get frustrated fast. I need to be more patient and systematic. Instead of random trying I should think more logically about what might have gone wrong.

**5. Conceptual understanding** (knowing the "why" not just the "how")
Rating: 4/5
Why: I always try to understand and comprehend the code i write, even if it is totally ai-generated. The WHY of things is the most important part for me and that's why when i encounter similar problems, usually i can find the solution on my own.

### My Lowest Area: Systems thinking and Conceptual understanding (both 2/5)

### Action Plan: 3 specific actions this week to improve

**Action 1:**
Every day this week I will spend 15 minutes reading official Python documentation instead of asking AI. I will try to understand one concept deeply - like how lists actually work in memory or why dictionaries are fast.

**Action 2:**
When I write code this week I will draw diagram on paper first showing how different parts connect. Before coding I will think about the system not just the function. This helps with systems thinking.

**Action 3:**
For every solution I write this week I will ask myself "why this way and not other way?" and write down the trade-offs. This practice critical thinking and conceptual understanding together.


