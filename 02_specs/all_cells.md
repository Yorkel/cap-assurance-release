# All Rendered Prompts — Screening (07) + OAT (08)

Generated from `_prompts.py` via `build_screening_cell()` and `build_oat_cell()`.
This file is auto-regenerable — do not hand-edit. See [_prompts.py](../_prompts.py) for the source.

---

## Part 1 — Screening cells (notebook 07)

14 cells at 200 Q each. Baseline is the minimum defensible configuration; each toggle changes ONE thing from baseline (except `full_desc_plus_rule` which tests OAT C=B directly). Screening isolates main effects only — interactions are not tested at pilot scale (deferred to future work).

### `baseline`

**Overrides from baseline:** *no overrides — baseline*

**System message** (63 chars):

```
You classify UK parliamentary questions into CAP policy topics.
```

**User template** (2133 chars):

```
Below is a UK parliamentary question. Classify it into one of the CAP policy topics.

CAP policy topics:

1) Macroeconomics: domestic macroeconomic policy, inflation, interest rates, budget, tax, monetary policy
2) Civil Rights: civil rights, discrimination (racial, gender, age, disability), voting rights, privacy, freedom of speech
3) Health: healthcare, insurance, drugs, disease prevention, mental health, medical services
4) Agriculture: agriculture, farming, food safety, fisheries, subsidies, animal/crop disease
5) Labor: labour, worker safety, employment, training, unions, wages, fair labour standards
6) Education: education, primary/secondary/higher, vocational training, special education
7) Environment: environment, pollution, climate, waste, species protection, conservation
8) Energy: energy, nuclear, electricity, natural gas/oil, coal, alternative/renewable
9) Immigration: immigration, refugees, citizenship
10) Transportation: transportation, roads, rail, air travel, maritime, infrastructure
12) Law & Crime: law and crime, enforcement, courts, prisons, police, juvenile, drugs, family issues
13) Social Welfare: welfare, low-income assistance, elderly, disabled, child care, volunteer orgs
14) Housing: housing, urban/rural development, homelessness, community development
15) Domestic Commerce: commerce, banking, finance, small business, tourism, consumer safety, sports
16) Defence: defence, military, intelligence, arms, personnel, procurement, operations
17) Technology: technology, space, telecommunications, broadcast, computers, science
18) Foreign Trade: foreign trade, exports, tariffs, investment, exchange rates, competitiveness
19) International Affairs: international affairs, foreign aid, diplomacy, organisations, specific countries
20) Govt Operations: government operations, bureaucracy, appointments, intergov relations, administration
21) Public Lands: public lands, national parks, natural resources, water, territorial issues
23) Culture: culture, cultural policy

Return JSON: {"label": <integer>}. You must always choose one of the codes above. Never return null.

Question: {question}
```

---

### `full_descriptions`

**Overrides from baseline:** `description_detail='full'`

**System message** (63 chars):

```
You classify UK parliamentary questions into CAP policy topics.
```

**User template** (3254 chars):

```
Below is a UK parliamentary question. Classify it into one of the CAP policy topics.

CAP policy topics:

1) Macroeconomics: general domestic macroeconomic policy, inflation, interest rates, monetary policy, national budget, tax code, industrial policy, price controls
2) Civil Rights: civil rights, minority/ethnic/racial discrimination, gender and sexuality, age/disability discrimination, voting rights, freedom of speech, right to privacy
3) Health: healthcare including reform, insurance, drug industry, medical facilities, disease prevention, mental health, long-term care, drug/tobacco abuse
4) Agriculture: agriculture including trade, subsidies to farmers, food safety, marketing, animal/crop disease, fisheries
5) Labor: labor including worker safety, employment training, benefits, unions, fair labor standards, youth employment, migrant workers
6) Education: education including higher/primary/secondary, underprivileged, vocational, special education, education excellence
7) Environment: environment including drinking water, waste disposal, hazardous waste, air pollution/climate, species and forest protection, conservation
8) Energy: energy including nuclear, electricity, natural gas/oil, coal, alternative/renewable, conservation
9) Immigration: immigration, refugees, citizenship
10) Transportation: transportation including mass transit, highways, air travel, rail, maritime, infrastructure
12) Law & Crime: law and crime including enforcement, white collar crime, drugs, courts, prisons, juvenile crime, child abuse, family issues, police
13) Social Welfare: social welfare including low-income assistance, elderly assistance, disabled assistance, volunteer organisations, child care
14) Housing: housing including community/urban/rural development, low-income/veterans/elderly/homeless housing
15) Domestic Commerce: domestic commerce including banking, securities, consumer finance, insurance regulation, corporate management, small business, copyrights, disaster relief, tourism, consumer safety, sports
16) Defence: defence including alliances, intelligence, readiness, nuclear arms, military aid, personnel, procurement, installations, civil defence, contractors, foreign operations
17) Technology: technology including space, science transfer, telecommunications, broadcast, weather forecasting, computers
18) Foreign Trade: foreign trade including agreements, exports, private investments, competitiveness, tariffs/imports, exchange rates
19) International Affairs: international affairs including foreign aid, developing countries, international finance, Western Europe/EU, specific countries, human rights, organisations, terrorism, diplomats
20) Govt Operations: government operations including intergovernmental relations, bureaucracy, postal service, employees, appointments, currency, procurement, property, tax administration, scandals, branch relations, political campaigns
21) Public Lands: public lands including national parks, indigenous affairs, natural resources and forest management, water resources, territorial/dependency issues
23) Culture: culture including general cultural policy

Return JSON: {"label": <integer>}. You must always choose one of the codes above. Never return null.

Question: {question}
```

---

### `coding_rule`

**Overrides from baseline:** `coding_rule=True`

**System message** (63 chars):

```
You classify UK parliamentary questions into CAP policy topics.
```

**User template** (2915 chars):

```
Below is a UK parliamentary question. Classify it into one of the CAP policy topics.

CAP policy topics:

1) Macroeconomics: domestic macroeconomic policy, inflation, interest rates, budget, tax, monetary policy
2) Civil Rights: civil rights, discrimination (racial, gender, age, disability), voting rights, privacy, freedom of speech
3) Health: healthcare, insurance, drugs, disease prevention, mental health, medical services
4) Agriculture: agriculture, farming, food safety, fisheries, subsidies, animal/crop disease
5) Labor: labour, worker safety, employment, training, unions, wages, fair labour standards
6) Education: education, primary/secondary/higher, vocational training, special education
7) Environment: environment, pollution, climate, waste, species protection, conservation
8) Energy: energy, nuclear, electricity, natural gas/oil, coal, alternative/renewable
9) Immigration: immigration, refugees, citizenship
10) Transportation: transportation, roads, rail, air travel, maritime, infrastructure
12) Law & Crime: law and crime, enforcement, courts, prisons, police, juvenile, drugs, family issues
13) Social Welfare: welfare, low-income assistance, elderly, disabled, child care, volunteer orgs
14) Housing: housing, urban/rural development, homelessness, community development
15) Domestic Commerce: commerce, banking, finance, small business, tourism, consumer safety, sports
16) Defence: defence, military, intelligence, arms, personnel, procurement, operations
17) Technology: technology, space, telecommunications, broadcast, computers, science
18) Foreign Trade: foreign trade, exports, tariffs, investment, exchange rates, competitiveness
19) International Affairs: international affairs, foreign aid, diplomacy, organisations, specific countries
20) Govt Operations: government operations, bureaucracy, appointments, intergov relations, administration
21) Public Lands: public lands, national parks, natural resources, water, territorial issues
23) Culture: culture, cultural policy

Coding rule: Code each question by the substantive policy content it raises, not by its procedural framing, target population, policy instrument, or venue. Three traps to resist:

- Target-population trap: the group a policy affects isn't the topic (e.g., a question about disabled anglers' fishing licences is Civil Rights — disability policy — not Labor or Social Welfare).
- Policy-instrument trap: the mechanism a policy uses isn't the topic (e.g., a question about tax credits for childcare is Social Welfare — childcare policy — not Macroeconomics or Domestic Commerce).
- Venue trap: where a question is asked, or what forum it references, isn't the topic (e.g., a question about WHO recommendations on NHS reform is Health — healthcare policy — not International Affairs).

Return JSON: {"label": <integer>}. You must always choose one of the codes above. Never return null.

Question: {question}
```

---

### `full_desc_plus_rule`

**Overrides from baseline:** `description_detail='full'`, `coding_rule=True`

**System message** (63 chars):

```
You classify UK parliamentary questions into CAP policy topics.
```

**User template** (4036 chars):

```
Below is a UK parliamentary question. Classify it into one of the CAP policy topics.

CAP policy topics:

1) Macroeconomics: general domestic macroeconomic policy, inflation, interest rates, monetary policy, national budget, tax code, industrial policy, price controls
2) Civil Rights: civil rights, minority/ethnic/racial discrimination, gender and sexuality, age/disability discrimination, voting rights, freedom of speech, right to privacy
3) Health: healthcare including reform, insurance, drug industry, medical facilities, disease prevention, mental health, long-term care, drug/tobacco abuse
4) Agriculture: agriculture including trade, subsidies to farmers, food safety, marketing, animal/crop disease, fisheries
5) Labor: labor including worker safety, employment training, benefits, unions, fair labor standards, youth employment, migrant workers
6) Education: education including higher/primary/secondary, underprivileged, vocational, special education, education excellence
7) Environment: environment including drinking water, waste disposal, hazardous waste, air pollution/climate, species and forest protection, conservation
8) Energy: energy including nuclear, electricity, natural gas/oil, coal, alternative/renewable, conservation
9) Immigration: immigration, refugees, citizenship
10) Transportation: transportation including mass transit, highways, air travel, rail, maritime, infrastructure
12) Law & Crime: law and crime including enforcement, white collar crime, drugs, courts, prisons, juvenile crime, child abuse, family issues, police
13) Social Welfare: social welfare including low-income assistance, elderly assistance, disabled assistance, volunteer organisations, child care
14) Housing: housing including community/urban/rural development, low-income/veterans/elderly/homeless housing
15) Domestic Commerce: domestic commerce including banking, securities, consumer finance, insurance regulation, corporate management, small business, copyrights, disaster relief, tourism, consumer safety, sports
16) Defence: defence including alliances, intelligence, readiness, nuclear arms, military aid, personnel, procurement, installations, civil defence, contractors, foreign operations
17) Technology: technology including space, science transfer, telecommunications, broadcast, weather forecasting, computers
18) Foreign Trade: foreign trade including agreements, exports, private investments, competitiveness, tariffs/imports, exchange rates
19) International Affairs: international affairs including foreign aid, developing countries, international finance, Western Europe/EU, specific countries, human rights, organisations, terrorism, diplomats
20) Govt Operations: government operations including intergovernmental relations, bureaucracy, postal service, employees, appointments, currency, procurement, property, tax administration, scandals, branch relations, political campaigns
21) Public Lands: public lands including national parks, indigenous affairs, natural resources and forest management, water resources, territorial/dependency issues
23) Culture: culture including general cultural policy

Coding rule: Code each question by the substantive policy content it raises, not by its procedural framing, target population, policy instrument, or venue. Three traps to resist:

- Target-population trap: the group a policy affects isn't the topic (e.g., a question about disabled anglers' fishing licences is Civil Rights — disability policy — not Labor or Social Welfare).
- Policy-instrument trap: the mechanism a policy uses isn't the topic (e.g., a question about tax credits for childcare is Social Welfare — childcare policy — not Macroeconomics or Domestic Commerce).
- Venue trap: where a question is asked, or what forum it references, isn't the topic (e.g., a question about WHO recommendations on NHS reform is Health — healthcare policy — not International Affairs).

Return JSON: {"label": <integer>}. You must always choose one of the codes above. Never return null.

Question: {question}
```

---

### `fewshots_label_only`

**Overrides from baseline:** `fewshots='label_only'`

**System message** (63 chars):

```
You classify UK parliamentary questions into CAP policy topics.
```

**User template** (4547 chars):

```
Below is a UK parliamentary question. Classify it into one of the CAP policy topics.

CAP policy topics:

1) Macroeconomics: domestic macroeconomic policy, inflation, interest rates, budget, tax, monetary policy
2) Civil Rights: civil rights, discrimination (racial, gender, age, disability), voting rights, privacy, freedom of speech
3) Health: healthcare, insurance, drugs, disease prevention, mental health, medical services
4) Agriculture: agriculture, farming, food safety, fisheries, subsidies, animal/crop disease
5) Labor: labour, worker safety, employment, training, unions, wages, fair labour standards
6) Education: education, primary/secondary/higher, vocational training, special education
7) Environment: environment, pollution, climate, waste, species protection, conservation
8) Energy: energy, nuclear, electricity, natural gas/oil, coal, alternative/renewable
9) Immigration: immigration, refugees, citizenship
10) Transportation: transportation, roads, rail, air travel, maritime, infrastructure
12) Law & Crime: law and crime, enforcement, courts, prisons, police, juvenile, drugs, family issues
13) Social Welfare: welfare, low-income assistance, elderly, disabled, child care, volunteer orgs
14) Housing: housing, urban/rural development, homelessness, community development
15) Domestic Commerce: commerce, banking, finance, small business, tourism, consumer safety, sports
16) Defence: defence, military, intelligence, arms, personnel, procurement, operations
17) Technology: technology, space, telecommunications, broadcast, computers, science
18) Foreign Trade: foreign trade, exports, tariffs, investment, exchange rates, competitiveness
19) International Affairs: international affairs, foreign aid, diplomacy, organisations, specific countries
20) Govt Operations: government operations, bureaucracy, appointments, intergov relations, administration
21) Public Lands: public lands, national parks, natural resources, water, territorial issues
23) Culture: culture, cultural policy

Examples:

Example 1:
Question: "Business leaders at the CBI conference in Birmingham this week expressed support for the Government's policy of preparing the economy for possible United Kingdom entry into the single European currency. They also expressed support for the Government's spending plans, and felt that they were sustainable and that cuts in public spending were not required. In view of the policies put forward by the Conservative party on both those issues, does my right hon. Friend agree that it will be many years before that party regains the confidence of UK business?"
Answer: {"label": 1}

Example 2:
Question: "Q6. [10883]  When my right hon. Friend meets President Bush, will he put high on the agenda the plight of hundreds and thousands of Afghans, caused by the failure of food to get through to villages in Afghanistan?"
Answer: {"label": 19}

Example 3:
Question: "I am sure that my right hon. Friend will have been impressed by the incredible courage of Adrian Sudbury, who is using the last weeks of his life to campaign for more bone marrow donors to come forward. I have been impressed by the response so far of the Secretaries of State for Children, Schools and Families and for Health, but what more can my right hon. Friend do to help my friend Adrian to achieve his legacy and help 7,000 people to live?"
Answer: {"label": 3}

Example 4:
Question: "While the Prime Minister is on the subject of disabled people, may I ask whether he is aware that Labour’s attack on vulnerable people has been extended to disabled anglers? They have seen the cost of their fishing licence
30 Apr 2008 : Column 304
go up by 37 per cent., as opposed to 2 per cent. for able-bodied people—if, that is, they can find a post office from which to buy one"
Answer: {"label": 2}

Example 5:
Question: "Has my right hon. Friend noticed that all opinion polls show that the overwhelming majority of country dwellers are opposed to hunting with hounds?"
Answer: {"label": 7}

Example 6:
Question: "It seems certain that coal miners’ beat knee is about to be made a prescribed industrial disease. In order that we can avoid another feeding frenzy for solicitors, will the Prime Minister get his Ministers to meet interested MPs to see whether a scheme can be established that gives value for money to the taxpayer, fair compensation to the coal miner and nothing to the solicitor?"
Answer: {"label": 8}

Return JSON: {"label": <integer>}. You must always choose one of the codes above. Never return null.

Question: {question}
```

---

### `fewshots_reasoning`

**Overrides from baseline:** `fewshots='reasoning'`, `output_format='reasoning_label'`

**System message** (63 chars):

```
You classify UK parliamentary questions into CAP policy topics.
```

**User template** (5172 chars):

```
Below is a UK parliamentary question. Classify it into one of the CAP policy topics.

CAP policy topics:

1) Macroeconomics: domestic macroeconomic policy, inflation, interest rates, budget, tax, monetary policy
2) Civil Rights: civil rights, discrimination (racial, gender, age, disability), voting rights, privacy, freedom of speech
3) Health: healthcare, insurance, drugs, disease prevention, mental health, medical services
4) Agriculture: agriculture, farming, food safety, fisheries, subsidies, animal/crop disease
5) Labor: labour, worker safety, employment, training, unions, wages, fair labour standards
6) Education: education, primary/secondary/higher, vocational training, special education
7) Environment: environment, pollution, climate, waste, species protection, conservation
8) Energy: energy, nuclear, electricity, natural gas/oil, coal, alternative/renewable
9) Immigration: immigration, refugees, citizenship
10) Transportation: transportation, roads, rail, air travel, maritime, infrastructure
12) Law & Crime: law and crime, enforcement, courts, prisons, police, juvenile, drugs, family issues
13) Social Welfare: welfare, low-income assistance, elderly, disabled, child care, volunteer orgs
14) Housing: housing, urban/rural development, homelessness, community development
15) Domestic Commerce: commerce, banking, finance, small business, tourism, consumer safety, sports
16) Defence: defence, military, intelligence, arms, personnel, procurement, operations
17) Technology: technology, space, telecommunications, broadcast, computers, science
18) Foreign Trade: foreign trade, exports, tariffs, investment, exchange rates, competitiveness
19) International Affairs: international affairs, foreign aid, diplomacy, organisations, specific countries
20) Govt Operations: government operations, bureaucracy, appointments, intergov relations, administration
21) Public Lands: public lands, national parks, natural resources, water, territorial issues
23) Culture: culture, cultural policy

Examples:

Example 1:
Question: "Business leaders at the CBI conference in Birmingham this week expressed support for the Government's policy of preparing the economy for possible United Kingdom entry into the single European currency. They also expressed support for the Government's spending plans, and felt that they were sustainable and that cuts in public spending were not required. In view of the policies put forward by the Conservative party on both those issues, does my right hon. Friend agree that it will be many years before that party regains the confidence of UK business?"
Answer: {"reasoning": "Single European currency is domestic monetary policy; international venue trap resisted", "label": 1}

Example 2:
Question: "Q6. [10883]  When my right hon. Friend meets President Bush, will he put high on the agenda the plight of hundreds and thousands of Afghans, caused by the failure of food to get through to villages in Afghanistan?"
Answer: {"reasoning": "Humanitarian aid coordination via foreign diplomacy; Defence/Agriculture traps resisted", "label": 19}

Example 3:
Question: "I am sure that my right hon. Friend will have been impressed by the incredible courage of Adrian Sudbury, who is using the last weeks of his life to campaign for more bone marrow donors to come forward. I have been impressed by the response so far of the Secretaries of State for Children, Schools and Families and for Health, but what more can my right hon. Friend do to help my friend Adrian to achieve his legacy and help 7,000 people to live?"
Answer: {"reasoning": "Bone marrow donation is health-service delivery; welfare-framing trap resisted", "label": 3}

Example 4:
Question: "While the Prime Minister is on the subject of disabled people, may I ask whether he is aware that Labour’s attack on vulnerable people has been extended to disabled anglers? They have seen the cost of their fishing licence
30 Apr 2008 : Column 304
go up by 37 per cent., as opposed to 2 per cent. for able-bodied people—if, that is, they can find a post office from which to buy one"
Answer: {"reasoning": "Disability-targeted policy is Civil Rights; target-population trap in sporting frame resisted", "label": 2}

Example 5:
Question: "Has my right hon. Friend noticed that all opinion polls show that the overwhelming majority of country dwellers are opposed to hunting with hounds?"
Answer: {"reasoning": "Hunting policy is wildlife regulation; rural-venue trap (Agriculture) resisted", "label": 7}

Example 6:
Question: "It seems certain that coal miners’ beat knee is about to be made a prescribed industrial disease. In order that we can avoid another feeding frenzy for solicitors, will the Prime Minister get his Ministers to meet interested MPs to see whether a scheme can be established that gives value for money to the taxpayer, fair compensation to the coal miner and nothing to the solicitor?"
Answer: {"reasoning": "Coal industry question is Energy; occupational-disease trap (Labor) resisted", "label": 8}

Return JSON: {"reasoning": "<brief>", "label": <integer>}. You must always choose one of the codes above. Never return null.

Question: {question}
```

