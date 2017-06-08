""" Tools """
import binascii
import os
from readme_api.models import UserDetails

def check_token(access_token, user_id, platform):
    """ This modu """
    if access_token == 0:
        return False
    if platform == "android":
        get_token = UserDetails.objects.filter(
            android_token=access_token,
            id=user_id
            )
    if platform == "ios":
        get_token = UserDetails.objects.filter(
            ios_token=access_token,
            id=user_id
            )
    if platform == "desktop":
        get_token = UserDetails.objects.filter(
            desktop_token=access_token,
            id=user_id
            )
    if len(get_token) != 0:
        return True
    else:
        return False

def generate_hash():
    """ This module will generate the hash for access token """
    return str(binascii.b2a_hex(os.urandom(15)))
