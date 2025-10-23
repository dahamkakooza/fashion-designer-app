from django.contrib import admin
from django.urls import path, include
from django.http import JsonResponse
from utils.simple_client import SimpleClient  # Use the simple test client

def api_root(request):
    return JsonResponse({
        'message': 'Fashion Designer API',
        'endpoints': {
            'test_connection': '/api/test-connection/',
            'trending': '/api/recommendations/trending/',
        },
        'status': 'running'
    })

def test_connection(request):
    """Test Supabase connection"""
    success, message = SimpleClient.test_connection()
    return JsonResponse({
        'success': success,
        'message': message
    })

# Start with minimal URLs
urlpatterns = [
    path('', api_root, name='api-root'),
    path('api/test-connection/', test_connection, name='test-connection'),
    path('api/recommendations/', include('recommendations.urls')),
    # Comment out other URLs temporarily
    # path('api/auth/', include('authentication.urls')),
    # path('api/wardrobe/', include('wardrobe.urls')),
]