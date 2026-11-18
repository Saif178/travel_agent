from pathlib import Path
from agents import Runner
from .agents import travel_manager

async def plan_trip(origin, destination, start_date, end_date, travelers=1,
                    budget="Not specified", interests="General sightseeing",
                    pace="Balanced", accommodation="Mid-range",
                    passport_nationality="Not provided", extra_notes="", output=None):
    prompt = f'''
Plan this trip using specialist research agents.
Origin: {origin}
Destination: {destination}
Dates: {start_date} to {end_date}
Travelers: {travelers}
Total budget/currency: {budget}
Interests: {interests}
Pace: {pace}
Accommodation: {accommodation}
Passport nationality: {passport_nationality}
Additional notes: {extra_notes or "None"}

Provide trip overview, assumptions, destination fit, day-by-day itinerary, indicative budget
breakdown, transport/accommodation guidance, visa/entry and safety notes, source URLs, and
booking/pre-departure checklist. Distinguish researched prices from estimates. Never claim to
have booked anything. Direct users to official sources for time-sensitive rules.
'''
    result = await Runner.run(travel_manager, prompt)
    report = str(result.final_output)
    if output:
        path = Path(output)
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(report, encoding="utf-8")
    return report
