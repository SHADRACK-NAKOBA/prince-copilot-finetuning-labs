# Lab 1: Build a business launch pack with Microsoft Copilot in Edge

[← Back to README](../README.md) · Next lab: [Fine-tune a language model →](02-fine-tune-a-language-model.md)

| | |
|---|---|
| **Time** | 45–60 minutes |
| **Cost** | Free (personal Microsoft account) |
| **Code** | None |
| **You'll produce** | A business plan with a logo (Word), financial projections with a chart (Excel), a 3-slide investor deck (PowerPoint) and an investor email (Outlook) |

## Scenario

You're launching a commercial cleaning company in New York City. Before meeting investors you need market research, a business plan, a 5-year profit projection, a pitch deck and an outreach email, all in one afternoon. You'll use **Copilot in Microsoft Edge** as your assistant across Word, Excel, PowerPoint and Outlook on the web.

## What's fixed in this version

| Problem in older guides | What to do here |
|---|---|
| The *Business Idea* download link pointed to a broken copy | It's in this repo: [`assets/Business-Idea.docx`](../assets/Business-Idea.docx) |
| "Set conversational style to **More Balanced**" no longer exists | Leave Copilot on its **default** mode. If you see a deep-reasoning mode (e.g. **Think Deeper**), don't use it here; it's slower and not needed |
| Copilot says it can't see the document | Turn on **context clues** (Step 0.3), or attach the file with **+** in Copilot |
| `$10, 000` in the profit prompt (stray space) | Use the corrected prompt in Step 3 |
| Copilot's table doesn't paste cleanly into Excel | Use the ready-made [`assets/financial-projections.csv`](../assets/financial-projections.csv) |
| Work/school account shows a different Copilot (or none) | Use a **personal** Microsoft account profile in Edge (Step 0.1) |

---

## Step 0: Get ready (5 minutes)

### 0.1 Sign in to Edge with a personal Microsoft account

1. Open **Microsoft Edge**. Update it first: **…** (top right) → **Help and feedback** → **About Microsoft Edge**, and let it update. Restart if asked.
2. Click the **profile icon** (top left) → **Add profile** / **Sign in** → sign in with your **personal Microsoft account** (outlook.com, hotmail.com or live.com).

   > No personal account? Create one free at https://signup.live.com.

### 0.2 Open OneDrive

1. In that profile, go to https://onedrive.live.com and sign in. Close any welcome pop-ups.
2. Open **My files** → **Documents**. Everything you create goes here.

### 0.3 Make sure Copilot can read the page

1. Click **…** in the Edge toolbar → **Settings** → search **Copilot**.
2. Turn **on** *Allow Copilot to read context clues on the web* (the name may be *Allow Copilot to access page content*).
3. Check that the **Copilot icon** appears at the top right of the Edge toolbar. If it doesn't, see [Troubleshooting #1](#troubleshooting).

---

## Step 1: Explore a document and research the idea (10 minutes)

1. Download the business idea document: open
   `https://github.com/SHADRACK-NAKOBA/prince-copilot-finetuning-labs/raw/main/assets/Business-Idea.docx`
   It saves to your **Downloads** folder.
2. In OneDrive → **Documents**, click **+ Create or upload** (or **+ Add new**) → **Files upload** → choose `Business-Idea.docx`.
3. Click the uploaded file. It opens in **Word for the web**.
4. Read it: a NYC office-cleaning business, eco-friendly products, local contractors, $10,000 start-up budget.
5. Click the **Copilot icon** in the Edge toolbar. The Copilot pane opens on the right. Make sure the **Chat** view is selected.
6. Type this prompt and press **Enter**:

   ```text
   Summarize this document into 5 key points, and suggest next steps.
   ```

7. If Copilot asks for permission to use the page, click **Allow**.

   ✅ **Expected:** 5 points (commercial focus, green products, local contractors, $10,000 budget, growing green-cleaning market) and next steps such as registering the business, insurance and marketing.

   > ⚠️ If Copilot says it can't read the document, click **+** next to the chat box → **Upload** → choose `Business-Idea.docx` from Downloads, then send the same prompt.

8. Ask a follow-up:

   ```text
   How do I go about setting up a business in New York?
   ```

   ✅ **Expected:** steps such as choosing a business structure, registering with New York State, getting an EIN, licences and insurance, with links to sources.

   > 💡 Copilot answers from the public web. It's a starting point, not legal or financial advice.

---

## Step 2: Create the business plan and logo (15 minutes)

