# MEDICARE — Hospital Infrastructure Command Center

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-3.x-green.svg)](https://flask.palletsprojects.com/)
[![IaC](https://img.shields.io/badge/IaC-Terraform-purple.svg)](https://www.terraform.io/)
[![Status](https://img.shields.io/badge/Status-Operational-brightgreen.svg)]()

A 24/7 digital command center demonstrating how a hospital's IT and DevOps team manages digital infrastructure (compute, databases, storage, networks, security, deployments, and monitoring) using **Infrastructure as Code (IaC)** and **Clean Coding** principles.

---

## Key Highlights

- **8 Responsive Interfaces**:
  1. **Hospital Infrastructure Overview (`index.html`)**: Fleet KPIs, cluster health breakdown, real-time topology map, circular health gauge, and sparkline charts.
  2. **Architecture Blueprint (`architecture.html`)**: Stage 1 Mural planning infographic, 7 IaC pillars, and live Seaborn regression analysis.
  3. **Infrastructure Management (`infrastructure.html`)**: Tabbed resource fleet table with simulated IaC resource provisioning.
  4. **Deployment Center (`deployments.html`)**: Staged multi-step release pipeline simulation with filterable deployment audit history.
  5. **Real-Time Monitoring (`monitoring.html`)**: Dynamic CPU, Memory, Storage, Network telemetry updating automatically every few seconds.
  6. **Security Center (`security.html`)**: Security health score (94/100), active firewall, SSL validation, access controls, and security event log.
  7. **Activity Logs (`logs.html`)**: Centralized audit trail with instant client-side search and multi-criteria filtering.
  8. **Settings (`settings.html`)**: Granular operational configurations with toast notifications.

- **Python Backend Engine (`app.py`)**:
  - Modular Flask architecture following Clean Code principles.
  - RESTful APIs for health, server fleet, live metrics, provisioning, and deployments.
  - Statistical Analysis Engine using **Pandas**, **Matplotlib**, and **Seaborn** to generate regression plots comparing *Provisioning Time vs Resource Utilization*.

---

## Quick Start (Local)

### 1. Double Click
Double-click **`run_server.bat`** on Windows. The server starts and automatically launches your browser to `http://127.0.0.1:5000`.

### 2. Manual CLI
```bash
pip install -r requirements.txt
python app.py
```
Open **`http://127.0.0.1:5000`** in your browser.

---

## Deployment Options

See [`DEPLOYMENT_GUIDE.md`](./DEPLOYMENT_GUIDE.md) for full instructions on:
- **Render** (Free Python cloud hosting)
- **Vercel** (Serverless cloud hosting)
- **GitHub Pages** (Static web hosting)
- **Docker** (Containerized execution)

---

## Architecture & Toolchain

| Stage | Tool | Role in Hospital Management System |
| :--- | :--- | :--- |
| **Plan** | Mural | Infrastructure topology & dependency mapping |
| **Code** | Terraform | Modular, reusable Infrastructure as Code definitions |
| **Version Control** | Git / GitHub | Infrastructure change tracking and peer reviews |
| **Build & Test** | Terraform Validate | Syntax checking and pre-flight execution planning |
| **Release** | Jenkins / Octopus | Automated staged deployment pipeline |
| **Operate** | Kubernetes / Cloud | Resilient hosting of hospital microservices |
| **Monitor** | Grafana / Prometheus | Continuous observability & SLA tracking |
