# Scenario 2: Cold Outbound Account with No Intent Signals, Pure ICP Fit Research

## Context

An AE at a compensation management SaaS platform (Pave) is working a named-account list of Series B/C companies in the 100–500 employee range where she suspects the company is still managing compensation reviews and equity grants in spreadsheets. There are no intent signals — no pricing page visit, no competitor comparison, no content download. The AE has done her own research across LinkedIn, Crunchbase, and the company's public blog and needs to determine whether the account warrants a full outreach sequence and, if so, what the personalized hook should be. She targets the VP of People or Head of Total Rewards as her primary buyer.

## Input

```
TARGET ACCOUNT
Account name: Assembled
Account website: assembled.com
Industry/vertical: B2B SaaS — Workforce Management (support team scheduling and forecasting)
Company size (employees): 180
Revenue range (if known): $10M–$20M ARR (estimated; no public disclosure)
HQ location: San Francisco, CA

MY ICP CRITERIA
- B2B SaaS company, 100–500 employees
- Has a dedicated People/HR function (minimum: 1 full-time HR leader or VP People)
- Growing headcount 20%+ in the last 12 months (indicator of compensation complexity increasing)
- Series B or later
- Does NOT currently use a dedicated comp management platform (Carta, Pave, Radford, Levely)
- Primary buyer: VP People / Head of Total Rewards / HR Director
- Company is at the stage where spreadsheet-based compensation is starting to break (approx. 150+ employees is the common inflection point)

MY PRODUCT / SERVICE
Product name: Pave
One-sentence description: Pave is a compensation management platform that replaces spreadsheets in compensation review cycles, equity grant management, and real-time benchmarking against market comp data from 7,500+ companies.
Core value proposition: Give People teams a defensible, data-grounded compensation process so they can run reviews in days instead of weeks and retain talent without overpaying or creating internal pay equity problems.
Primary buyer persona: VP of People / Head of Total Rewards at B2B SaaS companies with 100–500 employees

ACCOUNT SIGNALS

Funding / financial events:
- Raised $51M Series B led by New Enterprise Associates (NEA), closed August 2024 (Crunchbase)
- Total funding: $70M

Hiring velocity / job postings:
- LinkedIn shows headcount grew from 120 to 180 employees in the last 12 months (50% headcount growth)
- 4 open roles in the last 45 days: 2x Senior Software Engineer, 1x Head of People (new role — first time this title appears in their job history), 1x Talent Acquisition Partner
- The "Head of People" job description mentions "build our total compensation framework and equity philosophy from scratch" as a top-three listed responsibility

Tech stack indicators:
- No dedicated HR tech stack visible beyond Greenhouse ATS (confirmed via BuiltWith) and Lattice (performance management, confirmed via G2 review mentioning "Lattice for perf reviews")
- No comp management platform detected (no Carta, Pave, Radford, Levely, or Kamsa signatures)
- Workday not detected; likely on spreadsheets for HRIS functions at this size

Leadership changes:
- No current Head of People or VP People listed on LinkedIn company page (role is open — first hire)
- Founders areND Táíwò (CEO) and Ryan Wang (COO) — both previously at Stripe, per LinkedIn

Intent signals:
None detected.

Recent news / press / announcements:
- August 2024 Series B press release (NEA blog): "Assembled will use the capital to expand its enterprise go-to-market and double its engineering team"
- Company blog (October 2024): Post titled "How we think about hiring at Assembled" authored by COO Ryan Wang — discusses structured interview process but does not mention compensation philosophy or benchmarking
- No press mentions of compensation, pay equity, or HR technology in the last 12 months

Other signals:
- Glassdoor: 4.2/5 rating, 38 reviews — no compensation-specific complaints, but 3 reviews from the last 6 months mention "equity transparency could be better" and "compensation bands not clearly communicated during hiring"
- LinkedIn alumni data: 2 former Assembled employees in the last 12 months moved to companies that list "better comp transparency" as a reason for leaving on Glassdoor (inferred, not stated directly)

OUTREACH PREFERENCES
Preferred tone: Conversational but substantive (the VP People persona reads carefully and ignores generic vendor outreach)
Any competitors to reference or avoid: Do not reference Carta (equity-focused; different buyer), Radford (enterprise-only; wrong size segment), or Workday (wrong size)
Sequence architecture preference: Default (Email D1 → LinkedIn D3 → Call D5)
```

