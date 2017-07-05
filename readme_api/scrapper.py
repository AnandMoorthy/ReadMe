from newspaper import Article
from django.http import HttpResponse, JsonResponse


def spider(request):
    link = request.GET.get('link')
    if link is None or link == "":
        return JsonResponse({"message":"Link field can't be empty"}, status=401)
    article =  Article(link)
    article.download()
    article.parse()
    article_details = {
        "title": article.title,
        "cover": article.top_image,
        "body": article.text,
        "summary": article.text[:100]+"..."
    }
    return JsonResponse(article_details)
