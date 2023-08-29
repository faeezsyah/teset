from instagrapi import Client

from instagrapi import Client

cl = Client()
cl.delay_range = [0.1, 0.3]
cl.login('ana_.anachong', 'Illyanabilah2.')
user_id = cl.user_id_from_username("huhitsyaf")

try:
    data = cl.user_followers(user_id=user_id, amount = 15)
    usernames = [user_data.username for user_data in data.values()]
except:
    print("Something went wrong")
else:
    print("good")

