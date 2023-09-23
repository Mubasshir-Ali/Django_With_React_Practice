from . import views
# from django.urls import path
from django.urls import path, include, re_path
from .views import UserRegistrationView, UserLoginView, UserProfileView, UserChangePasswordView, SendPasswordResetEmailView, UserPasswordResetView #ProgramView #, InstituteView, DepartmentView, EmployeesView  
from .views import UserListView
from django.conf.urls.static import static
# from django.conf.urls import url
from django.conf import settings
from rest_framework.routers import DefaultRouter
from rest_framework import routers

# router = routers.DefaultRouter()
 
urlpatterns = [
    # path('api/', include(router.urls)),
    # path("", views.home, name="home"),
    # path('', include(router.urls)),
    path('user-list-view/', UserListView.as_view(), name="user-list-view"),
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('profile/', UserProfileView.as_view(), name='profile'),
    path('changepassword/', UserChangePasswordView.as_view(), name='changepassword'),
    path('send-reset-password-email/', SendPasswordResetEmailView.as_view(), name='send-reset-password-email'),
    path('reset-password/<uid>/<token>/', UserPasswordResetView.as_view(), name='reset-password'),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)