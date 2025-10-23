from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from utils.supabase_simple_client import SupabaseSimpleClient  # FIXED IMPORT

class WardrobeItemsView(APIView):
    def get(self, request):
        try:
            # Simplified for now - in real app, get user_id from token
            user_id = "test-user-id"  # Temporary
            filters = {'user_id': user_id}
            items = SupabaseSimpleClient.make_request('wardrobe_items', 'GET', filters)
            return Response(items)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    def post(self, request):
        try:
            user_id = "test-user-id"  # Temporary
            item_data = {
                'user_id': user_id,
                'name': request.data.get('name'),
                'category': request.data.get('category'),
                'subcategory': request.data.get('subcategory'),
                'color': request.data.get('color'),
                'brand': request.data.get('brand'),
                'image_url': request.data.get('image_url'),
                'tags': request.data.get('tags', []),
                'season': request.data.get('season', []),
                'occasion': request.data.get('occasion', [])
            }
            
            if not item_data['name'] or not item_data['category']:
                return Response(
                    {'error': 'Name and category are required'}, 
                    status=status.HTTP_400_BAD_REQUEST
                )
            
            created_item = SupabaseSimpleClient.make_request('wardrobe_items', 'POST', data=item_data)
            return Response(created_item[0] if created_item else {}, status=status.HTTP_201_CREATED)
                
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class WardrobeItemDetailView(APIView):
    def get(self, request, item_id):
        try:
            items = SupabaseSimpleClient.make_request('wardrobe_items', 'GET', {'id': item_id})
            if items:
                return Response(items[0])
            return Response({'error': 'Item not found'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class OutfitsView(APIView):
    def get(self, request):
        try:
            user_id = "test-user-id"  # Temporary
            filters = {'user_id': user_id}
            outfits = SupabaseSimpleClient.make_request('outfits', 'GET', filters)
            return Response(outfits)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    def post(self, request):
        try:
            user_id = "test-user-id"  # Temporary
            outfit_data = {
                'user_id': user_id,
                'name': request.data.get('name'),
                'description': request.data.get('description'),
                'items': request.data.get('items', []),
                'occasion': request.data.get('occasion'),
                'season': request.data.get('season'),
                'rating': request.data.get('rating'),
                'image_url': request.data.get('image_url'),
            }
            
            if not outfit_data['name']:
                return Response(
                    {'error': 'Outfit name is required'}, 
                    status=status.HTTP_400_BAD_REQUEST
                )
            
            created_outfit = SupabaseSimpleClient.make_request('outfits', 'POST', data=outfit_data)
            return Response(created_outfit[0] if created_outfit else {}, status=status.HTTP_201_CREATED)
                
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)