import asyncio
from datetime import date, timedelta
import streamlit as st
from src.travel_agent.workflow import plan_trip

st.set_page_config(page_title="AI Travel Agent", page_icon="✈️", layout="wide")
st.title("✈️ AI Travel Agent")
st.caption("Multi-agent destination research, itinerary planning, budgeting and travel logistics")

with st.form("trip_form"):
    a, b = st.columns(2)
    with a:
        origin = st.text_input("Starting city / airport", "Hyderabad, India")
        destination = st.text_input("Destination", "Japan")
        start = st.date_input("Departure", date.today() + timedelta(days=45))
        end = st.date_input("Return", date.today() + timedelta(days=52))
        travelers = st.number_input("Travelers", 1, 20, 2)
        passport = st.text_input("Passport nationality (for visa research)", "Indian")
    with b:
        budget = st.text_input("Total budget and currency", "INR 150,000")
        interests = st.text_area("Interests", "Culture, food, nature, museums")
        pace = st.selectbox("Pace", ["Balanced", "Relaxed", "Fast-paced", "Family-friendly"])
        stay = st.selectbox("Accommodation", ["Budget", "Mid-range", "Premium", "Luxury", "Flexible"])
        notes = st.text_area("Additional requirements", placeholder="Diet, accessibility, children, etc.")
    submitted = st.form_submit_button("Plan my trip", type="primary")

if submitted:
    if not origin.strip() or not destination.strip():
        st.error("Please enter both origin and destination.")
    elif end <= start:
        st.error("Return date must be after departure.")
    else:
        with st.spinner("Travel specialists are researching your trip..."):
            try:
                st.session_state["trip_report"] = asyncio.run(plan_trip(
                    origin.strip(), destination.strip(), start.isoformat(), end.isoformat(),
                    int(travelers), budget, interests, pace, stay, passport, notes,
                    "reports/latest_trip_plan.md"))
            except Exception as exc:
                st.error(f"{type(exc).__name__}: {exc}")

if st.session_state.get("trip_report"):
    st.divider()
    st.markdown(st.session_state["trip_report"])
    st.download_button("Download trip plan", st.session_state["trip_report"],
                       file_name="travel_plan.md", mime="text/markdown")

st.caption("Planning only: no ticketing, reservations, payments or guaranteed live inventory.")
