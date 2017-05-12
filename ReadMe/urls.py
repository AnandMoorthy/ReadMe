from django.conf.urls import include, url
from django.contrib import admin
from readme_api.user_basics import signup,login
from readme_api.app import submit_link,get_links,test_links

urlpatterns = [
    # Examples:
    # url(r'^$', 'ReadMe.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/v0.0.1/user/signup$',signup),
    url(r'^api/v0.0.1/user/login$',login),
    url(r'^api/v0.0.1/user/submit_link$',submit_link),
    url(r'^api/v0.0.1/user/get_links$',get_links),
    url(r'^api/v0.0.1/user/test_links$',test_links),
]
