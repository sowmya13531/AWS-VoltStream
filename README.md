# ⚡ VoltStream – AWS Serverless Energy Intelligence Platform

> A Production-Grade Full-Stack Energy Management Platform built using AWS Serverless Services, FastAPI, React, AWS Lambda, Amazon S3, CloudWatch, SNS, and IAM.

---

## 📖 Overview

VoltStream is a cloud-native Energy Intelligence Platform designed for modern **Prosumers**—households that both consume electricity from the utility grid and generate renewable solar energy through rooftop solar panels.

The platform provides:

* Real-time energy monitoring
* Solar generation tracking
* Smart appliance control
* Historical energy analytics
* Billing intelligence and budget alerts
* Fully serverless AWS deployment

The entire application is hosted using AWS managed services with zero server management and operates within AWS Free Tier limits.  

---

# 🚀 Features

## ⚡ Real-Time Energy Dashboard

Monitor:

* Grid Power Consumption
* Solar Energy Generation
* Net Energy Usage

Dashboard updates automatically every 4 seconds using live API polling. 

---

## 📊 Energy Analytics

Historical energy insights with:

* Daily View
* Weekly View
* Monthly View

Features:

* Interactive charts
* Generation vs Consumption comparison
* Hover-based energy breakdown
* Trend analysis



---

## 🔌 Smart Device Control

Control household appliances remotely:

* HVAC System
* Water Heater
* Pool Pump
* EV Charger
* Lighting
* Refrigerator

Features:

* Device status monitoring
* Real-time ON/OFF switching
* Server-side state updates



---

## 💰 Billing Intelligence

Provides:

* Current Balance
* Projected Monthly Bill
* Budget Tracking
* Budget Overrun Alerts
* Invoice History

Helps users proactively manage electricity expenses. 

---

# 🏗️ Architecture

```text
                    ┌─────────────────────┐
                    │     React Frontend  │
                    │   Amazon S3 Hosting │
                    └──────────┬──────────┘
                               │
                               ▼
                  HTTP Requests (Axios)
                               │
                               ▼
                ┌─────────────────────────┐
                │ Lambda Function URL     │
                │ Public HTTPS Endpoint   │
                └──────────┬──────────────┘
                           │
                           ▼
                ┌─────────────────────────┐
                │ AWS Lambda (Python 3.12)│
                │ FastAPI + Mangum        │
                └──────────┬──────────────┘
                           │
                           ▼
                ┌─────────────────────────┐
                │ Business Logic Layer    │
                │ Routes + Models         │
                └─────────────────────────┘

                           │

          ┌────────────────┴───────────────┐
          ▼                                ▼

 ┌──────────────────┐          ┌──────────────────┐
 │ CloudWatch Logs  │          │ CloudWatch Alarm │
 └──────────────────┘          └─────────┬────────┘
                                         │
                                         ▼

                               ┌────────────────┐
                               │ Amazon SNS     │
                               │ Email Alerts   │
                               └────────────────┘
```

Based on the deployed AWS serverless architecture. 

---

# ☁️ AWS Services Used

| Service             | Purpose                |
| ------------------- | ---------------------- |
| AWS Lambda          | Backend API Runtime    |
| Amazon S3           | Frontend Hosting       |
| Lambda Function URL | Public API Endpoint    |
| AWS IAM             | Access Control         |
| CloudWatch Logs     | Application Logging    |
| CloudWatch Alarms   | Monitoring             |
| Amazon SNS          | Email Notifications    |
| FastAPI             | REST API Framework     |
| Mangum              | FastAPI-Lambda Adapter |
| React + Vite        | Frontend Application   |



---

# 🛠️ Technology Stack

## Frontend

* React
* Vite
* Axios
* React Router
* Recharts
* Tailwind CSS
* Lucide Icons



---

## Backend

* FastAPI
* Pydantic
* Mangum
* Python 3.12



---

## Cloud Infrastructure

* AWS Lambda
* Amazon S3
* CloudWatch
* SNS
* IAM



---

# 📂 Project Structure

```text
VoltStream/
│
├── frontend/
│   ├── src/
│   │   ├── pages/
│   │   │   ├── LiveDashboard.jsx
│   │   │   ├── UsageHistory.jsx
│   │   │   ├── SmartControl.jsx
│   │   │   └── Invoices.jsx
│   │   │
│   │   ├── api/
│   │   └── components/
│   │
│   ├── public/
│   └── package.json
│
├── backend/
│   ├── voltstream_backend/
│   │   ├── main.py
│   │   ├── routes.py
│   │   ├── models.py
│   │   ├── mock_data.py
│   │   └── __init__.py
│   │
│   ├── requirements.txt
│   └── lambda_package.zip
│
└── README.md
```

