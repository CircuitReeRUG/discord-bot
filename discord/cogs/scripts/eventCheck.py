# Scrapes the cover website and adds events accordingly
# Stores the already parsed events in a json file

import icalendar
from wget import download
from os import remove, listdir
from json import load, dumps
# Json schema:
# {
#   "name": [
#     {
#       "date": "event date",
#       "time": "event time",
#       "location": "event location",
#       "description": "event description",
#       "link": ["cover link"]
#     }


# Return a link from the description
def get_link(desc: str) -> str:
    try:
        return desc.split("More information:")[1]
    except IndexError:
        return "No link available."


def download_cal() -> icalendar.Calendar:
    # Delete all previous calendars (if any)
    download("http://www.svcover.nl/calendar?format=webcal", "cover.ics", bar=None)

    path = "cover.ics"
    with open(path) as f:
        calendar = icalendar.Calendar.from_ical(f.read())

    with open("db.json", "r") as f:
        db = load(f)

    return calendar, db, path


# This function downloads the calendar from the SV Cover website and updates the database with the new events.
# Returns whether there was new data to update the database with.
def update_check(comm: str = None) -> list:

    calendar, db, path = download_cal()

    # Check if there are new events and check if the
    new_events = []
    for event in calendar.walk("vevent"):
        ev = event.get("summary", None)

        # 🤮
        try:
            organizer = ev.split(":")[0]
        except IndexError:
            organizer = "Unknown"

        try:
            summary = ev.split(": ")[1]
        except IndexError:
            summary = "No summary available."

        if summary not in db and (comm is None or organizer == comm):
            description = event.get("description", None)
            description = (
                description.split("\n\n")
                if description is not None
                else "No description available."
            )
            db[summary] = {
                "organizer": organizer,
                "date": event["dtstart"].dt.strftime("%Y-%m-%d"),
                "time": event["dtstart"].dt.strftime("%H:%M"),
                "location": event.get("location", "Unknown"),
                "description": (
                    description[1]
                    if description is not None
                    else "No description available."
                ),
                "link": (
                    get_link(description[0])
                    if description is not None
                    else "No link available."
                ),
            }
            new_events.append((summary,db[summary]))
    
    remove(path)
    
    if not new_events:
        return False

    with open("db.json", "w") as f:
        f.write(dumps(db, indent=2))

    

    return new_events
