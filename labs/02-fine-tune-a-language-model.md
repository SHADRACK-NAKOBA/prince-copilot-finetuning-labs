# Lab 2: Fine-tune a language model in Microsoft Foundry

[← Lab 1](01-copilot-in-edge.md) · [Back to README](../README.md) · Next lab: [Copilot Studio agent →](03-copilot-studio-agent.md)

| | |
|---|---|
| **Time** | 30 minutes hands-on + 30–90 minutes waiting for training |
| **Cost** | Typically under US $1 (training is billed per token; Developer deployment has no hourly hosting fee). Delete the resource group at the end |
| **Code** | None (one optional checker script) |
| **You'll produce** | A fine-tuned `gpt-4.1` travel assistant, and a side-by-side comparison with the base model |

## Scenario

You work for a travel agency building a vacation-planning chat app. The assistant must be **friendly, inspiring and consistent**, ask follow-up questions, and **never recommend hotels, flights, rental cars or restaurants**. You'll test how far **prompt engineering** gets you with a base model, then **fine-tune** the model on example conversations and compare.

## What's fixed in this version

| Problem in older guides | What to do here |
|---|---|
| "Search for **gpt-5**" in the deploy step, but the job uses gpt-4.1 | Deploy **gpt-4.1** as the base, so you compare like with like |
| gpt-5 as the fine-tuning base | gpt-5 only supports reinforcement fine-tuning, and it's invitation-only. **Supervised** fine-tuning works on **gpt-4.1** / **gpt-4.1-mini** |
| Broken dataset link | The file is in this repo: [`assets/travel-finetune-hotel.jsonl`](../assets/travel-finetune-hotel.jsonl) |
| File saves as `.jsonl.txt` and the upload is rejected | Step 3.1 shows how to save it correctly, plus an optional checker |
| Unclear region | Use **North Central US**, **Sweden Central** or **East US 2** (they support Global training) |
| Surprise hosting costs | Use the **Developer** deployment type: no hourly fee, auto-deleted after 24 hours |
| Empty troubleshooting section | 10 common problems with fixes at the end |

## Key ideas (2-minute read)

| Term | Meaning |
|---|---|
| **Prompt engineering** | Shape behaviour with instructions. Fast and free, but the model may drift from your style |
| **Fine-tuning** | Train a copy of the model on your example conversations so the behaviour is baked in |
| **Supervised fine-tuning (SFT)** | Training on input → ideal output pairs (system, user, assistant messages) |
| **JSONL** | One JSON object per line. Each line is one training conversation |
| **Global training** | Training runs in any Azure region. Cheaper per token, no data-residency guarantee |
| **Developer deployment** | Cheap test deployment for fine-tuned models: pay per token, no SLA, lives 24 hours |
| **Baseline** | The base model's behaviour, measured first, so you can prove fine-tuning helped |

---

## Step 1: Create the Foundry project (5 minutes)

1. Go to https://ai.azure.com and sign in with your Azure account. Close any tips or quick-start panes.
2. If you see a **New Foundry** toggle at the top, turn it **on**.
3. Click **Create project** (or **+ Create new**), and fill in:

   | Field | Value |
   |---|---|
   | Project name | `prince-finetune-demo` |
   | Expand **Advanced options** | |
   | Foundry resource | keep the default (`prince-finetune-demo-resource`) |
   | Subscription | your subscription |
   | Resource group | **Create new** → `rg-prince-finetune` |
   | Region | **North Central US**, **Sweden Central** or **East US 2** |

4. Click **Create** and wait 1–3 minutes until the project home page opens.

✅ **Checkpoint:** you're on the home page of `prince-finetune-demo`.

---

## Step 2: Deploy the base model (5 minutes)

1. Click **Discover** → **Models** (or **Find models** / **Model catalog**).
2. Search **gpt-4.1** → select **gpt-4.1** (not mini or nano).
3. Click **Deploy** → keep the defaults (deployment name `gpt-4.1`, type **Global Standard**) → **Deploy**.
4. The model opens in the **playground** when it's ready.

> ⚠️ **gpt-4.1 not in the catalog or no quota?** Use **gpt-4.1-mini** for *both* the base deployment and the fine-tuning job (Step 3). The lab works the same way.

✅ **Checkpoint:** the `gpt-4.1` deployment shows **Succeeded**.

---

## Step 3: Start the fine-tuning job (10 minutes)

Training takes a while, so start it now and test the base model while it runs.

### 3.1 Download the training file correctly

1. Open this link in your browser:
   `https://raw.githubusercontent.com/SHADRACK-NAKOBA/prince-copilot-finetuning-labs/main/assets/travel-finetune-hotel.jsonl`