---

### `persona`

**Overrides from baseline:** `persona=True`

**System message** (135 chars):

```
You are a parliamentary researcher classifying UK Prime Minister's Questions using the Comparative Agendas Project (CAP) coding scheme.
```

**User template** (2133 chars):

```
Below is a UK parliamentary question. Classify it into one of the CAP policy topics.

CAP policy topics:

1) Macroeconomics: domestic macroeconomic policy, inflation, interest rates, budget, tax, monetary policy
2) Civil Rights: civil rights, discrimination (racial, gender, age, disability), voting rights, privacy, freedom of speech
3) Health: healthcare, insurance, drugs, disease prevention, mental health, medical services
4) Agriculture: agriculture, farming, food safety, fisheries, subsidies, animal/crop disease
5) Labor: labour, worker safety, employment, training, unions, wages, fair labour standards
6) Education: education, primary/secondary/higher, vocational training, special education
7) Environment: environment, pollution, climate, waste, species protection, conservation
8) Energy: energy, nuclear, electricity, natural gas/oil, coal, alternative/renewable
9) Immigration: immigration, refugees, citizenship
10) Transportation: transportation, roads, rail, air travel, maritime, infrastructure
12) Law & Crime: law and crime, enforcement, courts, prisons, police, juvenile, drugs, family issues
13) Social Welfare: welfare, low-income assistance, elderly, disabled, child care, volunteer orgs
14) Housing: housing, urban/rural development, homelessness, community development
15) Domestic Commerce: commerce, banking, finance, small business, tourism, consumer safety, sports
16) Defence: defence, military, intelligence, arms, personnel, procurement, operations
17) Technology: technology, space, telecommunications, broadcast, computers, science
18) Foreign Trade: foreign trade, exports, tariffs, investment, exchange rates, competitiveness
19) International Affairs: international affairs, foreign aid, diplomacy, organisations, specific countries
20) Govt Operations: government operations, bureaucracy, appointments, intergov relations, administration
21) Public Lands: public lands, national parks, natural resources, water, territorial issues
23) Culture: culture, cultural policy

Return JSON: {"label": <integer>}. You must always choose one of the codes above. Never return null.

Question: {question}
```

---

### `cot_instruction`

**Overrides from baseline:** `cot_instruction=True`

**System message** (179 chars):

```
You classify UK parliamentary questions into CAP policy topics.

Think step by step: first identify the substantive policy issue at stake, then select the best-matching CAP topic.
```

**User template** (2133 chars):

```
Below is a UK parliamentary question. Classify it into one of the CAP policy topics.

CAP policy topics:

1) Macroeconomics: domestic macroeconomic policy, inflation, interest rates, budget, tax, monetary policy
2) Civil Rights: civil rights, discrimination (racial, gender, age, disability), voting rights, privacy, freedom of speech
3) Health: healthcare, insurance, drugs, disease prevention, mental health, medical services
4) Agriculture: agriculture, farming, food safety, fisheries, subsidies, animal/crop disease
5) Labor: labour, worker safety, employment, training, unions, wages, fair labour standards
6) Education: education, primary/secondary/higher, vocational training, special education
7) Environment: environment, pollution, climate, waste, species protection, conservation
8) Energy: energy, nuclear, electricity, natural gas/oil, coal, alternative/renewable
9) Immigration: immigration, refugees, citizenship
10) Transportation: transportation, roads, rail, air travel, maritime, infrastructure
12) Law & Crime: law and crime, enforcement, courts, prisons, police, juvenile, drugs, family issues
13) Social Welfare: welfare, low-income assistance, elderly, disabled, child care, volunteer orgs
14) Housing: housing, urban/rural development, homelessness, community development
15) Domestic Commerce: commerce, banking, finance, small business, tourism, consumer safety, sports
16) Defence: defence, military, intelligence, arms, personnel, procurement, operations
17) Technology: technology, space, telecommunications, broadcast, computers, science
18) Foreign Trade: foreign trade, exports, tariffs, investment, exchange rates, competitiveness
19) International Affairs: international affairs, foreign aid, diplomacy, organisations, specific countries
20) Govt Operations: government operations, bureaucracy, appointments, intergov relations, administration
21) Public Lands: public lands, national parks, natural resources, water, territorial issues
23) Culture: culture, cultural policy

Return JSON: {"label": <integer>}. You must always choose one of the codes above. Never return null.

Question: {question}
```

---

### `reasoning_output`

**Overrides from baseline:** `output_format='reasoning_label'`

**System message** (63 chars):

```
You classify UK parliamentary questions into CAP policy topics.
```

**User template** (2157 chars):

```
Below is a UK parliamentary question. Classify it into one of the CAP policy topics.

CAP policy topics:

1) Macroeconomics: domestic macroeconomic policy, inflation, interest rates, budget, tax, monetary policy
2) Civil Rights: civil rights, discrimination (racial, gender, age, disability), voting rights, privacy, freedom of speech
3) Health: healthcare, insurance, drugs, disease prevention, mental health, medical services
4) Agriculture: agriculture, farming, food safety, fisheries, subsidies, animal/crop disease
5) Labor: labour, worker safety, employment, training, unions, wages, fair labour standards
6) Education: education, primary/secondary/higher, vocational training, special education
7) Environment: environment, pollution, climate, waste, species protection, conservation
8) Energy: energy, nuclear, electricity, natural gas/oil, coal, alternative/renewable
9) Immigration: immigration, refugees, citizenship
10) Transportation: transportation, roads, rail, air travel, maritime, infrastructure
12) Law & Crime: law and crime, enforcement, courts, prisons, police, juvenile, drugs, family issues
13) Social Welfare: welfare, low-income assistance, elderly, disabled, child care, volunteer orgs
14) Housing: housing, urban/rural development, homelessness, community development
15) Domestic Commerce: commerce, banking, finance, small business, tourism, consumer safety, sports
16) Defence: defence, military, intelligence, arms, personnel, procurement, operations
17) Technology: technology, space, telecommunications, broadcast, computers, science
18) Foreign Trade: foreign trade, exports, tariffs, investment, exchange rates, competitiveness
19) International Affairs: international affairs, foreign aid, diplomacy, organisations, specific countries
20) Govt Operations: government operations, bureaucracy, appointments, intergov relations, administration
21) Public Lands: public lands, national parks, natural resources, water, territorial issues
23) Culture: culture, cultural policy

Return JSON: {"reasoning": "<brief>", "label": <integer>}. You must always choose one of the codes above. Never return null.

Question: {question}
```

---

### `freetext_output`

**Overrides from baseline:** `output_format='freetext'`

**System message** (63 chars):

```
You classify UK parliamentary questions into CAP policy topics.
```

**User template** (2231 chars):

```
Below is a UK parliamentary question. Classify it into one of the CAP policy topics.

CAP policy topics:

1) Macroeconomics: domestic macroeconomic policy, inflation, interest rates, budget, tax, monetary policy
2) Civil Rights: civil rights, discrimination (racial, gender, age, disability), voting rights, privacy, freedom of speech
3) Health: healthcare, insurance, drugs, disease prevention, mental health, medical services
4) Agriculture: agriculture, farming, food safety, fisheries, subsidies, animal/crop disease
5) Labor: labour, worker safety, employment, training, unions, wages, fair labour standards
6) Education: education, primary/secondary/higher, vocational training, special education
7) Environment: environment, pollution, climate, waste, species protection, conservation
8) Energy: energy, nuclear, electricity, natural gas/oil, coal, alternative/renewable
9) Immigration: immigration, refugees, citizenship
10) Transportation: transportation, roads, rail, air travel, maritime, infrastructure
12) Law & Crime: law and crime, enforcement, courts, prisons, police, juvenile, drugs, family issues
13) Social Welfare: welfare, low-income assistance, elderly, disabled, child care, volunteer orgs
14) Housing: housing, urban/rural development, homelessness, community development
15) Domestic Commerce: commerce, banking, finance, small business, tourism, consumer safety, sports
16) Defence: defence, military, intelligence, arms, personnel, procurement, operations
17) Technology: technology, space, telecommunications, broadcast, computers, science
18) Foreign Trade: foreign trade, exports, tariffs, investment, exchange rates, competitiveness
19) International Affairs: international affairs, foreign aid, diplomacy, organisations, specific countries
20) Govt Operations: government operations, bureaucracy, appointments, intergov relations, administration
21) Public Lands: public lands, national parks, natural resources, water, territorial issues
23) Culture: culture, cultural policy

State your classification in a single sentence ending with the CAP code number. Example: "This question is about healthcare waiting lists, CAP code 3." You must always choose one of the codes above.

Question: {question}
```

---

### `codebook_in_system`

**Overrides from baseline:** `codebook_in_system=True`

**System message** (1988 chars):

```
You classify UK parliamentary questions into CAP policy topics.

CAP policy topics:

1) Macroeconomics: domestic macroeconomic policy, inflation, interest rates, budget, tax, monetary policy
2) Civil Rights: civil rights, discrimination (racial, gender, age, disability), voting rights, privacy, freedom of speech
3) Health: healthcare, insurance, drugs, disease prevention, mental health, medical services
4) Agriculture: agriculture, farming, food safety, fisheries, subsidies, animal/crop disease
5) Labor: labour, worker safety, employment, training, unions, wages, fair labour standards
6) Education: education, primary/secondary/higher, vocational training, special education
7) Environment: environment, pollution, climate, waste, species protection, conservation
8) Energy: energy, nuclear, electricity, natural gas/oil, coal, alternative/renewable
9) Immigration: immigration, refugees, citizenship
10) Transportation: transportation, roads, rail, air travel, maritime, infrastructure
12) Law & Crime: law and crime, enforcement, courts, prisons, police, juvenile, drugs, family issues
13) Social Welfare: welfare, low-income assistance, elderly, disabled, child care, volunteer orgs
14) Housing: housing, urban/rural development, homelessness, community development
15) Domestic Commerce: commerce, banking, finance, small business, tourism, consumer safety, sports
16) Defence: defence, military, intelligence, arms, personnel, procurement, operations
17) Technology: technology, space, telecommunications, broadcast, computers, science
18) Foreign Trade: foreign trade, exports, tariffs, investment, exchange rates, competitiveness
19) International Affairs: international affairs, foreign aid, diplomacy, organisations, specific countries
20) Govt Operations: government operations, bureaucracy, appointments, intergov relations, administration
21) Public Lands: public lands, national parks, natural resources, water, territorial issues
23) Culture: culture, cultural policy
```

**User template** (208 chars):

```
Below is a UK parliamentary question. Classify it into one of the CAP policy topics.

Return JSON: {"label": <integer>}. You must always choose one of the codes above. Never return null.

Question: {question}
```

---

### `scope_time`

**Overrides from baseline:** `scope='time'`

**System message** (63 chars):

```
You classify UK parliamentary questions into CAP policy topics.
```

**User template** (2148 chars):

```
Below is a UK parliamentary question from 1997-2008. Classify it into one of the CAP policy topics.

CAP policy topics:

1) Macroeconomics: domestic macroeconomic policy, inflation, interest rates, budget, tax, monetary policy
2) Civil Rights: civil rights, discrimination (racial, gender, age, disability), voting rights, privacy, freedom of speech
3) Health: healthcare, insurance, drugs, disease prevention, mental health, medical services
4) Agriculture: agriculture, farming, food safety, fisheries, subsidies, animal/crop disease
5) Labor: labour, worker safety, employment, training, unions, wages, fair labour standards
6) Education: education, primary/secondary/higher, vocational training, special education
7) Environment: environment, pollution, climate, waste, species protection, conservation
8) Energy: energy, nuclear, electricity, natural gas/oil, coal, alternative/renewable
9) Immigration: immigration, refugees, citizenship
10) Transportation: transportation, roads, rail, air travel, maritime, infrastructure
12) Law & Crime: law and crime, enforcement, courts, prisons, police, juvenile, drugs, family issues
13) Social Welfare: welfare, low-income assistance, elderly, disabled, child care, volunteer orgs
14) Housing: housing, urban/rural development, homelessness, community development
15) Domestic Commerce: commerce, banking, finance, small business, tourism, consumer safety, sports
16) Defence: defence, military, intelligence, arms, personnel, procurement, operations
17) Technology: technology, space, telecommunications, broadcast, computers, science
18) Foreign Trade: foreign trade, exports, tariffs, investment, exchange rates, competitiveness
19) International Affairs: international affairs, foreign aid, diplomacy, organisations, specific countries
20) Govt Operations: government operations, bureaucracy, appointments, intergov relations, administration
21) Public Lands: public lands, national parks, natural resources, water, territorial issues
23) Culture: culture, cultural policy

Return JSON: {"label": <integer>}. You must always choose one of the codes above. Never return null.

Question: {question}
```

---

### `scope_speaker`

**Overrides from baseline:** `scope='speaker'`

**System message** (63 chars):

```
You classify UK parliamentary questions into CAP policy topics.
```

**User template** (2163 chars):

```
Below is a UK parliamentary question asked by a {speaker_party} MP. Classify it into one of the CAP policy topics.

CAP policy topics:

1) Macroeconomics: domestic macroeconomic policy, inflation, interest rates, budget, tax, monetary policy
2) Civil Rights: civil rights, discrimination (racial, gender, age, disability), voting rights, privacy, freedom of speech
3) Health: healthcare, insurance, drugs, disease prevention, mental health, medical services
4) Agriculture: agriculture, farming, food safety, fisheries, subsidies, animal/crop disease
5) Labor: labour, worker safety, employment, training, unions, wages, fair labour standards
6) Education: education, primary/secondary/higher, vocational training, special education
7) Environment: environment, pollution, climate, waste, species protection, conservation
8) Energy: energy, nuclear, electricity, natural gas/oil, coal, alternative/renewable
9) Immigration: immigration, refugees, citizenship
10) Transportation: transportation, roads, rail, air travel, maritime, infrastructure
12) Law & Crime: law and crime, enforcement, courts, prisons, police, juvenile, drugs, family issues
13) Social Welfare: welfare, low-income assistance, elderly, disabled, child care, volunteer orgs
14) Housing: housing, urban/rural development, homelessness, community development
15) Domestic Commerce: commerce, banking, finance, small business, tourism, consumer safety, sports
16) Defence: defence, military, intelligence, arms, personnel, procurement, operations
17) Technology: technology, space, telecommunications, broadcast, computers, science
18) Foreign Trade: foreign trade, exports, tariffs, investment, exchange rates, competitiveness
19) International Affairs: international affairs, foreign aid, diplomacy, organisations, specific countries
20) Govt Operations: government operations, bureaucracy, appointments, intergov relations, administration
21) Public Lands: public lands, national parks, natural resources, water, territorial issues
23) Culture: culture, cultural policy

Return JSON: {"label": <integer>}. You must always choose one of the codes above. Never return null.

Question: {question}
```

---

### `scope_jurisdiction`

**Overrides from baseline:** `scope='jurisdiction'`

**System message** (63 chars):

```
You classify UK parliamentary questions into CAP policy topics.
```

**User template** (2197 chars):

```
Below is a UK parliamentary question; apply the CAP coding scheme under UK parliamentary conventions. Classify it into one of the CAP policy topics.

CAP policy topics:

1) Macroeconomics: domestic macroeconomic policy, inflation, interest rates, budget, tax, monetary policy
2) Civil Rights: civil rights, discrimination (racial, gender, age, disability), voting rights, privacy, freedom of speech
3) Health: healthcare, insurance, drugs, disease prevention, mental health, medical services
4) Agriculture: agriculture, farming, food safety, fisheries, subsidies, animal/crop disease
5) Labor: labour, worker safety, employment, training, unions, wages, fair labour standards
6) Education: education, primary/secondary/higher, vocational training, special education
7) Environment: environment, pollution, climate, waste, species protection, conservation
8) Energy: energy, nuclear, electricity, natural gas/oil, coal, alternative/renewable
9) Immigration: immigration, refugees, citizenship
10) Transportation: transportation, roads, rail, air travel, maritime, infrastructure
12) Law & Crime: law and crime, enforcement, courts, prisons, police, juvenile, drugs, family issues
13) Social Welfare: welfare, low-income assistance, elderly, disabled, child care, volunteer orgs
14) Housing: housing, urban/rural development, homelessness, community development
15) Domestic Commerce: commerce, banking, finance, small business, tourism, consumer safety, sports
16) Defence: defence, military, intelligence, arms, personnel, procurement, operations
17) Technology: technology, space, telecommunications, broadcast, computers, science
18) Foreign Trade: foreign trade, exports, tariffs, investment, exchange rates, competitiveness
19) International Affairs: international affairs, foreign aid, diplomacy, organisations, specific countries
20) Govt Operations: government operations, bureaucracy, appointments, intergov relations, administration
21) Public Lands: public lands, national parks, natural resources, water, territorial issues
23) Culture: culture, cultural policy

Return JSON: {"label": <integer>}. You must always choose one of the codes above. Never return null.

Question: {question}
```

