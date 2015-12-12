from django.conf.urls import include, url
from django.contrib import admin
from user_profileapp.views import Index, Login, Logout, Perfil, UserRedirect, Feed, MembrosView, MinhasGravacoes
from pambaleiro.views import PambaleiroRegistration
from django.conf import settings
from django.conf.urls.static import static
from musica_app.views import MusicaView


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
    url(r'feed/$', Feed.as_view()),
    url(r'musica/$',MusicaView.as_view()),
    url(r'membros/$', MembrosView.as_view()),
    url(r'minhasgravacoes/$', MinhasGravacoes.as_view()),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
