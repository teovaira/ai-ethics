# Exercise 02: Designing Ethical Prompts

## Objective
Learn to rewrite prompts to prevent bias or misinformation by identifying problematic prompts and improving them.

**Remember:** Do your own analysis first before using AI to validate!

---

## Part A: Independent Analysis

### Prompt 1: The Problematic Version

**My poorly designed prompt:**
<!-- TODO: Write a prompt that could lead to biased/unsafe answers. Example:
"Write a job description for a nurse. Describe what she does daily."
-->

**Why it's problematic:**
<!-- TODO: Explain the issues. Example:
- Assumes nurses are female by using "she"
- Reinforces gender stereotypes
- Excludes male nurses from the description
-->

**Potential harm:**
<!-- TODO: What damage could this cause? Example:
- Discourages men from considering nursing careers
- Perpetuates gender stereotypes in healthcare
- Creates biased job descriptions that might violate equal opportunity laws
-->

**Hidden assumptions:**
<!-- TODO: What assumptions are baked in? Example:
- Assumes nurse = woman
- Assumes reader will accept this stereotype
- Assumes gender matters for the job description
-->

**My improved version:**
<!-- TODO: Rewrite to be better. Example:
"Write a job description for a nurse. Describe their daily responsibilities and required skills."
-->

**Explanation of improvements:**
<!-- TODO: Why is this better? Example:
- Uses gender-neutral "their" instead of assuming gender
- Focuses on job requirements not stereotypes
- Treats the role professionally without bias
- Inclusive language welcomes all genders
-->

---

### Prompt 2: The Problematic Version

**My poorly designed prompt:**
<!-- TODO: Write another biased prompt. Example:
"Generate an image of a successful business executive"
-->

**Why it's problematic:**
<!-- TODO: Explain the issues. Example:
- Doesn't specify diversity, AI likely defaults to white male
- "Successful" might trigger stereotypical imagery (suit, boardroom)
- Vague prompt allows AI to use biased training data patterns
-->

**Potential harm:**
<!-- TODO: What damage could this cause? Example:
- Reinforces that only certain people can be executives
- Excludes women and people of color from representation
- Perpetuates narrow view of success
-->

**Hidden assumptions:**
<!-- TODO: What assumptions are baked in? Example:
- Assumes AI knows what "successful" looks like
- Assumes default image will be representative
- Doesn't consider diversity matters
-->

**My improved version:**
<!-- TODO: Rewrite to be better. Example:
"Generate an image of a successful business executive. Include diverse representation across gender, ethnicity, and age. Show them in a modern professional setting."
-->

**Explanation of improvements:**
<!-- TODO: Why is this better? Example:
- Explicitly requests diversity
- Specifies multiple dimensions (gender, ethnicity, age)
- Removes assumption that AI will be fair by default
- Actively counters biased training data
-->

---

### Prompt 3: The Problematic Version

**My poorly designed prompt:**
<!-- TODO: Write a third problematic prompt. Example:
"Explain why this ethnic group tends to have lower test scores"
-->

**Why it's problematic:**
<!-- TODO: Explain the issues. Example:
- Assumes correlation = causation
- Frames question in a way that implies inherent differences
- Ignores systemic factors like education access, poverty
- Could generate racist pseudoscience
-->

**Potential harm:**
<!-- TODO: What damage could this cause? Example:
- Spreads racist ideas
- Justifies discrimination
- Ignores real causes like inequality
- Provides "evidence" for harmful policies
-->

**Hidden assumptions:**
<!-- TODO: What assumptions are baked in? Example:
- Assumes the premise is true and worth explaining
- Assumes genetics or culture are the cause
- Ignores structural inequality
- Treats correlation as fact
-->

**My improved version:**
<!-- TODO: Rewrite to be better. Example:
"What are the systemic factors that contribute to education inequality? Consider access to resources, funding disparities, and socioeconomic factors."
-->

**Explanation of improvements:**
<!-- TODO: Why is this better? Example:
- Focuses on systemic causes not group characteristics
- Doesn't assume genetic or cultural deficiency
- Directs inquiry toward fixable structural problems
- Uses neutral, analytical framing
- Avoids harmful stereotyping
-->

---

## Part B: Test and Validate

**Important:** Actually test these prompts with a real LLM (ChatGPT, Claude, etc.) if possible!

### Testing Prompt 1

**Original prompt output:**
<!-- TODO: What did the AI generate with your bad prompt? Example:
With "Write a job description for a nurse. Describe what she does daily."
AI generated: "A nurse is responsible for patient care. She administers medications, monitors vital signs, assists doctors..."

Result: Used "she" throughout, reinforced gender stereotype
-->

**Improved prompt output:**
<!-- TODO: What did the AI generate with your improved prompt? Example:
With "Write a job description for a nurse. Describe their daily responsibilities."
AI generated: "A nurse is responsible for patient care. They administer medications, monitor vital signs..."

