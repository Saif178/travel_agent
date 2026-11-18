from datetime import date
from agents import function_tool

@function_tool
def calculate_trip_duration(start_date: str, end_date: str) -> str:
    """Calculate trip nights and calendar days. Dates must use YYYY-MM-DD."""
    try:
        start, end = date.fromisoformat(start_date), date.fromisoformat(end_date)
        if end <= start:
            return "Invalid range: return date must be after departure date."
        nights = (end - start).days
        return f"{nights} nights / {nights + 1} calendar days."
    except ValueError:
        return "Invalid date format. Use YYYY-MM-DD."

@function_tool
def calculate_budget_per_person(total_budget: float, travelers: int) -> str:
    """Calculate equal per-person budget in the same currency as the input."""
    if total_budget < 0 or travelers < 1:
        return "Enter a non-negative budget and at least one traveler."
    return f"Estimated per-person budget: {total_budget / travelers:,.2f}."

@function_tool
def travel_planning_boundaries() -> str:
    """Describe travel planning capabilities and limitations."""
    return ("Research and planning only. This app cannot issue tickets, reserve hotels, "
            "guarantee live prices or availability, issue visas, or process payments. "
            "Direct users to official providers and government sources for confirmation.")
