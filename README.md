# PyRVA Bots
This is the PyRVA bot used in the pyrva discord server. 

Join the server here: https://discord.gg/PThzSm3n

## Cogs
| COG | Description | Status | Owner | 
|-----|-------------|--------|-------|
| fun | show some examples and general fun stuff | On-Going | Richard |
| utilities | these are some practical utilites that are helpful | On-Going | Richard |
| raffle | Monitor text channels to help with raffles | Functional | Cohan |
| meetup | post the up coming meetup meeting to a channel looping on a time  interval | In Progress | Richard |
| autobadge | automatically manage badges for people attending events | In Progress | TBD |

## Proposed Features

- [X] raffle
- [ ] fun
	- [X] random futurama pop culture quote. fight me about it -RSB
	- [X] random number generator for simulating rolling dice
	- [X] return the zen of python
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
	- [ ] create tool that automatically assigns a given badge based on presence

> 💡If someone can think of a way to write unit tests / pytests to test things like the raffle cog in particular I am all ears. My best case solution is to setup a Dev/Prod dynamic for testing but that feels like more work than its worth. 

## Deployment:

fire and forget:
```zsh
sudo docker-compose up -d
```

if you want to use the docker-compose during development be sure to destroy/increment the image or the docker-compose will just use the same image over and over. 
```
sudo docker-compose down --rmi all
```
> 💡one potential solution to this is to mount the directory but seemed more trouble than its worth atm. This was faster and ultimately more robust


---
# RSB Notes

## Special Thanks go to: 
- https://github.com/Crambin/Orderbot
- https://github.com/Xarlos89/ZorakBot
## Helpful Docs:
- [RealPython - How to make discord bot in python](https://realpython.com/how-to-make-a-discord-bot-python/#how-to-make-a-discord-bot-in-python)
- [Meetup API docs](https://secure.meetup.com/meetup_api/console/)
- [DiscordPy Read The Docs](https://discordpy.readthedocs.io/en/latest/index.html)
