import requests
import json
from django.conf import settings
import logging

logger = logging.getLogger(__name__)

class SupabaseSimpleClient:
    @staticmethod
    def get_headers():
        """Get the required headers for Supabase API"""
        return {
            'apikey': settings.SUPABASE_KEY,
            'Authorization': f'Bearer {settings.SUPABASE_KEY}',
            'Content-Type': 'application/json',
            'Prefer': 'return=representation'
        }
    
    @staticmethod
    def make_request(table, method='GET', filters=None, data=None):
        """Make direct HTTP requests to Supabase"""
        if not settings.SUPABASE_URL or not settings.SUPABASE_KEY:
            raise ValueError("Supabase credentials not configured. Check your .env file.")
        
        # Remove trailing slash from URL if present
        base_url = settings.SUPABASE_URL.rstrip('/')
        url = f"{base_url}/rest/v1/{table}"
        
        headers = SupabaseSimpleClient.get_headers()
        params = {}
        
        # Build query parameters for filters
        if filters:
            for key, value in filters.items():
                params[key] = f'eq.{value}'
        
        try:
            if method == 'GET':
                response = requests.get(url, headers=headers, params=params)
            elif method == 'POST':
                response = requests.post(url, headers=headers, json=data, params=params)
            elif method == 'PUT':
                response = requests.put(url, headers=headers, json=data, params=params)
            elif method == 'DELETE':
                response = requests.delete(url, headers=headers, params=params)
            else:
                raise ValueError(f"Unsupported method: {method}")
            
            response.raise_for_status()
            
            # Return empty list for 204 No Content
            if response.status_code == 204:
                return []
                
            return response.json() if response.content else []
            
        except requests.exceptions.RequestException as e:
            logger.error(f"Supabase API error: {e}")
            if hasattr(e, 'response') and e.response is not None:
                logger.error(f"Response status: {e.response.status_code}")
                logger.error(f"Response content: {e.response.text}")
            raise
    
    @staticmethod
    def test_connection():
        """Test Supabase connection"""
        try:
            # Try to get a single trend item
            response = SupabaseSimpleClient.make_request('fashion_trends', 'GET')
            return True, f"Connection successful. Found {len(response)} trend items."
        except Exception as e:
            return False, f"Connection failed: {e}"