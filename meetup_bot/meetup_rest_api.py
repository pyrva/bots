import json
import os

import requests as r


def _url(path):
    return "https://api.meetup.com/PyRVAUserGroup/" + path


def _get_upcoming():
    # request events from Meetup REST API
    response = r.get(_url("events"))
    new_list = response.json()
    # print (response.json())

    # file storage handling
    curpath = os.path.abspath(os.curdir)
    filename = "meetup_example/eventList.json"
    filepath = os.path.join(curpath, filename)
    print(f"Trying to open: {filepath}")

    if os.path.exists(f"{filepath}"):
        print("oh boy here we go again....")
        with open(filepath) as f:
            old_list = json.load(f)
    else:
        print("well where'd you leave it ya dingus?")
        old_list = open(f"{filepath}", "w+")

    ignore_list = ["Monthly online lecture night", "Monthly Coding Night (ONLINE!!!)"] #TODO: might want to parameterize this

    # compare old and new list
    if new_list != old_list:
        for x in response.json():
            if x["name"] not in ignore_list:
                event_info = f"Event: {x['name']} @Date: {x['local_date']} @Time: {x['local_time']}\nStatus: {x['status']}\nLink: {x['link']}"
                print(event_info)
    else:
        print("No New Updates")
        event_info = "No New Updates"

    # overwrite old list with new
    with open(f"{filename}", "w") as f:
        json.dump(new_list, f)

    
    #TODO select the events worth posting to discord and return only them
    ## Check the channel for Id's / keys of events already posted?

    return event_info 


if __name__ == "__main__":
    _get_upcoming()
