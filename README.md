# AI Travel Agent — OpenAI Agents SDK

A multi-agent travel planning application that researches destinations, creates day-by-day
itineraries, estimates budgets, and checks entry requirements and practical travel logistics.

## Agent team
- Travel Planning Manager: coordinates the trip and synthesizes the plan.
- Destination Research Specialist: destination fit, neighborhoods, attractions and seasonality.
- Itinerary Planner: day-by-day route and realistic pacing.
- Travel Budget Analyst: cost categories, ranges, assumptions and contingency.
- Travel Logistics and Safety Specialist: official entry/visa research, advisories and transfers.

The manager uses the OpenAI Agents SDK `Agent.as_tool()` pattern to consult specialists.

## Setup (Windows PowerShell)
```powershell
py -m venv .venv
.venv\Scripts\Activate.ps1
pip install --upgrade pip
pip install -r requirements.txt
Copy-Item .env.example .env
```
Add your OpenAI API key to `.env`; choose a model enabled for your API account.

## Run the dashboard
```powershell
streamlit run app.py
```
Enter origin, destination, dates, travelers, budget/currency, interests, pace, accommodation
and passport nationality. Generate and download the Markdown trip plan.

## CLI
```powershell
python -m src.travel_agent.cli --origin "Hyderabad, India" --destination "Japan" --start 2027-01-10 --end 2027-01-17 --travelers 2 --budget "INR 200000" --interests "Culture, food, nature" --passport "Indian"
```

## Project structure
```text
travel_agent_project/
├── app.py
├── requirements.txt
├── .env.example
├── README.md
├── src/
│   ├── __init__.py
│   └── travel_agent/
│       ├── __init__.py
│       ├── config.py
│       ├── tools.py
│       ├── agents.py
│       ├── workflow.py
│       └── cli.py
└── reports/
```

## Important limitations
This version researches and plans; it does not book flights, hotels, rental cars or tours, issue
tickets, process payments, or guarantee live inventory/prices. Visa and entry information must be
rechecked with the official embassy/immigration authority. It is not a substitute for official
travel advisories.

## Future integrations
Add authorized flight/hotel inventory APIs (e.g. Amadeus or another licensed provider), maps and
routing, weather and currency APIs. Keep secrets server-side, respect provider terms and require
explicit user confirmation before any paid booking action.
