import React from 'react';
import { useAuth } from '../../contexts/AuthContext';

const Header: React.FC = () => {
  const { user, logout } = useAuth();

  return (
    <header className="header">
      <div className="container">
        <h1>Fashion Designer App</h1>
        <nav>
          {user ? (
            <div className="user-menu">
              <span>Welcome, {user.email}</span>
              <button onClick={logout} className="logout-btn">
                Logout
              </button>
            </div>
          ) : (
            <span>Please log in</span>
          )}
        </nav>
      </div>
    </header>
  );
};

export default Header;