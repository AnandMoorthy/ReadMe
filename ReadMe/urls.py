""" Basic URL of Apps"""
from django.conf.urls import include, url
from django.contrib import admin
from readme_api.user_basics import signup, signin, forgot_password_handler, signout, check_user
from readme_api.app import submit_link, return_list_of_links, delete_link
from readme_api.spider import scraper

urlpatterns = [
    # Examples:
    # url(r'^$', 'ReadMe.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/v0.0.1/user/signup$', signup),
    url(r'^api/v0.0.1/user/login$', signin),
    url(r'^api/v0.0.1/user/signout$', signout),
    url(r'^api/v0.0.1/user/verify$', check_user),
    url(r'^api/v0.0.1/user/link/add$', submit_link),
    url(r'^api/v0.0.1/user/links$', return_list_of_links),
    url(r'^api/v0.0.1/user/link/delete$', delete_link),
    url(r'^api/v0.0.1/user/reset/password$', forgot_password_handler),
    url(r'^api/v0.0.1/user/scraper$', scraper),

]
