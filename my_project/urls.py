
from django.contrib import admin
from django.urls import path
from my_app import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name="home page"),
    path('form/',views.form, name="form page"),
]