---


## Part 2 — OAT cells (notebook 08)

3 axes × 3 levels each, monotonic on C axis (each step adds one component to the previous). **Only 7 of the 27 possible combinations are actually run** — the 7 are determined after notebook 07 identifies an anchor. The 7 = anchor + 2 alternatives per axis × 3 axes.

**Anchor locked 2026-04-20:** `OAT_CC_FA_DA` (full + rule + fewshots / label-only / no scope) — matches 06's C2_F1_D1.

**Fixed baseline across all OAT runs:** `description_detail='full'`, `persona=True`, `codebook_in_system=False`.

**Screening vs OAT starting points:** screening starts from a minimum-defensible baseline (short descriptions, no persona, label-only output, no scope) to test what each component adds. OAT starts from a richer baseline (full descriptions, persona on) to test swaps on each axis from a professional reference. Intentional.

**Speaker-party substitution at runtime:** cells with D=speaker scope contain a `{speaker_party}` placeholder. The pipeline fills this from `sst_main.csv` columns `filter_conid` / `filter_labid` / `filter_ldid` via `speaker_party_from_row()`, so caching is per-party (4 partitions: Conservative / Labour / Liberal Democrat / unaffiliated).

**Axis levels:**

- **C — Codebook richness (monotonic):**
  - `A`: full desc only (overrides: `{}`)
  - `B`: full + rule (overrides: `{'coding_rule': True}`)
  - `C`: full + rule + fewshots (overrides: `{'coding_rule': True, 'fewshots': 'label_only'}`)

- **F — Output reasoning scaffold:**
  - `A`: label only (overrides: `{'output_format': 'label_only'}`)
  - `B`: reasoning+label (overrides: `{'output_format': 'reasoning_label'}`)
  - `C`: reasoning+label + CoT (overrides: `{'output_format': 'reasoning_label', 'cot_instruction': True}`)

- **D — Scope declaration:**
  - `A`: no scope (overrides: `{'scope': 'none'}`)
  - `B`: time scope (overrides: `{'scope': 'time'}`)
  - `C`: speaker scope (overrides: `{'scope': 'speaker'}`)

### All 27 possible OAT combinations (7 actually run from the anchor)

#### `OAT_CA_FA_DA` — C=full desc only | F=label only | D=no scope

**System** (135 chars):

```
You are a parliamentary researcher classifying UK Prime Minister's Questions using the Comparative Agendas Project (CAP) coding scheme.
```

**User** (3254 chars):

```
Below is a UK parliamentary question. Classify it into one of the CAP policy topics.

CAP policy topics:

1) Macroeconomics: general domestic macroeconomic policy, inflation, interest rates, monetary policy, national budget, tax code, industrial policy, price controls
2) Civil Rights: civil rights, minority/ethnic/racial discrimination, gender and sexuality, age/disability discrimination, voting rights, freedom of speech, right to privacy
3) Health: healthcare including reform, insurance, drug industry, medical facilities, disease prevention, mental health, long-term care, drug/tobacco abuse
4) Agriculture: agriculture including trade, subsidies to farmers, food safety, marketing, animal/crop disease, fisheries
5) Labor: labor including worker safety, employment training, benefits, unions, fair labor standards, youth employment, migrant workers
6) Education: education including higher/primary/secondary, underprivileged, vocational, special education, education excellence
7) Environment: environment including drinking water, waste disposal, hazardous waste, air pollution/climate, species and forest protection, conservation
8) Energy: energy including nuclear, electricity, natural gas/oil, coal, alternative/renewable, conservation
9) Immigration: immigration, refugees, citizenship
10) Transportation: transportation including mass transit, highways, air travel, rail, maritime, infrastructure
12) Law & Crime: law and crime including enforcement, white collar crime, drugs, courts, prisons, juvenile crime, child abuse, family issues, police
13) Social Welfare: social welfare including low-income assistance, elderly assistance, disabled assistance, volunteer organisations, child care
14) Housing: housing including community/urban/rural development, low-income/veterans/elderly/homeless housing
15) Domestic Commerce: domestic commerce including banking, securities, consumer finance, insurance regulation, corporate management, small business, copyrights, disaster relief, tourism, consumer safety, sports
16) Defence: defence including alliances, intelligence, readiness, nuclear arms, military aid, personnel, procurement, installations, civil defence, contractors, foreign operations
17) Technology: technology including space, science transfer, telecommunications, broadcast, weather forecasting, computers
18) Foreign Trade: foreign trade including agreements, exports, private investments, competitiveness, tariffs/imports, exchange rates
19) International Affairs: international affairs including foreign aid, developing countries, international finance, Western Europe/EU, specific countries, human rights, organisations, terrorism, diplomats
20) Govt Operations: government operations including intergovernmental relations, bureaucracy, postal service, employees, appointments, currency, procurement, property, tax administration, scandals, branch relations, political campaigns
21) Public Lands: public lands including national parks, indigenous affairs, natural resources and forest management, water resources, territorial/dependency issues
23) Culture: culture including general cultural policy

Return JSON: {"label": <integer>}. You must always choose one of the codes above. Never return null.

Question: {question}
```

---

#### `OAT_CA_FA_DB` — C=full desc only | F=label only | D=time scope

**System** (135 chars):

```
You are a parliamentary researcher classifying UK Prime Minister's Questions using the Comparative Agendas Project (CAP) coding scheme.
```

**User** (3269 chars):

```
Below is a UK parliamentary question from 1997-2008. Classify it into one of the CAP policy topics.

CAP policy topics:

1) Macroeconomics: general domestic macroeconomic policy, inflation, interest rates, monetary policy, national budget, tax code, industrial policy, price controls
2) Civil Rights: civil rights, minority/ethnic/racial discrimination, gender and sexuality, age/disability discrimination, voting rights, freedom of speech, right to privacy
3) Health: healthcare including reform, insurance, drug industry, medical facilities, disease prevention, mental health, long-term care, drug/tobacco abuse
4) Agriculture: agriculture including trade, subsidies to farmers, food safety, marketing, animal/crop disease, fisheries
5) Labor: labor including worker safety, employment training, benefits, unions, fair labor standards, youth employment, migrant workers
6) Education: education including higher/primary/secondary, underprivileged, vocational, special education, education excellence
7) Environment: environment including drinking water, waste disposal, hazardous waste, air pollution/climate, species and forest protection, conservation
8) Energy: energy including nuclear, electricity, natural gas/oil, coal, alternative/renewable, conservation
9) Immigration: immigration, refugees, citizenship
10) Transportation: transportation including mass transit, highways, air travel, rail, maritime, infrastructure
12) Law & Crime: law and crime including enforcement, white collar crime, drugs, courts, prisons, juvenile crime, child abuse, family issues, police
13) Social Welfare: social welfare including low-income assistance, elderly assistance, disabled assistance, volunteer organisations, child care
14) Housing: housing including community/urban/rural development, low-income/veterans/elderly/homeless housing
15) Domestic Commerce: domestic commerce including banking, securities, consumer finance, insurance regulation, corporate management, small business, copyrights, disaster relief, tourism, consumer safety, sports
16) Defence: defence including alliances, intelligence, readiness, nuclear arms, military aid, personnel, procurement, installations, civil defence, contractors, foreign operations
17) Technology: technology including space, science transfer, telecommunications, broadcast, weather forecasting, computers
18) Foreign Trade: foreign trade including agreements, exports, private investments, competitiveness, tariffs/imports, exchange rates
19) International Affairs: international affairs including foreign aid, developing countries, international finance, Western Europe/EU, specific countries, human rights, organisations, terrorism, diplomats
20) Govt Operations: government operations including intergovernmental relations, bureaucracy, postal service, employees, appointments, currency, procurement, property, tax administration, scandals, branch relations, political campaigns
21) Public Lands: public lands including national parks, indigenous affairs, natural resources and forest management, water resources, territorial/dependency issues
23) Culture: culture including general cultural policy

Return JSON: {"label": <integer>}. You must always choose one of the codes above. Never return null.

Question: {question}
```

---

#### `OAT_CA_FA_DC` — C=full desc only | F=label only | D=speaker scope

**System** (135 chars):

```
You are a parliamentary researcher classifying UK Prime Minister's Questions using the Comparative Agendas Project (CAP) coding scheme.
```

**User** (3284 chars):

```
Below is a UK parliamentary question asked by a {speaker_party} MP. Classify it into one of the CAP policy topics.

CAP policy topics:

1) Macroeconomics: general domestic macroeconomic policy, inflation, interest rates, monetary policy, national budget, tax code, industrial policy, price controls
2) Civil Rights: civil rights, minority/ethnic/racial discrimination, gender and sexuality, age/disability discrimination, voting rights, freedom of speech, right to privacy
3) Health: healthcare including reform, insurance, drug industry, medical facilities, disease prevention, mental health, long-term care, drug/tobacco abuse
4) Agriculture: agriculture including trade, subsidies to farmers, food safety, marketing, animal/crop disease, fisheries
5) Labor: labor including worker safety, employment training, benefits, unions, fair labor standards, youth employment, migrant workers
6) Education: education including higher/primary/secondary, underprivileged, vocational, special education, education excellence
7) Environment: environment including drinking water, waste disposal, hazardous waste, air pollution/climate, species and forest protection, conservation
8) Energy: energy including nuclear, electricity, natural gas/oil, coal, alternative/renewable, conservation
9) Immigration: immigration, refugees, citizenship
10) Transportation: transportation including mass transit, highways, air travel, rail, maritime, infrastructure
12) Law & Crime: law and crime including enforcement, white collar crime, drugs, courts, prisons, juvenile crime, child abuse, family issues, police
13) Social Welfare: social welfare including low-income assistance, elderly assistance, disabled assistance, volunteer organisations, child care
14) Housing: housing including community/urban/rural development, low-income/veterans/elderly/homeless housing
15) Domestic Commerce: domestic commerce including banking, securities, consumer finance, insurance regulation, corporate management, small business, copyrights, disaster relief, tourism, consumer safety, sports
16) Defence: defence including alliances, intelligence, readiness, nuclear arms, military aid, personnel, procurement, installations, civil defence, contractors, foreign operations
17) Technology: technology including space, science transfer, telecommunications, broadcast, weather forecasting, computers
18) Foreign Trade: foreign trade including agreements, exports, private investments, competitiveness, tariffs/imports, exchange rates
19) International Affairs: international affairs including foreign aid, developing countries, international finance, Western Europe/EU, specific countries, human rights, organisations, terrorism, diplomats
20) Govt Operations: government operations including intergovernmental relations, bureaucracy, postal service, employees, appointments, currency, procurement, property, tax administration, scandals, branch relations, political campaigns
21) Public Lands: public lands including national parks, indigenous affairs, natural resources and forest management, water resources, territorial/dependency issues
23) Culture: culture including general cultural policy

Return JSON: {"label": <integer>}. You must always choose one of the codes above. Never return null.

Question: {question}
```

---

#### `OAT_CA_FB_DA` — C=full desc only | F=reasoning+label | D=no scope

**System** (135 chars):

```
You are a parliamentary researcher classifying UK Prime Minister's Questions using the Comparative Agendas Project (CAP) coding scheme.
```

**User** (3278 chars):

```
Below is a UK parliamentary question. Classify it into one of the CAP policy topics.

CAP policy topics:

1) Macroeconomics: general domestic macroeconomic policy, inflation, interest rates, monetary policy, national budget, tax code, industrial policy, price controls
2) Civil Rights: civil rights, minority/ethnic/racial discrimination, gender and sexuality, age/disability discrimination, voting rights, freedom of speech, right to privacy
3) Health: healthcare including reform, insurance, drug industry, medical facilities, disease prevention, mental health, long-term care, drug/tobacco abuse
4) Agriculture: agriculture including trade, subsidies to farmers, food safety, marketing, animal/crop disease, fisheries
5) Labor: labor including worker safety, employment training, benefits, unions, fair labor standards, youth employment, migrant workers
6) Education: education including higher/primary/secondary, underprivileged, vocational, special education, education excellence
7) Environment: environment including drinking water, waste disposal, hazardous waste, air pollution/climate, species and forest protection, conservation
8) Energy: energy including nuclear, electricity, natural gas/oil, coal, alternative/renewable, conservation
9) Immigration: immigration, refugees, citizenship
10) Transportation: transportation including mass transit, highways, air travel, rail, maritime, infrastructure
12) Law & Crime: law and crime including enforcement, white collar crime, drugs, courts, prisons, juvenile crime, child abuse, family issues, police
13) Social Welfare: social welfare including low-income assistance, elderly assistance, disabled assistance, volunteer organisations, child care
14) Housing: housing including community/urban/rural development, low-income/veterans/elderly/homeless housing
15) Domestic Commerce: domestic commerce including banking, securities, consumer finance, insurance regulation, corporate management, small business, copyrights, disaster relief, tourism, consumer safety, sports
16) Defence: defence including alliances, intelligence, readiness, nuclear arms, military aid, personnel, procurement, installations, civil defence, contractors, foreign operations
17) Technology: technology including space, science transfer, telecommunications, broadcast, weather forecasting, computers
18) Foreign Trade: foreign trade including agreements, exports, private investments, competitiveness, tariffs/imports, exchange rates
19) International Affairs: international affairs including foreign aid, developing countries, international finance, Western Europe/EU, specific countries, human rights, organisations, terrorism, diplomats
20) Govt Operations: government operations including intergovernmental relations, bureaucracy, postal service, employees, appointments, currency, procurement, property, tax administration, scandals, branch relations, political campaigns
21) Public Lands: public lands including national parks, indigenous affairs, natural resources and forest management, water resources, territorial/dependency issues
23) Culture: culture including general cultural policy

Return JSON: {"reasoning": "<brief>", "label": <integer>}. You must always choose one of the codes above. Never return null.

Question: {question}
```

---

#### `OAT_CA_FB_DB` — C=full desc only | F=reasoning+label | D=time scope

**System** (135 chars):

```
You are a parliamentary researcher classifying UK Prime Minister's Questions using the Comparative Agendas Project (CAP) coding scheme.
```

**User** (3293 chars):

```
Below is a UK parliamentary question from 1997-2008. Classify it into one of the CAP policy topics.

CAP policy topics:

1) Macroeconomics: general domestic macroeconomic policy, inflation, interest rates, monetary policy, national budget, tax code, industrial policy, price controls
2) Civil Rights: civil rights, minority/ethnic/racial discrimination, gender and sexuality, age/disability discrimination, voting rights, freedom of speech, right to privacy
3) Health: healthcare including reform, insurance, drug industry, medical facilities, disease prevention, mental health, long-term care, drug/tobacco abuse
4) Agriculture: agriculture including trade, subsidies to farmers, food safety, marketing, animal/crop disease, fisheries
5) Labor: labor including worker safety, employment training, benefits, unions, fair labor standards, youth employment, migrant workers
6) Education: education including higher/primary/secondary, underprivileged, vocational, special education, education excellence
7) Environment: environment including drinking water, waste disposal, hazardous waste, air pollution/climate, species and forest protection, conservation
8) Energy: energy including nuclear, electricity, natural gas/oil, coal, alternative/renewable, conservation
9) Immigration: immigration, refugees, citizenship
10) Transportation: transportation including mass transit, highways, air travel, rail, maritime, infrastructure
12) Law & Crime: law and crime including enforcement, white collar crime, drugs, courts, prisons, juvenile crime, child abuse, family issues, police
13) Social Welfare: social welfare including low-income assistance, elderly assistance, disabled assistance, volunteer organisations, child care
14) Housing: housing including community/urban/rural development, low-income/veterans/elderly/homeless housing
15) Domestic Commerce: domestic commerce including banking, securities, consumer finance, insurance regulation, corporate management, small business, copyrights, disaster relief, tourism, consumer safety, sports
16) Defence: defence including alliances, intelligence, readiness, nuclear arms, military aid, personnel, procurement, installations, civil defence, contractors, foreign operations
17) Technology: technology including space, science transfer, telecommunications, broadcast, weather forecasting, computers
18) Foreign Trade: foreign trade including agreements, exports, private investments, competitiveness, tariffs/imports, exchange rates
19) International Affairs: international affairs including foreign aid, developing countries, international finance, Western Europe/EU, specific countries, human rights, organisations, terrorism, diplomats
20) Govt Operations: government operations including intergovernmental relations, bureaucracy, postal service, employees, appointments, currency, procurement, property, tax administration, scandals, branch relations, political campaigns
21) Public Lands: public lands including national parks, indigenous affairs, natural resources and forest management, water resources, territorial/dependency issues
23) Culture: culture including general cultural policy

Return JSON: {"reasoning": "<brief>", "label": <integer>}. You must always choose one of the codes above. Never return null.

Question: {question}
```

---

#### `OAT_CA_FB_DC` — C=full desc only | F=reasoning+label | D=speaker scope

**System** (135 chars):

```
You are a parliamentary researcher classifying UK Prime Minister's Questions using the Comparative Agendas Project (CAP) coding scheme.
```

**User** (3308 chars):

```
Below is a UK parliamentary question asked by a {speaker_party} MP. Classify it into one of the CAP policy topics.

CAP policy topics:

1) Macroeconomics: general domestic macroeconomic policy, inflation, interest rates, monetary policy, national budget, tax code, industrial policy, price controls
2) Civil Rights: civil rights, minority/ethnic/racial discrimination, gender and sexuality, age/disability discrimination, voting rights, freedom of speech, right to privacy
3) Health: healthcare including reform, insurance, drug industry, medical facilities, disease prevention, mental health, long-term care, drug/tobacco abuse
4) Agriculture: agriculture including trade, subsidies to farmers, food safety, marketing, animal/crop disease, fisheries
5) Labor: labor including worker safety, employment training, benefits, unions, fair labor standards, youth employment, migrant workers
6) Education: education including higher/primary/secondary, underprivileged, vocational, special education, education excellence
7) Environment: environment including drinking water, waste disposal, hazardous waste, air pollution/climate, species and forest protection, conservation
8) Energy: energy including nuclear, electricity, natural gas/oil, coal, alternative/renewable, conservation
9) Immigration: immigration, refugees, citizenship
10) Transportation: transportation including mass transit, highways, air travel, rail, maritime, infrastructure
12) Law & Crime: law and crime including enforcement, white collar crime, drugs, courts, prisons, juvenile crime, child abuse, family issues, police
13) Social Welfare: social welfare including low-income assistance, elderly assistance, disabled assistance, volunteer organisations, child care
14) Housing: housing including community/urban/rural development, low-income/veterans/elderly/homeless housing
15) Domestic Commerce: domestic commerce including banking, securities, consumer finance, insurance regulation, corporate management, small business, copyrights, disaster relief, tourism, consumer safety, sports
16) Defence: defence including alliances, intelligence, readiness, nuclear arms, military aid, personnel, procurement, installations, civil defence, contractors, foreign operations
17) Technology: technology including space, science transfer, telecommunications, broadcast, weather forecasting, computers
18) Foreign Trade: foreign trade including agreements, exports, private investments, competitiveness, tariffs/imports, exchange rates
19) International Affairs: international affairs including foreign aid, developing countries, international finance, Western Europe/EU, specific countries, human rights, organisations, terrorism, diplomats
20) Govt Operations: government operations including intergovernmental relations, bureaucracy, postal service, employees, appointments, currency, procurement, property, tax administration, scandals, branch relations, political campaigns
21) Public Lands: public lands including national parks, indigenous affairs, natural resources and forest management, water resources, territorial/dependency issues
23) Culture: culture including general cultural policy

Return JSON: {"reasoning": "<brief>", "label": <integer>}. You must always choose one of the codes above. Never return null.

Question: {question}
```

