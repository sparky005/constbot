##A twitter bot to help our President finally read the US Constitution

Are you worried that Donald J. Trump hasn't read the constitution? Worry no more! This bot will tweet it over to him in small, bite-sized chunks.

Trouble is, he probably won't notice just one person tweeting at him ever hour. So I encourage you to run this, too!

The easiest way to run it is through a cronjob on a Linux server. If you don't have a Linux server, you can use a VPS ([shameless referral link](https://m.do.co/c/2a56dcfde348))

This setup guide assumes you already have python3 and git installed

Setup:
Install tweepy, clone the repo
```
sudo pip install tweepy
git clone https://github.com/sparky005/constbot.git
```
Change the consumer.py file to use your Twitter API keys. If you don't know how to do that, check out [these instructions](https://www.gabfirethemes.com/create-twitter-api-key/) that I found Googling.

Set up a bash script to run it like so:
```
cd /path/to/constbot/directory
python3 constbot.py
```

Create the crontab file to run it at your chosen interval:
```
15 * * * * /path/to/bash/script.sh # this will run it every hour on the quarter hour
```

And finally, register your crontab:
```
crontab /your/crontab/file.txt
```

That's it!
