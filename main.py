from scrap import scrap_user
from notify import notify_by_email
from cryptography.fernet import Fernet
import os
import json

data = open('users.token', 'rb').read()
users = json.loads(Fernet(os.environ['FERNET_KEY']).decrypt(data))['users']
for user in users:
    ret = scrap_user(user['user'])
    print(user['user'], ret)
    if ret is not None and not any(entry[1] == 'Accepted' for entry in ret):
        notify_by_email(user['user'], user['email'])