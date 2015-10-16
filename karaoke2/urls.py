from django.conf.urls import include, url
from django.contrib import admin
from user_profileapp.views import Index

urlpatterns = [
    # Examples:
    # url(r'^$', 'karaoke2.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', Index.as_view()),
]
