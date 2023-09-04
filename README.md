# r4r30plus_text_notifications
scans r4r30plus for any posts that have f4r or f4m in the title every 30 min 

Get the secrets and client id for reddit from https://www.reddit.com/prefs/apps

Get a free twilio trail account from https://www.twilio.com/en-us

this is just a simple python script that scraps r4r30post and send a text message every time a new post by with a f4r or f4m is in the title. 

Use it as a simple templete to get notifications from other subreddits(only works with non private subreddits).

Change the criteria of what you want to get notified about. the praw documentation is here to filter using post title or for a specic URL. https://praw.readthedocs.io/en/stable/getting_started/quick_start.html
