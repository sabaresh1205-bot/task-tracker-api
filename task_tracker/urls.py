from django.contrib import admin
from django.urls import include, path
from users.views import RegisterView
from rest_framework_simplejwt.views import TokenObtainPairView

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('', include('tasks.urls')),
    
    path('auth/register/', RegisterView.as_view()),
    path('auth/login/', TokenObtainPairView.as_view()),
    
    path('', include('users.urls')),
    path('', include('tasks.urls')),
]
