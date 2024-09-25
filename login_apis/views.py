from django.shortcuts import render
from django.http import JsonResponse,HttpResponse
from rest_framework import generics
from rest_framework.decorators import api_view
from .serializer import Users_models_serializer,CustomTokenObtainPairSerializer,CustomUserSerializer
from rest_framework.parsers import JSONParser
from .models import users
import bcrypt
from rest_framework_simplejwt.tokens import RefreshToken,UntypedToken,AccessToken
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView
# Create your views here.
class register_users(generics.ListCreateAPIView):
    queryset=users.objects.all()
    serializer_class=Users_models_serializer
@api_view(["POST"])
def register_user(request):
    if request.method == "POST":
        
        existing_user_check=users.objects.filter(username=request.data["username"])

        if existing_user_check:
            return Response("user already register")
            
        else:
            password=request.data.get("password")
        
            request.data["password"]=hash_password(password)
     
            serializer = Users_models_serializer(data=request.data)
            if serializer.is_valid():
                user_instance = serializer.save()  
                token = AccessToken.for_user(user_instance)
                refresh = RefreshToken.for_user(user_instance) 
                return Response({
                
                'token': str(token),
                'refresh_token':str(refresh)  
            })
            else:
                return Response(serializer.errors, status=400)
@api_view(["POST"])
def checktoken(request):
    print(request.headers)
    auth_header = request.headers.get('Authorization')
    print(auth_header)
    print(auth_header.startswith('Bearer '))
    if auth_header :
        print(auth_header)
        token = auth_header.split(' ')[1].strip()
        token=token[0:-1]
        access_token = AccessToken(token)
        user_id = access_token['user_id']
        print(user_id,user_id)
        user=users.objects.filter(id=user_id).first()
        if user:
            serializer=Users_models_serializer(user)
            return True
        else:
            return False    
    else:
        return Response({'error': 'Token not provided'}, status=400)
class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer
@api_view(["POST"])
def login(request):
    check_name = request.data.get("user_name")
    gmail_user=request.data.get("user_name")
    check_email = request.data.get("email")   
    plain_password = request.data.get("password") 

    # Find the user by username or email
    user_instance = users.objects.filter(username=check_name).first()

    if user_instance:
        
        hashed_password = user_instance.password
        check_password = check_passwords(plain_password, hashed_password)

        if check_password:
            # Pass the actual user instance, not the serialized data
            serializer = CustomUserSerializer(user_instance)
            token = AccessToken.for_user(user_instance)
            refresh = RefreshToken.for_user(user_instance)
            with open('templates\email.html','r') as email:
                      data=email.read()
                      print(gmail_user)
                      data=data.replace("user_name",gmail_user)
                      print(data)
            send_custom_email("Congratulations! You've Successfully Logged In!",message=data,recipient_list=[check_email])

            return Response({
                'token': str(token),
                'refresh_token': str(refresh),
                'user_data': serializer.data
            })
        else:
            return Response({"error": "Invalid credentials"}, status=400)
    else:
        return Response({"error": "User not found"}, status=404)
 
def hash_password(password: str) -> str:
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed.decode('utf-8')
def check_passwords(plain_password: str, hashed_password: str) -> bool:
    return bcrypt.checkpw(plain_password.encode('utf-8'), hashed_password.encode('utf-8'))
from django.core.mail import send_mail
from django.conf import settings
from django.core.mail import EmailMultiAlternatives

def send_custom_email(subject,message,recipient_list):
        print("called",recipient_list)
        email_subject = subject
        email_message = message
        email_recipient_list = recipient_list
        from_email = settings.DEFAULT_FROM_EMAIL  # or you can manually specify

        msg = EmailMultiAlternatives(subject, email_message, from_email, email_recipient_list)
        msg.attach_alternative(email_message, "text/html")
        msg.send()


          
          
          











    