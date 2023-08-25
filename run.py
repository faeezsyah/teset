from instagrapi import Client

from instagrapi import Client

cl = Client()
cl.login('elleeconella', 'Illyanabilah2.')

user_id = cl.user_id_from_username("huhitsyaf")

cl.user_followers(user_id=user_id, int = 0)