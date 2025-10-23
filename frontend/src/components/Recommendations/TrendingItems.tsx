import React, { useEffect, useState } from 'react';
import { FashionTrend } from '../../types';
import { apiService } from '../../services/api';

const TrendingItems: React.FC = () => {
  const [trends, setTrends] = useState<FashionTrend[]>([]);
  const [loading, setLoading] = useState(true);
  const [selectedCategory, setSelectedCategory] = useState<string>('');

  useEffect(() => {
    loadTrends();
  }, [selectedCategory]);

  const loadTrends = async () => {
    try {
      setLoading(true);
      const data = await apiService.getTrendingItems(selectedCategory || undefined);
      setTrends(data);
    } catch (error) {
      console.error('Error loading trends:', error);
    } finally {
      setLoading(false);
    }
  };

  const categories = ['all', 'outerwear', 'tops', 'bottoms', 'shoes', 'accessories', 'general'];

  return (
    <div className="trending-items">
      <h2>Current Fashion Trends</h2>
      
      <div className="category-filters">
        {categories.map(category => (
          <button
            key={category}
            onClick={() => setSelectedCategory(category === 'all' ? '' : category)}
            className={`category-btn ${selectedCategory === category ? 'active' : ''}`}
          >
            {category}
          </button>
        ))}
      </div>

      {loading ? (
        <div className="loading">Loading trends...</div>
      ) : (
        <div className="trends-grid">
          {trends.map(trend => (
            <div key={trend.id} className="trend-card">
              <div className="trend-image">
                {trend.image_urls && trend.image_urls.length > 0 ? (
                  <img src={trend.image_urls[0]} alt={trend.title} />
                ) : (
                  <div className="image-placeholder">No Image</div>
                )}
              </div>
              <div className="trend-info">
                <h3>{trend.title}</h3>
                <p>{trend.description}</p>
                <div className="trend-meta">
                  <span className="category">{trend.category}</span>
                  <span className="season">{trend.season}</span>
                </div>
              </div>
            </div>
          ))}
        </div>
      )}
    </div>
  );
};

export default TrendingItems;