1. With the document still open, ask Copilot:

   ```text
   Suggest a name for my cleaning business
   ```

2. Pick a name you like and tell Copilot, for example:

   ```text
   Let's go with the first one.
   ```

3. Ask for the plan:

   ```text
   Based on the contents of this document, create a business plan for my cleaning business.
   ```

   ✅ **Expected:** sections such as Executive Summary, Company Description, Market Analysis, Services, Marketing, Operations and Financial Plan, using your chosen name.

4. Create the Word document:
   1. In the Word tab, click **File** → **New** → **Blank document**. Close the **Designer** pane if it opens.
   2. Click the title **Document** at the top → rename it to `Business Plan` → press **Enter**.
5. In the Copilot pane, hover over the plan → click **Copy** (the copy icon under the answer). Paste into **Business Plan** with **Ctrl+V**. Delete any Copilot chatter such as "Sure! Here's…".
6. Ask for a logo:

   ```text
   Create a corporate logo for the cleaning company. The logo should be round and include an iconic New York landmark.
   ```

7. Iterate until you like it, for example:

   ```text
   Make it green and blue, with a simple flat design.
   ```

   > 💡 Image text often has spelling mistakes. Ask for **"no text in the logo"** and add the company name yourself in Word.

8. Right-click the logo you prefer → **Copy image**. In Word, click at the very top of the document → **Ctrl+V**. Resize it with the corner handles.

   ✅ **Checkpoint:** *Business Plan* in OneDrive → Documents, with your logo at the top. Word for the web saves automatically.

9. Close the Word tab and go back to **OneDrive → Documents**.

---

## Step 3: Generate and chart financial projections (10 minutes)

1. Ask Copilot (corrected prompt):

   ```text
   Create a table of projected profits for the next 5 years, starting with this year. The profit this year should be $10,000 and it should increase by 12% each year.
   ```

   ✅ **Expected values** (12% growth each year):

   | Year | Projected Profit |
   |---|---|
   | 2026 | $10,000.00 |
   | 2027 | $11,200.00 |
   | 2028 | $12,544.00 |
   | 2029 | $14,049.28 |
   | 2030 | $15,735.19 |

   > If Copilot's numbers differ, tell it: *"Recalculate: multiply the previous year by 1.12."*

2. Create the workbook:
   - If Copilot shows **Edit in Excel**, click it.
   - Otherwise: OneDrive → **+ Create or upload** → **Excel workbook**. Click cell **A1**, then copy the table from Copilot and paste it.
   - **Fastest fix if the paste is messy:** download [`assets/financial-projections.csv`](../assets/financial-projections.csv), then in Excel for the web, copy its contents in, or upload the CSV to OneDrive and open it.
3. Rename the workbook to `Financial projections` (click the title at the top).
4. Ask Copilot:

   ```text
   What's a good way to visualize these projections in a chart?
   ```

   then:

   ```text
   How do I create a line chart in Excel?
   ```

5. Follow its guidance, or do this:
   1. Select **A1:B6** (both columns, header included).
   2. **Insert** → **Line chart** (or **Recommended charts** → **Line**) → choose the first **Line** style.
6. If the chart shows two lines, or the years plotted as values:
   1. Click the chart → **Chart** tab (or right-click) → **Select Data**.
   2. Set **Year** as the **horizontal (category) axis labels**, and keep only **Projected Profit** as a series.
7. Give the chart the title `Projected Profit 2026–2030`.

   ✅ **Checkpoint:** one rising line, from $10,000 to about $15,735.

8. Close the Excel tab and go back to **OneDrive → Documents**.

---

## Step 4: Build the investor presentation (15 minutes)

### Slide 1: Title

1. OneDrive → **+ Create or upload** → **PowerPoint presentation**. Close **Designer** if it opens.
2. Rename it to `Business Presentation`.
3. Title: your company name. Subtitle: `Investor Opportunity`.

### Slide 2: Benefits

1. **Home** → **New Slide** (arrow) → **Two Content**.
2. Title: `Benefits of Hiring a Commercial Cleaner`.
3. Ask Copilot:

   ```text
   Write a summary of the benefits of using a corporate cleaning company for your business. The summary should consist of five short bullet points.
   ```

4. Copy the bullets into the **left** placeholder. Delete Copilot's opening sentence.
5. Ask Copilot:

   ```text
   Create a photorealistic image of a clean office.
   ```

6. Right-click the image you like → **Copy image** → click the **right** placeholder → **Ctrl+V**.
7. If **Designer** opens, pick a design you like, then close it.

