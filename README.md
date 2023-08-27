# liskv3-node-monitor-telegram
A quick and dirty python script to check if a node is missing blocks and notify through Telegram

Simply pull the file and edit the config within.

Afterwards, add a cron entry to run the script every minute, like so:
```
* * * * * /usr/bin/python3 /location/of/lisk_monitor.py
```

**Short guide how to create a Telegram bot and retrieve the ChatID:**
1. Create a Bot using the official telegram BotFather (it has a verified symbol next to it when you add it as a contact).
2. Follow the prompts, and finally copy it’s HTTP API Token.
3. Visit this URL: ```https://api.telegram.org/botXXX:YYYYY/getUpdates``` (replace the XXX: YYYYY with your BOT HTTP API Token you just got from the Telegram BotFather)
4. Send your newly created bot a message
5. Refresh the URL, you will now be able to retrieve your personal telegram chat id to use within the script
