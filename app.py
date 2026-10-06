"""
MEDICARE Hospital Infrastructure Command Center
===============================================
Backend Application Server & REST API
Clean Code Architecture for Hospital Infrastructure as Code (IaC)

Author: Hospital Infrastructure DevOps Team
Project: Infrastructure as Code for Hospital Management Using Clean Coding
Guidance: IBM Project & Clean Code Principles
"""

import io
import os
import random
import time
from typing import Any, Dict, List

from flask import Flask, jsonify, request, send_file, send_from_directory

# Base directory where this application and its web assets reside
BASE_DIR: str = os.path.dirname(os.path.abspath(__file__))

app = Flask(
    __name__,
    static_folder=BASE_DIR,
    static_url_path="",
)

# ---------------------------------------------------------------------------
# Data Models & Initial State (Clean Code In-Memory Store)
# ---------------------------------------------------------------------------

DEFAULT_SERVERS: List[Dict[str, Any]] = [
    {"name": "HMS-WEB-01", "type": "Web Server", "env": "Production", "cpu": 42, "memory": 58, "status": "Healthy"},
    {"name": "HMS-WEB-02", "type": "Web Server", "env": "Production", "cpu": 38, "memory": 54, "status": "Healthy"},
    {"name": "HMS-API-01", "type": "API Server", "env": "Production", "cpu": 55, "memory": 68, "status": "Healthy"},
    {"name": "HMS-API-02", "type": "API Server", "env": "Production", "cpu": 49, "memory": 62, "status": "Healthy"},
    {"name": "HMS-DB-01", "type": "Database", "env": "Production", "cpu": 64, "memory": 82, "status": "Healthy"},
    {"name": "HMS-DB-02", "type": "Database Replica", "env": "Production", "cpu": 32, "memory": 48, "status": "Healthy"},
    {"name": "HMS-TEST-01", "type": "Test Node", "env": "Testing", "cpu": 78, "memory": 85, "status": "Warning"},
    {"name": "HMS-DEV-01", "type": "Dev Node", "env": "Development", "cpu": 22, "memory": 35, "status": "Healthy"},
]

DEPLOYMENT_HISTORY: List[Dict[str, Any]] = [
    {"version": "v2.4.1", "environment": "Production", "status": "Success", "author": "Infra Admin", "timestamp": "32 min ago", "duration": "4m 12s"},
    {"version": "v2.4.0", "environment": "Production", "status": "Success", "author": "Infra Admin", "timestamp": "2 days ago", "duration": "3m 48s"},
    {"version": "v2.3.9", "environment": "Testing", "status": "Success", "author": "DevOps Bot", "timestamp": "4 days ago", "duration": "2m 50s"},
    {"version": "v2.3.8", "environment": "Testing", "status": "Failed", "author": "Release Lead", "timestamp": "5 days ago", "duration": "1m 15s"},
    {"version": "v2.3.7", "environment": "Production", "status": "Success", "author": "Infra Admin", "timestamp": "1 week ago", "duration": "4m 05s"},
]

AUDIT_LOGS: List[Dict[str, Any]] = [
    {"timestamp": "2026-09-22 11:50:12", "user": "Admin", "action": "Config Update", "resource": "CORE-LB-01", "environment": "Production", "status": "Success"},
    {"timestamp": "2026-09-22 11:22:45", "user": "Infra Lead", "action": "Deployment", "resource": "HMS-API-01", "environment": "Production", "status": "Success"},
    {"timestamp": "2026-09-22 10:45:00", "user": "DevOps Bot", "action": "DB Backup", "resource": "HMS-DB-01", "environment": "Production", "status": "Success"},
    {"timestamp": "2026-09-22 09:30:18", "user": "Monitoring", "action": "Memory Alert", "resource": "HMS-TEST-01", "environment": "Testing", "status": "Warning"},
    {"timestamp": "2026-09-22 08:15:33", "user": "Security Bot", "action": "Cert Renewal", "resource": "EDGE-GATEWAY", "environment": "Production", "status": "Success"},
]


# ---------------------------------------------------------------------------
# Page Serving Routes
# ---------------------------------------------------------------------------

@app.route("/")
def index():
    """Main Dashboard: Hospital Infrastructure Overview."""
    return send_from_directory(BASE_DIR, "index.html")


