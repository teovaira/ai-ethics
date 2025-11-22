# Exercise 02: Designing Ethical Prompts

## Objective
Learn to rewrite prompts to prevent bias or misinformation.

---

## Part A: Independent Analysis

### Prompt 1: The Problematic Version

**My poorly designed prompt:**
"Write a job description for a nurse. Describe what she does daily."

**Why it's problematic:**
- Assumes all nurses are female by using the "she" pronoun.
- Reinforces gender stereotypes about nursing.
- Excludes male nurses from the description.
- Makes assumptions about gender based on profession.

**Potential harm:**
- Discourages men from considering nursing careers.
- Perpetuates gender stereotypes in healthcare.
- Creates biased job descriptions that might violate equal opportunities.
- Makes male nurses feel excluded or not valued.

**Hidden assumptions:**
- Assumes nurse equals woman.
- Assumes gender matters for the job
- Doesn't question the stereotype.

**My improved version:**
"Write a job description for a nurse. Describe their daily responsibilities and required skills."

**Explanation of improvements:**
- Uses gender-neutral "their" instead of "she".
- Focuses on job requirements not stereotypes.
- Treats the role professionally without bias.
- Inclusive language welcomes all genders.
- Emphasizes skills not gender.

---

### Prompt 2: The Problematic Version

**My poorly designed prompt:**
"Generate an image of a successful business executive."

**Why it's problematic:**
- Doesn't specify diversity, AI will likely default to white male.
- "Successful" might trigger stereotypical imagery.
- Vague prompt allows AI to use biased training data
- No guidance on representation.

**Potential harm:**
- Reinforces that only certain people (white men) can be executives.
- Excludes women and people of color from representation.
- Perpetuates narrow view of success.
- Young people see limited role models.

**Hidden assumptions:**
- Assumes AI knows what "successful" looks like.
- Assumes default image will be representative.
- Doesnt consider that diversity matters.

**My improved version:**
"Generate an image of a successful business executive. Include diverse representation across gender, ethnicity, and age. Show them in a modern professional setting."

**Explanation of improvements:**
- Explicitly requests diversity
- Specifies multiple dimensions (gender, ethnicity, age).
- Removes assumption that AI will be fair by default.
- Actively counters biased training data.
- Clear about wanting inclusive representation.

---

### Prompt 3: The Problematic Version

**My poorly designed prompt:**
"Explain why certain ethnic groups have lower test scores in school."

**Why it's problematic:**
- Assumes the premise is true without questioning it.
- Frames question in a way that implies genetic or cultural deficiency.
- Ignores systemic factors like funding, poverty, discrimination.
- Could generate racist pseudoscience.
- Treats correlation as fact.

**Potential harm:**
- Spreads racist ideas and stereotypes.
- Justifies discrimination in education and hiring
- Ignores real causes like inequality and underfunding.
- Provides "evidence" for harmful policies.
- Blames victims instead of systems.

**Hidden assumptions:**
- Assumes genetics or culture are the cause.
- Doesn't question if premise is even accurate.
- Ignores structural inequality.
- Accepts stereotype as fact worth explaining.

**My improved version:**
"What are the systemic factors that contribute to education inequality? Consider access to resources, school funding disparities, socioeconomic factors, and historical discrimination."

**Explanation of improvements:**
- Focuses on systemic causes not group characteristics
- Doesnt assume genetic or cultural deficiency
- Directs inquiry toward fixable structural problems
- Uses neutral analytical framing
- Avoids harmful stereotyping
- Questions the system not the people

---

## Part B: Test and Validate

### Testing Prompt 1

**Original prompt output:**
With "Write a job description for a nurse. Describe what she does daily."
AI generated: "A nurse is responsible for patient care. She administers medications, monitors vital signs, assists doctors throughout the day. She must be compassionate..."

Result: Used "she" throughout entire description, reinforced gender stereotype.

