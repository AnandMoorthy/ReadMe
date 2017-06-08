""" Main app code """
from time import strftime
# import urllib2
from django.http import JsonResponse
# from bs4 import BeautifulSoup
from readme_api.models import UserDetails, LinkDetails
from readme_api.tools import check_token
from readme_api.spider import scraper

def submit_link(request):
    """ Submit a new link """
    access_token = request.GET.get('token')
    link = request.GET.get('link')
    user_id = request.GET.get('user_id')
    platform = request.GET.get('platform')
    print access_token, link, user_id, platform
    if None in (access_token, link, platform, user_id):
        return JsonResponse({"message":"Fields Missing"}, status=400)
    now = strftime("%d-%m-%Y %H:%M:%S")
    if check_token(access_token, user_id, platform) is True:
        out = scraper(link)
        if platform == 'android':
            get_user_id = UserDetails.objects.filter(
                android_token=access_token,
                id=user_id
                )
        if platform == 'ios':
            get_user_id = UserDetails.objects.filter(
                ios_token=access_token,
                user_id=user_id
                )
        if platform == 'desktop':
            get_user_id = UserDetails.objects.filter(
                desktop_token=access_token,
                user_id=user_id
                )
        # get_user_id = UserDetails.objects.filter(token=access_token)
        #d = out['body'].encode('utf-8')
        LinkDetails.objects.create(
            url=link,
            submitted_on=now,
            user_id=get_user_id[0].id,
            title=out['title'],
            description=out['description'],
            image=out['picture'],
            body=out['body']
        )
        return JsonResponse({'message':'Link Added'}, status=200)
    else:
        return JsonResponse({'message':'Invalid user'}, status=401)

# def scrap_article(article_link):
#     """ Scrap Articles """
#     hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
#            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#            'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
#            'Accept-Encoding': 'none',
#            'Accept-Language': 'en-US,en;q=0.8',
#            'Connection': 'keep-alive'
#           }
#     req = urllib2.Request(article_link, headers=hdr)
#     url_r = urllib2.urlopen(req)
#     url_read = url_r.read()
#     url_r.close()
#     soup = BeautifulSoup(url_read, "lxml")
#     title = soup.find("meta", property="og:title")
#     description = soup.find("meta", property="og:description")
#     thumbnail = soup.find("meta", property="og:image")
#     title1 = soup.find("title").text
#     print "Title One"
#     print title1
#     # body = soup.find_all(['p', 'a', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'code', 'pre'])
#     if title is not None:
#         title = title['content']
#     else:
#         title = title1
#     if description is not None:
#         description = description['content']
#     else:
#         description = ""
#     if thumbnail is not None:
#         picture = thumbnail['content']
#     else:
#         picture = """
#             http://robcataniaphotography.com/wp-content/themes/invictus/images/dummy-image.jpg
#             """
#     article_details = {
#         'title':title,
#         'description':description,
#         'picture':picture
#         }
#     return article_details

def return_list_of_links(request):
    """ This module will return list of links user stored """
    final_data = []
    access_token = request.GET.get('token')
    platform = request.GET.get('platform')
    user_id = request.GET.get('user_id')
    if None in (access_token, platform, user_id):
        return JsonResponse({"message":"Fields Missing"}, status=400)
    if check_token(access_token, user_id, platform) is True:
        if platform == 'android':
            get_user_id = UserDetails.objects.filter(
                android_token=access_token,
                id=user_id
                )
        if platform == 'ios':
            get_user_id = UserDetails.objects.filter(
                ios_token=access_token,
                id=user_id
                )
        if platform == 'ios':
            get_user_id = UserDetails.objects.filter(
                desktop_token=access_token,
                id=user_id
                )
        get_link_details = LinkDetails.objects.filter(
            user_id=get_user_id[0].id
            ).order_by('-id')
        for data in get_link_details:
            link_data = {
                'id':data.id,
                'link':data.url,
                'submitted_on':data.submitted_on,
                'user_id':data.user_id,
                'title':data.title,
                'description':data.description,
                'image':data.image,
                'body':data.body
                }
            final_data.append(link_data)
        return JsonResponse(final_data, safe=False)
    else:
        return JsonResponse(
            {
                "message":"Invalid User"
            },
            status=409
        )

def delete_link(request):
    """ This module will delete a particular link"""
    platform = request.GET.get('platform')
    token = request.GET.get('token')
    user_id = request.GET.get('user_id')
    link_id = request.GET.get('link_id')
    # print platform,token,link_id
    if None in (platform, token, link_id, user_id):
        return JsonResponse({"message":"Fields Missing"}, status=400)
    if check_token(token, user_id, platform) is True:
        #print 'Delete Process currently skipped'
        LinkDetails.objects.filter(id=link_id).delete()
        return JsonResponse(
            {
                "message": "Deletion Success"
            },
            status=200
        )
    else:
        return JsonResponse(
            {
                "message":"Invalid User"
            },
            status=409
        )
