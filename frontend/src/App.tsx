import React from 'react';
import { AuthProvider, useAuth } from './contexts/AuthContext';
import Header from './components/Layout/Header';
import TrendingItems from './components/Recommendations/TrendingItems';
import LoginForm from './components/Auth/LoginForm';
import './App.css';

const AppContent: React.FC = () => {
  const { user, loading } = useAuth();

  if (loading) {
    return <div className="loading">Loading...</div>;
  }

  return (
    <div className="App">
      <Header />
      <main className="main-content">
        {user ? (
          <div className="dashboard">
            <h1>Welcome to Your Fashion Dashboard</h1>
            <TrendingItems />
            {/* Add more components here */}
          </div>
        ) : (
          <div className="auth-container">
            <LoginForm />
          </div>
        )}
      </main>
    </div>
  );
};

function App() {
  return (
    <AuthProvider>
      <AppContent />
    </AuthProvider>
  );
}

export default App;