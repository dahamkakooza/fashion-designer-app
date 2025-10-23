import requests
from django.conf import settings

class SimpleClient:
    @staticmethod
    def test_connection():
        try:
            if not settings.SUPABASE_URL or not settings.SUPABASE_KEY:
                return False, "Missing Supabase credentials"
            
            url = f"{settings.SUPABASE_URL}/rest/v1/fashion_trends"
            headers = {
                'apikey': settings.SUPABASE_KEY,
                'Authorization': f'Bearer {settings.SUPABASE_KEY}',
            }
            
            response = requests.get(url, headers=headers, params={'limit': '1'})
            if response.status_code == 200:
                return True, "Connection successful"
            else:
                return False, f"HTTP {response.status_code}: {response.text}"
        except Exception as e:
            return False, f"Error: {e}"