import os
import openai
from dotenv import load_dotenv
from langchain import OpenAI, LLMChain, PromptTemplate
from langchain.memory import ConversationBufferWindowMemory

load_dotenv()

if os.getenv("OPENAI_API_KEY"):
    openAI_client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
    
def initialize_chain(instructions, memory=None):
    if memory is None:
        memory = ConversationBufferWindowMemory()
        memory.ai_prefix = "Assistant"

    template = f"""
    Instructions: {instructions}
    {{{memory.memory_key}}}
    Human: {{human_input}}
    Assistant:"""

    prompt = PromptTemplate(
        input_variables=["history", "human_input"], template=template
    )

    chain = LLMChain(
        llm=OpenAI(temperature=0),
        prompt=prompt,
        verbose=True,
        memory=ConversationBufferWindowMemory(),
    )
    return chain


def initialize_meta_chain():
    meta_template = meta_template = """
    Assistant has just had the below interactions with a User. Assistant followed their "Instructions" closely. Your job is to critique the Assistant's performance and then revise the Instructions so that Assistant would quickly and correctly respond in the future.

    ####

    {chat_history}

    ####

    Please reflect on these interactions.

    You should first critique Assistant's performance. What could Assistant have done better? What should the Assistant remember about this user? Are there things this user always wants? Indicate this with "Critique: ...".

    You should next revise the Instructions so that Assistant would quickly and correctly respond in the future. Assistant's goal is to satisfy the user in as few interactions as possible. Assistant will only see the new Instructions, not the interaction history, so anything important must be summarized in the Instructions. Don't forget any important details in the current Instructions! Indicate the new Instructions by "Instructions: ...".
    """

    meta_prompt = PromptTemplate(
        input_variables=["chat_history"], template=meta_template
    )

    meta_chain = LLMChain(
        llm=OpenAI(temperature=0), # strict
        prompt=meta_prompt,
        verbose=True,
    )
    return meta_chain


def get_chat_history(chain_memory):
    memory_key = chain_memory.memory_key
    chat_history = chain_memory.load_memory_variables(memory_key)[memory_key]
    return chat_history


def get_new_instructions(meta_output):
    delimiter = "Instructions: "
    new_instructions = meta_output[meta_output.find(delimiter) + len(delimiter) :]
    return new_instructions

def main(task, max_iters=3, max_meta_iters=5):
    failed_phrase = "task failed"
    success_phrase = "task succeeded"
    key_phrases = [success_phrase, failed_phrase]

    instructions = "None"
    for i in range(max_meta_iters):
        print(f"[Episode {i+1}/{max_meta_iters}]")
        chain = initialize_chain(instructions, memory=None)
        output = chain.predict(human_input=task)
        for j in range(max_iters):
            print(f"(Step {j+1}/{max_iters})")
            print(f"Assistant: {output}")
            print(f"Human: ")
            human_input = input()
            if any(phrase in human_input.lower() for phrase in key_phrases):
                break
            output = chain.predict(human_input=human_input)
        if success_phrase in human_input.lower():
            print(f"Succeeded!")
            return
        meta_chain = initialize_meta_chain()
        meta_output = meta_chain.predict(chat_history=get_chat_history(chain.memory))
        print(f"Feedback: {meta_output}")
        instructions = get_new_instructions(meta_output)
        print(f"New Instructions: {instructions}")
        print("\n" + "#" * 80 + "\n")
    print(f"Failed!")

def get_categories(data):
    formatted_categories = [category.title() for category in data["categories"]]

    final_string = ", ".join(formatted_categories)
    return final_string

def get_search_patterns(data):
    formatted_string = ", ".join(
        [
            f"{category} - search pattern: {', '.join(patterns)}"
            for category, patterns in data["categories"].items()
            if patterns
        ]
    )
    return formatted_string
prompt = """Given a news article, complete the following actions

1. Summarize the news content in less than 100 words

2. Provide a category(ies) for the article ({{ categories }}). If none of the categories provided fits the article’s content, return Others as the category. It should only be one of these categories: {{ categories }}, Others.
- To determine the category, these are the search patterns for each category:
{{ search_patterns }}

3. Determine whether the article focuses on an individual engaging in the action rather than their associated company, and provide a true or false response. For example, ascertain if the article is about Tim Cook investing personally, not Apple as a company.

4. Give me a risk rating (low, medium or high) based on the following cases and include one sentence of 15 words or less reasoning for the justification of the selected risk:
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

Return the data in JSON format: {"summary": "", "category": "", "risk_rating": "", "subject_summary": "", "risk_justification": ""}"""

categories_json = {
  "categories": {
    "Source of Wealth": [
      "net worth",
      "worth",
      "income",
      "inherit",
      "inheritance",
      "receive",
      "gifted",
      "settlement",
      "sale proceeds",
      "merger & acquisition",
      "M&A",
      "leveraged buyout"
    ],
    "Family Circumstances": [
      "Marry",
      "marriage",
      "divorce",
      "separation",
      "children",
      "child"
    ],
    "Sanctioned Countries": [
      "Cuba",
      "Iran",
      "North Korea",
      "Syria",
      "Crimea",
      "Russia",
      "Ukraine",
      "Afghanistan",
      "Albania",
      "Algeria",
      "Angola",
      "Bahamas",
      "Bangladesh",
      "Barbados",
      "Belarus",
      "Belize",
      "Bolivia",
      "Botswana",
      "Burkina Faso",
      "Burundi",
      "Cambodia",
      "Cameroon",
      "Central African Republic",
      "Chad",
      "Cayman Islands",
      "Comoros",
      "Congo",
      "Democratic Republic of Côte d'Ivoire",
      "Djibouti",
      "Dominican Republic",
      "Ecuador",
      "Egypt"
    ],
    "Sensitive Industries": [
      "Casinos",
      "Arms Dealer",
      "Arms Material",
      "Private Military Service Provider",
      "Diamond",
      "Precious stones",
      "Money Remittance Business"
    ],
    "Others": []
  }
}

categories = get_categories(categories_json)
search_patterns = get_search_patterns(categories_json)
prompt = prompt.replace("{{ categories }}", categories)
prompt = prompt.replace("{{ search_patterns }}", search_patterns)

task = "Improve this prompt {{ <prompt> }} for more clear and more accurate outputs."
task = task.replace("<prompt>", prompt)

main(task)