## Expected Output Criteria

- [ ] Signal Inventory table is produced with all visible signals correctly classified and recency-rated; the "Head of People is a new/open role" signal must be identified as HIRING_VELOCITY and noted as particularly significant (first compensation leader = no incumbent process = high buy-readiness)
- [ ] ICP Fit Dimensions Table scores all 7 stated ICP dimensions; "Does NOT use a dedicated comp platform" receives STRONG FIT based on the absence of any detected comp tool; "VP People / Head of Total Rewards exists" should be scored PARTIAL FIT or flagged — the role is open, not filled, which is a nuance the skill must surface
- [ ] Overall Fit Score should be 4/5 (Strong Fit) — all core dimensions match, but there is no intent signal and the primary buyer role is currently vacant (a score of 5 would be incorrect given no trigger within 30 days and no intent signal)
- [ ] "Why Now" Trigger correctly identifies the open "Head of People" role with the "build total compensation framework from scratch" responsibility as the primary trigger — specifically that whomever fills this role in the next 30–60 days will be the exact buyer making a comp platform decision, and outreaching now to the COO/CEO before the hire lands creates the opportunity to be in the conversation from Day 1
- [ ] Pain Point 1 is anchored to specific signals: the "build comp framework from scratch" job description language + the absence of any comp tool + the 50% headcount growth = the company will be running its first structured compensation review with 180+ employees and no tooling; generic pain points like "spreadsheets are manual" without citing these specific signals are not acceptable
- [ ] Pain Point 2 is anchored to the Glassdoor signals: equity transparency complaints and unclear comp bands = a specific internal pay equity / retention risk that scales with every new hire at this stage
- [ ] Email personalized first line references the "Head of People" job posting and the "build compensation framework from scratch" language specifically — not a generic opener about the Series B or company growth
- [ ] Email body is 75–120 words, conversational tone, no feature lists, ends with a low-friction CTA (note: primary buyer is not hired yet — the CTA should be directed at the CEO or COO as a "get in front of the conversation before the hire" frame, or alternatively at whoever currently owns the People function)
- [ ] LinkedIn connection note is 300 characters or fewer, includes a character count, references the Head of People job posting or the comp framework language as the hook, is not a pitch
- [ ] Cold call opener establishes relevance via the comp-framework-from-scratch signal and ends with a permission question; the opener does not pitch product
- [ ] Signal gaps section in the Account Outreach Brief Summary explicitly notes: no intent signal detected, VP People buyer role is vacant (outreach should target CEO/COO as interim decision-maker), no HRIS platform confirmed beyond Greenhouse
- [ ] Account Outreach Brief Summary recommends targeting ND Táíwò (CEO) or Ryan Wang (COO) as interim buyer given the VP People role is open — this is a specific, non-generic decision about who to address the sequence to, and it must be based on the signal that the role is vacant
- [ ] The three channel outputs share the same "get ahead of the new Head of People hire" hook — they do not each choose a different angle

## What failure looks like

A bad output writes Pain Point 1 as "at 180 employees, you're probably starting to feel the pain of spreadsheet-based comp reviews" — a generic stage-fit observation that any B2B SaaS company at this size might receive, not an observation anchored to the signals provided. It fails to flag that the VP People buyer role is open and that the outreach should be directed at the CEO/COO — defaulting instead to "send to VP People" even though the inputs clearly show the role is vacant. It scores the account 5/5 (Priority Tier) ignoring the absence of a RECENT intent signal and the buyer-vacancy nuance, overstating the urgency. The email opens with "I noticed you recently raised your Series B" — a WARM/AGED signal from 10 months ago that is not the strongest hook, rather than leading with the active, RECENT Head of People job posting. The LinkedIn note says something generic like "We help People teams at fast-growing SaaS companies manage compensation — would love to connect!" without referencing anything specific to Assembled's current moment.
