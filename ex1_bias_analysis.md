# Exercise 01: Understanding AI Bias

## Objective
Identify and explain bias in AI systems.
---

## Part A: Build Your Foundation (NO AI FIRST)

### 1. Find or simulate a short example of model bias

**Type of bias I'm examining:**
Gender bias in profession 

**My example of this bias:**
When I ask AI image generator to "show me a software engineer" it generates mostly images of men. When I ask for "show me a nurse" it generates mostly women. This shows that AI learned gender stereotypes from training data.

**Evidence or scenario proving that this bias exists:**
I tested with AI image tool. "Generate image of software engineer" and it gave me 8 pictures of men and 1 woman. "Generate image of nurse" and gave me 7 women and 1 man. This pattern shows bias - AI assumes engineers are male and nurses are female.

### 2. Explain in your own words why that bias may exist

**My explanation of the root cause:**
The training data probably had more pictures of male engineers because in real life tech industry has more men than women historically. Same for nurses - more women nurses in the data. The AI just learns what it sees in the data, so it repeats the stereotype. It doesn't know this is unfair, it just learns the pattern and recycles it.


### 3. Propose one mitigation

**My proposed solution:**
Balance the training dataset to include equal numbers of men and women in all professions. If we show AI that engineers can be any gender and nurses can be any gender, it will stop assuming gender based on profession stereotyping of the past.

---

## Part B: Strategic AI Use 

### Questions I asked AI:

**Question 1:**
"I found gender bias example: AI shows mostly men for engineers and women for nurses. I think it exists because training data reflects real world gender imbalance in these professions. My proposed mitigation: balance the training data with equal gender representation. What am I missing? What underlying causes haven't I considered?"

**AI's response:**
AI explained that bias can happen at multiple stages not just training data. Even how we label data can introduce bias (like tagging "nurse" images with "she" pronouns). Also AI pointed out intersectional bias - when gender bias combines with race bias the problem gets worse. AI suggested that my solution might create new problems like unrealistic data that doesn't reflect real world for some cases.

**What new insights did I gain:**
- I learned that bias happens in data collection, labeling, algorithm design, and deployment - not just in raw data
- Intersectional bias means biases multiply - like AI might show even fewer black women engineers
- Sometimes we need data to reflect reality (like for statistics) but other times we want to show diversity (like for job ads) - different use cases need different approaches.

---

**Question 2: Exploring edge cases**
"What happens when this gender bias appears in healthcare, hiring, or criminal justice? I think in healthcare it could cause misdiagnosis if AI assumes certain conditions are gender specific. In hiring it denies jobs to qualified people. In criminal justice it might lead to unfair targeting. What are the real-world implications?"

**AI's response:**
AI confirmed my thoughts and added more serious examples. In healthcare, AI might miss heart attack symptoms in women because trained mostly on male data. In hiring, AI resume screeners have actually rejected women's resumes at some companies. In criminal justice, facial recognition fails more on women and people of color leading to wrong arrests.

**Real-world consequences I didn't consider:**
- In healthcare: women and minorities getting misdiagnosed or undertreated because AI trained on male/white patient data.
- In loans: people denied credit because AI thinks their demographic is risky.
- In education: students from certain backgrounds get flagged unfairly by monitoring systems
- The bias creates feedback loop - AI makes biased decisions, which creates more biased data, on which the AI is trained from the start, which makes AI worse from every aspect in terms of generated output.

---

## Part C: Critical Reflection

### What % did you complete before using AI?
I completed about 75% before using AI. I found my own example, explained why it happens, and proposed solution all by myself. Then I used AI to check my thinking and learn deeper about bias types and real world impacts.

### Did AI replace your thinking or amplify it?
AI amplified my thinking. I had my own ideas first and AI helped me go deeper and see angles I missed. If I asked AI first I would just read its answer and not really understand. Because I thought it through first the AI explanations made more sense and I remembered them better.

### Could you explain this to someone else without AI?
Yes, I could explain gender bias in AI, why it happens (training data reflects real world inequality), and how to fix it (balance data and check for bias at all stages). I understand it because I worked through it myself.

### What did you contribute that AI couldn't?
I found a specific example that I actually tested myself. I thought through the problem from my perspective as someone learning to code. I connected it to my experience with AI tools. AI gave me information but I asked the questions that mattered to me.



