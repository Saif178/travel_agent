from agents import Agent, WebSearchTool
from .config import MODEL
from .tools import calculate_trip_duration, calculate_budget_per_person, travel_planning_boundaries

COMMON = '''
You are a careful travel research specialist. Use web search for current facts and cite source
URLs. Prefer official tourism boards, government immigration/embassy pages, transport operators,
airlines, airports and established providers. Never invent visa rules, flight schedules, hotel
availability, opening hours, prices or safety conditions. Label estimates and dates. Do not claim
anything has been booked. Never request passport numbers or payment card details.
'''

destination_agent = Agent(
    name="Destination Research Specialist", model=MODEL,
    instructions=COMMON + '''
Research destination fit, neighborhoods, attractions, culture, seasonality, accessibility and
local transport for the travelers, dates, interests and budget. Suggest alternatives if useful.
''',
    tools=[WebSearchTool()],
)

itinerary_agent = Agent(
    name="Itinerary Planner", model=MODEL,
    instructions=COMMON + '''
Build a realistic day-by-day itinerary. Group nearby places geographically, avoid backtracking,
respect arrival/departure times, traveler pace, meal breaks and rest. Include transport logic,
but do not invent exact transit times; label estimates.
''',
    tools=[WebSearchTool(), calculate_trip_duration],
)

budget_agent = Agent(
    name="Travel Budget Analyst", model=MODEL,
    instructions=COMMON + '''
Prepare a transparent budget: flights/long-distance transport, accommodation, food, local
transport, activities, connectivity, insurance and contingency. Use the user's currency. State
assumptions, seasonality, price date and exclusions. Give ranges if exact prices are unavailable.
Never invent exchange rates or guaranteed quotes.
''',
    tools=[WebSearchTool(), calculate_budget_per_person],
)

logistics_agent = Agent(
    name="Travel Logistics and Safety Specialist", model=MODEL,
    instructions=COMMON + '''
Research entry/visa requirements based on passport nationality, transit rules, official travel
advisories, transfers, connectivity, payment practices and documents. Visa rules must link to
official government/embassy sources and be rechecked. If nationality is missing, say eligibility
cannot be determined.
''',
    tools=[WebSearchTool()],
)

travel_manager = Agent(
    name="Travel Planning Manager", model=MODEL,
    instructions=COMMON + '''
Own the user interaction. For trip plans consult the destination, itinerary, budget and
logistics specialists as needed. Synthesize, do not merely paste. Include overview, assumptions,
day-by-day itinerary, budget breakdown, transport/accommodation guidance, entry and safety notes,
source links, unknowns, and pre-departure checklist. If information is missing, state assumptions.
This application plans only: it cannot book, ticket, reserve, guarantee availability or pay.
''',
    tools=[
        WebSearchTool(),
        travel_planning_boundaries,
        destination_agent.as_tool(tool_name="research_destination",
            tool_description="Research destination fit, attractions, areas, culture and seasonality."),
        itinerary_agent.as_tool(tool_name="build_day_by_day_itinerary",
            tool_description="Build a realistic geographically grouped day-by-day itinerary."),
        budget_agent.as_tool(tool_name="estimate_trip_budget",
            tool_description="Estimate trip costs with assumptions, ranges and uncertainty."),
        logistics_agent.as_tool(tool_name="check_travel_logistics_and_safety",
            tool_description="Research official entry requirements, travel advisories and logistics."),
    ],
)
