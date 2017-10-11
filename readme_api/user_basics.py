""" User Basics """
from time import strftime
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from basicauth import decode
from readme_api.models import UserDetails
from readme_api.tools import generate_hash
from readme_api.email_handler import send_forgot_password_email, send_signup_email

@csrf_exempt
def signin(request):
    """ Login Module """
    body_unicode = request.body.decode('utf-8')
    body = json.loads(body_unicode)
    platform = body['platform']
    print platform
    if 'HTTP_AUTHORIZATION' not in request.META:
        return JsonResponse({"details":"Authorization code missing"}, status=401)
    email, password = decode(request.META['HTTP_AUTHORIZATION'])
    print email, password
    token = generate_hash()
    user_details = UserDetails.objects.filter(email=email)
    if len(user_details) == 0:
        return JsonResponse({'message':'Invalid Email'}, status=401)
    if user_details[0].password == password:
        if platform == "android":
            UserDetails.objects.filter(
                email=email
            ).update(android_token=token)
        if platform == "ios":
            UserDetails.objects.filter(
                email=email
            ).update(ios_token=token)
        if platform == "desktop":
            UserDetails.objects.filter(
                email=email
            ).update(desktop_token=token)
        # UserDetails.objects.filter(email=email).update(token=token)
        get_user_details = UserDetails.objects.filter(email=email)
        if platform == "android":
            token_platform = get_user_details[0].android_token
        if platform == "ios":
            token_platform = get_user_details[0].ios_token
        if platform == "desktop":
            token_platform = get_user_details[0].desktop_token
        data_to_return = {
            'id':get_user_details[0].id,
            'name':get_user_details[0].name,
            'username':get_user_details[0].username,
            'email':get_user_details[0].email,
            'access_token':token_platform,
            }
        return JsonResponse({'message':'Login Success', 'user':data_to_return}, status=200)
    else:
        return JsonResponse({'message':'Incorrect Password'}, status=401)

@csrf_exempt
def signup(request):
    """ SignUp Module """
    name = request.GET.get('name')
    username = request.GET.get('username')
    password = request.GET.get('password')
    email = request.GET.get('email')
    platform = request.GET.get('platform')
    now = strftime("%d-%m-%Y %H:%M:%S")
    if name is None or username is None or password is None or email is None:
        return JsonResponse({"message":"Fields can't be empty"}, status=400)
    if platform is None:
        return JsonResponse({"message":"Fields can't be empty"}, status=400)
    check_username = UserDetails.objects.filter(username=username)
    check_email = UserDetails.objects.filter(email=email)
    if len(check_username) != 0:
        return JsonResponse({'message':'Username already exist choose different'}, status=409)
    if len(check_email) != 0:
        return JsonResponse({'message':'Email already exist, please login'}, status=409)
    try:
        token = generate_hash()
        create_user = UserDetails.objects.create(
            name=name,
            username=username,
            email=email,
            password=password,
            email_verified='no',
            signin_on=now,
            )
        if platform == "android":
            UserDetails.objects.filter(
                id=create_user.id
            ).update(android_token=token)
        if platform == "ios":
            UserDetails.objects.filter(
                id=create_user.id
            ).update(ios_token=token)
        if platform == "desktop":
            UserDetails.objects.filter(
                id=create_user.id
            ).update(desktop_token=token)
        ack = send_signup_email(email, name, token)
        print ack
        return JsonResponse({
            'message':'Signup Done'
        }, status=200)
    except Exception as e:
        print e
        return JsonResponse({'message':e}, status=500)

def signout(request):
    """ App User Signout"""
    token = request.GET.get('token')
    platform = request.GET.get('platform')
    user_id = request.GET.get('user_id')
    if None in (token, platform, user_id):
        return JsonResponse(
            {
                "message":"Fields can't be empty"
                },
            status=400
            )
    if platform == "android":
        UserDetails.objects.filter(
            id=user_id,
            android_token=token
            ).update(
                android_token=0
                )
    if platform == "ios":
        UserDetails.objects.filter(
            id=user_id,
            ios_token=token
            ).update(
                ios_platform=0
                )
    if platform == "desktop":
        UserDetails.objects.filter(
            id=user_id,
            desktop_token=token
            ).update(
                desktop_platform=0
                )
    return JsonResponse({"message":"Done"}, status=200)

def check_user(request):
    """Check the user valid or not """
    token = request.GET.get('token')
    user_id = request.GET.get('user_id')
    platform = request.GET.get('platform')
    if None in (token, user_id, platform):
        return JsonResponse(
            {
                "message":"Fields can't be empty"
                },
            status=400
            )
    if str(token) == "0":
        return JsonResponse(
            {
                "message":"Invalid User"
            }, status=401
        )
    else:
        try:
            if platform == 'android':
                user = UserDetails.objects.filter(
                    android_token=token,
                    id=user_id
                )
            elif platform == 'ios':
                user = UserDetails.objects.filter(
                    ios_token=token,
                    id=user_id
                )
            elif platform == 'desktop':
                user = UserDetails.objects.filter(
                    ios_token=token,
                    id=user_id
                )
            else:
                return JsonResponse(
                    {
                        "message":"Invalid Request"
                    }, status=409
                )
        except:
            return JsonResponse(
                {
                    "message":"Error"
                }, status=500
            )
        if len(user) != 0:
            return JsonResponse(
                {
                    "message":"Valid User"
                }, status=200
            )
        else:
            return JsonResponse(
                {
                    "message":"Invalid user"
                }, status=401
            )

def forgot_password_handler(request):
    """ This Module will handle forgot password"""
    email = request.GET.get('email')
    if email is None or email == "":
        return JsonResponse(
            {
                "message":"Fields can't be empty"
                },
            status=400
            )
    user_details = UserDetails.objects.filter(email=email)
    if len(user_details) == 0:
        return JsonResponse(
            {
                "message":"Not a registered email, please signup"
                },
            status=200
            )
    if str(user_details[0].token) == "0":
        new_token = generate_hash()
        update_token = UserDetails.objects.filter(email=email).update(token=new_token)
        update_token.save()
    name = user_details[0].name
    current_token = UserDetails.objects.filter(email=email)
    ack = send_forgot_password_email(email, name, current_token[0].token)
    if ack is True:
        return JsonResponse(
            {
                "message":"We have sent a mail to reset your password, please check your email"
                },
            status=200
            )
    return JsonResponse(
        {
            "message":"Erro! While sending reset email"
            },
        status=502
        )
