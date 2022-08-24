# PyRVA Bots

>❗This was an experiment based on some feedback 

Special Thanks go to: 
- https://github.com/Crambin/Orderbot
- https://github.com/Xarlos89/ZorakBot

# 
Bot | Service | Description | Status | Owner
---|---|---|---|---
simple_example | Discord | show how to connect to bot | On-Going | Richard
raffle_bot | Discord | Monitor text channels to help with raffles | Functional | Cohan
meetup_bot | Discord | post the up coming meetup meeting to a channel looping on a time  interval | In Progress | Richard

---
## Proposed Features

- [X] raffle bot
- [ ] utilities
	- [X] let me google that for you
	- [X] pip search
	- [ ] return random pip package
	- [X] bot ping latency check
	- [ ] user inspection?
	- [ ] run python snippet
	- [ ] pprint help message
	- [X] github repo message
- [ ] Meetup
	- [X] ask when the next meetup is
    - [ ] scrapes the meetup API for relavant info and posts this info to discord auto magically
- [ ] announcements
	- [ ] user would post an announcement and bot would post it in the announcements section
- [ ] Assign badge to people attending specific events
	- [X] create a list of who is present in meeting



---
# Deployment:

fire and forget:
```zsh
sudo docker-compose up -d
```

if you want to use the docker-compose in development be sure to destroy/increment the image or the docker-compose will just use the same image over and over. 
```
sudo docker-compose down --rmi all
```
> 💡one potential solution to this is the mount the directory but seemed more trouble than its worth atm. 


---
## RSB Notes

### Helpful Docs:
- [RealPython - How to make discord bot in python](https://realpython.com/how-to-make-a-discord-bot-python/#how-to-make-a-discord-bot-in-python)
- [Meetup API docs](https://secure.meetup.com/meetup_api/console/)
- [DiscordPy Read The Docs](https://discordpy.readthedocs.io/en/latest/index.html)
