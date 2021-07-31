
from django.contrib import admin
from django.urls import path
from my_app import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name="home page"),
    path('form/',views.form, name="form page"),
    path('musician_list/',views.musician_list, name="musicianlist"),
    path('musician_list/<int:pk>', views.single_musician_detail, name = "detail page"),
    path('albums/',views.albums,name="albumlist"),
]
