from django.urls import path, include
from .views import *
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'Api', UserViewSet)

router2 = routers.SimpleRouter()
router2.register(r'Api2', User2ViewSet)


urlpatterns = [
    path('Yuridik/', include(router.urls)),
    path('Jismoniy/', include(router2.urls)),
    path('Yuridik/<int:id>/', UserDetail.as_view()),
]