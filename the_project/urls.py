from django.urls import include, path
from rest_framework import routers
from planetary_play import views

router = routers.DefaultRouter()
router.register(r'planetary_body', views.PlanetaryBodyViewSet)
router.register(r'planets', views.PlanetViewSet)


urlpatterns = [
    path('', include(router.urls)),
]
