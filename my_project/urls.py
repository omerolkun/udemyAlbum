
from django.contrib import admin
from django.urls import path
from my_app import views
from my_app.views import AlbumsOgli, Musicians


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name="home page"),
    path('form/',views.form, name="form page"),
    path('musician_list/',Musicians.as_view(), name="musicianlist"),
    path('musician_list/<int:pk>', views.single_musician_detail, name = "detail page"),
    path('album_list/',AlbumsOgli.as_view(),name="albumlist"),
    path('addmusician',views.addMusician, name="addsinger"),
    path('addalbum/',views.addAlbum,name="addalbums"),
    path('details/',views.detailSinger, name="detailsingerpage"),
    path('details/<int:torlak_kemal>/',views.detailMusicianName,name="finaldetail"),
    path('musician_form/',views.musician_form,name="musician_form"),
    path('album_form/',views.album_form, name='album_form'),
    path('edit_artist/<int:pelkas_melkas>/',views.edit_artist,name='edit_artist_page'),
    path('edit_album/<int:album_id_omercik>',views.editAlbum,name='edit_album_page'),
    path('delete_album/<int:album_no>',views.deleteAlbum,name='delete_album_page'),
    path('detail_album/<int:album_detail_id>', views.detail_album,name='detail_album_page'),
    path('delete_artist/<int:singer_id>', views.deleteArtist, name='delete_artist_page'),

]
