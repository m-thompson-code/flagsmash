from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'main.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', 'main.views.views.home', name = 'home'),
    url(r'^playerform/$', 'main.views.views.player_form', name = 'player_form'),
    url(r'^ranking/$', 'main.views.views.ranking', name = 'ranking'),
    url(r'^tournaments/$', 'main.views.views.tournaments', name = 'tournaments'),
    url(r'^tournaments/(?P<id>[\w-]+)/$', 'main.views.views.tournament_details', name = 'tournament_details'),
    url(r'^player/(?P<name>[\w-]+)/$', 'main.views.views.player_profile', name = 'player_profile'),
    url(r'^admin/', include(admin.site.urls)),
)