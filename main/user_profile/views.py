# views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
import jwt, datetime
from rest_framework import viewsets
from .models import UserProfile
from .serializers import UserProfileSerializer
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.hashers import make_password
import bcrypt

from django.contrib.auth.hashers import check_password
from items_listing.models import ItemListing
from items_listing.serializers import ItemListingSerializer
from items_listing.models import ItemListing
from items_listing.serializers import ItemListingSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action

class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer


# class UserRegistrationView(APIView):
#     def post(self, request):
#         serializer = UserProfileSerializer(data=request.data)

#         if serializer.is_valid():
#             # Create a new user profile
#             user = serializer.save()
#             plain_password = request.data['password']
            
#             # Hash the password using bcrypt
#             hashed_password = bcrypt.hashpw(plain_password.encode('utf-8'), bcrypt.gensalt())

#             user.password = hashed_password.decode('utf-8')  # Store the hashed password in the user model
#             user.save()
#             # You may want to add additional logic here, such as sending a confirmation email

#             return Response({"message": "User registered successfully."}, status=status.HTTP_201_CREATED)

#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
from rest_framework import generics, permissions
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from .serializers import UserSerializer

class CreateUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = [
        permissions.AllowAny  # Allow anyone to register
    ]
    serializer_class = UserSerializer

class CustomAuthToken(ObtainAuthToken):
    # Use custom authentication view if needed
    pass

class UserProfileView(generics.RetrieveUpdateAPIView):
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user

# class LoginView(APIView):
#     def post(self,request):
#         email = request.data['email']
#         entered_password = request.data['password']

#         user = UserProfile.objects.filter(email=email).first()

#         if user is None:
#             raise AuthenticationFailed('User not found!')
        
#         if bcrypt.checkpw(entered_password.encode("utf-8"), user.password.encode("utf-8")):
#             payload = {
#                 'id': user.id,
#                 'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
#                 'iat': datetime.datetime.utcnow()
#             }

#             token = jwt.encode(payload, 'secret', algorithm='HS256')
#             decoded_payload = jwt.decode(token, 'secret', algorithms=['HS256'])
#             print(decoded_payload)
          
#             response = Response()
#             response.set_cookie(key='jwt', value=token, httponly=True)
#             response.data = {
#                 'message': decoded_payload, 
#             }

#             return response

#         raise AuthenticationFailed('Incorrect password!')
# class LogoutView(APIView):
#     def post(self,request):
#         response = Response()
        
#         response.delete_cookie('jwt')
#         response.data = {
#             'message' : 'successfully logged out!'
#         }
#         return response               
    

class SpecificItemsView(APIView):
    def get(self, request):
        token = request.COOKIES.get('jwt')
        if token is None:
            raise AuthenticationFailed('Unauthenticated!')
        print (token)
        try:
            decoded_payload = jwt.decode(token, 'secret', algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Token has expired')
        except jwt.DecodeError as e:
            # Print or log the error message for debugging purposes
            print(f"Token decode error: {e}")
            raise AuthenticationFailed(f'Token is invalid')

        user_id = decoded_payload.get('id')
        items = ItemListing.objects.filter(owner_id=user_id)
        serializer = ItemListingSerializer(items, many=True)
        return Response(serializer.data)    
    
class ItemViewSet(viewsets.ModelViewSet):
    queryset = ItemListing.objects.all()
    serializer_class = ItemListingSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(owner=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, pk=None):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def perform_destroy(self, instance):
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    @action(detail=False, methods=['GET'])
    def user_items(self, request):
        user_id = request.user.id
        items = ItemListing.objects.filter(owner_id=user_id)
        serializer = ItemListingSerializer(items, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['GET'])
    def specific_item(self, request, pk=None):
        try:
            item = ItemListing.objects.get(id=pk, owner=request.user)
        except ItemListing.DoesNotExist:
            raise AuthenticationFailed('Item not found for this user')
        
        serializer = ItemListingSerializer(item)
        return Response(serializer.data)

def token_check(request):
    token = request.COOKIES.get('jwt')
    if token is None:
        raise AuthenticationFailed('Unauthenticated!')
    print (token)
    try:
        decoded_payload = jwt.decode(token, 'secret', algorithms='HS256')
    except jwt.ExpiredSignatureError:
        raise AuthenticationFailed('Token has expired')
    except jwt.DecodeError as e:
            # Print or log the error message for debugging purposes
        print(f"Token decode error: {e}")
        raise AuthenticationFailed('Token is invalid')

    user_id = decoded_payload.get('id')
    items = ItemListing.objects.filter(owner_id=user_id)
    return items