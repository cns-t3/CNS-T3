prompt = """Given a news article, complete the following actions

1. Summarize the news content in less than 100 words

2. Provide a category(ies) for the article (Source of Wealth, Family Circumstances, Sanctioned Countries, Sensitive industries). If none of the categories provided fits the article’s content, return Others as the category. It should only be one of these 5 categories: Source of Wealth, Family Circumstances, Sanctioned Countries, Sensitive industries, Others.
- To determine the category, these are the search patterns for each category:
- Source of wealth – search patterns : net worth, worth, income, inherit, inheritance, receive, gifted, settlement, sale proceeds, merger & acquisition, M&A, leveraged buyout
- Family circumstances – search patterns:  Marry, marriage, divorce, separation, children, child
- Sanctioned countries – search patterns (limited set): Cuba, Iran, North Korea, Syria, Crimea, Russia, Ukraine, Afghanistan, Albania, Algeria, Angola, Bahamas, Bangladesh, Barbados, Belarus, Belize, Bolivia, Botswana, Burkina Faso, Burundi, Cambodia, Cameroon, Central African Republic, Chad, Cayman Islands, Comoros, Congo, Democratic Republic of Côte d'Ivoire, Djibouti, Dominican Republic, Ecuador, Egypt
- Sensitive industries – search patterns: Casinos, Arms Dealer, Arms Material, Private Military Service Provider, Diamond, Precious stones, Money Remittance Business 

It should only be one of these 5 categories: Source of Wealth, Family Circumstances, Sanctioned Countries, Sensitive industries, Others.

3. Determine whether the article focuses on an individual engaging in the action rather than their associated company, and provide a true or false response. For example, ascertain if the article is about Tim Cook investing personally, not Apple as a company.

4. Give me a risk rating (low, medium or high) based on the following cases:
High Risk Rating Cases:
- Legal Issues: Scandals or legal troubles involving the client, News about the client being involved in fraud or money laundering investigations.
- Financial Distress: Reports of the client facing bankruptcy or financial instability, Significant debt or default issues.
- Sanctions and Embargoes: News indicating that the client or their associated entities are subject to sanctions or embargoes, News indicating that the client is investing in a sanctioned country (given above).
- Politically Exposed Persons (PEP): Identification of the client as a PEP, News about the client's involvement with politically sensitive activities.
Industry-specific Risks: Regulatory violations or controversies within the client's industry, Any news indicating non-compliance with industry standards.

Medium-Risk Cases:
- Change in Business Activities: Reports of significant changes in the client's business model or activities.
- Mergers and Acquisitions: News about the client being involved in mergers, acquisitions, or significant corporate restructuring.
- Market Performance: Fluctuations in the client's stock prices or financial performance.
- Management Changes: Significant changes in the client's leadership or management team.
- Partnerships and Alliances: News about the client forming partnerships or alliances that may pose moderate risks.

If the news does not belong to any of the above cases, return Low for its risk rating.

5. Identify the subject in the article, be it an entity or person. Generate a profile summary of the subject based on the information from the article in less than 100 words.

Return the data in JSON format: {"summary": "", "category": "", "is_related": true/false, "risk_rating":"", "subject_summary": ""}"""