---

#### `OAT_CA_FC_DA` — C=full desc only | F=reasoning+label + CoT | D=no scope

**System** (251 chars):

```
You are a parliamentary researcher classifying UK Prime Minister's Questions using the Comparative Agendas Project (CAP) coding scheme.

Think step by step: first identify the substantive policy issue at stake, then select the best-matching CAP topic.
```

**User** (3278 chars):

```
Below is a UK parliamentary question. Classify it into one of the CAP policy topics.

CAP policy topics:

1) Macroeconomics: general domestic macroeconomic policy, inflation, interest rates, monetary policy, national budget, tax code, industrial policy, price controls
2) Civil Rights: civil rights, minority/ethnic/racial discrimination, gender and sexuality, age/disability discrimination, voting rights, freedom of speech, right to privacy
3) Health: healthcare including reform, insurance, drug industry, medical facilities, disease prevention, mental health, long-term care, drug/tobacco abuse
4) Agriculture: agriculture including trade, subsidies to farmers, food safety, marketing, animal/crop disease, fisheries
5) Labor: labor including worker safety, employment training, benefits, unions, fair labor standards, youth employment, migrant workers
6) Education: education including higher/primary/secondary, underprivileged, vocational, special education, education excellence
7) Environment: environment including drinking water, waste disposal, hazardous waste, air pollution/climate, species and forest protection, conservation
8) Energy: energy including nuclear, electricity, natural gas/oil, coal, alternative/renewable, conservation
9) Immigration: immigration, refugees, citizenship
10) Transportation: transportation including mass transit, highways, air travel, rail, maritime, infrastructure
12) Law & Crime: law and crime including enforcement, white collar crime, drugs, courts, prisons, juvenile crime, child abuse, family issues, police
13) Social Welfare: social welfare including low-income assistance, elderly assistance, disabled assistance, volunteer organisations, child care
14) Housing: housing including community/urban/rural development, low-income/veterans/elderly/homeless housing
15) Domestic Commerce: domestic commerce including banking, securities, consumer finance, insurance regulation, corporate management, small business, copyrights, disaster relief, tourism, consumer safety, sports
16) Defence: defence including alliances, intelligence, readiness, nuclear arms, military aid, personnel, procurement, installations, civil defence, contractors, foreign operations
17) Technology: technology including space, science transfer, telecommunications, broadcast, weather forecasting, computers
18) Foreign Trade: foreign trade including agreements, exports, private investments, competitiveness, tariffs/imports, exchange rates
19) International Affairs: international affairs including foreign aid, developing countries, international finance, Western Europe/EU, specific countries, human rights, organisations, terrorism, diplomats
20) Govt Operations: government operations including intergovernmental relations, bureaucracy, postal service, employees, appointments, currency, procurement, property, tax administration, scandals, branch relations, political campaigns
21) Public Lands: public lands including national parks, indigenous affairs, natural resources and forest management, water resources, territorial/dependency issues
23) Culture: culture including general cultural policy

Return JSON: {"reasoning": "<brief>", "label": <integer>}. You must always choose one of the codes above. Never return null.

Question: {question}
```

---

#### `OAT_CA_FC_DB` — C=full desc only | F=reasoning+label + CoT | D=time scope

**System** (251 chars):

```
You are a parliamentary researcher classifying UK Prime Minister's Questions using the Comparative Agendas Project (CAP) coding scheme.

Think step by step: first identify the substantive policy issue at stake, then select the best-matching CAP topic.
```

**User** (3293 chars):

```
Below is a UK parliamentary question from 1997-2008. Classify it into one of the CAP policy topics.

CAP policy topics:

1) Macroeconomics: general domestic macroeconomic policy, inflation, interest rates, monetary policy, national budget, tax code, industrial policy, price controls
2) Civil Rights: civil rights, minority/ethnic/racial discrimination, gender and sexuality, age/disability discrimination, voting rights, freedom of speech, right to privacy
3) Health: healthcare including reform, insurance, drug industry, medical facilities, disease prevention, mental health, long-term care, drug/tobacco abuse
4) Agriculture: agriculture including trade, subsidies to farmers, food safety, marketing, animal/crop disease, fisheries
5) Labor: labor including worker safety, employment training, benefits, unions, fair labor standards, youth employment, migrant workers
6) Education: education including higher/primary/secondary, underprivileged, vocational, special education, education excellence
7) Environment: environment including drinking water, waste disposal, hazardous waste, air pollution/climate, species and forest protection, conservation
8) Energy: energy including nuclear, electricity, natural gas/oil, coal, alternative/renewable, conservation
9) Immigration: immigration, refugees, citizenship
10) Transportation: transportation including mass transit, highways, air travel, rail, maritime, infrastructure
12) Law & Crime: law and crime including enforcement, white collar crime, drugs, courts, prisons, juvenile crime, child abuse, family issues, police
13) Social Welfare: social welfare including low-income assistance, elderly assistance, disabled assistance, volunteer organisations, child care
14) Housing: housing including community/urban/rural development, low-income/veterans/elderly/homeless housing
15) Domestic Commerce: domestic commerce including banking, securities, consumer finance, insurance regulation, corporate management, small business, copyrights, disaster relief, tourism, consumer safety, sports
16) Defence: defence including alliances, intelligence, readiness, nuclear arms, military aid, personnel, procurement, installations, civil defence, contractors, foreign operations
17) Technology: technology including space, science transfer, telecommunications, broadcast, weather forecasting, computers
18) Foreign Trade: foreign trade including agreements, exports, private investments, competitiveness, tariffs/imports, exchange rates
19) International Affairs: international affairs including foreign aid, developing countries, international finance, Western Europe/EU, specific countries, human rights, organisations, terrorism, diplomats
20) Govt Operations: government operations including intergovernmental relations, bureaucracy, postal service, employees, appointments, currency, procurement, property, tax administration, scandals, branch relations, political campaigns
21) Public Lands: public lands including national parks, indigenous affairs, natural resources and forest management, water resources, territorial/dependency issues
23) Culture: culture including general cultural policy

Return JSON: {"reasoning": "<brief>", "label": <integer>}. You must always choose one of the codes above. Never return null.

Question: {question}
```

---

#### `OAT_CA_FC_DC` — C=full desc only | F=reasoning+label + CoT | D=speaker scope

**System** (251 chars):

```
You are a parliamentary researcher classifying UK Prime Minister's Questions using the Comparative Agendas Project (CAP) coding scheme.

Think step by step: first identify the substantive policy issue at stake, then select the best-matching CAP topic.
```

**User** (3308 chars):

```
Below is a UK parliamentary question asked by a {speaker_party} MP. Classify it into one of the CAP policy topics.

CAP policy topics:

1) Macroeconomics: general domestic macroeconomic policy, inflation, interest rates, monetary policy, national budget, tax code, industrial policy, price controls
2) Civil Rights: civil rights, minority/ethnic/racial discrimination, gender and sexuality, age/disability discrimination, voting rights, freedom of speech, right to privacy
3) Health: healthcare including reform, insurance, drug industry, medical facilities, disease prevention, mental health, long-term care, drug/tobacco abuse
4) Agriculture: agriculture including trade, subsidies to farmers, food safety, marketing, animal/crop disease, fisheries
5) Labor: labor including worker safety, employment training, benefits, unions, fair labor standards, youth employment, migrant workers
6) Education: education including higher/primary/secondary, underprivileged, vocational, special education, education excellence
7) Environment: environment including drinking water, waste disposal, hazardous waste, air pollution/climate, species and forest protection, conservation
8) Energy: energy including nuclear, electricity, natural gas/oil, coal, alternative/renewable, conservation
9) Immigration: immigration, refugees, citizenship
10) Transportation: transportation including mass transit, highways, air travel, rail, maritime, infrastructure
12) Law & Crime: law and crime including enforcement, white collar crime, drugs, courts, prisons, juvenile crime, child abuse, family issues, police
13) Social Welfare: social welfare including low-income assistance, elderly assistance, disabled assistance, volunteer organisations, child care
14) Housing: housing including community/urban/rural development, low-income/veterans/elderly/homeless housing
15) Domestic Commerce: domestic commerce including banking, securities, consumer finance, insurance regulation, corporate management, small business, copyrights, disaster relief, tourism, consumer safety, sports
16) Defence: defence including alliances, intelligence, readiness, nuclear arms, military aid, personnel, procurement, installations, civil defence, contractors, foreign operations
17) Technology: technology including space, science transfer, telecommunications, broadcast, weather forecasting, computers
18) Foreign Trade: foreign trade including agreements, exports, private investments, competitiveness, tariffs/imports, exchange rates
19) International Affairs: international affairs including foreign aid, developing countries, international finance, Western Europe/EU, specific countries, human rights, organisations, terrorism, diplomats
20) Govt Operations: government operations including intergovernmental relations, bureaucracy, postal service, employees, appointments, currency, procurement, property, tax administration, scandals, branch relations, political campaigns
21) Public Lands: public lands including national parks, indigenous affairs, natural resources and forest management, water resources, territorial/dependency issues
23) Culture: culture including general cultural policy

Return JSON: {"reasoning": "<brief>", "label": <integer>}. You must always choose one of the codes above. Never return null.

Question: {question}
```

---

#### `OAT_CB_FA_DA` — C=full + rule | F=label only | D=no scope

**System** (135 chars):

```
You are a parliamentary researcher classifying UK Prime Minister's Questions using the Comparative Agendas Project (CAP) coding scheme.
```

**User** (4036 chars):

```
Below is a UK parliamentary question. Classify it into one of the CAP policy topics.

CAP policy topics:

1) Macroeconomics: general domestic macroeconomic policy, inflation, interest rates, monetary policy, national budget, tax code, industrial policy, price controls
2) Civil Rights: civil rights, minority/ethnic/racial discrimination, gender and sexuality, age/disability discrimination, voting rights, freedom of speech, right to privacy
3) Health: healthcare including reform, insurance, drug industry, medical facilities, disease prevention, mental health, long-term care, drug/tobacco abuse
4) Agriculture: agriculture including trade, subsidies to farmers, food safety, marketing, animal/crop disease, fisheries
5) Labor: labor including worker safety, employment training, benefits, unions, fair labor standards, youth employment, migrant workers
6) Education: education including higher/primary/secondary, underprivileged, vocational, special education, education excellence
7) Environment: environment including drinking water, waste disposal, hazardous waste, air pollution/climate, species and forest protection, conservation
8) Energy: energy including nuclear, electricity, natural gas/oil, coal, alternative/renewable, conservation
9) Immigration: immigration, refugees, citizenship
10) Transportation: transportation including mass transit, highways, air travel, rail, maritime, infrastructure
12) Law & Crime: law and crime including enforcement, white collar crime, drugs, courts, prisons, juvenile crime, child abuse, family issues, police
13) Social Welfare: social welfare including low-income assistance, elderly assistance, disabled assistance, volunteer organisations, child care
14) Housing: housing including community/urban/rural development, low-income/veterans/elderly/homeless housing
15) Domestic Commerce: domestic commerce including banking, securities, consumer finance, insurance regulation, corporate management, small business, copyrights, disaster relief, tourism, consumer safety, sports
16) Defence: defence including alliances, intelligence, readiness, nuclear arms, military aid, personnel, procurement, installations, civil defence, contractors, foreign operations
17) Technology: technology including space, science transfer, telecommunications, broadcast, weather forecasting, computers
18) Foreign Trade: foreign trade including agreements, exports, private investments, competitiveness, tariffs/imports, exchange rates
19) International Affairs: international affairs including foreign aid, developing countries, international finance, Western Europe/EU, specific countries, human rights, organisations, terrorism, diplomats
20) Govt Operations: government operations including intergovernmental relations, bureaucracy, postal service, employees, appointments, currency, procurement, property, tax administration, scandals, branch relations, political campaigns
21) Public Lands: public lands including national parks, indigenous affairs, natural resources and forest management, water resources, territorial/dependency issues
23) Culture: culture including general cultural policy

Coding rule: Code each question by the substantive policy content it raises, not by its procedural framing, target population, policy instrument, or venue. Three traps to resist:

- Target-population trap: the group a policy affects isn't the topic (e.g., a question about disabled anglers' fishing licences is Civil Rights — disability policy — not Labor or Social Welfare).
- Policy-instrument trap: the mechanism a policy uses isn't the topic (e.g., a question about tax credits for childcare is Social Welfare — childcare policy — not Macroeconomics or Domestic Commerce).
- Venue trap: where a question is asked, or what forum it references, isn't the topic (e.g., a question about WHO recommendations on NHS reform is Health — healthcare policy — not International Affairs).

Return JSON: {"label": <integer>}. You must always choose one of the codes above. Never return null.

Question: {question}
```

---

#### `OAT_CB_FA_DB` — C=full + rule | F=label only | D=time scope

**System** (135 chars):

```
You are a parliamentary researcher classifying UK Prime Minister's Questions using the Comparative Agendas Project (CAP) coding scheme.
```

**User** (4051 chars):

```
Below is a UK parliamentary question from 1997-2008. Classify it into one of the CAP policy topics.

CAP policy topics:

1) Macroeconomics: general domestic macroeconomic policy, inflation, interest rates, monetary policy, national budget, tax code, industrial policy, price controls
2) Civil Rights: civil rights, minority/ethnic/racial discrimination, gender and sexuality, age/disability discrimination, voting rights, freedom of speech, right to privacy
3) Health: healthcare including reform, insurance, drug industry, medical facilities, disease prevention, mental health, long-term care, drug/tobacco abuse
4) Agriculture: agriculture including trade, subsidies to farmers, food safety, marketing, animal/crop disease, fisheries
5) Labor: labor including worker safety, employment training, benefits, unions, fair labor standards, youth employment, migrant workers
6) Education: education including higher/primary/secondary, underprivileged, vocational, special education, education excellence
7) Environment: environment including drinking water, waste disposal, hazardous waste, air pollution/climate, species and forest protection, conservation
8) Energy: energy including nuclear, electricity, natural gas/oil, coal, alternative/renewable, conservation
9) Immigration: immigration, refugees, citizenship
10) Transportation: transportation including mass transit, highways, air travel, rail, maritime, infrastructure
12) Law & Crime: law and crime including enforcement, white collar crime, drugs, courts, prisons, juvenile crime, child abuse, family issues, police
13) Social Welfare: social welfare including low-income assistance, elderly assistance, disabled assistance, volunteer organisations, child care
14) Housing: housing including community/urban/rural development, low-income/veterans/elderly/homeless housing
15) Domestic Commerce: domestic commerce including banking, securities, consumer finance, insurance regulation, corporate management, small business, copyrights, disaster relief, tourism, consumer safety, sports
16) Defence: defence including alliances, intelligence, readiness, nuclear arms, military aid, personnel, procurement, installations, civil defence, contractors, foreign operations
17) Technology: technology including space, science transfer, telecommunications, broadcast, weather forecasting, computers
18) Foreign Trade: foreign trade including agreements, exports, private investments, competitiveness, tariffs/imports, exchange rates
19) International Affairs: international affairs including foreign aid, developing countries, international finance, Western Europe/EU, specific countries, human rights, organisations, terrorism, diplomats
20) Govt Operations: government operations including intergovernmental relations, bureaucracy, postal service, employees, appointments, currency, procurement, property, tax administration, scandals, branch relations, political campaigns
21) Public Lands: public lands including national parks, indigenous affairs, natural resources and forest management, water resources, territorial/dependency issues
23) Culture: culture including general cultural policy

Coding rule: Code each question by the substantive policy content it raises, not by its procedural framing, target population, policy instrument, or venue. Three traps to resist:

- Target-population trap: the group a policy affects isn't the topic (e.g., a question about disabled anglers' fishing licences is Civil Rights — disability policy — not Labor or Social Welfare).
- Policy-instrument trap: the mechanism a policy uses isn't the topic (e.g., a question about tax credits for childcare is Social Welfare — childcare policy — not Macroeconomics or Domestic Commerce).
- Venue trap: where a question is asked, or what forum it references, isn't the topic (e.g., a question about WHO recommendations on NHS reform is Health — healthcare policy — not International Affairs).

Return JSON: {"label": <integer>}. You must always choose one of the codes above. Never return null.

Question: {question}
```

---

#### `OAT_CB_FA_DC` — C=full + rule | F=label only | D=speaker scope

**System** (135 chars):

```
You are a parliamentary researcher classifying UK Prime Minister's Questions using the Comparative Agendas Project (CAP) coding scheme.
```

**User** (4066 chars):

