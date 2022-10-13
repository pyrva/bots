import json
from pathlib import Path

import requests as r


def _url(path):
    return f"https://api.meetup.com/PyRVAUserGroup/{path}"


def _get_upcoming():
    current_events = r.get(_url("events")).json()
    event_cache = Path("eventList.json")
    print(f"Trying to open: {event_cache}")
    if event_cache.exists():
        print("oh boy here we go again....")
        old_list = json.loads(event_cache.read_text())
    else:
        print("well where'd you leave it ya dingus?")
        old_list = []
    if current_events != old_list:
        ignore_list = ["Monthly online lecture night",
            "Monthly Coding Night (ONLINE!!!)"]

        for x in current_events:
            if x["name"] not in ignore_list:
                event_info = f"Event: {x['name']} @Date: {x['local_date']} @Time: {x['local_time']}\nStatus: {x['status']}\nLink: {x['link']}"
                print(event_info)
    else:
        print("No New Updates")
        event_info = "No New Updates"
    json.dump(current_events, event_cache.open('w'))
    return event_info


def _get_next():
    response = r.get(_url("events"))
    event_list = response.json()
    x = event_list[0]
    return f"Event: {x['name']} @Date: {x['local_date']} @Time: {x['local_time']}\nStatus: {x['status']}\nLink: {x['link']}"


if __name__ == "__main__":
    # _get_upcoming()

    print(_get_next())
