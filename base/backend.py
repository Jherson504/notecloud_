import json
from django.contrib.auth.models import User
from pathlib import Path
import os


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


def update_json():
    users_list = []

    users = User.objects.all()

    for user in users:
        users_list.append(user.username)

    username_json = open(os.path.join(
        BASE_DIR, 'static', 'json', 'usernames.json'), 'w')

    text = json.dumps(
        {
            'usernames': users_list
        }
    )
    username_json.write(text)
    username_json.close()
