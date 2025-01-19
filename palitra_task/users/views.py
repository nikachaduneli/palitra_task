from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import UserRegisterSerializer, UserProfileSerializer, PasswordResetSerializer
from django.contrib.auth.tokens import default_token_generator
from .models import User
from .utils import send_activation_email, send_password_reset_email
from rest_framework.permissions import AllowAny
from django.utils.http import urlsafe_base64_decode
from rest_framework import status
from django.utils.encoding import force_str
from django.shortcuts import get_object_or_404
from drf_yasg.utils import swagger_auto_schema


class RegisterView(APIView):

    serializer_class = UserRegisterSerializer

    @swagger_auto_schema(request_body=serializer_class)
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            activation_url = send_activation_email(user, request)
            print(activation_url)
            return Response({"message": "Registration successful, please check your email to activate your account."}, status=201)
        return Response(serializer.errors, status=400)


class ActivateUser(APIView):
    permission_classes = [AllowAny]

    def get(self, request, uid, token, *args, **kwargs):
        try:
            uid = urlsafe_base64_decode(uid).decode()
            user = User.objects.get(pk=uid)
        except (TypeError, ValueError, OverflowError, User.DoesNotExist):
            return Response({'error': 'Invalid activation link.'}, status=400)

        if default_token_generator.check_token(user, token):
            user.is_active = True
            user.save()
            return Response({'message': 'Account activated successfully.'}, status=200)
        else:
            return Response({'error': 'Invalid or expired token.'}, status=400)


class OwnProfileView(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = UserProfileSerializer

    def get(self, request):
        user = request.user

        data = {
            'username': user.username,
            'email': user.email
        }

        if user.profile_image: data['profile_image'] = user.profile_image.url
        return Response(data)

    @swagger_auto_schema(request_body=serializer_class)
    def put(self, request):
        user = request.user
        serializer = self.serializer_class(instance=user, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Profile updated successfully'}, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class Profileview(APIView):
    def get(self, request, pk):
        user = get_object_or_404(User, pk=pk)
        data = {
            'username': user.username,
            'email': user.email
        }
        if user.profile_image: data['profile_image'] = user.profile_image.url
        return Response(data)


class PasswordResetRequestAPIView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        email = request.data.get('email')
        if not email:
            return Response({'error': 'Email is required.'}, status=status.HTTP_400_BAD_REQUEST)
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            return Response({'error': 'User with this email does not exist.'}, status=status.HTTP_404_NOT_FOUND)

        reset_link = send_password_reset_email(user, request)
        print(reset_link)

        return Response({'message': 'Password reset link sent to email.'}, status=status.HTTP_200_OK)


class PasswordResetAPIView(APIView):
    permission_classes = [AllowAny]
    serializer_class = PasswordResetSerializer


    @swagger_auto_schema(request_body=serializer_class)
    def post(self, request, uidb64, token):
        try:
            uid = force_str(urlsafe_base64_decode(uidb64))
            user = User.objects.get(pk=uid)
        except (TypeError, ValueError, OverflowError, User.DoesNotExist):
            return Response({'error': 'Invalid UID or token.'}, status=status.HTTP_400_BAD_REQUEST)

        if not default_token_generator.check_token(user, token):
            return Response({'error': 'Invalid or expired token.'}, status=status.HTTP_400_BAD_REQUEST)


        serializer = self.serializer_class(instance=user, data=request.data)
        if serializer.is_valid():
            serializer.save()

        return Response({'message': 'Password has been reset successfully.'}, status=status.HTTP_200_OK)
