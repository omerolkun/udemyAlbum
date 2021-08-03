
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

]
