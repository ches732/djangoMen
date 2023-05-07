from django.urls import path, include
from riddles import admin
from riddles.views import *
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'men', MenViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(router.urls)),
]
