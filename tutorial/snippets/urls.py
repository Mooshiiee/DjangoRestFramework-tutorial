from django.urls import path, include
from rest_framework.routers import DefaultRouter

from snippets import views

router = DefaultRouter()
router.register(r'snippets', views.SnippetViewSet, basename='snippet')
router.register(r'users', views.UserViewSet, basename='user')

#an addition to handle all URL suffixes such as .json .xml .whateveryourheartdesires
urlpatterns = [
    path('', include(router.urls))
]