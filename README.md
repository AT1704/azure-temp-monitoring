# 🌡️ Azure Temperature Monitoring with Prometheus, Grafana & Python Exporter

This project builds an end-to-end monitoring solution that tracks **real-time temperature in Tallinn** using a custom Python exporter. The entire stack is deployed on an **Azure VM** with infrastructure provisioned by **Terraform**, and services managed with **Docker Compose**.

---

## 📦 What’s Included

| Layer            | Technology                     | Purpose                                 |
|------------------|---------------------------------|-----------------------------------------|
| Cloud Infra       | Terraform + Azure               | Spin up Ubuntu VM with networking       |
| Monitoring Stack  | Docker, Prometheus, Grafana     | Store and visualize metrics             |
| Exporter          | Python (Flask + requests)       | Fetch Tallinn temp and expose to Prometheus |

---

## 📁 Project Structure

```
azure-temp-monitoring/
├── terraform/                  # Terraform configs for Azure VM
│   └── main.tf, variables.tf...
├── docker/                     # Docker Compose setup
│   ├── docker-compose.yml
│   └── prometheus/
│       └── prometheus.yml
├── scripts/                    # Python Flask app exporter
│   ├── fetch_temperature.py
│   └── README.md               # (Exporter-specific doc)
└── PROJECT_OVERVIEW.md         # (This file)
```

---

## 🚀 Deployment Guide

### 1. 🧱 Provision Infrastructure (Local Machine)
```bash
cd terraform/
terraform init
terraform apply
```
This creates an Ubuntu 22.04 VM with public IP, NSG, and other dependencies.

---

### 2. 🔐 SSH into Azure VM
```bash
ssh azureuser@<your-public-ip>
```

---

### 3. 🐳 Start Monitoring Stack
```bash
cd azure-temp-monitoring/docker
docker-compose up -d
```

---

### 4. 🐍 Run the Flask Exporter
```bash
cd ../scripts
nohup python3 fetch_temperature.py &
```

This exposes a Prometheus metric on:
```
http://<vm-ip>:9100/metrics
```

You should see:
```
temperature_celsius{location="Tallinn"} 18.0
```

---

## 📊 Grafana Setup

1. Visit Grafana at:  
   `http://<your-vm-ip>:3000` (admin/admin)

2. **Add Prometheus data source**:  
   - Type: Prometheus  
   - URL: `http://prometheus:9090`

3. **Create a dashboard**:  
   - Query: `temperature_celsius`  
   - Visualization: Gauge or Time Series

---

## 🐍 Python Exporter Details

`fetch_temperature.py` does the following:
- Calls: `https://wttr.in/Tallinn?format=j1`
- Extracts: `current_condition[0]["temp_C"]`
- Exposes: Prometheus metric via `/metrics`

Example output:
```
temperature_celsius{location="Tallinn"} 17.5
```

> You can test locally with:  
> `curl http://localhost:9100/metrics`

---

## 🧹 Tear Down

To remove all resources:
```bash
cd terraform/
terraform destroy
```

To stop just the services:
```bash
cd docker/
docker-compose down

sudo pkill -f fetch_temperature.py  # Kill Flask exporter
```

---

## 🔐 Notes

- The Flask server is for demo purposes. Use a production WSGI server like Gunicorn for real deployments.
- `wttr.in` is free but may be rate-limited; for reliability, consider Open-Meteo or other APIs.

---

## 📎 GitHub Repo

🔗 [github.com/AT1704/azure-temp-monitoring](https://github.com/AT1704/azure-temp-monitoring)

---

## 🙋‍♂️ Author
 
DevOps | Cloud | Monitoring | Automation

---

## 📝 License

MIT – Use freely for personal or educational purposes.