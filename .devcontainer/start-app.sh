#!/bin/bash

echo "🎬 Starting Fashion Designer App..."

# Start backend
echo "🐍 Starting Django backend on port 8000..."
cd backend
python manage.py runserver 0.0.0.0:8000 &

# Wait for backend to start
sleep 5

# Start frontend
echo "⚛️ Starting React frontend on port 3000..."
cd ../frontend
npm start &

echo "✅ Both services are starting..."
echo "🌐 Your app will be available at:"
echo "   - Frontend: https://${CODESPACE_NAME}-3000.${GITHUB_CODESPACES_PORT_FORWARDING_DOMAIN}"
echo "   - Backend:  https://${CODESPACE_NAME}-8000.${GITHUB_CODESPACES_PORT_FORWARDING_DOMAIN}"
echo ""
echo "Press Ctrl+C to stop all services"

# Keep the script running
wait
