import argparse, asyncio
from .workflow import plan_trip

def main():
    p = argparse.ArgumentParser(description="OpenAI Agents SDK travel planner")
    p.add_argument("--origin", required=True)
    p.add_argument("--destination", required=True)
    p.add_argument("--start", required=True, help="YYYY-MM-DD")
    p.add_argument("--end", required=True, help="YYYY-MM-DD")
    p.add_argument("--travelers", type=int, default=1)
    p.add_argument("--budget", default="Not specified")
    p.add_argument("--interests", default="General sightseeing")
    p.add_argument("--pace", default="Balanced")
    p.add_argument("--accommodation", default="Mid-range")
    p.add_argument("--passport", default="Not provided")
    p.add_argument("--notes", default="")
    p.add_argument("--output", default="reports/trip_plan.md")
    a = p.parse_args()
    report = asyncio.run(plan_trip(a.origin, a.destination, a.start, a.end, a.travelers,
        a.budget, a.interests, a.pace, a.accommodation, a.passport, a.notes, a.output))
    print(report)
    print(f"Saved to {a.output}")

if __name__ == "__main__":
    main()
