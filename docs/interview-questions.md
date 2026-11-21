# Interview questions

[← Back to README](../README.md)

## Your 60-second pitch

> "I completed three generative AI projects on Microsoft's stack, covering the use, customise and build path. First, I used Copilot in Edge to turn a one-page business idea into a business plan, financial projections with a chart, an investor deck and an email, checking the AI's numbers along the way. Second, I fine-tuned gpt-4.1 in Microsoft Foundry with supervised fine-tuning, after baselining the base model with a strong system prompt, and compared both with a scorecard for tone, follow-up questions and rule-following. I used Global training and a Developer deployment to keep costs low. Third, I built a Copilot Studio agent that answers HR and IT policy questions from an employee handbook using RAG with citations, added five topics, and turned off general knowledge and web search so it refuses off-topic requests. I tested in-scope and out-of-scope questions before calling it done."

## Lab 1: Copilot

**1. What is Copilot in Edge good for, and where do you need to be careful?**
Summarising pages and documents, drafting content, generating images and simple data. Be careful with facts, numbers and legal/financial advice: it's grounded on web results and can be wrong, so you verify.

**2. Copilot gave the wrong 5-year projection. How do you handle it?**
Check the maths independently (×1.12 per year), ask it to recalculate step by step, or compute it in Excel with a formula. Never paste AI numbers into an investor deck unchecked.

**3. What's the difference between Copilot in Edge (personal account) and Microsoft 365 Copilot?**
The personal Copilot uses public web and the page you share. Microsoft 365 Copilot is licensed per user, works inside the tenant, and can use work data (mail, files, Teams) with enterprise data protection and admin controls.

## Lab 2: Fine-tuning

**4. When would you fine-tune instead of prompt engineering?**
When you need a behaviour or style **consistently**, a long prompt is costly or unreliable, or you want a smaller/cheaper model to match a bigger one. Try prompt engineering (and RAG for knowledge) first.

**5. Fine-tuning vs RAG?**
Fine-tuning changes **behaviour** (tone, format, rules). RAG supplies **knowledge** at question time (current, citable). Policies that change → RAG. Brand voice → fine-tuning. Often you use both.

**6. What does SFT training data look like?**
JSONL, one conversation per line: system, user and assistant messages. The assistant message is the ideal answer the model should learn. Azure needs at least 10 examples; real projects use hundreds.

**7. Why gpt-4.1 and not gpt-5 for this lab?**
Supervised fine-tuning is supported on gpt-4.1 / gpt-4.1-mini. gpt-5 only supports reinforcement fine-tuning, which is invitation-only.

**8. Global vs Standard training? Developer vs Standard deployment?**
Global training is cheaper per token but has no data-residency guarantee. A Developer deployment is pay-per-token with no hourly hosting fee and a 24-hour life, made for evaluation. Standard/Global deployments add an hourly hosting fee but are for production.

**9. How did you evaluate the fine-tuned model?**
Same system prompt, same questions for both models, scored on explicit criteria (tone, follow-up question, avoids banned recommendations, handles off-topic). In production: a larger test set, automated evaluators and a hold-out validation file.

**10. What are the risks of fine-tuning?**
Overfitting on a small dataset, baking in mistakes from bad examples, cost of training and hosting, retraining when the base model retires, and losing general ability if the data is too narrow.

## Lab 3: Copilot Studio

**11. How does RAG work in Copilot Studio?**
The agent searches its knowledge sources (files, SharePoint, websites) for relevant passages, then generates an answer grounded in them, with citations.

**12. Topics vs generative answers: when do you use each?**
Topics for predictable, scripted flows (report an incident, contact HR, collect details). Generative answers from knowledge for the long tail of questions. Generative orchestration chooses between them using descriptions.

**13. How did you stop the agent answering off-topic questions?**
Turned off general knowledge and web search, wrote explicit refusal rules in the instructions, and tested off-topic prompts. It's not a 100% guarantee, so testing matters.

**14. The agent gives an answer that isn't in the handbook. What do you check?**
General knowledge setting, the activity map (which source/topic was used), whether the file is **Ready**, the instructions ("never guess"), and whether you started a fresh test conversation after changes.

**15. How would you take this to production?**
Use SharePoint as the source so HR updates the policy in one place, add authentication, publish to Teams, monitor analytics (resolution rate, escalations), add escalation to a human, and review answers regularly.

**16. Why use a fictional handbook in a lab, and what about real data?**
To avoid exposing real company or personal data. With real data: respect permissions (users see only what they can access), data-loss-prevention policies and the organisation's AI usage rules.
