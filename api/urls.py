from django.conf.urls import url, include

from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register('main', views.MainViewSet)


urlpatterns = [
    url(r'', include(router.urls))
]