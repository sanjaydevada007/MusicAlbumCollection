from django.conf.urls import url
from . import views

app_name= 'music'
# /music/
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),

    url(r'^register/$', views.UserFormView.as_view(), name='register'),

    #/music/71
    url(r'^(?P<pk>[0-9]+)/$',views.DetailView.as_view(), name='detail'),
    # music/album/add
    url(r'^album/add/$', views.AlbumCreate.as_view(),name= 'album-add'),


    # music/album/2/
    url(r'^album/(?P<pk>[0-9]+)/$', views.AlbumUpdate.as_view(),name= 'album-update'),


    # music/album/2/delete
    url(r'^album/(?P<pk>[0-9]+)/delete/$', views.AlbumDelete.as_view(),name= 'album-delete'),

    url(r'^(?P<album_id>[0-9]+)/create_song/$', views.song_form, name='create_song'),


    url(r'^(?P<album_id>[0-9]+)/delete_song/(?P<song_id>[0-9]+)/$', views.delete_song, name='delete_song'),
]



