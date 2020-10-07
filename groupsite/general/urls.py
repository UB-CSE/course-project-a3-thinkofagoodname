from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('download/', views.download, name='download'),
    path('project/', views.project, name='project'),
    path('sharing/', views.sharing, name='sharing'),
]

