export interface FashionTrend {
  id: string;
  title: string;
  description: string;
  category: string;
  season: string;
  year: number;
  trend_data: any;
  image_urls: string[];
  created_at: string;
}

export interface WardrobeItem {
  id: string;
  user_id: string;
  name: string;
  category: string;
  subcategory?: string;
  color?: string;
  brand?: string;
  image_url?: string;
  tags: string[];
  season: string[];
  occasion: string[];
  created_at: string;
}

export interface OutfitRecommendation {
  name: string;
  items: string[];
  confidence_score: number;
  reason: string;
  items_details: any[];
}

export interface User {
  id: string;
  email: string;
  username?: string;
}