from django.urls import path, include
from . import views
# from .views import UserRegistrationView, LoginView, LogoutView
from .views import GetAllItemsView
from rest_framework.routers import DefaultRouter






urlpatterns = [
    path('allitems/', GetAllItemsView.as_view(), name='allitems'),
    

    path('items/', views.ItemListingViewSet.as_view({'get': 'list', 'post': 'create'})),


    # path('login/', LoginView.as_view()),
    # path('logout/', LogoutView.as_view()),
    # path("", include(router.urls)),


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