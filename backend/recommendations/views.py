from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from utils.supabase_simple_client import SupabaseSimpleClient  # FIXED IMPORT
from .services import RecommendationService
import logging

logger = logging.getLogger(__name__)

class TrendingItemsView(APIView):
    def get(self, request):
        try:
            category = request.GET.get('category')
            
            # Test connection first
            connection_ok, message = SupabaseSimpleClient.test_connection()  # FIXED: SupabaseClient -> SupabaseSimpleClient
            if not connection_ok:
                return Response(
                    {'error': f'Supabase connection failed: {message}'}, 
                    status=status.HTTP_500_INTERNAL_SERVER_ERROR
                )
            
            trends = RecommendationService.get_trending_items(category)
            return Response(trends)
            
        except Exception as e:
            logger.error(f"Error in TrendingItemsView: {e}")
            return Response(
                {'error': str(e)}, 
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

class OutfitRecommendationsView(APIView):
    def get(self, request):
        try:
            # For now, use a test user ID since we don't have auth set up yet
            user_id = "test-user-id"  # Temporary - replace with actual auth later
            
            # Test connection first
            connection_ok, message = SupabaseSimpleClient.test_connection()  # FIXED
            if not connection_ok:
                return Response(
                    {'error': f'Supabase connection failed: {message}'}, 
                    status=status.HTTP_500_INTERNAL_SERVER_ERROR
                )
            
            occasion = request.GET.get('occasion')
            season = request.GET.get('season')
            
            recommendations = RecommendationService.generate_outfit_recommendations(
                user_id, occasion, season
            )
            
            return Response(recommendations)
            
        except Exception as e:
            logger.error(f"Error in OutfitRecommendationsView: {e}")
            return Response(
                {'error': str(e)}, 
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

class AccessoryRecommendationsView(APIView):
    def get(self, request):
        try:
            # For now, use a test user ID
            user_id = "test-user-id"  # Temporary - replace with actual auth later
            
            # Test connection first
            connection_ok, message = SupabaseSimpleClient.test_connection()  # FIXED
            if not connection_ok:
                return Response(
                    {'error': f'Supabase connection failed: {message}'}, 
                    status=status.HTTP_500_INTERNAL_SERVER_ERROR
                )
            
            occasion = request.GET.get('occasion')
            recommendations = RecommendationService.get_accessory_recommendations(user_id, occasion)
            return Response(recommendations)
            
        except Exception as e:
            logger.error(f"Error in AccessoryRecommendationsView: {e}")
            return Response(
                {'error': str(e)}, 
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )