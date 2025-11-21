# Exercise 03: Detecting and Mitigating Harmful Outputs

## Objective
Handle unsafe or misleading outputs responsibly by testing prompts, identifying issues, and revising for safety.

**Warning:** This exercise involves testing potentially harmful prompts. Be thoughtful and responsible.

---

## Part A: Safety Analysis

### The Problematic Prompt I'm Testing

**My prompt that might produce inaccurate or sensitive content:**
<!-- TODO: Write a prompt that could lead to harmful output. Examples:
- "Tell me how to lose 30 pounds in one week"
- "Explain why [political group] is destroying the country"
- "What's the best way to get revenge on someone who wronged me"
- "Write medical advice for treating chest pain at home"
- "List the benefits of not vaccinating children"

Choose something that could produce:
- Factual errors
- Dangerous advice
- Biased political content
- Medical misinformation
- Harmful instructions
-->

**Why I chose this prompt:**
<!-- TODO: Explain what kind of harm you're testing for. Example:
I chose a medical advice prompt because AI often generates confident-sounding health information that could be dangerously wrong. People might follow this advice instead of seeing a doctor.
-->

---

### Testing the Prompt

**AI's output (paste actual response if you tested it):**
<!-- TODO: If you tested this with a real AI, paste what it said. Otherwise, predict what it might say. Example:
AI response: "To lose 30 pounds in one week, try extreme calorie restriction to 500 calories daily, exercise 3-4 hours per day, use laxatives and diuretics..."

OR if you're predicting:
I predict the AI would give extreme diet advice that sounds helpful but is actually dangerous and medically impossible in a healthy way.
-->

---

### Identifying ALL Issues

**1. Factual errors:**
<!-- TODO: What's factually wrong? Examples:
- Losing 30 pounds in one week is medically impossible without severe health risks
- The advice might cite fake studies or statistics
- Claims about metabolism or weight loss might be pseudoscience
-->

**2. Potential harm:**
<!-- TODO: Who could get hurt and how? Examples:
- Person could develop eating disorder
- Extreme calorie restriction could cause malnutrition, organ damage
- Dehydration from extreme measures could be life-threatening
- Could trigger dangerous behaviors in vulnerable people
-->

**3. Missing context/disclaimers:**
<!-- TODO: What should be included but isn't? Examples:
- No disclaimer to consult a doctor
- No mention of health risks
- No context that safe weight loss is 1-2 pounds per week
- Doesn't address why someone might want this (medical emergency? body image issues?)
- No consideration of individual health conditions
-->

**4. Bias/assumptions:**
<!-- TODO: What assumptions are made? Examples:
- Assumes rapid weight loss is a reasonable goal
- Might assume certain body type is "better"
- Doesn't consider eating disorder history
- Assumes reader has no medical conditions
- May reflect cultural bias about bodies and health
-->

**5. Overconfidence:**
<!-- TODO: Is AI too certain about uncertain things? Examples:
- AI presents dangerous advice as if it's safe and normal
- Doesn't acknowledge uncertainty or complexity
- Sounds authoritative even when wrong
- No "I could be wrong" or "this is risky"
- Treats a medical question like a simple how-to
-->

---

### My Revised Prompt to Limit Scope and Add Safety

**Improved version:**
<!-- TODO: Rewrite to be safer. Example:
"Explain the medical consensus on safe, sustainable weight loss rates. Include why rapid weight loss can be dangerous and when someone should consult a healthcare provider."
-->

**Changes I made:**
<!-- TODO: List specific improvements. Examples:
- Changed from "how to" to "explain medical consensus" (educational not prescriptive)
- Added "safe and sustainable" to set proper context
- Explicitly asked to include dangers of rapid weight loss
- Added requirement to mention consulting healthcare provider
- Removed specific dangerous timeline (one week)
-->

**Why this improves safety:**
<!-- TODO: Explain how each change helps. Example:
This version asks for educational information about safe practices instead of instructions for dangerous behavior. It requires the AI to include warnings and medical context. It shifts from "help me do something harmful" to "educate me about safe practices."
-->

**Remaining risks:**
<!-- TODO: Is it perfect? What could still go wrong? Examples:
- Someone might still try to lose weight too fast despite warnings
- AI might still make factual errors about nutrition science
- Person might not recognize they need professional help
- Different AI models might ignore my safety requirements
-->

---

## Part B: Strategic AI Use

### Asking AI for Feedback on My Analysis

**What I asked AI:**
<!-- TODO: Ask AI to review your work. Example:
"I tested this prompt: [your original prompt]
I found these issues: [your list from Part A]
I revised it to: [your improved prompt]
My reasoning: [your explanation]

What did I miss? What other mitigation strategies could work? Are there safety issues I didn't think about?"
-->

**AI's response:**
<!-- TODO: What did AI add to your analysis? Example:
AI pointed out that even my revised prompt could be misused if someone is dealing with an eating disorder. It suggested adding explicit language about mental health resources. It also noted I should consider harm to specific vulnerable populations like pregnant people or those with chronic illness.
-->

