from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import requests
from django.conf import settings
from utils.supabase_simple_client import SupabaseSimpleClient

class SignUpView(APIView):
    def post(self, request):
        try:
            email = request.data.get('email')
            password = request.data.get('password')
            username = request.data.get('username')
            full_name = request.data.get('full_name')
            
            if not email or not password:
                return Response(
                    {'error': 'Email and password are required'}, 
                    status=status.HTTP_400_BAD_REQUEST
                )
            
            # Use Supabase auth API directly
            auth_url = f"{settings.SUPABASE_URL}/auth/v1/signup"
            headers = {
                'apikey': settings.SUPABASE_KEY,
                'Content-Type': 'application/json',
            }
            
            data = {
                'email': email,
                'password': password,
                'data': {
                    'username': username,
                    'full_name': full_name
                }
            }
            
            response = requests.post(auth_url, headers=headers, json=data)
            
            if response.status_code == 200:
                auth_data = response.json()
                return Response({
                    'message': 'User created successfully',
                    'user_id': auth_data.get('user', {}).get('id'),
                    'email': auth_data.get('user', {}).get('email')
                }, status=status.HTTP_201_CREATED)
            else:
                return Response(
                    {'error': response.json().get('msg', 'Failed to create user')}, 
                    status=status.HTTP_400_BAD_REQUEST
                )
                
        except Exception as e:
            return Response(
                {'error': str(e)}, 
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

class LoginView(APIView):
    def post(self, request):
        try:
            email = request.data.get('email')
            password = request.data.get('password')
            
            if not email or not password:
                return Response(
                    {'error': 'Email and password are required'}, 
                    status=status.HTTP_400_BAD_REQUEST
                )
            
            # Use Supabase auth API directly
            auth_url = f"{settings.SUPABASE_URL}/auth/v1/token?grant_type=password"
            headers = {
                'apikey': settings.SUPABASE_KEY,
                'Content-Type': 'application/json',
            }
            
            data = {
                'email': email,
                'password': password
            }
            
            response = requests.post(auth_url, headers=headers, json=data)
            
            if response.status_code == 200:
                auth_data = response.json()
                return Response({
                    'message': 'Login successful',
                    'access_token': auth_data.get('access_token'),
                    'user': {
                        'id': auth_data.get('user', {}).get('id'),
                        'email': auth_data.get('user', {}).get('email'),
                    }
                }, status=status.HTTP_200_OK)
            else:
                return Response(
                    {'error': 'Invalid credentials'}, 
                    status=status.HTTP_401_UNAUTHORIZED
                )
                
        except Exception as e:
            return Response(
                {'error': str(e)}, 
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

class LogoutView(APIView):
    def post(self, request):
        try:
            # For Supabase, logout is typically handled on the client side
            # But we can invalidate the token if needed
            return Response({'message': 'Logged out successfully'})
        except Exception as e:
            return Response(
                {'error': str(e)}, 
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

class ProfileView(APIView):
    def get(self, request):
        try:
            # Get user ID from token (simplified for now)
            auth_header = request.headers.get('Authorization')
            if not auth_header or not auth_header.startswith('Bearer '):
                return Response({'error': 'Unauthorized'}, status=status.HTTP_401_UNAUTHORIZED)
            
            token = auth_header.split(' ')[1]
            
            # Get user profile from Supabase
            auth_url = f"{settings.SUPABASE_URL}/auth/v1/user"
            headers = {
                'apikey': settings.SUPABASE_KEY,
                'Authorization': f'Bearer {token}',
            }
            
            response = requests.get(auth_url, headers=headers)
            
            if response.status_code == 200:
                user_data = response.json()
                
                # Get additional profile data from profiles table
                user_id = user_data.get('id')
                if user_id:
                    try:
                        profile_data = SupabaseSimpleClient.make_request(
                            'profiles', 
                            'GET', 
                            {'id': user_id}
                        )
                        if profile_data:
                            user_data['profile'] = profile_data[0]
                    except:
                        # If profile doesn't exist yet, that's ok
                        pass
                
                return Response(user_data)
            else:
                return Response(
                    {'error': 'Invalid token'}, 
                    status=status.HTTP_401_UNAUTHORIZED
                )
                
        except Exception as e:
            return Response(
                {'error': str(e)}, 
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )