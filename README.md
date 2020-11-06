# pomodorobot
This script implements a bot for a discord server, that enables multiple people to coordinate pomodoro breaks together.

In the off-chance that I or anyone else ever recycles this...

In order to run this script locally, create a .env file which looks like the following:

#.env  
DISCORD_TOKEN=insert token  
DISCORD_GUILD="insert name of discord server"  

This tutorial has a good explanation on how to set up a bot in Discord's developer portal:  
https://realpython.com/how-to-make-a-discord-bot-python/#how-to-make-a-discord-bot-in-the-developer-portal

Here is some combination of the commands I used to get this to deploy on heroku (I also set up the env variables manually through its config vars setting):

```
sudo snap install --classic heroku  
heroku login  
heroku apps:create insert_name_of_bot  
heroku buildpacks:set heroku/python  
git push heroku main  
heroku ps:scale web=1  
heroku logs --tail  
```
