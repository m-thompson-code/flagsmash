from django.conf.urls import patterns, include, url
from django.contrib import admin
from views.views import BracketList, BracketDetail
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'main.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', 'main.views.views.home', name = 'home'),
    url(r'^playerform/$', 'main.views.views.player_form', name = 'player_form'),
    url(r'^playermatchform/$', 'main.views.views.player_match_form', name = 'player_match_form'),
    url(r'^bracket/$', 'main.views.views.bracket', name = 'bracket'),
    url(r'^bracket_data/$', 'main.views.views.bracket_data', name = 'bracket_data'),
    url(r'^data/bracket/$', BracketList.as_view()),
    url(r'^data/bracket/(?P<pk>[0-9]+)/$', BracketDetail.as_view()),
    url(r'^player/(?P<id>\d+)/$', 'main.views.views.player_profile', name = 'player_profile'),
    url(r'^admin/', include(admin.site.urls)),
)