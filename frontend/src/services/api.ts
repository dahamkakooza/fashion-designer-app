import axios from 'axios';
import { FashionTrend, OutfitRecommendation, WardrobeItem } from '../types';

// For Create React App
const API_BASE_URL = process.env.REACT_APP_API_BASE_URL || 'http://localhost:8000/api';

const api = axios.create({
  baseURL: API_BASE_URL,
  headers: {
    'Content-Type': 'application/json',
  },
});

// Add auth token to requests
api.interceptors.request.use((config) => {
  const token = localStorage.getItem('access_token');
  if (token) {
    config.headers.Authorization = `Bearer ${token}`;
  }
  return config;
});

export const apiService = {
  // Trends
  getTrendingItems: async (category?: string): Promise<FashionTrend[]> => {
    const params = category ? { category } : {};
    const response = await api.get('/recommendations/trending/', { params });
    return response.data;
  },

  // Recommendations
  getOutfitRecommendations: async (occasion?: string, season?: string): Promise<OutfitRecommendation[]> => {
    const params: any = {};
    if (occasion) params.occasion = occasion;
    if (season) params.season = season;
    
    const response = await api.get('/recommendations/outfits/', { params });
    return response.data;
  },

  getAccessoryRecommendations: async (occasion?: string): Promise<any[]> => {
    const params = occasion ? { occasion } : {};
    const response = await api.get('/recommendations/accessories/', { params });
    return response.data;
  },

  // Wardrobe
  getWardrobeItems: async (): Promise<WardrobeItem[]> => {
    const response = await api.get('/wardrobe/items/');
    return response.data;
  },

  addWardrobeItem: async (item: Partial<WardrobeItem>): Promise<WardrobeItem> => {
    const response = await api.post('/wardrobe/items/', item);
    return response.data;
  },

  // Auth
  signUp: async (email: string, password: string, username: string, fullName?: string) => {
    const response = await api.post('/auth/signup/', {
      email,
      password,
      username,
      full_name: fullName,
    });
    return response.data;
  },

  login: async (email: string, password: string) => {
    const response = await api.post('/auth/login/', {
      email,
      password,
    });
    return response.data;
  },

  logout: async () => {
    const response = await api.post('/auth/logout/');
    return response.data;
  },

  getProfile: async () => {
    const response = await api.get('/auth/profile/');
    return response.data;
  },
};

export default api;