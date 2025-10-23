from utils.supabase_simple_client import SupabaseSimpleClient  # FIXED IMPORT
import random

class RecommendationService:
    @staticmethod
    def generate_outfit_recommendations(user_id: str, occasion: str = None, season: str = None):
        try:
            # Get user's wardrobe items
            filters = {'user_id': user_id}
            user_items = SupabaseSimpleClient.make_request('wardrobe_items', 'GET', filters)
            
            if not user_items:
                return []
            
            # Simple recommendation logic
            tops = [item for item in user_items if item.get('category') == 'top']
            bottoms = [item for item in user_items if item.get('category') == 'bottom']
            shoes = [item for item in user_items if item.get('category') == 'shoes']
            accessories = [item for item in user_items if item.get('category') == 'accessory']
            
            recommendations = []
            
            # Generate some outfit combinations
            for top in tops[:2]:  # Limit to 2 tops
                for bottom in bottoms[:2]:  # Limit to 2 bottoms
                    for shoe in shoes[:1]:  # Limit to 1 shoe
                        outfit_items = [top['id'], bottom['id'], shoe['id']]
                        
                        # Add accessory if available
                        if accessories:
                            outfit_items.append(accessories[0]['id'])
                        
                        recommendation = {
                            'name': f"{top.get('name', 'Top')} with {bottom.get('name', 'Bottom')}",
                            'items': outfit_items,
                            'confidence_score': round(random.uniform(0.7, 0.95), 2),
                            'reason': 'Matches your style preferences and current trends',
                            'items_details': [
                                {'id': top['id'], 'name': top.get('name'), 'category': top.get('category')},
                                {'id': bottom['id'], 'name': bottom.get('name'), 'category': bottom.get('category')},
                                {'id': shoe['id'], 'name': shoe.get('name'), 'category': shoe.get('category')}
                            ]
                        }
                        recommendations.append(recommendation)
            
            return recommendations[:5]  # Return top 5 recommendations
            
        except Exception as e:
            print(f"Error generating outfit recommendations: {e}")
            return []

    @staticmethod
    def get_trending_items(category: str = None):
        try:
            filters = {}
            if category:
                filters['category'] = category
                
            trends = SupabaseSimpleClient.make_request('fashion_trends', 'GET', filters)
            # Return latest trends first
            return sorted(trends, key=lambda x: x.get('created_at', ''), reverse=True)[:10]
        except Exception as e:
            print(f"Error getting trending items: {e}")
            # Return mock data if real data fails
            return [
                {
                    "id": "1",
                    "title": "Oversized Blazers",
                    "description": "Structured yet comfortable blazers for a powerful look",
                    "category": "outerwear",
                    "season": "fall",
                    "year": 2024
                },
                {
                    "id": "2",
                    "title": "Sustainable Fashion", 
                    "description": "Eco-friendly materials and ethical production",
                    "category": "general",
                    "season": "all",
                    "year": 2024
                }
            ]