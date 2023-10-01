from django.urls import path, include
from . import views
# from .views import UserRegistrationView, LoginView, LogoutView, SpecificItemsView,ItemViewSet
from .views import SpecificItemsView,ItemViewSet, CreateUserView, CustomAuthToken, UserProfileView
from rest_framework.routers import DefaultRouter

# router = DefaultRouter()
# router.register(r'items', ItemListingViewSet)
# router.register(r'allitems', GetAllItemsView)
# router.register(r'users/', UserProfileViewSet)
# router.register(r'register/', UserRegistrationView)
# router.register(r'login/', LoginView)
# router.register(r'logout/', LogoutView)




urlpatterns = [
    path('users/', views.UserProfileViewSet.as_view({'get': 'list', 'post': 'create'})),
    # path('register/', UserRegistrationView.as_view(), name='user-registration'),
    path('register/', CreateUserView.as_view(), name = "user-registration"),
    path('login/', CustomAuthToken.as_view(), name='login'),
    path('profile/', UserProfileView.as_view(), name='profile'),
    path('specificitems/', SpecificItemsView.as_view(), name='specificitems'),
    path('users/items/', ItemViewSet.as_view({'get': 'list', 'post': 'create'}),name='useritems'),


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