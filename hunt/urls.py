from django.conf.urls import url
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
        url(r'^$', views.index, name="index"),
        url(r'^logout/?$', auth_views.logout, {'next_page':'login'}, name="logout"),
        url(r'^login/?$', auth_views.login, name="login"),
        url(r'^signup/?$', views.signup, name="signup"),
        url(r'^base/?$', views.base, name="base"),
        #url(r'^leaderboard/?$', views.leaderboard, name="leaderboard"),
        url(r'^play/?$', views.play, name="play"),
        url(r'^level/(?P<level_number>\d+)/?$', views.level, name="level"),
        url(r'^rules/?$',views.rules, name="rules"),
        url(r'^userdetails/?$',views.userdetails, name="userdetails"),
        url(r'^demo/?$',views.index, name="index"),
]
