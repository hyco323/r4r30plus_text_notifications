import praw #THIS IS THE REDDIT API WRAPPER PACKAGE. MAKES IT EASY TO DEAL WITH THE REDDIT API
from twilio.rest import Client #TWILLIO PACKAGE TO SEND THE TEXT MESSAGE
import time 

# Your Reddit app credentials from https://www.reddit.com/prefs/apps. 
# Make sure to use 'script' and not a 'web app'

CLIENT_ID = "INSERT YOUR ID YOU GOT FROM THE REDDIT DEV PAGE"
CLIENT_SECRET = "INSERT YOUR SECRET YOU GOT FROM THE REDDIT DEV PAGE"
USER_AGENT = "MAKE SOMETHING UP FOR THIS"
USERNAME = "YOUR REDDIT USERNAME"
PASSWORD = "YOUR REDDIT PASSWORD"

# Twilio credentials.
# you need to make a trail account with twilio to send text messages
TWILIO_SID = "INSERT YOUR SID YOU GOT FROM TWILLIO"
TWILIO_AUTH_TOKEN = "TOKEN FOUND ON YOUR TWILLIO PROFILE"
TWILIO_PHONE_NUMBER = 'YOUR TWILLIO NUMBER'
DEST_PHONE_NUMBER = 'NUMBER TO SEND YOUR TEXT TO'

reddit = praw.Reddit(client_id=CLIENT_ID,
                     client_secret=CLIENT_SECRET,
                     user_agent=USER_AGENT,
                     username=USERNAME,
                     password=PASSWORD)

client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN) #SETS UP THE TWILLIO CLIENT WITH YOUR INFO TO SEND MESSAGES
post_ids = [] # empty list that will be apended with post ids as the programs run to ensure you dont get notified for only new posts.
              # will be reset when you close the program.
def check_new_posts(): 
    for post in reddit.subreddit('R4R30Plus').new(limit=10):  #LOOPS THROUGH THE 10 NEWEST POSTS IN THE R4R30PLUS SUBREDDIT
      if post.id in posts_ids:
				if "f4r" in post.title.lower() or "f4m" in post.title.lower(): # CHECKS FOR ANY FEMALE POSTS
					message = f"there is a new message on r4r30plus; check it out:\n{post.title}\n" # ITS THE MESSAGE THAT WILL BE SENT TO YOU, EDIT IT TO SAY WHATEVER YOU LIKE
					client.messages.create(body=message, from_=TWILIO_PHONE_NUMBER, to=DEST_PHONE_NUMBER) # THE PART OF THE CODE THAT ACTUALLY SENDS THE MESSAGE
			else:
        print('No new posts, will try again in 30 minutes.')

if __name__ == "__main__":
    while True: #INFINATE LOOP, STOP THE PROGRAM WITH CTRL-C
        try:
            check_new_posts() #RUNS THE PROGRAM ABOVE
            time.sleep(1800)  # WAITS 30 MINUTES TO CHECK AGAIN, CHANGE IT TO FIT YOUR ANNOYANCE LEVEL.
        except Exception as e:
            print(f"Error: {e}") #IF YOU GET A 403 ERROR, IT BECAUSE YOU DIDNT CHOOSE SCRIPT IN REDDIT DEV PART OR THE SUBREDDIT YOU WANT TO GET NOTIFICATIONS FROM IS PRIVATE
            time.sleep(300)
