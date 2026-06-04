# Scenario 1: Inbound-Intent Account with Dual Trigger Event

## Context

A mid-market SaaS company has recently shown intent signals (a pricing page visit and a G2 review comparing two competitors), and the SDR at a revenue intelligence platform has also spotted a cluster of relevant hiring signals and a recent funding event. The SDR works at a company called Clari (pipeline forecasting and revenue intelligence), targeting a VP of Sales at a 350-person SaaS company called Fieldwork, which makes field service management software for HVAC, plumbing, and electrical contractors. The SDR needs to synthesize these signals and produce outreach copy before the morning sequence launch.

## Input

```
TARGET ACCOUNT
Account name: Fieldwork
Account website: fieldworkhq.com
Industry/vertical: B2B SaaS — Field Service Management
Company size (employees): 350
Revenue range (if known): $25M–$40M ARR (estimated from LinkedIn headcount growth and Crunchbase funding totals)
HQ location: Scottsdale, AZ

MY ICP CRITERIA
- B2B SaaS company, 200–1000 employees
- Has a dedicated sales team of 20+ reps
- Uses Salesforce CRM (required — product integrates natively)
- Has experienced 30%+ revenue growth in last 12 months (signal: aggressive hiring)
- Series B or later
- VP Sales or CRO is primary buyer; Sales Ops / RevOps is champion
- Deals are primarily outbound-motion (not pure PLG)

MY PRODUCT / SERVICE
Product name: Clari Revenue Platform
One-sentence description: Clari captures every buyer and seller signal in Salesforce to give revenue teams an AI-driven forecast they can actually defend — and surfaces deal risk before it becomes a miss.
Core value proposition: Replace gut-feel forecasting with AI-grounded pipeline visibility so revenue leaders can call their number with confidence and reps can know which deals to prioritize.
Primary buyer persona: VP of Sales / CRO at B2B SaaS companies with outbound-led motions

ACCOUNT SIGNALS

Funding / financial events:
- Raised $30M Series C led by Bessemer Venture Partners, closed April 2026 (Crunchbase)
- Total funding: $58M

Hiring velocity / job postings:
- 6 open roles on LinkedIn posted in last 30 days: 2x Account Executive (Mid-Market), 1x Sales Development Representative, 1x Revenue Operations Analyst, 1x Sales Enablement Manager, 1x Director of Sales Operations
- LinkedIn headcount grew from 280 to 350 employees in the last 6 months (25% headcount growth)

Tech stack indicators:
- Salesforce CRM confirmed via BuiltWith (updated 14 days ago)
- Outreach.io confirmed as SEP (sales engagement platform) via BuiltWith
- No revenue intelligence or forecasting tool detected (no Clari, Gong, Chorus, or Bowtie signatures visible)

Leadership changes:
- No recent C-suite change detected
- Current VP of Sales: Marcus Webb (confirmed LinkedIn, 18 months in role, joined from Zendesk)

Recent news / press / announcements:
- April 2026 Series C press release mentions "accelerating go-to-market and expanding enterprise sales team"
- G2 page shows 3 recent customer reviews (March–April 2026) citing "strong product" but "sales process is manual and we don't get visibility until end of quarter"

Intent signals:
- Clari pricing page visited 3 times in the last 14 days (HubSpot / intent data from Bombora — "Revenue Operations Software" topic surge: 85th percentile)
- Compared Clari vs. Gong on G2 3 days ago (tracked via G2 Buyer Intent)

Other signals:
- Job description for Director of Sales Operations includes "own forecasting accuracy and CRM hygiene" as first listed responsibility — signals the company recognizes it has a forecasting problem

OUTREACH PREFERENCES
Preferred tone: Conversational (not formal)
Any competitors to reference or avoid: Gong is a competitor — acknowledge the comparison but do not disparage; position on accuracy/forecasting vs. conversation intelligence
Sequence architecture preference: Default (Email D1 → LinkedIn D3 → Call D5)
```

## Expected Output Criteria

- [ ] Signal Inventory table is produced with all 9+ signals correctly classified by type (FUNDING_EVENT, HIRING_VELOCITY, TECH_STACK_CHANGE, INTENT_SIGNAL, COMPANY_NEWS, etc.) and recency rating
- [ ] ICP Fit Dimensions Table scores each of the 7 stated ICP criteria explicitly (not merged or skipped)
- [ ] Overall Fit Score is 5/5 (Priority Tier) given all dimensions match and there are multiple RECENT/WARM triggers including a direct intent signal
- [ ] "Why Now" Trigger correctly identifies the G2 buyer intent signal (Clari vs. Gong comparison 3 days ago) as the highest-urgency trigger, with a rationale about the active evaluation window
- [ ] Both pain points are anchored to specific provided signals (not generic); Pain Point 1 should reference the forecasting-gap customer reviews, the Director of Sales Operations job description language, and the intent signal; Pain Point 2 should reference the headcount growth / scale pain or the hiring of a RevOps Analyst against a backdrop of no current forecasting tool
- [ ] Email body is 75–120 words, does not list product features, personalizes to the G2 comparison or the Series C as the trigger, and ends with a low-friction CTA (specific time offer or single yes/no question)
- [ ] Email subject line Option A uses curiosity or question framing; Option B references a specific trigger event (the intent research or the funding event)
- [ ] LinkedIn connection note is 300 characters or fewer, includes a character count, references something account-specific, and does not read as a sales pitch
- [ ] Cold call opener is 2–3 sentences, includes a permission question at the end, references the intent signal or funding event as the relevance hook, and does not open with a product pitch
- [ ] Cold call objection handles are provided: "What's this about?" bridge (2 sentences) and "Not interested" soft close (1 sentence)
- [ ] Competitor sensitivity is observed: Gong is referenced in context of the G2 comparison without disparagement; positioning differentiates on forecasting accuracy rather than conversation intelligence features
- [ ] Account Outreach Brief Summary is produced in the exact CRM-ready format specified, including all fields (Fit Score, Why Now, Primary Pain, Secondary Pain, sequence timeline, signals used, signal gaps)
- [ ] The three channel outputs share the same personalized hook and pain point frame — they are not three independent generic templates

## What failure looks like

A bad output generates pain points like "you probably struggle with pipeline visibility" or "growing companies often have forecasting challenges" without citing a specific signal from the provided input. It writes an email opener like "I came across Fieldwork and thought you'd be interested in Clari" — which is generic and ignores the G2 buyer intent signal entirely. It presents three channel outputs with different hooks (e.g., the email references the Series C but the LinkedIn note references the RevOps hiring and the call opener says "I see you're growing fast"), rather than coordinating all three around one central theme. The LinkedIn note exceeds 300 characters. The cold call opener leads with a product description rather than establishing relevance first. The fit score is anything other than 5/5 given the volume and quality of matching signals provided.
