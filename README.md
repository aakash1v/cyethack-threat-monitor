# Threat Monitoring & Alert Management Backend

## Overview
This project is a backend service built using Django and Django REST Framework
for ingesting security events and managing alerts in a role-based system.

The system is designed as a simplified backend module that could integrate with
surveillance systems, SIEM tools, or AI-based threat detection engines.

---
## Live Deployment

The backend is deployed and accessible at:

  - Base URL: https://p1.aakash1.online
  - Swagger API Docs: https://p1.aakash1.online/api/docs/

HTTPS is enabled using Let’s Encrypt and Nginx.

## Sample User Credentials (For Testing)
```bash
  User Type : Admin
  Username  : admin
  Password  : password113
  
  User Type : Analyst
  Username  : analyst
  Password  : password113

```

## Features
- JWT-based authentication
- Role-based access control (Admin, Analyst)
- Security event ingestion
- Automatic alert generation for high-severity events
- Alert status management
- Pagination, filtering, and validation
- Swagger API documentation

---

## Tech Stack
- Python
- Django
- Django REST Framework
- SimpleJWT
- drf-spectacular
- SQLite 

---

## User Roles
- **Admin**
  - Ingest events
  - View and update alerts
- **Analyst**
  - View alerts (read-only)

---

## API Endpoints

### Authentication
- `POST /api/auth/login/`
- `POST /api/auth/refresh/`

### Threat Events
- `POST /api/events/` (Admin only)

### Alerts
- `GET /api/alerts/`
- `PATCH /api/alerts/{id}/status/` (Admin only)

---

## Alert Generation Logic
An alert is automatically created when a threat event with severity
**HIGH** or **CRITICAL** is ingested. This logic is enforced at the data layer
using Django signals to ensure consistency.

---

## Environment variables

```bash
  DEBUG=False
  SECRET_KEY=change-this-secret-key
  ALLOWED_HOSTS=p1.aakash1.online,127.0.0.1,localhost


```
---

## Setup Instructions

```bash
    git clone https://github.com/aakash1v/cyethack-threat-monitor.git
    cd cyethack-threat-monitor

    python -m venv venv
    source venv/bin/activate

    pip install -r requirements.txt

    python manage.py migrate
    python manage.py createsuperuser
    python manage.py runserver

``` 


