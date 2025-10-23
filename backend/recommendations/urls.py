from django.urls import path
from . import views

urlpatterns = [
    path('outfits/', views.OutfitRecommendationsView.as_view(), name='outfit-recommendations'),
    path('trending/', views.TrendingItemsView.as_view(), name='trending-items'),
    path('accessories/', views.AccessoryRecommendationsView.as_view(), name='accessory-recommendations'),
]