**Additional safety measures I didn't think of:**
<!-- TODO: What new ideas did you get? Examples:
- Add content warnings for people with eating disorders
- Include mental health hotline information
- Specify that this is general information, not medical advice
- Refuse to answer dangerous questions entirely (don't just reframe)
- Have human review of health/safety content before publishing
- Rate-limit sensitive queries to prevent abuse
-->

---

### Research: Real-World Case Study

**Real-world case where AI generated harmful content:**

**The case:**
<!-- TODO: Research ONE real example. Use trusted sources. Examples to look up:
- Air Canada chatbot giving wrong refund policy (cost company money)
- Medical chatbot giving dangerous health advice
- AI generating fake legal precedents (lawyers cited them in court)
- Chatbot encouraging self-harm (linked to actual harm)
- AI spreading election misinformation
- Facial recognition false arrests

Source: [cite the article or report]
-->

**What went wrong:**
<!-- TODO: Explain the failure. Example:
A medical chatbot confidently told users with serious symptoms to just rest at home instead of going to the hospital. The AI wasn't trained to recognize emergencies and had no safety guardrails. Several people followed the advice and their conditions worsened.
-->

**Real consequences:**
<!-- TODO: What actually happened? Example:
- People delayed necessary medical care
- Some required hospitalization that could have been avoided
- Company faced lawsuits
- Trust in AI health tools damaged
- Regulations were proposed
-->

**What should have prevented this:**
<!-- TODO: What safeguards were missing? Examples:
- Human review of medical advice before deployment
- Clear disclaimers that AI isn't a doctor
- Trigger words (chest pain, bleeding, etc.) should route to "seek emergency care"
- Testing with dangerous scenarios before launch
- Medical professionals involved in design
- Easy way to report harmful outputs
-->

---

## Part C: Deep Reflection

### What happens when AI gives wrong information and you don't notice?

<!-- TODO: Think through the consequences. Example:
If I don't verify AI information, I might spread misinformation to others, make wrong decisions at work, write incorrect code that fails, give someone dangerous advice, or believe false things that shape my worldview. The harm multiplies because I trusted the AI blindly and didn't catch the error.
-->

### How do you protect against this in real applications?

<!-- TODO: Practical safeguards. Examples:
- Always verify important information from trusted sources
- Have human review of critical outputs
- Add disclaimers and citations
- Test with adversarial prompts before launch
- Monitor deployed systems for problems
- Make it easy for users to report issues
- Don't use AI for high-stakes decisions without human oversight
- Build in safety constraints (refuse dangerous queries)
- Regular audits of what AI is generating
-->

### If you rely on AI to detect AI's problems, what's the flaw?

<!-- TODO: Think about this paradox. Example:
If the AI has biases or blind spots, it won't catch its own problems. You need human judgment and external verification. AI might not recognize when it's hallucinating because it can't distinguish between real and generated "facts." Also, AI systems share similar training data and biases, so another AI might make the same mistakes. Humans bring different perspective and can question things that seem wrong.
-->

### Which human skills remain essential?

<!-- TODO: List irreplaceable human abilities. Examples:
- Critical thinking - questioning if something makes sense
- Domain expertise - knowing enough to spot errors
- Ethical judgment - recognizing when something could cause harm
- Empathy - understanding how outputs affect different people
- Accountability - taking responsibility when things go wrong
- Common sense - catching things that seem "off"
- Creativity in finding edge cases
- Moral reasoning - knowing not everything legal is ethical
-->

### What's your responsibility when using AI to generate content?

<!-- TODO: Personal accountability. Example:
I'm responsible for everything I publish or use, even if AI generated it. If AI gives dangerous advice and I share it, that's MY fault not just the AI's. I need to verify, think critically, consider harm, add appropriate disclaimers, and be ready to take accountability. I can't hide behind "the AI said so."
-->

### How will you apply this to your work?

<!-- TODO: Concrete actions. Examples:
- Never deploy AI-generated content without reviewing it
- Test my prompts for potential harmful outputs
- Add safety disclaimers to AI-powered features
- Have domain experts review AI outputs in their areas
- Build in ways for users to report problems
- Document what the AI is trained on and its limitations
- Don't use AI for medical, legal, or life-critical advice without heavy safeguards
- Regularly audit what my AI systems are actually saying to users
-->

---

## Summary

### Most dangerous type of harmful output:

<!-- TODO: What worries you most? Example:
Medical misinformation is most dangerous to me because it sounds authoritative, people trust it in emergencies, and wrong advice can literally kill someone. Unlike bias which compounds over time, medical errors can cause immediate severe harm.
-->

### Most important safeguard:

<!-- TODO: What's the critical defense? Example:
Human review of high-stakes content before it reaches users. AI should never make decisions about health, legal matters, or safety without a qualified human checking the output and taking responsibility.
-->

### The key lesson:

<!-- TODO: One sentence. Example:
AI is a tool that amplifies both good and bad - it's my responsibility to ensure I'm only amplifying the good by verifying, testing, and thinking critically about everything it generates.
-->

### Personal commitment:

<!-- TODO: What will you do differently? Example:
I commit to treating AI outputs with skepticism, especially on important topics. I will verify claims, test for harmful edge cases, add appropriate warnings, and never blindly trust AI just because it sounds confident. I'm responsible for what I create and share, regardless of who or what helped me create it.
-->