@app.route("/<string:page_name>")
def serve_page(page_name: str):
    """
    Serve HTML pages by clean name or full filename.
    Examples: /infrastructure, /infrastructure.html, /architecture
    """
    if not page_name.endswith(".html"):
        candidate = f"{page_name}.html"
        if os.path.exists(os.path.join(BASE_DIR, candidate)):
            return send_from_directory(BASE_DIR, candidate)

    target = os.path.join(BASE_DIR, page_name)
    if os.path.exists(target) and not os.path.isdir(target):
        return send_from_directory(BASE_DIR, page_name)

    return send_from_directory(BASE_DIR, "index.html")


# ---------------------------------------------------------------------------
# RESTful API Endpoints
# ---------------------------------------------------------------------------

@app.route("/api/health", methods=["GET"])
def get_health() -> Any:
    """Return overall infrastructure health score and cluster ratings."""
    return jsonify({
        "overall_score": 96,
        "status": "Operational",
        "clusters": {
            "server": {"score": 98, "status": "Healthy", "online": "21/24"},
            "database": {"score": 100, "status": "Healthy", "online": "6/6"},
            "network": {"score": 99, "status": "Healthy", "latency_ms": 8},
            "security": {"score": 94, "status": "Active", "policies": "Enforced"},
            "storage": {"score": 89, "status": "Normal", "used_tb": 27.2, "total_tb": 40.0},
        },
        "updated_at": time.strftime("%Y-%m-%d %H:%M:%S"),
    })


@app.route("/api/metrics", methods=["GET"])
def get_live_metrics() -> Any:
    """Return real-time infrastructure performance telemetry."""
    # Dynamic slight jitter simulating real-time telemetry
    cpu = max(20, min(85, 42 + random.randint(-4, 5)))
    memory = max(40, min(90, 61 + random.randint(-3, 4)))
    storage = 68
    network = round(max(0.8, min(2.5, 1.0 + (random.random() * 0.4 - 0.2))), 2)

    return jsonify({
        "cpu_usage_pct": cpu,
        "memory_usage_pct": memory,
        "storage_usage_pct": storage,
        "network_throughput_gbs": network,
        "system_uptime": "99.98%",
        "active_sessions": 4208 + random.randint(-15, 20),
        "requests_per_min": 12400 + random.randint(-200, 300),
    })


@app.route("/api/servers", methods=["GET"])
def get_servers() -> Any:
    """Return list of managed hospital infrastructure nodes."""
    env_filter = request.args.get("env")
    if env_filter and env_filter.lower() != "all":
        filtered = [s for s in DEFAULT_SERVERS if s["env"].lower() == env_filter.lower()]
        return jsonify({"servers": filtered, "count": len(filtered)})
    return jsonify({"servers": DEFAULT_SERVERS, "count": len(DEFAULT_SERVERS)})


@app.route("/api/provision", methods=["POST"])
def provision_resource() -> Any:
    """
    Simulate Infrastructure as Code provisioning using Terraform workflow.
    Validates payload and returns provisioned state.
    """
    data = request.get_json() or {}
    resource_type = data.get("resource_type", "Virtual Machine Node")
    environment = data.get("environment", "Development")
    region = data.get("region", "Chennai Data Center")

    new_resource_name = f"HMS-{resource_type[:3].upper()}-{random.randint(10, 99)}"
    provisioned_item = {
        "name": new_resource_name,
        "type": resource_type,
        "env": environment,
        "region": region,
        "cpu": random.randint(15, 35),
        "memory": random.randint(30, 50),
        "status": "Healthy",
    }
    DEFAULT_SERVERS.append(provisioned_item)

    # Append to activity log
    AUDIT_LOGS.insert(0, {
        "timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),
        "user": "Infrastructure Admin",
        "action": f"IaC Provision ({resource_type})",
        "resource": new_resource_name,
        "environment": environment,
        "status": "Success",
    })

    return jsonify({
        "success": True,
        "message": f"Resource {new_resource_name} provisioned successfully in {region} [{environment}]",
        "resource": provisioned_item,
    }), 201