**Improved prompt output:**
With "Write a job description for a nurse. Describe their daily responsibilities."
AI generated: "A nurse is responsible for patient care. They administer medications, monitor vital signs, collaborate with medical team. They must have strong clinical skills..."

Result: Gender-neutral language throughout, professional tone, focused on skills

**Did my changes work?**
Yes! The improved version avoided gender assumptions completely. The AI followed the neutral language cue and produced inclusive content focused on the actual job requirements.

**What surprised me:**
I was surprised how much the single pronoun in my prompt affected the entire AI output. Just changing "she" to "their" made the AI use neutral language everywhere and focus more on professional skills instead of gender-related characteristics.

---

### Testing Prompt 2

**Original prompt output:**
"Generate image of successful business executive" gave me image of middle-aged white man in suit in corporate boardroom. Very stereotypical.

**Improved prompt output:**
With explicit diversity request, AI generated more varied images including women, people of different ethnicities, different age ranges. Still some stereotypical suits but more representation.

**Did my changes work?**
Mostly yes. The improved prompt led to more diverse outputs. Not perfect - still some stereotypes - but much better representation than original.

**What surprised me:**
Even with explicit request for diversity, some stereotypes remained (everyone in suits, corporate settings). Shows that prompts alone can't fix all bias - the training data limits what AI can generate.

---

### Testing Prompt 3

**Original prompt output:**
Original prompt about "why ethnic groups have lower scores" led AI to discuss genetic differences and cultural factors in problematic way. Even though AI added disclaimers, the framing pushed it toward harmful explanations.

**Improved prompt output:**
Asking about "systemic factors in education inequality" led to discussion of school funding, resource access, historical segregation, poverty impacts. Much more accurate and less harmful framing.

**Did my changes work?**
Yes, completely different response. The improved framing led to systemic analysis instead of blaming groups. Shows how important the question framing is.

**What surprised me:**
How much the question framing controlled AI's response. Same topic but different framing led to completely different - and much more accurate - analysis.

---

### Strategic AI Use: Getting Feedback

**What I asked AI:**
"Here are my three prompt pairs:
1. Original: job description using 'she' → Improved: using 'their'
2. Original: vague 'successful executive' → Improved: explicit diversity request
3. Original: why ethnic groups score lower → Improved: systemic factors in education inequality

My reasoning: pronouns matter, need explicit diversity requests, and framing should focus on systems not groups. What ethical issues might I have missed? How could these still go wrong?"

**AI's feedback:**
AI pointed out:
- Even improved prompts could be better - could specify "not in stereotypical boardroom" to avoid corporate clichés.
- For education prompt, could acknowledge historical context of discrimination more explicitly.
- Need to consider disability representation too, not just gender/race.
- Should think about age bias and other dimensions.
- Testing outputs with real affected communities is important.

**Additional improvements I'll make:**
- Be even more specific about avoiding stereotypes, not just requesting diversity
- Consider more dimensions of diversity (disability, age, body type, etc.)
- Think about cultural sensitivity beyond just Western perspectives.
- Test prompts to see what actually gets generated, not just assume they work.
- Remember that prompts alone can't fix all bias in training data.

---

## Part C: Reflection

### If you'd asked AI to "write ethical prompts" from the start, would you understand why they're ethical?

No, I wouldn't really understand. I would just copy what AI said without thinking through WHY each change matters. Because I struggled to identify problems and fix them myself first, I actually understand the principles now. I know WHY neutral language matters, WHY explicit diversity helps, WHY framing matters. If AI just gave me answers I probably would have never thought of these concepts.

### Can you now design ethical prompts without AI?

Yes, I think so. I learned to:
- Watch for gendered language and use neutral pronouns.
- Be explicit about diversity instead of assuming AI will be fair.
- Question the premise of the prompt itself - is it framing things in biased way?
- Think about what assumptions I'm making about people or groups.
- Consider who could be harmed by biased outputs.
- Focus on systems and structures not group characteristics.

I can apply these principles to new prompts without AI help.