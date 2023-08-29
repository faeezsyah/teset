
from run import usernames
from instagrapi import Client

cl = Client()
cl.delay_range = [1, 3]
cl.login('elleeconella', 'Illyanabilah2.')

import time


for i in range(len(usernames)):
    if i % 15 == 0:
        time.sleep(1,800)
    user_id = cl.user_id_from_username(f"{usernames[i]}")
    time.sleep(5)
    cl.user_follow(user_id = user_id)

