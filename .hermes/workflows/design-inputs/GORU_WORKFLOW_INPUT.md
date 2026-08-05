# Goru: Workflow Design Input

Here is my concrete assessment of v1 from the Gemini 3.1 Pro seat.

## 1. What v1 gets WRONG about my seat
v1 fundamentally misunderstands the difference between "under-used capacity" and "clerical labor." It assigns me (Gemini 3.1 Pro) to Stage 3 for "bulk eligibility/audit work" and quote-checking. 

I am severely under-used if relegated to tasks a regex or Python script (`verify_quotes.py`) can do perfectly. Gemini 3.1 Pro possesses a 1-million+ token context window and native multimodal grounding. Using a frontier model to do rote clerical checklist-checking just because the seat has 99% headroom is a waste of intelligence. My capacity isn't for doing small tasks in bulk; it's for doing tasks that require holding massive, unbroken context.

## 2. Which stage I should take (and evidence)
I should take **Stage 0 (Data survey)** and/or **Stage 1 (Frontier/topic framing)** away from Hwao/Lana. 
*Evidence:* Framing a frontier or surveying archive data requires synthesizing dozens of full-text arXiv papers, database schemas, and past debate maps simultaneously. Hwao and Lana (Claude) will hit context constraints or severe degradation if you feed them 50 full papers to map a topic. My massive context window allows me to hold the entire relevant corpus in memory without chunking or RAG, ensuring no nuance or contradiction between papers is lost. I should build the global map, and Lana should write the targeted prose.

## 3. Where this workflow will BREAK in practice (Failure Mode)
The workflow will break at the transition between **Stage 4 (Reviewed script)** and **Stage 5 (Execute + funnel)**. 
*Failure mode:* Kimi does a static, pre-execution review of Hwao's script. If the script contains a runtime data-shape error—like a Pandas `.merge()` that silently drops 90% of the rows due to an unexpected NaN in the real VizieR data—Kimi will miss it because it can't see the live data during static review. When Hwao executes in Stage 5, the script will run successfully but produce a catastrophic silent data drop. The pipeline has no feedback loop for runtime data shape validation before it becomes a receipt.

## 4. What is missing entirely as a stage
**Stage 5.5: Data Sanity / Distribution Check.**
Right now, you jump from execution (5) straight to receipts (6) and drafting (7). There is no stage that asks, *"Did the script output actually make physical/statistical sense?"* You need a stage where the generated statistical distributions are sanity-checked (e.g., "Wait, why are all the galaxies suddenly at redshift z=0?"). This should be an automated statistical diff against expected bounds, reviewed by an agent, before Lana ever sees it to draft prose.

## 5. Cutting one Kimi gate
If we must cut one of the three Kimi gates to save meter costs, **cut KIMI GATE 1 (Contract freeze)** and give it to Lana (Claude CLI).

*How:* Lana acts as the adversarial reviewer against Hwao's draft contract. Lana is exceptionally strong at semantic reasoning, framing, and logical consistency.
*What we lose:* We lose Kimi's specific, paranoid instinct for spotting subtle "licences to publish a known systematic under a disclaimer." 
*Why it's worth it:* We can afford to lose Kimi here because the contract is just text. If the contract is slightly flawed, Kimi's ruthless auditing in **Gate 2 (Script review)** and **Gate 3 (Final referee)** will still catch the actual mechanical exploitation or overclaim before it lands. Kimi's metered intelligence is best spent on code logic (Gate 2) and final scientific claims (Gate 3), not negotiating the initial planning document. 

WORKFLOW_INPUT_COMPLETE
