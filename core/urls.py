from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
from django.urls import path, include

from rest_framework import routers

from resize_app import views

router = routers.DefaultRouter()
router.register(r'create/task', views.CreateTaskAPI, basename='create')


urlpatterns = [
    path('api/', include(router.urls)),
    path('api/get/<uuid:pk>/', views.GetStatusAPI.as_view()),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