2. Press **Ctrl+S** (Save as).
3. Set **Save as type** to **All files (\*.\*)** and the file name to exactly `travel-finetune-hotel.jsonl`. Click **Save**.

   > ⚠️ Windows hides extensions. If your file is really `travel-finetune-hotel.jsonl.txt`, the upload fails. In File Explorer choose **View → Show → File name extensions** to check, and rename it if needed.

4. **(Optional) Check the file** if you have Python and this repo cloned:

   ```bash
   python scripts/validate_jsonl.py path/to/travel-finetune-hotel.jsonl
   ```

   ✅ **Expected:** `Examples: 10`, `~1,8xx tokens per epoch`, `✅ Looks good.`

   > 💡 The file has **exactly 10** examples, which is the minimum Azure OpenAI accepts. Don't delete any lines.

### 3.2 Configure and submit the job

1. In the left menu click **Fine-tune** (or **Fine-tuning**).
2. Click **Fine-tune** / **+ Fine-tune model** (top right).
3. Configure:

   | Setting | Value |
   |---|---|
   | Base model | **gpt-4.1** (or gpt-4.1-mini, see Step 2) |
   | Customization method | **Supervised** |
   | Training type | **Global** |
   | Training data | **Upload new dataset** → choose `travel-finetune-hotel.jsonl` |
   | Validation data | None |
   | Suffix | `ft-travel` |
   | Automatically deploy model after job completion | ✅ **Selected** |
   | Deployment type | **Developer** |
   | Hyperparameters (epochs, batch size, learning rate) | Leave the defaults |

4. Click **Submit**.

   ✅ **Expected:** the job appears with status **Queued**, then **Running**. Select it and open the **Monitor** tab to watch progress.

> ⏳ Training plus deployment typically takes **30–90 minutes** and sometimes longer, depending on capacity. Carry on with Step 4.

---

## Step 4: Test the base model (the baseline) (10 minutes)

1. In the left menu click **Models** / **Deployments** → select your **gpt-4.1** base deployment → it opens in the playground.
2. With the **Instructions** box empty or default, ask:

   ```text
   What can you do?
   ```

   ✅ **Expected:** a generic answer. You want a travel assistant.

3. Set **Instructions** to:

   ```text
   You are an AI assistant that helps people plan their travel.
   ```

   Click **Apply** / **Save** if shown, then ask `What can you do?` again.

   ✅ **Expected:** travel help, but it may offer to **book flights, hotels and cars**, which you don't want.

4. Replace **Instructions** with the full system message (this is the same one in the training file):

   ```text
   You are an AI travel assistant that helps people plan their trips. Your objective is to offer support for travel-related inquiries, such as visa requirements, weather forecasts, local attractions, and cultural norms.
   You should not provide any hotel, flight, rental car or restaurant recommendations.
   Ask engaging questions to help someone plan their trip and think about what they want to do on their holiday.
   ```

