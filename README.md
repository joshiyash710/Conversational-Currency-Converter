💱 Conversational Currency Converter

A friendly AI assistant for currency conversion, built with LangChain, Hugging Face, and Streamlit.

Talk naturally, ask for conversions between currencies, and get instant results using live exchange rates. Perfect for demonstrating real-world AI agent capabilities with tool integration.

🚀 Features

Multi-turn conversational interface

Converts between multiple currencies using live exchange rates

Built using Hugging Face Inference API for the LLM

Conversational agent implemented with LangChain / LangGraph

User-friendly Streamlit UI

Follow-up questions handled automatically if the target currency is missing

Clean separation of agent logic (agent_core.py) and UI (app.py)

🛠 Tech Stack
Component	Technology / Library
LLM	Hugging Face (Mistral-7B-Instruct-v0.2)
Agent	LangChain / LangGraph (create_react_agent)
Tools / Conversion	Python requests + live exchange rates API
Frontend / UI	Streamlit
Environment	Python 3.10+, virtualenv (venv)
📦 Installation

Clone the repository:

git clone https://github.com/joshiyash710/Conversational-Currency-Converter.git
cd Conversational-Currency-Converter


Create and activate a virtual environment:

python -m venv venv
# Windows
venv\Scripts\activate
# macOS / Linux
source venv/bin/activate


Install all dependencies in one command:

pip install -r requirements.txt


Add your Hugging Face API token to a .env file in the root directory:

HUGGINGFACEHUB_API_TOKEN=your_token_here


Run the Streamlit app:

streamlit run app.py


That’s it! The app should launch in your browser and you can start chatting with the currency conversion agent immediately.

⚡ Usage

Type your messages naturally in the chat input

The agent will ask follow-ups if necessary

Example interactions:

User: Convert 500 rupees to USD
Assistant: 500 INR is approximately 6.02 USD.

User: I want to convert 100 dollars
Assistant: Sure, which currency should I convert it to?
User: Euros
Assistant: 100 USD is approximately 92 EUR.

🧩 Project Structure
LangChain_AI-Agents/
├─ agent_core.py       # LLM, agent, and tool logic
├─ app.py              # Streamlit frontend
├─ requirements.txt    # Python dependencies
├─ .env                # Hugging Face API token (not tracked)
└─ README.md

🌐 Supported Currencies

USD (Dollar)

INR (Rupee)

EUR (Euro)

GBP (Pound)

JPY (Yen)

More can be added easily by extending CURRENCY_ALIASES in agent_core.py.

📈 Next Features / TODO

Auto-detect currencies from free-text (e.g., "500 rupees to dollars")

Live charts of conversion trends

Multi-currency conversions in one request

Export conversation history

⚖️ License

MIT License – free to use, modify, and distribute.