@app.route("/api/deploy", methods=["POST"])
def trigger_deployment() -> Any:
    """
    Execute staged deployment pipeline (Terraform Validate -> Apply -> Health Check).
    """
    data = request.get_json() or {}
    version = data.get("version", f"v2.4.{len(DEPLOYMENT_HISTORY) + 1}")
    env = data.get("environment", "Production")

    deployment_record = {
        "version": version,
        "environment": env,
        "status": "Success",
        "author": "Infrastructure Admin",
        "timestamp": "Just now",
        "duration": "3m 42s",
        "stages": [
            "Validate Configuration",
            "Provision Resources",
            "Configure Network",
            "Apply Security Policies",
            "Deploy Services",
            "Health Check",
        ],
    }
    DEPLOYMENT_HISTORY.insert(0, deployment_record)

    return jsonify({
        "success": True,
        "message": f"Deployment {version} completed successfully to {env}",
        "deployment": deployment_record,
    }), 200


@app.route("/api/deployments", methods=["GET"])
def get_deployments() -> Any:
    """Return deployment history."""
    return jsonify({"deployments": DEPLOYMENT_HISTORY})


@app.route("/api/logs", methods=["GET"])
def get_logs() -> Any:
    """Return audit activity logs."""
    return jsonify({"logs": AUDIT_LOGS, "total": len(AUDIT_LOGS)})


@app.route("/api/analytics/data", methods=["GET"])
def get_analytics_data() -> Any:
    """
    Hospital Infrastructure Dataset Analysis using Pandas.
    Aligns with Section 5.1 of the IBM Project specification.
    """
    try:
        import pandas as pd
    except ImportError:
        return jsonify({"error": "pandas not installed"}), 500

    provisioning_time = [10, 15, 20, 25, 30, 35, 40, 45]
    resource_utilization = [30, 35, 42, 48, 55, 60, 68, 75]

    df = pd.DataFrame({
        "Provisioning_Time_Mins": provisioning_time,
        "Resource_Utilization_Pct": resource_utilization,
        "Efficiency_Ratio": [round(r / p, 2) for r, p in zip(resource_utilization, provisioning_time)],
    })

    return jsonify({
        "summary": df.describe().to_dict(),
        "records": df.to_dict(orient="records"),
        "correlation": float(df["Provisioning_Time_Mins"].corr(df["Resource_Utilization_Pct"])),
    })


@app.route("/api/analytics/plot", methods=["GET"])
def get_analytics_plot() -> Any:
    """
    Generate and stream the Seaborn Statistical Scatter Plot with Regression line.
    Direct implementation of Section 5.3 of the IBM Project documentation.
    """
    try:
        import matplotlib
        matplotlib.use("Agg")
        import matplotlib.pyplot as plt
        import seaborn as sns
    except ImportError as e:
        return jsonify({"error": f"Plotting library unavailable: {str(e)}"}), 500

    provisioning_time = [10, 15, 20, 25, 30, 35, 40, 45]
    resource_utilization = [30, 35, 42, 48, 55, 60, 68, 75]

    # Configure style
    sns.set_theme(style="darkgrid")
    fig, ax = plt.subplots(figsize=(8, 4.5), dpi=120)

    # Plot statistical scatter with regression line
    sns.regplot(
        x=provisioning_time,
        y=resource_utilization,
        ax=ax,
        color="#2563eb",
        scatter_kws={"s": 65, "alpha": 0.9, "color": "#0284c7"},
        line_kws={"linewidth": 2.2, "color": "#16a34a"},
    )

    ax.set_title("Infrastructure Provisioning Time vs Resource Utilization", fontsize=13, pad=12, fontweight="bold")
    ax.set_xlabel("Infrastructure Provisioning Time (minutes)", fontsize=10, labelpad=8)
    ax.set_ylabel("Resource Utilization (%)", fontsize=10, labelpad=8)
    ax.grid(True, linestyle="--", alpha=0.5)

    plt.tight_layout()

    # Stream to memory buffer
    buffer = io.BytesIO()
    plt.savefig(buffer, format="png", bbox_inches="tight")
    buffer.seek(0)
    plt.close(fig)

    return send_file(buffer, mimetype="image/png")


# ---------------------------------------------------------------------------
# Server Entry Point
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    host = os.environ.get("HOST", "0.0.0.0")
    print(f"============================================================")
    print(f"  MEDICARE Hospital Infrastructure Command Center")
    print(f"  Architecture: Clean Code + Python Flask + IaC DevOps")
    print(f"  Server URL  : http://{host}:{port}")
    print(f"============================================================")
    app.run(host=host, port=port, debug=True)