5. Ask each question below and fill in the **Base** column of the scorecard ([Step 6](#scorecard)):

   ```text
   Where in Rome should I stay?
   ```
   ```text
   I'm mostly there for the food. Where should I stay to be within walking distance of affordable restaurants?
   ```
   ```text
   What are some local delicacies I should try?
   ```
   ```text
   When is the best time of year to visit in terms of the weather?
   ```
   ```text
   What's the best way to get around the city?
   ```
   ```text
   Can you explain how blockchain works?
   ```

   Watch the **tone** (flat or lively?), whether it **asks a follow-up question**, and whether it **slips** and names hotels or restaurants.

---

## Step 5: Review the training file (5 minutes)

Open `travel-finetune-hotel.jsonl` in Notepad or VS Code. The first example, formatted for reading:

```json
{"messages": [
  {"role": "system", "content": "You are an AI travel assistant that helps people plan their trips. ... Ask engaging questions to help someone plan their trip and think about what they want to do on their holiday."},
  {"role": "user", "content": "What's a must-see in Paris?"},
  {"role": "assistant", "content": "Oh la la! You simply must twirl around the Eiffel Tower and snap a chic selfie! After that, consider visiting the Louvre Museum to see the Mona Lisa and other masterpieces. What type of attractions are you most interested in?"}
]}
```

Notice:

- Every example uses the **same system message** you tested in Step 4.
- Every assistant reply is **playful**, **inspiring**, and **ends with a question**. That's the style the model learns.
- The last example (*"Can you tell me about quantum computing?"*) teaches the model to **steer off-topic questions back to travel**.

> 💡 Real projects use **50–500+** high-quality examples. 10 is enough to see the effect in a lab.

---

## Step 6: Test the fine-tuned model and compare (10 minutes)

1. Click **Fine-tune** → select your job. When the status is **Completed**, open the **Logs** tab to see the training steps.
2. Go to **Models** / **Deployments**. Find the deployment named like `gpt-4.1-2025-04-14.ft-…-ft-travel`. Wait until its status is **Succeeded**.

   > If automatic deployment failed: open the completed job → **Deploy** → type **Developer** → **Deploy**.

3. Select the fine-tuned deployment to open it in the playground.
4. Paste the **same Instructions** as Step 4.4.
5. Ask the **same six questions** and fill in the **Fine-tuned** column.

### Scorecard

Score each answer 0–2 (0 = no, 1 = partly, 2 = yes):

| Question | Friendly, inspiring tone (Base / FT) | Ends with a follow-up question (Base / FT) | Avoids hotel/restaurant recommendations (Base / FT) |
|---|---|---|---|
| Where in Rome should I stay? | / | / | / |
| Within walking distance of affordable restaurants? | / | / | / |
| Local delicacies? | / | / | / |
| Best time of year (weather)? | / | / | / |
| Best way to get around? | / | / | / |
| How does blockchain work? (off-topic) | / | / | / |
| **Total (out of 12 each)** | / | / | / |

✅ **Expected:** the fine-tuned model sounds more like the training examples (playful, consistent, almost always ending with a question). Answers vary from run to run; judge the **behaviour**, not the exact words.

### Decide

- **Fine-tuned clearly better on the rules you care about?** Fine-tuning is worth it for this use case.
- **About the same?** Stick with prompt engineering: cheaper, and no training to maintain.
- **Want more?** Add more (and more varied) examples, especially the cases where it failed.

---

## Step 7: Clean up

1. Go to https://portal.azure.com → **Resource groups** → `rg-prince-finetune`.
2. Click **Delete resource group** → type the name → **Delete**.

The Developer deployment deletes itself after 24 hours anyway, but deleting the resource group removes everything (base deployment, fine-tuned model, files) and stops all charges.

```bash
# or from a terminal
az group delete --name rg-prince-finetune --yes --no-wait
```

---

## Troubleshooting

| # | Problem | Cause | Fix |
|---|---|---|---|
| 1 | **gpt-4.1 not in the fine-tuning base model list** | Region doesn't support it, or it's no longer offered to new customers | Use a region from Step 1. Try **gpt-4.1-mini**. If neither is listed, check the *Fine-tuning models* table on Microsoft Learn (link in README) |
| 2 | **gpt-5 can't be selected with Supervised** | gpt-5 only supports reinforcement fine-tuning (invitation-only) | Use gpt-4.1 or gpt-4.1-mini with **Supervised** |
| 3 | Upload rejected: *invalid file* / *file format not supported* | File saved as `.jsonl.txt`, or opened and re-saved by Word/Excel | Re-download (Step 3.1), save as **All files**, run `validate_jsonl.py` |
| 4 | *Training file has fewer than 10 examples* | Lines deleted or file truncated | Re-download the original file. It has exactly 10 |
| 5 | **Quota exceeded** when submitting or deploying | No fine-tuning or deployment quota in the region | Use **Global** training. Try another listed region, or request quota: **Management center → Quota** |
| 6 | Job stuck in **Queued** / **Pending** for a long time | Training capacity is busy | Wait. It often starts within an hour. Don't resubmit duplicates |
| 7 | Job **Failed** | Data or capacity issue | Open the job → read the error in **Logs** / **Details**. Validate the file, then resubmit |
| 8 | Fine-tuned model not in **Models/Deployments** | Auto-deploy failed or still running | Open the completed job → **Deploy** → **Developer** |
| 9 | The fine-tuned deployment disappeared | Developer deployments live **24 hours** | Redeploy from the completed job; the trained model is kept |
| 10 | The fine-tuned model doesn't seem different | Only 10 examples, or you changed the Instructions | Use the **exact** same system message as the training data. Compare several questions with the scorecard, not one answer |

## What you learned

- How to **baseline** a model with prompt engineering before you train anything.
- How **SFT data** is structured (system / user / assistant in JSONL) and how it teaches tone and boundaries.
- How to run a fine-tuning job in Foundry: **Supervised**, **Global** training, **Developer** deployment.
- How to **evaluate** base vs fine-tuned with the same prompts and a scorecard, and decide if fine-tuning is worth it.

Next lab: [Build a Copilot Studio agent →](03-copilot-studio-agent.md)
