from django.http import HttpResponse,HttpResponseRedirect,JsonResponse
from django.views.decorators.csrf import csrf_exempt
from models import UserDetails
from time import strftime
from Crypto.Hash import SHA256

@csrf_exempt
def signup(request):
    name = request.POST.get('name')
    username = request.POST.get('username')
    password = request.POST.get('password')
    email =  request.POST.get('email')
    now = strftime("%d-%m-%Y %H:%M:%S")
    if name == None or username == None or password == None or email == None:
        return JsonResponse({"message":"Fields can't be empty"},status=400)
    check_username = UserDetails.objects.filter(username=username)
    check_email = UserDetails.objects.filter(email=email)
    access_token = SHA256.new(username).hexdigest()
    if len(check_username) != 0:
        return JsonResponse({'message':'Username already exist choose different'},status=409)
    if len(check_email) != 0:
        return JsonResponse({'message':'Email already exist, please login'},status=409)
    try:
        creat_user = UserDetails.objects.create(
                name=name,
                username=username,
                email=email,
                password=password,
                token=access_token,
                signin_on=now,
                )
        return JsonResponse({
                                'message':'Signup Done',
                                'access_token':access_token
                            },status=200)
    except Exception as e:
        return JsonResponse({'message':e},status=500)

@csrf_exempt
def login(request):
    """Login Module """
    email = request.GET.get('email')
    password = request.GET.get('password')
    print email, password
    if email == 'anand' and password == 'anand123':
        return JsonResponse({'message':'Login Success'})
    else:
        return JsonResponse({'message':'Login Failed'}, status=401)
    # if username == None or password == None:
    #     return JsonResponse({"message":"Fields can't be empty"},status=400)
    # access_token = SHA256.new(username).hexdigest()
    # get_token = UserDetails.objects.filter(username=username,password=password)
    # if len(get_token) == 0:
    #     return JsonResponse({'message':'Invalid User'},status=401)
    # same_token = str(access_token) == str(get_token[0].token)
    # if same_token == True:
    #     return JsonResponse({'message':'Valid User'},status=200)
    # else:
    #     return JsonResponse({'message':'Invalid User'},status=401)

def change_password(request):
    return HttpResponse("Password Recovery Endpoint")