```
Below is a UK parliamentary question asked by a {speaker_party} MP. Classify it into one of the CAP policy topics.

CAP policy topics:

1) Macroeconomics: general domestic macroeconomic policy, inflation, interest rates, monetary policy, national budget, tax code, industrial policy, price controls
2) Civil Rights: civil rights, minority/ethnic/racial discrimination, gender and sexuality, age/disability discrimination, voting rights, freedom of speech, right to privacy
3) Health: healthcare including reform, insurance, drug industry, medical facilities, disease prevention, mental health, long-term care, drug/tobacco abuse
4) Agriculture: agriculture including trade, subsidies to farmers, food safety, marketing, animal/crop disease, fisheries
5) Labor: labor including worker safety, employment training, benefits, unions, fair labor standards, youth employment, migrant workers
6) Education: education including higher/primary/secondary, underprivileged, vocational, special education, education excellence
7) Environment: environment including drinking water, waste disposal, hazardous waste, air pollution/climate, species and forest protection, conservation
8) Energy: energy including nuclear, electricity, natural gas/oil, coal, alternative/renewable, conservation
9) Immigration: immigration, refugees, citizenship
10) Transportation: transportation including mass transit, highways, air travel, rail, maritime, infrastructure
12) Law & Crime: law and crime including enforcement, white collar crime, drugs, courts, prisons, juvenile crime, child abuse, family issues, police
13) Social Welfare: social welfare including low-income assistance, elderly assistance, disabled assistance, volunteer organisations, child care
14) Housing: housing including community/urban/rural development, low-income/veterans/elderly/homeless housing
15) Domestic Commerce: domestic commerce including banking, securities, consumer finance, insurance regulation, corporate management, small business, copyrights, disaster relief, tourism, consumer safety, sports
16) Defence: defence including alliances, intelligence, readiness, nuclear arms, military aid, personnel, procurement, installations, civil defence, contractors, foreign operations
17) Technology: technology including space, science transfer, telecommunications, broadcast, weather forecasting, computers
18) Foreign Trade: foreign trade including agreements, exports, private investments, competitiveness, tariffs/imports, exchange rates
19) International Affairs: international affairs including foreign aid, developing countries, international finance, Western Europe/EU, specific countries, human rights, organisations, terrorism, diplomats
20) Govt Operations: government operations including intergovernmental relations, bureaucracy, postal service, employees, appointments, currency, procurement, property, tax administration, scandals, branch relations, political campaigns
21) Public Lands: public lands including national parks, indigenous affairs, natural resources and forest management, water resources, territorial/dependency issues
23) Culture: culture including general cultural policy

Coding rule: Code each question by the substantive policy content it raises, not by its procedural framing, target population, policy instrument, or venue. Three traps to resist:

- Target-population trap: the group a policy affects isn't the topic (e.g., a question about disabled anglers' fishing licences is Civil Rights — disability policy — not Labor or Social Welfare).
- Policy-instrument trap: the mechanism a policy uses isn't the topic (e.g., a question about tax credits for childcare is Social Welfare — childcare policy — not Macroeconomics or Domestic Commerce).
- Venue trap: where a question is asked, or what forum it references, isn't the topic (e.g., a question about WHO recommendations on NHS reform is Health — healthcare policy — not International Affairs).

Return JSON: {"label": <integer>}. You must always choose one of the codes above. Never return null.

Question: {question}
```

---

#### `OAT_CB_FB_DA` — C=full + rule | F=reasoning+label | D=no scope

**System** (135 chars):

```
You are a parliamentary researcher classifying UK Prime Minister's Questions using the Comparative Agendas Project (CAP) coding scheme.
```

**User** (4060 chars):

```
Below is a UK parliamentary question. Classify it into one of the CAP policy topics.

CAP policy topics:

1) Macroeconomics: general domestic macroeconomic policy, inflation, interest rates, monetary policy, national budget, tax code, industrial policy, price controls
2) Civil Rights: civil rights, minority/ethnic/racial discrimination, gender and sexuality, age/disability discrimination, voting rights, freedom of speech, right to privacy
3) Health: healthcare including reform, insurance, drug industry, medical facilities, disease prevention, mental health, long-term care, drug/tobacco abuse
4) Agriculture: agriculture including trade, subsidies to farmers, food safety, marketing, animal/crop disease, fisheries
5) Labor: labor including worker safety, employment training, benefits, unions, fair labor standards, youth employment, migrant workers
6) Education: education including higher/primary/secondary, underprivileged, vocational, special education, education excellence
7) Environment: environment including drinking water, waste disposal, hazardous waste, air pollution/climate, species and forest protection, conservation
8) Energy: energy including nuclear, electricity, natural gas/oil, coal, alternative/renewable, conservation
9) Immigration: immigration, refugees, citizenship
10) Transportation: transportation including mass transit, highways, air travel, rail, maritime, infrastructure
12) Law & Crime: law and crime including enforcement, white collar crime, drugs, courts, prisons, juvenile crime, child abuse, family issues, police
13) Social Welfare: social welfare including low-income assistance, elderly assistance, disabled assistance, volunteer organisations, child care
14) Housing: housing including community/urban/rural development, low-income/veterans/elderly/homeless housing
15) Domestic Commerce: domestic commerce including banking, securities, consumer finance, insurance regulation, corporate management, small business, copyrights, disaster relief, tourism, consumer safety, sports
16) Defence: defence including alliances, intelligence, readiness, nuclear arms, military aid, personnel, procurement, installations, civil defence, contractors, foreign operations
17) Technology: technology including space, science transfer, telecommunications, broadcast, weather forecasting, computers
18) Foreign Trade: foreign trade including agreements, exports, private investments, competitiveness, tariffs/imports, exchange rates
19) International Affairs: international affairs including foreign aid, developing countries, international finance, Western Europe/EU, specific countries, human rights, organisations, terrorism, diplomats
20) Govt Operations: government operations including intergovernmental relations, bureaucracy, postal service, employees, appointments, currency, procurement, property, tax administration, scandals, branch relations, political campaigns
21) Public Lands: public lands including national parks, indigenous affairs, natural resources and forest management, water resources, territorial/dependency issues
23) Culture: culture including general cultural policy

Coding rule: Code each question by the substantive policy content it raises, not by its procedural framing, target population, policy instrument, or venue. Three traps to resist:

- Target-population trap: the group a policy affects isn't the topic (e.g., a question about disabled anglers' fishing licences is Civil Rights — disability policy — not Labor or Social Welfare).
- Policy-instrument trap: the mechanism a policy uses isn't the topic (e.g., a question about tax credits for childcare is Social Welfare — childcare policy — not Macroeconomics or Domestic Commerce).
- Venue trap: where a question is asked, or what forum it references, isn't the topic (e.g., a question about WHO recommendations on NHS reform is Health — healthcare policy — not International Affairs).

Return JSON: {"reasoning": "<brief>", "label": <integer>}. You must always choose one of the codes above. Never return null.

Question: {question}
```

---

#### `OAT_CB_FB_DB` — C=full + rule | F=reasoning+label | D=time scope

**System** (135 chars):

```
You are a parliamentary researcher classifying UK Prime Minister's Questions using the Comparative Agendas Project (CAP) coding scheme.
```

**User** (4075 chars):

```
Below is a UK parliamentary question from 1997-2008. Classify it into one of the CAP policy topics.

CAP policy topics:

1) Macroeconomics: general domestic macroeconomic policy, inflation, interest rates, monetary policy, national budget, tax code, industrial policy, price controls
2) Civil Rights: civil rights, minority/ethnic/racial discrimination, gender and sexuality, age/disability discrimination, voting rights, freedom of speech, right to privacy
3) Health: healthcare including reform, insurance, drug industry, medical facilities, disease prevention, mental health, long-term care, drug/tobacco abuse
4) Agriculture: agriculture including trade, subsidies to farmers, food safety, marketing, animal/crop disease, fisheries
5) Labor: labor including worker safety, employment training, benefits, unions, fair labor standards, youth employment, migrant workers
6) Education: education including higher/primary/secondary, underprivileged, vocational, special education, education excellence
7) Environment: environment including drinking water, waste disposal, hazardous waste, air pollution/climate, species and forest protection, conservation
8) Energy: energy including nuclear, electricity, natural gas/oil, coal, alternative/renewable, conservation
9) Immigration: immigration, refugees, citizenship
10) Transportation: transportation including mass transit, highways, air travel, rail, maritime, infrastructure
12) Law & Crime: law and crime including enforcement, white collar crime, drugs, courts, prisons, juvenile crime, child abuse, family issues, police
13) Social Welfare: social welfare including low-income assistance, elderly assistance, disabled assistance, volunteer organisations, child care
14) Housing: housing including community/urban/rural development, low-income/veterans/elderly/homeless housing
15) Domestic Commerce: domestic commerce including banking, securities, consumer finance, insurance regulation, corporate management, small business, copyrights, disaster relief, tourism, consumer safety, sports
16) Defence: defence including alliances, intelligence, readiness, nuclear arms, military aid, personnel, procurement, installations, civil defence, contractors, foreign operations
17) Technology: technology including space, science transfer, telecommunications, broadcast, weather forecasting, computers
18) Foreign Trade: foreign trade including agreements, exports, private investments, competitiveness, tariffs/imports, exchange rates
19) International Affairs: international affairs including foreign aid, developing countries, international finance, Western Europe/EU, specific countries, human rights, organisations, terrorism, diplomats
20) Govt Operations: government operations including intergovernmental relations, bureaucracy, postal service, employees, appointments, currency, procurement, property, tax administration, scandals, branch relations, political campaigns
21) Public Lands: public lands including national parks, indigenous affairs, natural resources and forest management, water resources, territorial/dependency issues
23) Culture: culture including general cultural policy

Coding rule: Code each question by the substantive policy content it raises, not by its procedural framing, target population, policy instrument, or venue. Three traps to resist:

- Target-population trap: the group a policy affects isn't the topic (e.g., a question about disabled anglers' fishing licences is Civil Rights — disability policy — not Labor or Social Welfare).
- Policy-instrument trap: the mechanism a policy uses isn't the topic (e.g., a question about tax credits for childcare is Social Welfare — childcare policy — not Macroeconomics or Domestic Commerce).
- Venue trap: where a question is asked, or what forum it references, isn't the topic (e.g., a question about WHO recommendations on NHS reform is Health — healthcare policy — not International Affairs).

Return JSON: {"reasoning": "<brief>", "label": <integer>}. You must always choose one of the codes above. Never return null.

Question: {question}
```

---

#### `OAT_CB_FB_DC` — C=full + rule | F=reasoning+label | D=speaker scope

**System** (135 chars):

```
You are a parliamentary researcher classifying UK Prime Minister's Questions using the Comparative Agendas Project (CAP) coding scheme.
```

**User** (4090 chars):

```
Below is a UK parliamentary question asked by a {speaker_party} MP. Classify it into one of the CAP policy topics.

CAP policy topics:

1) Macroeconomics: general domestic macroeconomic policy, inflation, interest rates, monetary policy, national budget, tax code, industrial policy, price controls
2) Civil Rights: civil rights, minority/ethnic/racial discrimination, gender and sexuality, age/disability discrimination, voting rights, freedom of speech, right to privacy
3) Health: healthcare including reform, insurance, drug industry, medical facilities, disease prevention, mental health, long-term care, drug/tobacco abuse
4) Agriculture: agriculture including trade, subsidies to farmers, food safety, marketing, animal/crop disease, fisheries
5) Labor: labor including worker safety, employment training, benefits, unions, fair labor standards, youth employment, migrant workers
6) Education: education including higher/primary/secondary, underprivileged, vocational, special education, education excellence
7) Environment: environment including drinking water, waste disposal, hazardous waste, air pollution/climate, species and forest protection, conservation
8) Energy: energy including nuclear, electricity, natural gas/oil, coal, alternative/renewable, conservation
9) Immigration: immigration, refugees, citizenship
10) Transportation: transportation including mass transit, highways, air travel, rail, maritime, infrastructure
12) Law & Crime: law and crime including enforcement, white collar crime, drugs, courts, prisons, juvenile crime, child abuse, family issues, police
13) Social Welfare: social welfare including low-income assistance, elderly assistance, disabled assistance, volunteer organisations, child care
14) Housing: housing including community/urban/rural development, low-income/veterans/elderly/homeless housing
15) Domestic Commerce: domestic commerce including banking, securities, consumer finance, insurance regulation, corporate management, small business, copyrights, disaster relief, tourism, consumer safety, sports
16) Defence: defence including alliances, intelligence, readiness, nuclear arms, military aid, personnel, procurement, installations, civil defence, contractors, foreign operations
17) Technology: technology including space, science transfer, telecommunications, broadcast, weather forecasting, computers
18) Foreign Trade: foreign trade including agreements, exports, private investments, competitiveness, tariffs/imports, exchange rates
19) International Affairs: international affairs including foreign aid, developing countries, international finance, Western Europe/EU, specific countries, human rights, organisations, terrorism, diplomats
20) Govt Operations: government operations including intergovernmental relations, bureaucracy, postal service, employees, appointments, currency, procurement, property, tax administration, scandals, branch relations, political campaigns
21) Public Lands: public lands including national parks, indigenous affairs, natural resources and forest management, water resources, territorial/dependency issues
23) Culture: culture including general cultural policy

Coding rule: Code each question by the substantive policy content it raises, not by its procedural framing, target population, policy instrument, or venue. Three traps to resist:

- Target-population trap: the group a policy affects isn't the topic (e.g., a question about disabled anglers' fishing licences is Civil Rights — disability policy — not Labor or Social Welfare).
- Policy-instrument trap: the mechanism a policy uses isn't the topic (e.g., a question about tax credits for childcare is Social Welfare — childcare policy — not Macroeconomics or Domestic Commerce).
- Venue trap: where a question is asked, or what forum it references, isn't the topic (e.g., a question about WHO recommendations on NHS reform is Health — healthcare policy — not International Affairs).

Return JSON: {"reasoning": "<brief>", "label": <integer>}. You must always choose one of the codes above. Never return null.

Question: {question}
```

---

#### `OAT_CB_FC_DA` — C=full + rule | F=reasoning+label + CoT | D=no scope

**System** (251 chars):

```
You are a parliamentary researcher classifying UK Prime Minister's Questions using the Comparative Agendas Project (CAP) coding scheme.

Think step by step: first identify the substantive policy issue at stake, then select the best-matching CAP topic.
```

**User** (4060 chars):

```
Below is a UK parliamentary question. Classify it into one of the CAP policy topics.

CAP policy topics:

1) Macroeconomics: general domestic macroeconomic policy, inflation, interest rates, monetary policy, national budget, tax code, industrial policy, price controls
2) Civil Rights: civil rights, minority/ethnic/racial discrimination, gender and sexuality, age/disability discrimination, voting rights, freedom of speech, right to privacy
3) Health: healthcare including reform, insurance, drug industry, medical facilities, disease prevention, mental health, long-term care, drug/tobacco abuse
4) Agriculture: agriculture including trade, subsidies to farmers, food safety, marketing, animal/crop disease, fisheries
5) Labor: labor including worker safety, employment training, benefits, unions, fair labor standards, youth employment, migrant workers
6) Education: education including higher/primary/secondary, underprivileged, vocational, special education, education excellence
7) Environment: environment including drinking water, waste disposal, hazardous waste, air pollution/climate, species and forest protection, conservation
8) Energy: energy including nuclear, electricity, natural gas/oil, coal, alternative/renewable, conservation
9) Immigration: immigration, refugees, citizenship
10) Transportation: transportation including mass transit, highways, air travel, rail, maritime, infrastructure
12) Law & Crime: law and crime including enforcement, white collar crime, drugs, courts, prisons, juvenile crime, child abuse, family issues, police
13) Social Welfare: social welfare including low-income assistance, elderly assistance, disabled assistance, volunteer organisations, child care
14) Housing: housing including community/urban/rural development, low-income/veterans/elderly/homeless housing
15) Domestic Commerce: domestic commerce including banking, securities, consumer finance, insurance regulation, corporate management, small business, copyrights, disaster relief, tourism, consumer safety, sports
16) Defence: defence including alliances, intelligence, readiness, nuclear arms, military aid, personnel, procurement, installations, civil defence, contractors, foreign operations
17) Technology: technology including space, science transfer, telecommunications, broadcast, weather forecasting, computers
18) Foreign Trade: foreign trade including agreements, exports, private investments, competitiveness, tariffs/imports, exchange rates
19) International Affairs: international affairs including foreign aid, developing countries, international finance, Western Europe/EU, specific countries, human rights, organisations, terrorism, diplomats
20) Govt Operations: government operations including intergovernmental relations, bureaucracy, postal service, employees, appointments, currency, procurement, property, tax administration, scandals, branch relations, political campaigns
21) Public Lands: public lands including national parks, indigenous affairs, natural resources and forest management, water resources, territorial/dependency issues
23) Culture: culture including general cultural policy

Coding rule: Code each question by the substantive policy content it raises, not by its procedural framing, target population, policy instrument, or venue. Three traps to resist:

- Target-population trap: the group a policy affects isn't the topic (e.g., a question about disabled anglers' fishing licences is Civil Rights — disability policy — not Labor or Social Welfare).
- Policy-instrument trap: the mechanism a policy uses isn't the topic (e.g., a question about tax credits for childcare is Social Welfare — childcare policy — not Macroeconomics or Domestic Commerce).
- Venue trap: where a question is asked, or what forum it references, isn't the topic (e.g., a question about WHO recommendations on NHS reform is Health — healthcare policy — not International Affairs).

Return JSON: {"reasoning": "<brief>", "label": <integer>}. You must always choose one of the codes above. Never return null.

Question: {question}
```

---

#### `OAT_CB_FC_DB` — C=full + rule | F=reasoning+label + CoT | D=time scope

**System** (251 chars):

```
You are a parliamentary researcher classifying UK Prime Minister's Questions using the Comparative Agendas Project (CAP) coding scheme.

Think step by step: first identify the substantive policy issue at stake, then select the best-matching CAP topic.
```

**User** (4075 chars):

