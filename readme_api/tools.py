from django.http import HttpResponse
from models import UserDetails

def check_token(access_token):
    get_token = UserDetails.objects.filter(token=access_token)
    if len(get_token) != 0:
        return True
    else:
        return False
