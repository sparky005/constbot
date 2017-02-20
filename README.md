##A twitter bot to help our President finally read the US Constitution

Are you worried that Donald J. Trump hasn't read the constitution? Worry no more! This bot will tweet it over to him in small, bite-sized chunks.

Trouble is, he probably won't notice just one person tweeting at him ever hour. So I encourage you to set up your own! The more bots tweeting the Constitution directly at our President, the better our chances of him actually being forced to read it.

I've recently updated the app so that it runs on [Heroku](heroku.com), so you can get it up and running without needing a server and **for free!**

Prerequisites:

1. You'll need [git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git) and [heroku-toolbelt](https://devcenter.heroku.com/articles/heroku-cli) installed on your system. Those links should have instructions for all platforms.  
2. Set up a new Twitter account for the bot. Make sure you give it a phone number, or else it won't be allowed to post. Stayed signed in as this account for the next step.  
3. Create a new Twitter app and save the API keys. You can follow  [these instructions](https://www.gabfirethemes.com/create-twitter-api-key/) for help.  
4. Sign up for a [Heroku Account](https://signup.heroku.com/). You'll need to 'verify' your account with a credit card before proceeding, but don't worry, we'll be operating on the free tier so you won't be charged.  
5. Create a new app in Heroku. Call it whatever you want, the name doesn't matter. We will push the code to this app later.  


Okay, on to the actual setup:

1. Clone the repo to your local machine. On the command line:  

	```
	git clone https://github.com/sparky005/constbot.git
	```

2. Edit the consumer.py file to include your API keys from step 3 above.  
3. In your command line, cd into the constbot directory and commit the changes you made to the consumer.py file:  

	```
	cd constbot/
	git add consumer.py -f
	git commit -m "Add API keys"
	```

4. Now log in to heroku and push the local repo up:  

	```
	heroku login
 	<type your username and password>
	heroku git:remote -a <nameOfHerokuApp>
	git push heroku master
	```
5. Now we just need to schedule the heroku app to run. To do this, we can add Heroku's scheduler:  

	```
	heroku addons:create scheduler:standard
	heroku addons:open scheduler
	```
6. The second command will open a new browser window with the scheduler options. Type 'worker' next to the $ symbol and choose how often you want the app to run.

That's it!