```
Below is a UK parliamentary question from 1997-2008. Classify it into one of the CAP policy topics.

CAP policy topics:

1) Macroeconomics: general domestic macroeconomic policy, inflation, interest rates, monetary policy, national budget, tax code, industrial policy, price controls
2) Civil Rights: civil rights, minority/ethnic/racial discrimination, gender and sexuality, age/disability discrimination, voting rights, freedom of speech, right to privacy
3) Health: healthcare including reform, insurance, drug industry, medical facilities, disease prevention, mental health, long-term care, drug/tobacco abuse
4) Agriculture: agriculture including trade, subsidies to farmers, food safety, marketing, animal/crop disease, fisheries
5) Labor: labor including worker safety, employment training, benefits, unions, fair labor standards, youth employment, migrant workers
6) Education: education including higher/primary/secondary, underprivileged, vocational, special education, education excellence
7) Environment: environment including drinking water, waste disposal, hazardous waste, air pollution/climate, species and forest protection, conservation
8) Energy: energy including nuclear, electricity, natural gas/oil, coal, alternative/renewable, conservation
9) Immigration: immigration, refugees, citizenship
10) Transportation: transportation including mass transit, highways, air travel, rail, maritime, infrastructure
12) Law & Crime: law and crime including enforcement, white collar crime, drugs, courts, prisons, juvenile crime, child abuse, family issues, police
13) Social Welfare: social welfare including low-income assistance, elderly assistance, disabled assistance, volunteer organisations, child care
14) Housing: housing including community/urban/rural development, low-income/veterans/elderly/homeless housing
15) Domestic Commerce: domestic commerce including banking, securities, consumer finance, insurance regulation, corporate management, small business, copyrights, disaster relief, tourism, consumer safety, sports
16) Defence: defence including alliances, intelligence, readiness, nuclear arms, military aid, personnel, procurement, installations, civil defence, contractors, foreign operations
17) Technology: technology including space, science transfer, telecommunications, broadcast, weather forecasting, computers
18) Foreign Trade: foreign trade including agreements, exports, private investments, competitiveness, tariffs/imports, exchange rates
19) International Affairs: international affairs including foreign aid, developing countries, international finance, Western Europe/EU, specific countries, human rights, organisations, terrorism, diplomats
20) Govt Operations: government operations including intergovernmental relations, bureaucracy, postal service, employees, appointments, currency, procurement, property, tax administration, scandals, branch relations, political campaigns
21) Public Lands: public lands including national parks, indigenous affairs, natural resources and forest management, water resources, territorial/dependency issues
23) Culture: culture including general cultural policy

Coding rule: Code each question by the substantive policy content it raises, not by its procedural framing, target population, policy instrument, or venue. Three traps to resist:

- Target-population trap: the group a policy affects isn't the topic (e.g., a question about disabled anglers' fishing licences is Civil Rights — disability policy — not Labor or Social Welfare).
- Policy-instrument trap: the mechanism a policy uses isn't the topic (e.g., a question about tax credits for childcare is Social Welfare — childcare policy — not Macroeconomics or Domestic Commerce).
- Venue trap: where a question is asked, or what forum it references, isn't the topic (e.g., a question about WHO recommendations on NHS reform is Health — healthcare policy — not International Affairs).

Return JSON: {"reasoning": "<brief>", "label": <integer>}. You must always choose one of the codes above. Never return null.

Question: {question}
```

---

#### `OAT_CB_FC_DC` — C=full + rule | F=reasoning+label + CoT | D=speaker scope

**System** (251 chars):

```
You are a parliamentary researcher classifying UK Prime Minister's Questions using the Comparative Agendas Project (CAP) coding scheme.

Think step by step: first identify the substantive policy issue at stake, then select the best-matching CAP topic.
```

**User** (4090 chars):

```
Below is a UK parliamentary question asked by a {speaker_party} MP. Classify it into one of the CAP policy topics.

CAP policy topics:

1) Macroeconomics: general domestic macroeconomic policy, inflation, interest rates, monetary policy, national budget, tax code, industrial policy, price controls
2) Civil Rights: civil rights, minority/ethnic/racial discrimination, gender and sexuality, age/disability discrimination, voting rights, freedom of speech, right to privacy
3) Health: healthcare including reform, insurance, drug industry, medical facilities, disease prevention, mental health, long-term care, drug/tobacco abuse
4) Agriculture: agriculture including trade, subsidies to farmers, food safety, marketing, animal/crop disease, fisheries
5) Labor: labor including worker safety, employment training, benefits, unions, fair labor standards, youth employment, migrant workers
6) Education: education including higher/primary/secondary, underprivileged, vocational, special education, education excellence
7) Environment: environment including drinking water, waste disposal, hazardous waste, air pollution/climate, species and forest protection, conservation
8) Energy: energy including nuclear, electricity, natural gas/oil, coal, alternative/renewable, conservation
9) Immigration: immigration, refugees, citizenship
10) Transportation: transportation including mass transit, highways, air travel, rail, maritime, infrastructure
12) Law & Crime: law and crime including enforcement, white collar crime, drugs, courts, prisons, juvenile crime, child abuse, family issues, police
13) Social Welfare: social welfare including low-income assistance, elderly assistance, disabled assistance, volunteer organisations, child care
14) Housing: housing including community/urban/rural development, low-income/veterans/elderly/homeless housing
15) Domestic Commerce: domestic commerce including banking, securities, consumer finance, insurance regulation, corporate management, small business, copyrights, disaster relief, tourism, consumer safety, sports
16) Defence: defence including alliances, intelligence, readiness, nuclear arms, military aid, personnel, procurement, installations, civil defence, contractors, foreign operations
17) Technology: technology including space, science transfer, telecommunications, broadcast, weather forecasting, computers
18) Foreign Trade: foreign trade including agreements, exports, private investments, competitiveness, tariffs/imports, exchange rates
19) International Affairs: international affairs including foreign aid, developing countries, international finance, Western Europe/EU, specific countries, human rights, organisations, terrorism, diplomats
20) Govt Operations: government operations including intergovernmental relations, bureaucracy, postal service, employees, appointments, currency, procurement, property, tax administration, scandals, branch relations, political campaigns
21) Public Lands: public lands including national parks, indigenous affairs, natural resources and forest management, water resources, territorial/dependency issues
23) Culture: culture including general cultural policy

Coding rule: Code each question by the substantive policy content it raises, not by its procedural framing, target population, policy instrument, or venue. Three traps to resist:

- Target-population trap: the group a policy affects isn't the topic (e.g., a question about disabled anglers' fishing licences is Civil Rights — disability policy — not Labor or Social Welfare).
- Policy-instrument trap: the mechanism a policy uses isn't the topic (e.g., a question about tax credits for childcare is Social Welfare — childcare policy — not Macroeconomics or Domestic Commerce).
- Venue trap: where a question is asked, or what forum it references, isn't the topic (e.g., a question about WHO recommendations on NHS reform is Health — healthcare policy — not International Affairs).

Return JSON: {"reasoning": "<brief>", "label": <integer>}. You must always choose one of the codes above. Never return null.

Question: {question}
```

---

#### `OAT_CC_FA_DA` — C=full + rule + fewshots | F=label only | D=no scope

**System** (135 chars):

```
You are a parliamentary researcher classifying UK Prime Minister's Questions using the Comparative Agendas Project (CAP) coding scheme.
```

**User** (6450 chars):

```
Below is a UK parliamentary question. Classify it into one of the CAP policy topics.

CAP policy topics:

1) Macroeconomics: general domestic macroeconomic policy, inflation, interest rates, monetary policy, national budget, tax code, industrial policy, price controls
2) Civil Rights: civil rights, minority/ethnic/racial discrimination, gender and sexuality, age/disability discrimination, voting rights, freedom of speech, right to privacy
3) Health: healthcare including reform, insurance, drug industry, medical facilities, disease prevention, mental health, long-term care, drug/tobacco abuse
4) Agriculture: agriculture including trade, subsidies to farmers, food safety, marketing, animal/crop disease, fisheries
5) Labor: labor including worker safety, employment training, benefits, unions, fair labor standards, youth employment, migrant workers
6) Education: education including higher/primary/secondary, underprivileged, vocational, special education, education excellence
7) Environment: environment including drinking water, waste disposal, hazardous waste, air pollution/climate, species and forest protection, conservation
8) Energy: energy including nuclear, electricity, natural gas/oil, coal, alternative/renewable, conservation
9) Immigration: immigration, refugees, citizenship
10) Transportation: transportation including mass transit, highways, air travel, rail, maritime, infrastructure
12) Law & Crime: law and crime including enforcement, white collar crime, drugs, courts, prisons, juvenile crime, child abuse, family issues, police
13) Social Welfare: social welfare including low-income assistance, elderly assistance, disabled assistance, volunteer organisations, child care
14) Housing: housing including community/urban/rural development, low-income/veterans/elderly/homeless housing
15) Domestic Commerce: domestic commerce including banking, securities, consumer finance, insurance regulation, corporate management, small business, copyrights, disaster relief, tourism, consumer safety, sports
16) Defence: defence including alliances, intelligence, readiness, nuclear arms, military aid, personnel, procurement, installations, civil defence, contractors, foreign operations
17) Technology: technology including space, science transfer, telecommunications, broadcast, weather forecasting, computers
18) Foreign Trade: foreign trade including agreements, exports, private investments, competitiveness, tariffs/imports, exchange rates
19) International Affairs: international affairs including foreign aid, developing countries, international finance, Western Europe/EU, specific countries, human rights, organisations, terrorism, diplomats
20) Govt Operations: government operations including intergovernmental relations, bureaucracy, postal service, employees, appointments, currency, procurement, property, tax administration, scandals, branch relations, political campaigns
21) Public Lands: public lands including national parks, indigenous affairs, natural resources and forest management, water resources, territorial/dependency issues
23) Culture: culture including general cultural policy

Coding rule: Code each question by the substantive policy content it raises, not by its procedural framing, target population, policy instrument, or venue. Three traps to resist:

- Target-population trap: the group a policy affects isn't the topic (e.g., a question about disabled anglers' fishing licences is Civil Rights — disability policy — not Labor or Social Welfare).
- Policy-instrument trap: the mechanism a policy uses isn't the topic (e.g., a question about tax credits for childcare is Social Welfare — childcare policy — not Macroeconomics or Domestic Commerce).
- Venue trap: where a question is asked, or what forum it references, isn't the topic (e.g., a question about WHO recommendations on NHS reform is Health — healthcare policy — not International Affairs).

Examples:

Example 1:
Question: "Business leaders at the CBI conference in Birmingham this week expressed support for the Government's policy of preparing the economy for possible United Kingdom entry into the single European currency. They also expressed support for the Government's spending plans, and felt that they were sustainable and that cuts in public spending were not required. In view of the policies put forward by the Conservative party on both those issues, does my right hon. Friend agree that it will be many years before that party regains the confidence of UK business?"
Answer: {"label": 1}

Example 2:
Question: "Q6. [10883]  When my right hon. Friend meets President Bush, will he put high on the agenda the plight of hundreds and thousands of Afghans, caused by the failure of food to get through to villages in Afghanistan?"
Answer: {"label": 19}

Example 3:
Question: "I am sure that my right hon. Friend will have been impressed by the incredible courage of Adrian Sudbury, who is using the last weeks of his life to campaign for more bone marrow donors to come forward. I have been impressed by the response so far of the Secretaries of State for Children, Schools and Families and for Health, but what more can my right hon. Friend do to help my friend Adrian to achieve his legacy and help 7,000 people to live?"
Answer: {"label": 3}

Example 4:
Question: "While the Prime Minister is on the subject of disabled people, may I ask whether he is aware that Labour’s attack on vulnerable people has been extended to disabled anglers? They have seen the cost of their fishing licence
30 Apr 2008 : Column 304
go up by 37 per cent., as opposed to 2 per cent. for able-bodied people—if, that is, they can find a post office from which to buy one"
Answer: {"label": 2}

Example 5:
Question: "Has my right hon. Friend noticed that all opinion polls show that the overwhelming majority of country dwellers are opposed to hunting with hounds?"
Answer: {"label": 7}

Example 6:
Question: "It seems certain that coal miners’ beat knee is about to be made a prescribed industrial disease. In order that we can avoid another feeding frenzy for solicitors, will the Prime Minister get his Ministers to meet interested MPs to see whether a scheme can be established that gives value for money to the taxpayer, fair compensation to the coal miner and nothing to the solicitor?"
Answer: {"label": 8}

Return JSON: {"label": <integer>}. You must always choose one of the codes above. Never return null.

Question: {question}
```

---

#### `OAT_CC_FA_DB` — C=full + rule + fewshots | F=label only | D=time scope

**System** (135 chars):

```
You are a parliamentary researcher classifying UK Prime Minister's Questions using the Comparative Agendas Project (CAP) coding scheme.
```

**User** (6465 chars):

```
Below is a UK parliamentary question from 1997-2008. Classify it into one of the CAP policy topics.

CAP policy topics:

1) Macroeconomics: general domestic macroeconomic policy, inflation, interest rates, monetary policy, national budget, tax code, industrial policy, price controls
2) Civil Rights: civil rights, minority/ethnic/racial discrimination, gender and sexuality, age/disability discrimination, voting rights, freedom of speech, right to privacy
3) Health: healthcare including reform, insurance, drug industry, medical facilities, disease prevention, mental health, long-term care, drug/tobacco abuse
4) Agriculture: agriculture including trade, subsidies to farmers, food safety, marketing, animal/crop disease, fisheries
5) Labor: labor including worker safety, employment training, benefits, unions, fair labor standards, youth employment, migrant workers
6) Education: education including higher/primary/secondary, underprivileged, vocational, special education, education excellence
7) Environment: environment including drinking water, waste disposal, hazardous waste, air pollution/climate, species and forest protection, conservation
8) Energy: energy including nuclear, electricity, natural gas/oil, coal, alternative/renewable, conservation
9) Immigration: immigration, refugees, citizenship
10) Transportation: transportation including mass transit, highways, air travel, rail, maritime, infrastructure
12) Law & Crime: law and crime including enforcement, white collar crime, drugs, courts, prisons, juvenile crime, child abuse, family issues, police
13) Social Welfare: social welfare including low-income assistance, elderly assistance, disabled assistance, volunteer organisations, child care
14) Housing: housing including community/urban/rural development, low-income/veterans/elderly/homeless housing
15) Domestic Commerce: domestic commerce including banking, securities, consumer finance, insurance regulation, corporate management, small business, copyrights, disaster relief, tourism, consumer safety, sports
16) Defence: defence including alliances, intelligence, readiness, nuclear arms, military aid, personnel, procurement, installations, civil defence, contractors, foreign operations
17) Technology: technology including space, science transfer, telecommunications, broadcast, weather forecasting, computers
18) Foreign Trade: foreign trade including agreements, exports, private investments, competitiveness, tariffs/imports, exchange rates
19) International Affairs: international affairs including foreign aid, developing countries, international finance, Western Europe/EU, specific countries, human rights, organisations, terrorism, diplomats
20) Govt Operations: government operations including intergovernmental relations, bureaucracy, postal service, employees, appointments, currency, procurement, property, tax administration, scandals, branch relations, political campaigns
21) Public Lands: public lands including national parks, indigenous affairs, natural resources and forest management, water resources, territorial/dependency issues
23) Culture: culture including general cultural policy

Coding rule: Code each question by the substantive policy content it raises, not by its procedural framing, target population, policy instrument, or venue. Three traps to resist:

- Target-population trap: the group a policy affects isn't the topic (e.g., a question about disabled anglers' fishing licences is Civil Rights — disability policy — not Labor or Social Welfare).
- Policy-instrument trap: the mechanism a policy uses isn't the topic (e.g., a question about tax credits for childcare is Social Welfare — childcare policy — not Macroeconomics or Domestic Commerce).
- Venue trap: where a question is asked, or what forum it references, isn't the topic (e.g., a question about WHO recommendations on NHS reform is Health — healthcare policy — not International Affairs).

Examples:

Example 1:
Question: "Business leaders at the CBI conference in Birmingham this week expressed support for the Government's policy of preparing the economy for possible United Kingdom entry into the single European currency. They also expressed support for the Government's spending plans, and felt that they were sustainable and that cuts in public spending were not required. In view of the policies put forward by the Conservative party on both those issues, does my right hon. Friend agree that it will be many years before that party regains the confidence of UK business?"
Answer: {"label": 1}

Example 2:
Question: "Q6. [10883]  When my right hon. Friend meets President Bush, will he put high on the agenda the plight of hundreds and thousands of Afghans, caused by the failure of food to get through to villages in Afghanistan?"
Answer: {"label": 19}

Example 3:
Question: "I am sure that my right hon. Friend will have been impressed by the incredible courage of Adrian Sudbury, who is using the last weeks of his life to campaign for more bone marrow donors to come forward. I have been impressed by the response so far of the Secretaries of State for Children, Schools and Families and for Health, but what more can my right hon. Friend do to help my friend Adrian to achieve his legacy and help 7,000 people to live?"
Answer: {"label": 3}

Example 4:
Question: "While the Prime Minister is on the subject of disabled people, may I ask whether he is aware that Labour’s attack on vulnerable people has been extended to disabled anglers? They have seen the cost of their fishing licence
30 Apr 2008 : Column 304
go up by 37 per cent., as opposed to 2 per cent. for able-bodied people—if, that is, they can find a post office from which to buy one"
Answer: {"label": 2}

Example 5:
Question: "Has my right hon. Friend noticed that all opinion polls show that the overwhelming majority of country dwellers are opposed to hunting with hounds?"
Answer: {"label": 7}

Example 6:
Question: "It seems certain that coal miners’ beat knee is about to be made a prescribed industrial disease. In order that we can avoid another feeding frenzy for solicitors, will the Prime Minister get his Ministers to meet interested MPs to see whether a scheme can be established that gives value for money to the taxpayer, fair compensation to the coal miner and nothing to the solicitor?"
Answer: {"label": 8}

Return JSON: {"label": <integer>}. You must always choose one of the codes above. Never return null.

Question: {question}
```

---

#### `OAT_CC_FA_DC` — C=full + rule + fewshots | F=label only | D=speaker scope

**System** (135 chars):

```
You are a parliamentary researcher classifying UK Prime Minister's Questions using the Comparative Agendas Project (CAP) coding scheme.
```

**User** (6480 chars):

