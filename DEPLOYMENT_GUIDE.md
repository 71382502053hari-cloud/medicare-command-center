# MEDICARE Hospital Infrastructure Command Center — Deployment Guide

This guide details all available methods to run and deploy the **MEDICARE Hospital Infrastructure Command Center** using Python (Flask) and HTML/CSS/JS.

---

## 1. Local Deployment (Fastest & Immediate)

### Option A: One-Click Windows Launcher
1. Navigate into the `medicare-app` directory.
2. Double-click **`run_server.bat`** (or right-click `run_server.ps1` → *Run with PowerShell*).
3. The script will automatically open your default browser to `http://127.0.0.1:5000` and start the Flask backend.

### Option B: Terminal Command
1. Open PowerShell or Command Prompt in the `medicare-app` directory:
   ```powershell
   cd c:\Users\Student\Downloads\medicare-command-center\medicare-app
   ```
2. Ensure dependencies are installed:
   ```powershell
   pip install -r requirements.txt
   ```
3. Start the application:
   ```powershell
   python app.py
   ```
4. Access the command center in your browser at:
   - **Dashboard**: `http://127.0.0.1:5000/`
   - **Architecture Blueprint**: `http://127.0.0.1:5000/architecture.html`
   - **Live Seaborn Regression Plot**: `http://127.0.0.1:5000/api/analytics/plot`

---

## 2. Cloud Deployment: Render (Free Python Web Service)

Render provides free hosting for Python Flask applications.

1. **Push the project to GitHub**:
   - Create a new GitHub repository (or use your existing repository: `Infrastructure-as-Code-for-Hospital-Management-`).
   - Push the contents of `medicare-app` to your repository.
2. **Log into Render**:
   - Go to [render.com](https://render.com/) and sign in with GitHub.
3. **Create New Web Service**:
   - Click **New +** → **Web Service**.
   - Select your GitHub repository.
   - Set the following settings:
     - **Name**: `medicare-command-center`
     - **Region**: Closest to you (e.g., Singapore or Frankfurt)
     - **Branch**: `main`
     - **Root Directory**: `medicare-app` (or leave empty if repository root)
     - **Runtime**: `Python 3`
     - **Build Command**: `pip install -r requirements.txt`
     - **Start Command**: `gunicorn app:app`
     - **Instance Type**: `Free`
4. Click **Create Web Service**.
5. Render will automatically build the environment and provide a public URL:
   `https://medicare-command-center.onrender.com`

---

## 3. Cloud Deployment: Vercel (Serverless Python)

1. Install the Vercel CLI or connect via the Vercel Dashboard:
   - [vercel.com](https://vercel.com/)
2. Import your GitHub repository.
3. Vercel automatically detects `vercel.json` and configures the Python serverless runtime.
4. Click **Deploy**.
5. Your website is instantly live with global CDN caching.

---

## 4. Static Hosting: GitHub Pages

If you want a 100% serverless static website that runs purely in the client:

1. In your GitHub repository, go to **Settings** → **Pages**.
2. Under **Build and deployment**:
   - **Source**: Deploy from a branch.
   - **Branch**: `main`, folder: `/` (root) or `/docs`.
3. Click **Save**.
4. Within 1-2 minutes, your website will be live at:
   `https://<your-username>.github.io/<repo-name>/`

*Note: All 7 pages, navigation, simulations, and modals function completely client-side. The Architecture page gracefully displays the blueprint and offline fallbacks for plotting.*

---

## 5. Containerized Deployment (Docker)

To run the application inside an isolated Docker container:

1. Build the Docker image:
   ```bash
   docker build -t medicare-command-center .
   ```
2. Run the container:
   ```bash
   docker run -d -p 5000:5000 --name medicare_app medicare-command-center
   ```
3. Or use Docker Compose:
   ```bash
   docker compose up -d
   ```
4. Access the application at `http://localhost:5000`.

---

## Project Structure

```
medicare-app/
├── app.py                      # Flask backend & RESTful API endpoints
├── index.html                  # Main Hospital Infrastructure Overview
├── architecture.html           # IaC Architecture Blueprint & Mural Infographic
├── infrastructure.html         # Compute, Database, Storage, Network Fleet
├── deployments.html            # Staged Deployment Center & Release History
├── monitoring.html             # Real-Time Telemetry & Resource Utilization
├── security.html               # Security Score, Firewall, SSL & Policies
├── logs.html                   # Audit Activity Logs & Live Search
├── settings.html               # Configuration & Operations Settings
├── css/style.css               # Shared Modern Design System & Theming
├── js/script.js                # Frontend Interactivity & API Connectivity
├── assets/images/
│   └── mural-architecture.png  # Mural Stage 1 Planning Infographic
├── requirements.txt            # Python dependencies (Flask, pandas, seaborn, gunicorn)
├── Procfile                    # Cloud process declaration (Render/Heroku)
├── vercel.json                 # Vercel serverless configuration
├── render.yaml                 # Render Infrastructure Blueprint
├── Dockerfile                  # Container definition
├── docker-compose.yml          # Container orchestration
├── run_server.bat              # One-click Windows batch launcher
├── run_server.ps1              # PowerShell server launcher
└── DEPLOYMENT_GUIDE.md         # Full deployment documentation
```
