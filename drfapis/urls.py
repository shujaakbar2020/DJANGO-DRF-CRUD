from django.urls import include, path
from django.contrib import admin
from rest_framework import routers
from quickstart.views import CreateBook, UserViewSet, GroupViewSet, BookViewSet, CreateBook

routers = routers.DefaultRouter()
routers.register(r'users', UserViewSet)
routers.register(r'groups', GroupViewSet)
routers.register(r'books', BookViewSet)
routers.register(r'create', CreateBook)

urlpatterns = [
    path('', include(routers.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('admin/', admin.site.urls),
]