```
Below is a UK parliamentary question asked by a {speaker_party} MP. Classify it into one of the CAP policy topics.

CAP policy topics:

1) Macroeconomics: general domestic macroeconomic policy, inflation, interest rates, monetary policy, national budget, tax code, industrial policy, price controls
2) Civil Rights: civil rights, minority/ethnic/racial discrimination, gender and sexuality, age/disability discrimination, voting rights, freedom of speech, right to privacy
3) Health: healthcare including reform, insurance, drug industry, medical facilities, disease prevention, mental health, long-term care, drug/tobacco abuse
4) Agriculture: agriculture including trade, subsidies to farmers, food safety, marketing, animal/crop disease, fisheries
5) Labor: labor including worker safety, employment training, benefits, unions, fair labor standards, youth employment, migrant workers
6) Education: education including higher/primary/secondary, underprivileged, vocational, special education, education excellence
7) Environment: environment including drinking water, waste disposal, hazardous waste, air pollution/climate, species and forest protection, conservation
8) Energy: energy including nuclear, electricity, natural gas/oil, coal, alternative/renewable, conservation
9) Immigration: immigration, refugees, citizenship
10) Transportation: transportation including mass transit, highways, air travel, rail, maritime, infrastructure
12) Law & Crime: law and crime including enforcement, white collar crime, drugs, courts, prisons, juvenile crime, child abuse, family issues, police
13) Social Welfare: social welfare including low-income assistance, elderly assistance, disabled assistance, volunteer organisations, child care
14) Housing: housing including community/urban/rural development, low-income/veterans/elderly/homeless housing
15) Domestic Commerce: domestic commerce including banking, securities, consumer finance, insurance regulation, corporate management, small business, copyrights, disaster relief, tourism, consumer safety, sports
16) Defence: defence including alliances, intelligence, readiness, nuclear arms, military aid, personnel, procurement, installations, civil defence, contractors, foreign operations
17) Technology: technology including space, science transfer, telecommunications, broadcast, weather forecasting, computers
18) Foreign Trade: foreign trade including agreements, exports, private investments, competitiveness, tariffs/imports, exchange rates
19) International Affairs: international affairs including foreign aid, developing countries, international finance, Western Europe/EU, specific countries, human rights, organisations, terrorism, diplomats
20) Govt Operations: government operations including intergovernmental relations, bureaucracy, postal service, employees, appointments, currency, procurement, property, tax administration, scandals, branch relations, political campaigns
21) Public Lands: public lands including national parks, indigenous affairs, natural resources and forest management, water resources, territorial/dependency issues
23) Culture: culture including general cultural policy

Coding rule: Code each question by the substantive policy content it raises, not by its procedural framing, target population, policy instrument, or venue. Three traps to resist:

- Target-population trap: the group a policy affects isn't the topic (e.g., a question about disabled anglers' fishing licences is Civil Rights — disability policy — not Labor or Social Welfare).
- Policy-instrument trap: the mechanism a policy uses isn't the topic (e.g., a question about tax credits for childcare is Social Welfare — childcare policy — not Macroeconomics or Domestic Commerce).
- Venue trap: where a question is asked, or what forum it references, isn't the topic (e.g., a question about WHO recommendations on NHS reform is Health — healthcare policy — not International Affairs).

Examples:

Example 1:
Question: "Business leaders at the CBI conference in Birmingham this week expressed support for the Government's policy of preparing the economy for possible United Kingdom entry into the single European currency. They also expressed support for the Government's spending plans, and felt that they were sustainable and that cuts in public spending were not required. In view of the policies put forward by the Conservative party on both those issues, does my right hon. Friend agree that it will be many years before that party regains the confidence of UK business?"
Answer: {"label": 1}

Example 2:
Question: "Q6. [10883]  When my right hon. Friend meets President Bush, will he put high on the agenda the plight of hundreds and thousands of Afghans, caused by the failure of food to get through to villages in Afghanistan?"
Answer: {"label": 19}

Example 3:
Question: "I am sure that my right hon. Friend will have been impressed by the incredible courage of Adrian Sudbury, who is using the last weeks of his life to campaign for more bone marrow donors to come forward. I have been impressed by the response so far of the Secretaries of State for Children, Schools and Families and for Health, but what more can my right hon. Friend do to help my friend Adrian to achieve his legacy and help 7,000 people to live?"
Answer: {"label": 3}

Example 4:
Question: "While the Prime Minister is on the subject of disabled people, may I ask whether he is aware that Labour’s attack on vulnerable people has been extended to disabled anglers? They have seen the cost of their fishing licence
30 Apr 2008 : Column 304
go up by 37 per cent., as opposed to 2 per cent. for able-bodied people—if, that is, they can find a post office from which to buy one"
Answer: {"label": 2}

Example 5:
Question: "Has my right hon. Friend noticed that all opinion polls show that the overwhelming majority of country dwellers are opposed to hunting with hounds?"
Answer: {"label": 7}

Example 6:
Question: "It seems certain that coal miners’ beat knee is about to be made a prescribed industrial disease. In order that we can avoid another feeding frenzy for solicitors, will the Prime Minister get his Ministers to meet interested MPs to see whether a scheme can be established that gives value for money to the taxpayer, fair compensation to the coal miner and nothing to the solicitor?"
Answer: {"label": 8}

Return JSON: {"label": <integer>}. You must always choose one of the codes above. Never return null.

Question: {question}
```

---

#### `OAT_CC_FB_DA` — C=full + rule + fewshots | F=reasoning+label | D=no scope

**System** (135 chars):

```
You are a parliamentary researcher classifying UK Prime Minister's Questions using the Comparative Agendas Project (CAP) coding scheme.
```

**User** (6474 chars):

```
Below is a UK parliamentary question. Classify it into one of the CAP policy topics.

CAP policy topics:

1) Macroeconomics: general domestic macroeconomic policy, inflation, interest rates, monetary policy, national budget, tax code, industrial policy, price controls
2) Civil Rights: civil rights, minority/ethnic/racial discrimination, gender and sexuality, age/disability discrimination, voting rights, freedom of speech, right to privacy
3) Health: healthcare including reform, insurance, drug industry, medical facilities, disease prevention, mental health, long-term care, drug/tobacco abuse
4) Agriculture: agriculture including trade, subsidies to farmers, food safety, marketing, animal/crop disease, fisheries
5) Labor: labor including worker safety, employment training, benefits, unions, fair labor standards, youth employment, migrant workers
6) Education: education including higher/primary/secondary, underprivileged, vocational, special education, education excellence
7) Environment: environment including drinking water, waste disposal, hazardous waste, air pollution/climate, species and forest protection, conservation
8) Energy: energy including nuclear, electricity, natural gas/oil, coal, alternative/renewable, conservation
9) Immigration: immigration, refugees, citizenship
10) Transportation: transportation including mass transit, highways, air travel, rail, maritime, infrastructure
12) Law & Crime: law and crime including enforcement, white collar crime, drugs, courts, prisons, juvenile crime, child abuse, family issues, police
13) Social Welfare: social welfare including low-income assistance, elderly assistance, disabled assistance, volunteer organisations, child care
14) Housing: housing including community/urban/rural development, low-income/veterans/elderly/homeless housing
15) Domestic Commerce: domestic commerce including banking, securities, consumer finance, insurance regulation, corporate management, small business, copyrights, disaster relief, tourism, consumer safety, sports
16) Defence: defence including alliances, intelligence, readiness, nuclear arms, military aid, personnel, procurement, installations, civil defence, contractors, foreign operations
17) Technology: technology including space, science transfer, telecommunications, broadcast, weather forecasting, computers
18) Foreign Trade: foreign trade including agreements, exports, private investments, competitiveness, tariffs/imports, exchange rates
19) International Affairs: international affairs including foreign aid, developing countries, international finance, Western Europe/EU, specific countries, human rights, organisations, terrorism, diplomats
20) Govt Operations: government operations including intergovernmental relations, bureaucracy, postal service, employees, appointments, currency, procurement, property, tax administration, scandals, branch relations, political campaigns
21) Public Lands: public lands including national parks, indigenous affairs, natural resources and forest management, water resources, territorial/dependency issues
23) Culture: culture including general cultural policy

Coding rule: Code each question by the substantive policy content it raises, not by its procedural framing, target population, policy instrument, or venue. Three traps to resist:

- Target-population trap: the group a policy affects isn't the topic (e.g., a question about disabled anglers' fishing licences is Civil Rights — disability policy — not Labor or Social Welfare).
- Policy-instrument trap: the mechanism a policy uses isn't the topic (e.g., a question about tax credits for childcare is Social Welfare — childcare policy — not Macroeconomics or Domestic Commerce).
- Venue trap: where a question is asked, or what forum it references, isn't the topic (e.g., a question about WHO recommendations on NHS reform is Health — healthcare policy — not International Affairs).

Examples:

Example 1:
Question: "Business leaders at the CBI conference in Birmingham this week expressed support for the Government's policy of preparing the economy for possible United Kingdom entry into the single European currency. They also expressed support for the Government's spending plans, and felt that they were sustainable and that cuts in public spending were not required. In view of the policies put forward by the Conservative party on both those issues, does my right hon. Friend agree that it will be many years before that party regains the confidence of UK business?"
Answer: {"label": 1}

Example 2:
Question: "Q6. [10883]  When my right hon. Friend meets President Bush, will he put high on the agenda the plight of hundreds and thousands of Afghans, caused by the failure of food to get through to villages in Afghanistan?"
Answer: {"label": 19}

Example 3:
Question: "I am sure that my right hon. Friend will have been impressed by the incredible courage of Adrian Sudbury, who is using the last weeks of his life to campaign for more bone marrow donors to come forward. I have been impressed by the response so far of the Secretaries of State for Children, Schools and Families and for Health, but what more can my right hon. Friend do to help my friend Adrian to achieve his legacy and help 7,000 people to live?"
Answer: {"label": 3}

Example 4:
Question: "While the Prime Minister is on the subject of disabled people, may I ask whether he is aware that Labour’s attack on vulnerable people has been extended to disabled anglers? They have seen the cost of their fishing licence
30 Apr 2008 : Column 304
go up by 37 per cent., as opposed to 2 per cent. for able-bodied people—if, that is, they can find a post office from which to buy one"
Answer: {"label": 2}

Example 5:
Question: "Has my right hon. Friend noticed that all opinion polls show that the overwhelming majority of country dwellers are opposed to hunting with hounds?"
Answer: {"label": 7}

Example 6:
Question: "It seems certain that coal miners’ beat knee is about to be made a prescribed industrial disease. In order that we can avoid another feeding frenzy for solicitors, will the Prime Minister get his Ministers to meet interested MPs to see whether a scheme can be established that gives value for money to the taxpayer, fair compensation to the coal miner and nothing to the solicitor?"
Answer: {"label": 8}

Return JSON: {"reasoning": "<brief>", "label": <integer>}. You must always choose one of the codes above. Never return null.

Question: {question}
```

---

#### `OAT_CC_FB_DB` — C=full + rule + fewshots | F=reasoning+label | D=time scope

**System** (135 chars):

```
You are a parliamentary researcher classifying UK Prime Minister's Questions using the Comparative Agendas Project (CAP) coding scheme.
```

**User** (6489 chars):

```
Below is a UK parliamentary question from 1997-2008. Classify it into one of the CAP policy topics.

CAP policy topics:

1) Macroeconomics: general domestic macroeconomic policy, inflation, interest rates, monetary policy, national budget, tax code, industrial policy, price controls
2) Civil Rights: civil rights, minority/ethnic/racial discrimination, gender and sexuality, age/disability discrimination, voting rights, freedom of speech, right to privacy
3) Health: healthcare including reform, insurance, drug industry, medical facilities, disease prevention, mental health, long-term care, drug/tobacco abuse
4) Agriculture: agriculture including trade, subsidies to farmers, food safety, marketing, animal/crop disease, fisheries
5) Labor: labor including worker safety, employment training, benefits, unions, fair labor standards, youth employment, migrant workers
6) Education: education including higher/primary/secondary, underprivileged, vocational, special education, education excellence
7) Environment: environment including drinking water, waste disposal, hazardous waste, air pollution/climate, species and forest protection, conservation
8) Energy: energy including nuclear, electricity, natural gas/oil, coal, alternative/renewable, conservation
9) Immigration: immigration, refugees, citizenship
10) Transportation: transportation including mass transit, highways, air travel, rail, maritime, infrastructure
12) Law & Crime: law and crime including enforcement, white collar crime, drugs, courts, prisons, juvenile crime, child abuse, family issues, police
13) Social Welfare: social welfare including low-income assistance, elderly assistance, disabled assistance, volunteer organisations, child care
14) Housing: housing including community/urban/rural development, low-income/veterans/elderly/homeless housing
15) Domestic Commerce: domestic commerce including banking, securities, consumer finance, insurance regulation, corporate management, small business, copyrights, disaster relief, tourism, consumer safety, sports
16) Defence: defence including alliances, intelligence, readiness, nuclear arms, military aid, personnel, procurement, installations, civil defence, contractors, foreign operations
17) Technology: technology including space, science transfer, telecommunications, broadcast, weather forecasting, computers
18) Foreign Trade: foreign trade including agreements, exports, private investments, competitiveness, tariffs/imports, exchange rates
19) International Affairs: international affairs including foreign aid, developing countries, international finance, Western Europe/EU, specific countries, human rights, organisations, terrorism, diplomats
20) Govt Operations: government operations including intergovernmental relations, bureaucracy, postal service, employees, appointments, currency, procurement, property, tax administration, scandals, branch relations, political campaigns
21) Public Lands: public lands including national parks, indigenous affairs, natural resources and forest management, water resources, territorial/dependency issues
23) Culture: culture including general cultural policy

Coding rule: Code each question by the substantive policy content it raises, not by its procedural framing, target population, policy instrument, or venue. Three traps to resist:

- Target-population trap: the group a policy affects isn't the topic (e.g., a question about disabled anglers' fishing licences is Civil Rights — disability policy — not Labor or Social Welfare).
- Policy-instrument trap: the mechanism a policy uses isn't the topic (e.g., a question about tax credits for childcare is Social Welfare — childcare policy — not Macroeconomics or Domestic Commerce).
- Venue trap: where a question is asked, or what forum it references, isn't the topic (e.g., a question about WHO recommendations on NHS reform is Health — healthcare policy — not International Affairs).

Examples:

Example 1:
Question: "Business leaders at the CBI conference in Birmingham this week expressed support for the Government's policy of preparing the economy for possible United Kingdom entry into the single European currency. They also expressed support for the Government's spending plans, and felt that they were sustainable and that cuts in public spending were not required. In view of the policies put forward by the Conservative party on both those issues, does my right hon. Friend agree that it will be many years before that party regains the confidence of UK business?"
Answer: {"label": 1}

Example 2:
Question: "Q6. [10883]  When my right hon. Friend meets President Bush, will he put high on the agenda the plight of hundreds and thousands of Afghans, caused by the failure of food to get through to villages in Afghanistan?"
Answer: {"label": 19}

Example 3:
Question: "I am sure that my right hon. Friend will have been impressed by the incredible courage of Adrian Sudbury, who is using the last weeks of his life to campaign for more bone marrow donors to come forward. I have been impressed by the response so far of the Secretaries of State for Children, Schools and Families and for Health, but what more can my right hon. Friend do to help my friend Adrian to achieve his legacy and help 7,000 people to live?"
Answer: {"label": 3}

Example 4:
Question: "While the Prime Minister is on the subject of disabled people, may I ask whether he is aware that Labour’s attack on vulnerable people has been extended to disabled anglers? They have seen the cost of their fishing licence
30 Apr 2008 : Column 304
go up by 37 per cent., as opposed to 2 per cent. for able-bodied people—if, that is, they can find a post office from which to buy one"
Answer: {"label": 2}

Example 5:
Question: "Has my right hon. Friend noticed that all opinion polls show that the overwhelming majority of country dwellers are opposed to hunting with hounds?"
Answer: {"label": 7}

Example 6:
Question: "It seems certain that coal miners’ beat knee is about to be made a prescribed industrial disease. In order that we can avoid another feeding frenzy for solicitors, will the Prime Minister get his Ministers to meet interested MPs to see whether a scheme can be established that gives value for money to the taxpayer, fair compensation to the coal miner and nothing to the solicitor?"
Answer: {"label": 8}

Return JSON: {"reasoning": "<brief>", "label": <integer>}. You must always choose one of the codes above. Never return null.

Question: {question}
```

---

#### `OAT_CC_FB_DC` — C=full + rule + fewshots | F=reasoning+label | D=speaker scope

**System** (135 chars):

```
You are a parliamentary researcher classifying UK Prime Minister's Questions using the Comparative Agendas Project (CAP) coding scheme.
```

**User** (6504 chars):

```
Below is a UK parliamentary question asked by a {speaker_party} MP. Classify it into one of the CAP policy topics.

CAP policy topics:

1) Macroeconomics: general domestic macroeconomic policy, inflation, interest rates, monetary policy, national budget, tax code, industrial policy, price controls
2) Civil Rights: civil rights, minority/ethnic/racial discrimination, gender and sexuality, age/disability discrimination, voting rights, freedom of speech, right to privacy
3) Health: healthcare including reform, insurance, drug industry, medical facilities, disease prevention, mental health, long-term care, drug/tobacco abuse
4) Agriculture: agriculture including trade, subsidies to farmers, food safety, marketing, animal/crop disease, fisheries
5) Labor: labor including worker safety, employment training, benefits, unions, fair labor standards, youth employment, migrant workers
6) Education: education including higher/primary/secondary, underprivileged, vocational, special education, education excellence
7) Environment: environment including drinking water, waste disposal, hazardous waste, air pollution/climate, species and forest protection, conservation
8) Energy: energy including nuclear, electricity, natural gas/oil, coal, alternative/renewable, conservation
9) Immigration: immigration, refugees, citizenship
10) Transportation: transportation including mass transit, highways, air travel, rail, maritime, infrastructure
12) Law & Crime: law and crime including enforcement, white collar crime, drugs, courts, prisons, juvenile crime, child abuse, family issues, police
13) Social Welfare: social welfare including low-income assistance, elderly assistance, disabled assistance, volunteer organisations, child care
14) Housing: housing including community/urban/rural development, low-income/veterans/elderly/homeless housing
15) Domestic Commerce: domestic commerce including banking, securities, consumer finance, insurance regulation, corporate management, small business, copyrights, disaster relief, tourism, consumer safety, sports
16) Defence: defence including alliances, intelligence, readiness, nuclear arms, military aid, personnel, procurement, installations, civil defence, contractors, foreign operations
17) Technology: technology including space, science transfer, telecommunications, broadcast, weather forecasting, computers
18) Foreign Trade: foreign trade including agreements, exports, private investments, competitiveness, tariffs/imports, exchange rates
19) International Affairs: international affairs including foreign aid, developing countries, international finance, Western Europe/EU, specific countries, human rights, organisations, terrorism, diplomats
20) Govt Operations: government operations including intergovernmental relations, bureaucracy, postal service, employees, appointments, currency, procurement, property, tax administration, scandals, branch relations, political campaigns
21) Public Lands: public lands including national parks, indigenous affairs, natural resources and forest management, water resources, territorial/dependency issues
23) Culture: culture including general cultural policy

Coding rule: Code each question by the substantive policy content it raises, not by its procedural framing, target population, policy instrument, or venue. Three traps to resist:

- Target-population trap: the group a policy affects isn't the topic (e.g., a question about disabled anglers' fishing licences is Civil Rights — disability policy — not Labor or Social Welfare).
- Policy-instrument trap: the mechanism a policy uses isn't the topic (e.g., a question about tax credits for childcare is Social Welfare — childcare policy — not Macroeconomics or Domestic Commerce).
- Venue trap: where a question is asked, or what forum it references, isn't the topic (e.g., a question about WHO recommendations on NHS reform is Health — healthcare policy — not International Affairs).

Examples:

Example 1:
Question: "Business leaders at the CBI conference in Birmingham this week expressed support for the Government's policy of preparing the economy for possible United Kingdom entry into the single European currency. They also expressed support for the Government's spending plans, and felt that they were sustainable and that cuts in public spending were not required. In view of the policies put forward by the Conservative party on both those issues, does my right hon. Friend agree that it will be many years before that party regains the confidence of UK business?"
Answer: {"label": 1}

Example 2:
Question: "Q6. [10883]  When my right hon. Friend meets President Bush, will he put high on the agenda the plight of hundreds and thousands of Afghans, caused by the failure of food to get through to villages in Afghanistan?"
Answer: {"label": 19}

Example 3:
Question: "I am sure that my right hon. Friend will have been impressed by the incredible courage of Adrian Sudbury, who is using the last weeks of his life to campaign for more bone marrow donors to come forward. I have been impressed by the response so far of the Secretaries of State for Children, Schools and Families and for Health, but what more can my right hon. Friend do to help my friend Adrian to achieve his legacy and help 7,000 people to live?"
Answer: {"label": 3}

Example 4:
Question: "While the Prime Minister is on the subject of disabled people, may I ask whether he is aware that Labour’s attack on vulnerable people has been extended to disabled anglers? They have seen the cost of their fishing licence
30 Apr 2008 : Column 304
go up by 37 per cent., as opposed to 2 per cent. for able-bodied people—if, that is, they can find a post office from which to buy one"
Answer: {"label": 2}

Example 5:
Question: "Has my right hon. Friend noticed that all opinion polls show that the overwhelming majority of country dwellers are opposed to hunting with hounds?"
Answer: {"label": 7}

Example 6:
Question: "It seems certain that coal miners’ beat knee is about to be made a prescribed industrial disease. In order that we can avoid another feeding frenzy for solicitors, will the Prime Minister get his Ministers to meet interested MPs to see whether a scheme can be established that gives value for money to the taxpayer, fair compensation to the coal miner and nothing to the solicitor?"
Answer: {"label": 8}

Return JSON: {"reasoning": "<brief>", "label": <integer>}. You must always choose one of the codes above. Never return null.

Question: {question}
```

