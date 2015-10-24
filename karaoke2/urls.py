from django.conf.urls import include, url
from django.contrib import admin
from user_profileapp.views import Index, Login, Logout, Perfil, UserRedirect
from pambaleiro.views import PambaleiroRegistration

'''
urlpatterns = [
    # Examples:
    # url(r'^$', 'karaoke2.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', Index.as_view()),
    url(r'login/$',  Login.as_view()),
    url(r'logout/$', Logout.as_view()),
    url(r'perfil/$', Perfil.as_view()),
    url(r'profile/$', UserRedirect.as_view())
]
'''
urlpatterns = [
    # Examples:
    # url(r'^$', 'karaoke2.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', Index.as_view()),
    url(r'login/$',  Login.as_view()),
    url(r'logout/$', Logout.as_view()),
    url(r'perfil/$', Perfil.as_view()),
    url(r'profile/$', UserRedirect.as_view()),
    url(r'register/$', PambaleiroRegistration.as_view()),
]
