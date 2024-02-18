from django.contrib import admin
from django.urls import path
from rest_framework import routers

from store.views import BookViewSet

router = routers.DefaultRouter()
router.register(r'books', BookViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
]

urlpatterns += router.urls