---

#### `OAT_CC_FC_DA` — C=full + rule + fewshots | F=reasoning+label + CoT | D=no scope

**System** (251 chars):

```
You are a parliamentary researcher classifying UK Prime Minister's Questions using the Comparative Agendas Project (CAP) coding scheme.

Think step by step: first identify the substantive policy issue at stake, then select the best-matching CAP topic.
```

**User** (6474 chars):

```
Below is a UK parliamentary question. Classify it into one of the CAP policy topics.

CAP policy topics:

1) Macroeconomics: general domestic macroeconomic policy, inflation, interest rates, monetary policy, national budget, tax code, industrial policy, price controls
2) Civil Rights: civil rights, minority/ethnic/racial discrimination, gender and sexuality, age/disability discrimination, voting rights, freedom of speech, right to privacy
3) Health: healthcare including reform, insurance, drug industry, medical facilities, disease prevention, mental health, long-term care, drug/tobacco abuse
4) Agriculture: agriculture including trade, subsidies to farmers, food safety, marketing, animal/crop disease, fisheries
5) Labor: labor including worker safety, employment training, benefits, unions, fair labor standards, youth employment, migrant workers
6) Education: education including higher/primary/secondary, underprivileged, vocational, special education, education excellence
7) Environment: environment including drinking water, waste disposal, hazardous waste, air pollution/climate, species and forest protection, conservation
8) Energy: energy including nuclear, electricity, natural gas/oil, coal, alternative/renewable, conservation
9) Immigration: immigration, refugees, citizenship
10) Transportation: transportation including mass transit, highways, air travel, rail, maritime, infrastructure
12) Law & Crime: law and crime including enforcement, white collar crime, drugs, courts, prisons, juvenile crime, child abuse, family issues, police
13) Social Welfare: social welfare including low-income assistance, elderly assistance, disabled assistance, volunteer organisations, child care
14) Housing: housing including community/urban/rural development, low-income/veterans/elderly/homeless housing
15) Domestic Commerce: domestic commerce including banking, securities, consumer finance, insurance regulation, corporate management, small business, copyrights, disaster relief, tourism, consumer safety, sports
16) Defence: defence including alliances, intelligence, readiness, nuclear arms, military aid, personnel, procurement, installations, civil defence, contractors, foreign operations
17) Technology: technology including space, science transfer, telecommunications, broadcast, weather forecasting, computers
18) Foreign Trade: foreign trade including agreements, exports, private investments, competitiveness, tariffs/imports, exchange rates
19) International Affairs: international affairs including foreign aid, developing countries, international finance, Western Europe/EU, specific countries, human rights, organisations, terrorism, diplomats
20) Govt Operations: government operations including intergovernmental relations, bureaucracy, postal service, employees, appointments, currency, procurement, property, tax administration, scandals, branch relations, political campaigns
21) Public Lands: public lands including national parks, indigenous affairs, natural resources and forest management, water resources, territorial/dependency issues
23) Culture: culture including general cultural policy

Coding rule: Code each question by the substantive policy content it raises, not by its procedural framing, target population, policy instrument, or venue. Three traps to resist:

- Target-population trap: the group a policy affects isn't the topic (e.g., a question about disabled anglers' fishing licences is Civil Rights — disability policy — not Labor or Social Welfare).
- Policy-instrument trap: the mechanism a policy uses isn't the topic (e.g., a question about tax credits for childcare is Social Welfare — childcare policy — not Macroeconomics or Domestic Commerce).
- Venue trap: where a question is asked, or what forum it references, isn't the topic (e.g., a question about WHO recommendations on NHS reform is Health — healthcare policy — not International Affairs).

Examples:

Example 1:
Question: "Business leaders at the CBI conference in Birmingham this week expressed support for the Government's policy of preparing the economy for possible United Kingdom entry into the single European currency. They also expressed support for the Government's spending plans, and felt that they were sustainable and that cuts in public spending were not required. In view of the policies put forward by the Conservative party on both those issues, does my right hon. Friend agree that it will be many years before that party regains the confidence of UK business?"
Answer: {"label": 1}

Example 2:
Question: "Q6. [10883]  When my right hon. Friend meets President Bush, will he put high on the agenda the plight of hundreds and thousands of Afghans, caused by the failure of food to get through to villages in Afghanistan?"
Answer: {"label": 19}

Example 3:
Question: "I am sure that my right hon. Friend will have been impressed by the incredible courage of Adrian Sudbury, who is using the last weeks of his life to campaign for more bone marrow donors to come forward. I have been impressed by the response so far of the Secretaries of State for Children, Schools and Families and for Health, but what more can my right hon. Friend do to help my friend Adrian to achieve his legacy and help 7,000 people to live?"
Answer: {"label": 3}

Example 4:
Question: "While the Prime Minister is on the subject of disabled people, may I ask whether he is aware that Labour’s attack on vulnerable people has been extended to disabled anglers? They have seen the cost of their fishing licence
30 Apr 2008 : Column 304
go up by 37 per cent., as opposed to 2 per cent. for able-bodied people—if, that is, they can find a post office from which to buy one"
Answer: {"label": 2}

Example 5:
Question: "Has my right hon. Friend noticed that all opinion polls show that the overwhelming majority of country dwellers are opposed to hunting with hounds?"
Answer: {"label": 7}

Example 6:
Question: "It seems certain that coal miners’ beat knee is about to be made a prescribed industrial disease. In order that we can avoid another feeding frenzy for solicitors, will the Prime Minister get his Ministers to meet interested MPs to see whether a scheme can be established that gives value for money to the taxpayer, fair compensation to the coal miner and nothing to the solicitor?"
Answer: {"label": 8}

Return JSON: {"reasoning": "<brief>", "label": <integer>}. You must always choose one of the codes above. Never return null.

Question: {question}
```

---

#### `OAT_CC_FC_DB` — C=full + rule + fewshots | F=reasoning+label + CoT | D=time scope

**System** (251 chars):

```
You are a parliamentary researcher classifying UK Prime Minister's Questions using the Comparative Agendas Project (CAP) coding scheme.

Think step by step: first identify the substantive policy issue at stake, then select the best-matching CAP topic.
```

**User** (6489 chars):

```
Below is a UK parliamentary question from 1997-2008. Classify it into one of the CAP policy topics.

CAP policy topics:

1) Macroeconomics: general domestic macroeconomic policy, inflation, interest rates, monetary policy, national budget, tax code, industrial policy, price controls
2) Civil Rights: civil rights, minority/ethnic/racial discrimination, gender and sexuality, age/disability discrimination, voting rights, freedom of speech, right to privacy
3) Health: healthcare including reform, insurance, drug industry, medical facilities, disease prevention, mental health, long-term care, drug/tobacco abuse
4) Agriculture: agriculture including trade, subsidies to farmers, food safety, marketing, animal/crop disease, fisheries
5) Labor: labor including worker safety, employment training, benefits, unions, fair labor standards, youth employment, migrant workers
6) Education: education including higher/primary/secondary, underprivileged, vocational, special education, education excellence
7) Environment: environment including drinking water, waste disposal, hazardous waste, air pollution/climate, species and forest protection, conservation
8) Energy: energy including nuclear, electricity, natural gas/oil, coal, alternative/renewable, conservation
9) Immigration: immigration, refugees, citizenship
10) Transportation: transportation including mass transit, highways, air travel, rail, maritime, infrastructure
12) Law & Crime: law and crime including enforcement, white collar crime, drugs, courts, prisons, juvenile crime, child abuse, family issues, police
13) Social Welfare: social welfare including low-income assistance, elderly assistance, disabled assistance, volunteer organisations, child care
14) Housing: housing including community/urban/rural development, low-income/veterans/elderly/homeless housing
15) Domestic Commerce: domestic commerce including banking, securities, consumer finance, insurance regulation, corporate management, small business, copyrights, disaster relief, tourism, consumer safety, sports
16) Defence: defence including alliances, intelligence, readiness, nuclear arms, military aid, personnel, procurement, installations, civil defence, contractors, foreign operations
17) Technology: technology including space, science transfer, telecommunications, broadcast, weather forecasting, computers
18) Foreign Trade: foreign trade including agreements, exports, private investments, competitiveness, tariffs/imports, exchange rates
19) International Affairs: international affairs including foreign aid, developing countries, international finance, Western Europe/EU, specific countries, human rights, organisations, terrorism, diplomats
20) Govt Operations: government operations including intergovernmental relations, bureaucracy, postal service, employees, appointments, currency, procurement, property, tax administration, scandals, branch relations, political campaigns
21) Public Lands: public lands including national parks, indigenous affairs, natural resources and forest management, water resources, territorial/dependency issues
23) Culture: culture including general cultural policy

Coding rule: Code each question by the substantive policy content it raises, not by its procedural framing, target population, policy instrument, or venue. Three traps to resist:

- Target-population trap: the group a policy affects isn't the topic (e.g., a question about disabled anglers' fishing licences is Civil Rights — disability policy — not Labor or Social Welfare).
- Policy-instrument trap: the mechanism a policy uses isn't the topic (e.g., a question about tax credits for childcare is Social Welfare — childcare policy — not Macroeconomics or Domestic Commerce).
- Venue trap: where a question is asked, or what forum it references, isn't the topic (e.g., a question about WHO recommendations on NHS reform is Health — healthcare policy — not International Affairs).

Examples:

Example 1:
Question: "Business leaders at the CBI conference in Birmingham this week expressed support for the Government's policy of preparing the economy for possible United Kingdom entry into the single European currency. They also expressed support for the Government's spending plans, and felt that they were sustainable and that cuts in public spending were not required. In view of the policies put forward by the Conservative party on both those issues, does my right hon. Friend agree that it will be many years before that party regains the confidence of UK business?"
Answer: {"label": 1}

Example 2:
Question: "Q6. [10883]  When my right hon. Friend meets President Bush, will he put high on the agenda the plight of hundreds and thousands of Afghans, caused by the failure of food to get through to villages in Afghanistan?"
Answer: {"label": 19}

Example 3:
Question: "I am sure that my right hon. Friend will have been impressed by the incredible courage of Adrian Sudbury, who is using the last weeks of his life to campaign for more bone marrow donors to come forward. I have been impressed by the response so far of the Secretaries of State for Children, Schools and Families and for Health, but what more can my right hon. Friend do to help my friend Adrian to achieve his legacy and help 7,000 people to live?"
Answer: {"label": 3}

Example 4:
Question: "While the Prime Minister is on the subject of disabled people, may I ask whether he is aware that Labour’s attack on vulnerable people has been extended to disabled anglers? They have seen the cost of their fishing licence
30 Apr 2008 : Column 304
go up by 37 per cent., as opposed to 2 per cent. for able-bodied people—if, that is, they can find a post office from which to buy one"
Answer: {"label": 2}

Example 5:
Question: "Has my right hon. Friend noticed that all opinion polls show that the overwhelming majority of country dwellers are opposed to hunting with hounds?"
Answer: {"label": 7}

Example 6:
Question: "It seems certain that coal miners’ beat knee is about to be made a prescribed industrial disease. In order that we can avoid another feeding frenzy for solicitors, will the Prime Minister get his Ministers to meet interested MPs to see whether a scheme can be established that gives value for money to the taxpayer, fair compensation to the coal miner and nothing to the solicitor?"
Answer: {"label": 8}

Return JSON: {"reasoning": "<brief>", "label": <integer>}. You must always choose one of the codes above. Never return null.

Question: {question}
```

---

#### `OAT_CC_FC_DC` — C=full + rule + fewshots | F=reasoning+label + CoT | D=speaker scope

**System** (251 chars):

```
You are a parliamentary researcher classifying UK Prime Minister's Questions using the Comparative Agendas Project (CAP) coding scheme.

Think step by step: first identify the substantive policy issue at stake, then select the best-matching CAP topic.
```

**User** (6504 chars):

```
Below is a UK parliamentary question asked by a {speaker_party} MP. Classify it into one of the CAP policy topics.

CAP policy topics:

1) Macroeconomics: general domestic macroeconomic policy, inflation, interest rates, monetary policy, national budget, tax code, industrial policy, price controls
2) Civil Rights: civil rights, minority/ethnic/racial discrimination, gender and sexuality, age/disability discrimination, voting rights, freedom of speech, right to privacy
3) Health: healthcare including reform, insurance, drug industry, medical facilities, disease prevention, mental health, long-term care, drug/tobacco abuse
4) Agriculture: agriculture including trade, subsidies to farmers, food safety, marketing, animal/crop disease, fisheries
5) Labor: labor including worker safety, employment training, benefits, unions, fair labor standards, youth employment, migrant workers
6) Education: education including higher/primary/secondary, underprivileged, vocational, special education, education excellence
7) Environment: environment including drinking water, waste disposal, hazardous waste, air pollution/climate, species and forest protection, conservation
8) Energy: energy including nuclear, electricity, natural gas/oil, coal, alternative/renewable, conservation
9) Immigration: immigration, refugees, citizenship
10) Transportation: transportation including mass transit, highways, air travel, rail, maritime, infrastructure
12) Law & Crime: law and crime including enforcement, white collar crime, drugs, courts, prisons, juvenile crime, child abuse, family issues, police
13) Social Welfare: social welfare including low-income assistance, elderly assistance, disabled assistance, volunteer organisations, child care
14) Housing: housing including community/urban/rural development, low-income/veterans/elderly/homeless housing
15) Domestic Commerce: domestic commerce including banking, securities, consumer finance, insurance regulation, corporate management, small business, copyrights, disaster relief, tourism, consumer safety, sports
16) Defence: defence including alliances, intelligence, readiness, nuclear arms, military aid, personnel, procurement, installations, civil defence, contractors, foreign operations
17) Technology: technology including space, science transfer, telecommunications, broadcast, weather forecasting, computers
18) Foreign Trade: foreign trade including agreements, exports, private investments, competitiveness, tariffs/imports, exchange rates
19) International Affairs: international affairs including foreign aid, developing countries, international finance, Western Europe/EU, specific countries, human rights, organisations, terrorism, diplomats
20) Govt Operations: government operations including intergovernmental relations, bureaucracy, postal service, employees, appointments, currency, procurement, property, tax administration, scandals, branch relations, political campaigns
21) Public Lands: public lands including national parks, indigenous affairs, natural resources and forest management, water resources, territorial/dependency issues
23) Culture: culture including general cultural policy

Coding rule: Code each question by the substantive policy content it raises, not by its procedural framing, target population, policy instrument, or venue. Three traps to resist:

- Target-population trap: the group a policy affects isn't the topic (e.g., a question about disabled anglers' fishing licences is Civil Rights — disability policy — not Labor or Social Welfare).
- Policy-instrument trap: the mechanism a policy uses isn't the topic (e.g., a question about tax credits for childcare is Social Welfare — childcare policy — not Macroeconomics or Domestic Commerce).
- Venue trap: where a question is asked, or what forum it references, isn't the topic (e.g., a question about WHO recommendations on NHS reform is Health — healthcare policy — not International Affairs).

Examples:

Example 1:
Question: "Business leaders at the CBI conference in Birmingham this week expressed support for the Government's policy of preparing the economy for possible United Kingdom entry into the single European currency. They also expressed support for the Government's spending plans, and felt that they were sustainable and that cuts in public spending were not required. In view of the policies put forward by the Conservative party on both those issues, does my right hon. Friend agree that it will be many years before that party regains the confidence of UK business?"
Answer: {"label": 1}

Example 2:
Question: "Q6. [10883]  When my right hon. Friend meets President Bush, will he put high on the agenda the plight of hundreds and thousands of Afghans, caused by the failure of food to get through to villages in Afghanistan?"
Answer: {"label": 19}

Example 3:
Question: "I am sure that my right hon. Friend will have been impressed by the incredible courage of Adrian Sudbury, who is using the last weeks of his life to campaign for more bone marrow donors to come forward. I have been impressed by the response so far of the Secretaries of State for Children, Schools and Families and for Health, but what more can my right hon. Friend do to help my friend Adrian to achieve his legacy and help 7,000 people to live?"
Answer: {"label": 3}

Example 4:
Question: "While the Prime Minister is on the subject of disabled people, may I ask whether he is aware that Labour’s attack on vulnerable people has been extended to disabled anglers? They have seen the cost of their fishing licence
30 Apr 2008 : Column 304
go up by 37 per cent., as opposed to 2 per cent. for able-bodied people—if, that is, they can find a post office from which to buy one"
Answer: {"label": 2}

Example 5:
Question: "Has my right hon. Friend noticed that all opinion polls show that the overwhelming majority of country dwellers are opposed to hunting with hounds?"
Answer: {"label": 7}

Example 6:
Question: "It seems certain that coal miners’ beat knee is about to be made a prescribed industrial disease. In order that we can avoid another feeding frenzy for solicitors, will the Prime Minister get his Ministers to meet interested MPs to see whether a scheme can be established that gives value for money to the taxpayer, fair compensation to the coal miner and nothing to the solicitor?"
Answer: {"label": 8}

Return JSON: {"reasoning": "<brief>", "label": <integer>}. You must always choose one of the codes above. Never return null.

Question: {question}
```

---

