""" Spider to scrap all the content """
import urllib2
from bs4 import BeautifulSoup
from django.http import JsonResponse
import validators

hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
       'Accept-Encoding': 'none',
       'Accept-Language': 'en-US,en;q=0.8',
       'Connection': 'keep-alive'
      }


def scraper(link):
    """ This module will scrap the content from the link"""
    # link = request.GET.get('link')
    if link is None:
        return JsonResponse({"message":"Fields can't be empty"}, status=400)
    link = link.encode('utf-8')
    req = urllib2.Request(link, headers=hdr)
    print "Link from Scraper"
    print link
    url_r = urllib2.urlopen(req)
    scrapped_data = url_r.read()
    url_r.close()
    soup = BeautifulSoup(scrapped_data, "lxml")
    title = soup.find("meta", property="og:title")
    description = soup.find("meta", property="og:description")
    thumbnail = soup.find("meta", property="og:image")
    title1 = soup.find("title").text
    article_body = ""
    body = soup.find_all(['p', 'a', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'code', 'pre'])
    for details in body:
        article_body += str(details)
    if title is not None:
        title = title['content']
    else:
        title = title1
    if description is not None:
        description = description['content']
    else:
        description = ""
    if thumbnail is not None:
        picture = thumbnail['content']
        #validators.url(thumbnail['content'])
        if not validators.url(thumbnail['content']):
            picture = 'http://robcataniaphotography.com/wp-content/themes/invictus/images/dummy-image.jpg'
    else:
        picture = 'http://robcataniaphotography.com/wp-content/themes/invictus/images/dummy-image.jpg'
    article_details = {
        'title':title,
        'description':description,
        'picture':picture,
        'body':article_body
        }
    return article_details

# def scrap_article(article_link):
#     """ Scrap Articles """
#     req = urllib2.Request(article_link, headers=hdr)
#     url_r = urllib2.urlopen(req)
#     url_read = url_r.read()
#     url_r.close()
#     soup = BeautifulSoup(url_read, "lxml")
#     title = soup.find("meta", property="og:title")
#     description = soup.find("meta", property="og:description")
#     thumbnail = soup.find("meta", property="og:image")
#     title1 = soup.find("title").text
#     body = soup.find_all(['p', 'a', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'code', 'pre'])
#     open_file = open('temp.html', 'w')
#     for b in body:
#         open_file.write(str(b))
#     open_file.close()
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
#
# scrap_article('https://www.thepolyglotdeveloper.com/2015/09/saving-data-in-your-react-native-mobile-application/')