### Slide 3: Professional staff (image analysis)

1. Download the photo: open
   `https://github.com/SHADRACK-NAKOBA/prince-copilot-finetuning-labs/raw/main/assets/mopping.png`
   It saves to **Downloads**.
2. In the Copilot pane, click **+** (next to the chat box) → **Upload image** → choose `mopping.png`. Type:

   ```text
   What does this image show?
   ```

   ✅ **Expected:** a person mopping a floor in an office or commercial space, cleaning equipment, a wet-floor sign or similar.

3. Follow up:

   ```text
   Would this image be helpful to promote a commercial cleaning business?
   ```

   Copilot gives an opinion, like a colleague would.

4. In PowerPoint: **New Slide** → **Two Content**. In one placeholder click the **Pictures** icon → **This device** → `mopping.png`.
5. Ask Copilot:

   ```text
   Write a short paragraph to accompany this image, emphasizing the professionalism of the cleaning staff we employ.
   ```

   Paste the text into the empty placeholder and edit it.
6. Ask Copilot:

   ```text
   Suggest a good title for a slide that contains the image and text.
   ```

   Use the title you like. Open **Design** → **Designer** to style the slide.

   ✅ **Checkpoint:** a 3-slide deck: title, benefits with an office image, professional staff with the mopping photo.

7. Close the PowerPoint tab.

---

## Step 5: Write the investor email (5 minutes)

1. In OneDrive, click the **App launcher** (the 3×3 dots, top left) → **Outlook**.
2. Click **New mail**. **To:** your own email address. **Subject:** `Business funding meeting request`.
3. In the Copilot pane:

   ```text
   Write an email to a bank manager requesting a meeting to discuss funding for a commercial cleaning business. The email should be concise and the tone should be professional.
   ```

4. Copy the body into your email. Replace placeholders like `[Your Name]` and `[Company Name]`.
5. Click **Send** (to yourself), or save it as a draft.

   ✅ **Checkpoint:** a professional email in your inbox or Drafts.

---

## Clean up

Nothing costs money in this lab. Optionally delete *Business-Idea*, *Business Plan*, *Financial projections* and *Business Presentation* from OneDrive, and the test email.

## Troubleshooting

| # | Problem | Cause | Fix |
|---|---|---|---|
| 1 | **Copilot icon is missing** or the pane won't open | Edge is out of date, signed in with a work account whose admin disabled Copilot, or the icon is hidden | Update Edge (Step 0.1). Use a **personal** account profile. **Settings** → search *Copilot* → turn on the setting that shows the Copilot button on the toolbar. Restart Edge |
| 2 | Copilot replies "I can't access this page" | Context clues / page access is off, or the Word page is protected | Turn on context clues (Step 0.3). Or attach the .docx with **+** in Copilot |
| 3 | **Image upload fails** (mopping.png) | File in a network/OneDrive-only or protected folder, or too large | Save it to **Downloads** or **Desktop** first, then upload again with **+** |
| 4 | Copilot won't create images | Image creation limits or the request was blocked | Wait a few minutes and try again. Rephrase simply: *"Draw a round logo with the Statue of Liberty, green and blue, no text"* |
| 5 | Logo or image has misspelled text | Image models are weak at text | Ask for "no text" and add text in Word/PowerPoint |
| 6 | **Excel chart shows wrong values** or two lines | Table pasted with extra spaces/rows, or Year used as a series | Use [`financial-projections.csv`](../assets/financial-projections.csv). Select **A1:B6** → **Insert → Line**. Fix the axis with **Select Data** (Step 3.6) |
| 7 | Numbers in the projection are wrong | The model did the maths in its head | Ask it to recalculate (×1.12 each year) or check against the table in Step 3 |
| 8 | **Screen doesn't match these steps** | Copilot and Office for the web change often | Follow the **labels** (Copy, +, Insert, Designer), not the exact position. Search Edge settings for "Copilot" if a toggle seems missing |
| 9 | "Save a copy to OneDrive" doesn't appear | The .docx downloaded instead of opening | That's expected. Upload it to OneDrive (Step 1.2) |

## What you learned

- Use Copilot in Edge to **summarize** a document and **research** next steps.
- Generate **long-form content** (a business plan) and **images** (logo, office photo), then edit them in Office for the web.
- Generate **data** and turn it into a **chart**, checking the maths.
- Use Copilot for **image understanding** (what's in this photo, is it useful?).
- Draft a **professional email** in seconds.

Next lab: [Fine-tune a language model →](02-fine-tune-a-language-model.md)
