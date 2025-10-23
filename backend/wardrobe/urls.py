from django.urls import path
from . import views

urlpatterns = [
    path('items/', views.WardrobeItemsView.as_view(), name='wardrobe-items'),
    path('items/<uuid:item_id>/', views.WardrobeItemDetailView.as_view(), name='wardrobe-item-detail'),
    path('outfits/', views.OutfitsView.as_view(), name='outfits'),
]