# Docker Setup Guide for VoltStream App

## Overview
This document explains how to build and run the VoltStream App using Docker.

## Prerequisites
- Docker installed on your system
- Docker Compose installed (comes with Docker Desktop)

## Project Structure
```
VoltStream App/
├── backend/
│   ├── Dockerfile
│   ├── .dockerignore
│   └── ... (Python FastAPI app)
├── frontend/
│   ├── Dockerfile
│   ├── .dockerignore
│   └── ... (React/Vite app)
├── docker-compose.yml
└── .env.docker
```

## Building the Application

### Option 1: Using Docker Compose (Recommended)
```bash
# Navigate to the project root
cd "VoltStream App"

# Build and start both services
docker-compose up --build

# Or run in detached mode (background)
docker-compose up -d --build
```

### Option 2: Build Individually
```bash
# Build backend image
docker build -t voltstream_backend ./backend

# Build frontend image
docker build -t voltstream_frontend ./frontend

# Run backend
docker run -p 8000:8000 voltstream_backend

# Run frontend (in another terminal)
docker run -p 3000:3000 voltstream_frontend
```

## Accessing the Application
- **Frontend**: http://localhost:3000
- **Backend API**: http://localhost:8000
- **API Docs**: http://localhost:8000/docs (FastAPI Swagger UI)

## Docker Compose Commands

```bash
# Start services
docker-compose up

# Start services in background
docker-compose up -d

# View logs
docker-compose logs

# View logs for specific service
docker-compose logs backend
docker-compose logs frontend

# Stop services
docker-compose stop

# Stop and remove containers
docker-compose down

# Remove containers and volumes
docker-compose down -v

# Rebuild images
docker-compose build

# Rebuild without cache
docker-compose build --no-cache
```

## Environment Variables
Configuration is defined in `.env.docker`:
- `BACKEND_PORT`: Backend service port (default: 8000)
- `FRONTEND_PORT`: Frontend service port (default: 3000)
- `VITE_API_URL`: API URL for frontend (default: http://localhost:8000)

## Development with Docker

### Hot Reload
The docker-compose configuration includes volume mounts for the backend to enable hot reload during development:

```bash
docker-compose up
```

The backend will automatically reload when you modify Python files.

### Rebuilding After Changes
```bash
# Rebuild services if you change dependencies
docker-compose build --no-cache

# Restart services
docker-compose restart
```

## Troubleshooting

### Port Already in Use
If you get port errors, you can change the ports in `docker-compose.yml`:

```yaml
ports:
  - "8001:8000"  # Map to 8001 instead
```

### Clear Everything and Start Fresh
```bash
docker-compose down -v
docker system prune -a
docker-compose up --build
```

### View Running Containers
```bash
docker ps
```

### Stop a Specific Service
```bash
docker-compose stop backend
# or
docker-compose stop frontend
```

## Production Deployment
For production, consider:
1. Using environment variables for configuration
2. Setting `restart: on-failure` in docker-compose.yml
3. Using a reverse proxy (nginx) in front of services
4. Implementing proper logging and monitoring
5. Using secrets management for sensitive data

## Network Communication
Services communicate via the `voltstream_network` bridge network:
- Backend is accessible at `http://backend:8000` from frontend container
- Frontend is accessible at `http://frontend:3000` from backend container
