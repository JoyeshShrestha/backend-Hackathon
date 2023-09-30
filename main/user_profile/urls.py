from django.urls import path
from . import views
from .views import UserRegistrationView, LoginView, LogoutView

urlpatterns = [
    path('users/', views.UserProfileViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('register/', UserRegistrationView.as_view(), name='user-registration'),
    path('login/', LoginView.as_view()),
    path('logout/', LogoutView.as_view()),


    # Define other API endpoints here
]























# from .views import RegisterView, LoginView, UserView, LogoutView, ForgetView, otpPassword, ResetPassword
# urlpatterns = [
    # path("users",UserProfileViewSet.as_view(),name='users'),
    
    # path("register",RegisterView.as_view(), name='register'),
    # path("login",LoginView.as_view(),name='login'),
    # path("user",UserView.as_view()),
    # path("logout",LogoutView.as_view(),name='logout'),
    # path("forgetpassword",ForgetView.as_view()),
    # path("otppassword",otpPassword.as_view()),
    # path("resetpassword",ResetPassword.as_view()),








# ]