from django.http import HttpResponse,HttpResponseRedirect,JsonResponse
from models import UserDetails,LinkDetails
from tools import check_token
from time import strftime
from bs4 import BeautifulSoup
import urllib2
import re
import json

def submit_link(request):
    access_token = request.GET.get('token')
    link = request.GET.get('link')
    if access_token == None or link == None:
        return JsonResponse({"message":"Fields Missing"},status=400)
    now = strftime("%d-%m-%Y %H:%M:%S")
    if check_token(access_token) is True:
        print link
        out = scrap_article(link)
        print out['title']
        get_user_id = UserDetails.objects.filter(token=access_token)
        insert_link = LinkDetails.objects.create(
                        url = link,
                        submitted_on = now,
                        user_id = get_user_id[0].id,
                        title = out['title'],
                        description = out['description'],
                        body = out['body'][0],
                        image_link = out['picture']
                        )
        return JsonResponse({'message':'Link Added'},status=200)
    else:
        return JsonResponse({'message':'Invalid user'},status=401)

def scrap_article(article_link):
    hdr = {'User-Agent': 'Mozilla/5.0'}
    req = urllib2.Request(article_link,headers=hdr)
    url_r = urllib2.urlopen(req)
    url_read = url_r.read()
    url_r.close()
    soup = BeautifulSoup(url_read,"lxml")
    title = soup.find("meta",  property="og:title")
    description = soup.find("meta",  property="og:description")
    thumbnail = soup.find("meta", property="og:image")
    body = soup.find_all(['p','a','h1','h2','h3','h4','h5','h6','code','pre'])
    if title is not None:
        title = title['content']
    else:
        title = "Title Not Found, Please Write Your own title to this article"
    if description is not None:
        description = description['content']
    else:
	       description = "Description Not Found, Please Write Your own Description to this article"
    if thumbnail is not None:
        picture = thumbnail['content']
    else:
        picture = "No Thumbnail, Please give a suitable thumbnail location to this article"
    article_details = {'title':title,'description':description,'picture':picture,'body':body}
    return article_details

def get_links(request):
    final_data = []
    access_token = request.GET.get('token')
    if access_token == None:
        return JsonResponse({"message":"Fields Missing"},status=400)
    if check_token(access_token) is True:
        get_user_id = UserDetails.objects.filter(token=access_token)
        get_link_details = LinkDetails.objects.filter(user_id=get_user_id)
        for data in get_link_details:
            link_data = {'link':data.url,'submitted_on':data.submitted_on}
            final_data.append(link_data)
    print final_data
    return JsonResponse(final_data,safe=False)

def test_links(request):
    link_details = []
    details = LinkDetails.objects.all()
    for data in details:
        obj = {
                'id':data.id,
                'title':data.title,
                'description':data.description,
                'body':data.body,
                'link':data.url,
                'image':data.image_link
                }
        link_details.append(obj)
    return JsonResponse(link_details,safe=False)