---

# 🔌 API Endpoints

| Method | Endpoint                    | Description            |
| ------ | --------------------------- | ---------------------- |
| GET    | `/api/v1/dashboard/live`    | Live power metrics     |
| GET    | `/api/v1/analytics/history` | Historical energy data |
| GET    | `/api/v1/devices`           | Device list            |
| PATCH  | `/api/v1/devices/{id}`      | Toggle device state    |
| GET    | `/api/v1/billing/summary`   | Billing information    |



---

# 📡 Request Lifecycle

### 1. User Opens Website

React application is served from Amazon S3.

### 2. Dashboard Loads

React triggers API requests using Axios.

### 3. Lambda Function URL Receives Request

Public HTTPS endpoint forwards request to Lambda.

### 4. AWS Lambda Executes

FastAPI application processes request.

### 5. Mangum Adapter

Converts Lambda event into ASGI request.

### 6. FastAPI Route Executes

Business logic generates response.

### 7. Response Returned

JSON data sent back to browser.

### 8. CloudWatch Records Metrics

Logs, duration, errors, and invocation data are captured.



---

# ⚙️ Local Development

## Backend Setup

```bash
git clone <repository-url>

cd backend

python -m venv venv

venv\Scripts\activate

pip install -r requirements.txt
```

Run locally:

```bash
uvicorn voltstream_backend.main:app --reload
```

---

## Frontend Setup

```bash
cd frontend

npm install

npm run dev
```

---

# ☁️ Deployment

## Backend Deployment

1. Package FastAPI application
2. Upload package to S3
3. Deploy Lambda function
4. Create Function URL
5. Configure IAM permissions

AWS Services Used:

* Lambda
* S3 Deployment Bucket
* IAM Role
* Lambda Function URL



---

## Frontend Deployment

1. Build React application

```bash
npm run build
```

2. Upload `dist/` folder to S3

3. Enable Static Website Hosting

4. Configure Public Access

5. Configure Cache Headers



---

# 🔍 Monitoring & Observability

## CloudWatch Logs

Tracks:

* Request IDs
* Execution Time
* Memory Usage
* Errors
* Invocation Count

```bash
aws logs tail /aws/lambda/voltstream-api --follow
```



---

## CloudWatch Alarms

### Error Alarm

Triggers when:

```text
Errors >= 5
within 5 minutes
```

### Duration Alarm

Triggers when:

```text
Average Duration >= 3000ms
```

### Throttle Alarm

Triggers when:

```text
Any Lambda Throttle Event
```



---

## SNS Notifications

Email notifications are automatically sent whenever an alarm enters the ALARM state.

Monitoring pipeline:

```text
Lambda
   ↓
CloudWatch Metrics
   ↓
CloudWatch Alarm
   ↓
SNS Topic
   ↓
Email Notification
```



---

# 💵 Cost Optimization

VoltStream is designed to run entirely within AWS Free Tier.

| Service           | Monthly Cost |
| ----------------- | ------------ |
| Lambda            | $0.00        |
| S3                | $0.00        |
| CloudWatch Logs   | $0.00        |
| CloudWatch Alarms | $0.00        |
| SNS               | $0.00        |

**Estimated Total Cost: $0.00/month**



---

# 🚨 Challenges & Solutions

| Issue                          | Resolution                                |
| ------------------------------ | ----------------------------------------- |
| Pydantic Linux binary mismatch | Built packages inside Lambda Docker image |
| Relative import failures       | Switched to relative imports              |
| CORS errors                    | Updated middleware configuration          |
| Uvicorn package bloat          | Removed from Lambda package               |
| Docker connection issues       | Started Docker Desktop                    |
| S3 bucket name conflicts       | Added account-specific suffix             |



---

# 🎯 Demo Flow

### Dashboard

* Show Grid Draw
* Show Solar Generation
* Show Net Usage

### Analytics

* Daily
* Weekly
* Monthly

### Smart Control

* Toggle HVAC
* Toggle Water Heater

### Billing

* Show budget alerts
* Show invoice history

### Swagger Documentation

* Open `/docs`
* Execute live API requests

### CloudWatch

* Show Logs
* Show Alarms



---

# 📈 Key Learnings

* AWS Serverless Architecture
* FastAPI Deployment on Lambda
* Lambda Function URLs
* Static Website Hosting with S3
* CloudWatch Monitoring
* SNS Alerting
* IAM Security
* Cost Optimization
* Infrastructure Automation

---



Tachyon AIML Internship 2026 – AWS Track