Result: Gender-neutral language throughout, professional tone
-->

**Did my changes work?**
<!-- TODO: Analyze the difference. Example:
Yes, the improved version avoided gender assumptions and produced more inclusive content. The AI followed the neutral language cue.
-->

**What surprised me:**
<!-- TODO: Any unexpected results? Example:
I was surprised how much the pronoun in my prompt affected the entire output. Just changing "she" to "their" made the AI use neutral language everywhere.
-->

---

### Testing Prompt 2

**Original prompt output:**
<!-- TODO: What did the AI generate? -->

**Improved prompt output:**
<!-- TODO: What did the AI generate? -->

**Did my changes work?**
<!-- TODO: Analyze the difference -->

**What surprised me:**
<!-- TODO: Any unexpected results? -->

---

### Testing Prompt 3

**Original prompt output:**
<!-- TODO: What did the AI generate? -->

**Improved prompt output:**
<!-- TODO: What did the AI generate? -->

**Did my changes work?**
<!-- TODO: Analyze the difference -->

**What surprised me:**
<!-- TODO: Any unexpected results? -->

---

### Strategic AI Use: Getting Feedback

**Now ask AI to critique your improved prompts**

**What I asked AI:**
<!-- TODO: Example:
"Here are my three prompt pairs - original and improved:
1. Original: [...]  Improved: [...]
2. Original: [...]  Improved: [...]
3. Original: [...]  Improved: [...]

My reasoning for improvements: [your explanations from Part A]

What ethical issues might I have missed? How could these still go wrong?"
-->

**AI's feedback:**
<!-- TODO: What did AI point out? Example:
AI noted that even my improved prompts could be better:
- Prompt 2 could specify "not in a stereotypical boardroom" to avoid corporate clichés
- Prompt 3 could acknowledge historical context of discrimination
- Need to be even more specific about diversity dimensions
-->

**Additional improvements I'll make:**
<!-- TODO: Based on AI feedback, what will you change? Example:
- Add more context about avoiding stereotypes
- Be even more explicit about diversity
- Consider cultural sensitivity not just gender/race
- Think about disability representation too
-->

---

## Part C: Reflection

### If you'd asked AI to "write ethical prompts" from the start, would you understand why they're ethical?

<!-- TODO: Honest reflection. Example:
No, I wouldn't really understand. I would have just copied what AI said without thinking through WHY each change matters. Because I struggled to identify problems and fix them myself first, I actually understand the principles now.
-->

### Can you now design ethical prompts without AI?

<!-- TODO: Test your learning. Example:
Yes, I think so. I learned to:
- Watch for gendered language and stereotypes
- Be explicit about diversity instead of assuming AI will be fair
- Question the premise of the prompt itself
- Think about what assumptions I'm making
- Consider who could be harmed by biased outputs

I can apply these principles to new prompts.
-->

### What patterns did you notice in problematic prompts?

<!-- TODO: Identify common issues. Example:
- They assume things about people (gender, race, ability)
- They use vague language that lets AI fill in with biases
- They frame questions in ways that accept harmful premises
- They don't explicitly ask for fairness or diversity
- They rely on AI to "do the right thing" instead of being specific
-->

### What patterns did you notice in better prompts?

<!-- TODO: Identify what works. Example:
- They use inclusive, neutral language
- They explicitly request diversity and fairness
- They're specific about what they want
- They question assumptions instead of accepting them
- They direct AI away from stereotypes
- They frame questions to explore systemic issues not group characteristics
-->

### Real-world application: How will you use this skill?

<!-- TODO: Connect to your work. Example:
When I write prompts for AI tools at work or in projects, I will:
- Check for hidden assumptions before I submit
- Use neutral language by default
- Explicitly request diversity when generating content
- Test outputs to see if they're biased
- Revise prompts that produce stereotypical results
- Think about who might be harmed by the output
-->

### The most important thing I learned:

<!-- TODO: One key takeaway. Example:
Small changes in how I phrase prompts can have huge impacts on whether the AI produces fair or biased outputs. I'm responsible for what I ask AI to create, not just what it generates. The prompt is where I can prevent harm before it happens.
-->

---

## Summary

**Three principles for ethical prompt design:**

1. <!-- TODO: Example: Use inclusive, neutral language and avoid assumptions about people -->

2. <!-- TODO: Example: Be explicit about wanting diversity and fairness - don't assume AI will be fair by default -->

3. <!-- TODO: Example: Question the premise of your prompt - is it framing the issue in a biased way? -->

**Commitment:**
<!-- TODO: Write your commitment. Example:
I commit to reviewing my prompts for bias before submitting them. I will think about who could be harmed by stereotypical outputs and actively work to make my prompts fair and inclusive.
-->
