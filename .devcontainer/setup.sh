#!/bin/bash

echo "🚀 Setting up Fashion Designer App in Codespace..."

# Update package list
sudo apt-get update

# Install Python dependencies
echo "📦 Installing Python dependencies..."
cd backend
pip install -r requirements.txt

# Install Node.js dependencies
echo "📦 Installing Node.js dependencies..."
cd ../frontend
npm install

echo "✅ Setup complete! Your environment is ready."
echo ""
echo "🎯 Next steps:"
echo "1. Update environment variables:"
echo "   cp backend/.env.example backend/.env"
echo "   cp frontend/.env.example frontend/.env"
echo "2. Edit the .env files with your Supabase credentials"
echo "3. Run: cd backend && python manage.py migrate"
echo "4. Start services:"
echo "   Backend: cd backend && python manage.py runserver 0.0.0.0:8000"
echo "   Frontend: cd frontend && npm start"
