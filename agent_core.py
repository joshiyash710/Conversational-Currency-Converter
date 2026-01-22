from dotenv import load_dotenv
load_dotenv()

from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_core.tools import tool
from langgraph.prebuilt import create_react_agent
import requests

# ---------------- LLM ----------------
llm = HuggingFaceEndpoint(
    repo_id="mistralai/Mistral-7B-Instruct-v0.2",
    task="text-generation",
    max_new_tokens=256,
    temperature=0.3,
)

chat_model = ChatHuggingFace(llm=llm)

# ---------------- TOOL ----------------
CURRENCY_ALIASES = {
    "rupee": "INR",
    "rupees": "INR",
    "rs": "INR",
    "inr": "INR",
    "dollar": "USD",
    "dollars": "USD",
    "usd": "USD",
    "euro": "EUR",
    "euros": "EUR",
    "pound": "GBP",
    "pounds": "GBP",
    "yen": "JPY",
    "jpy": "JPY",
}

def fetch_live_rate(from_currency: str, to_currency: str) -> float:
    """Fetches the latest conversion rate from exchangerate.host"""
    url = f"https://api.exchangerate.host/latest?base={from_currency}&symbols={to_currency}"
    resp = requests.get(url)
    if resp.status_code != 200:
        raise ValueError("Failed to fetch live rates.")
    data = resp.json()
    rate = data["rates"][to_currency]
    return rate

@tool
def convert_currency(amount: float, from_currency: str, to_currency: str) -> str:
    """Convert currency using live exchange rates."""
    from_code = CURRENCY_ALIASES.get(from_currency.lower(), from_currency.upper())
    to_code = CURRENCY_ALIASES.get(to_currency.lower(), to_currency.upper())

    try:
        rate = fetch_live_rate(from_code, to_code)
        converted = amount * rate
        return f"{amount} {from_code} is approximately {round(converted, 2)} {to_code}."
    except Exception as e:
        return f"Sorry, I could not fetch live rates: {e}"

# ---------------- AGENT ----------------
agent = create_react_agent(
    model=chat_model,
    tools=[convert_currency],
    prompt="""
You are a friendly currency conversion assistant.

Conversation rules:
- If the user provides amount and source currency but NOT target currency, ask which currency to convert to.
- If all information is available, use the convert_currency tool.
- The user may speak naturally (rupees, dollars, euros, etc).
- Do not mention tools or internal logic.
"""
)

# ---------------- CONVERSATION FUNCTION ----------------
def get_agent_response(messages):
    """
    Pass in the current list of messages:
    messages = [("user", "Hi"), ("assistant", "Hello!")]
    Returns updated messages after agent reply
    """
    response = agent.invoke({"messages": messages})
    return response["messages"]
