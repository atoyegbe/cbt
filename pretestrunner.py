from functools import lru_cache
from typing import Tuple

from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from cbtuser.models import CBTUser


valid_payload = {
            'date_of_birth': '1948-11-20',
            'first_name': "Dianna",
            'last_name': 'Pamerion',
            'password': 'pass123',
            'email': 'dianna@cbt.com'
}

@lru_cache
def get_user() -> Tuple[User, Token]:

    # user =  User.objects.get(username ="diaP123")
    if 1:
        user = User.objects.create_user(
            username="diaP123", email=valid_payload["email"], 
            password=valid_payload["password"]
        )
        user.save()
        cbtuser = CBTUser.objects.create(
            user=user, date_of_birth=valid_payload["date_of_birth"], 
            first_name=valid_payload["first_name"], last_name=valid_payload["last_name"]
        )
        cbtuser.save()

        token = Token.objects.get_or_create(user=user)
        return user, token


@lru_cache
def delete_all() -> None:

    u = User.objects.get(username="diaP123" or None)
    t = Token.objects.get(user__username="diaP123" or None)
    t.delete()
    u.delete()
