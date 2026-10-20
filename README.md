# Technical Support Management System

TSMS is an internal support-ticket system built with **React**, **Django REST Framework**, and **PostgreSQL**.

## Current increment

This initial development increment implements the secure foundation and core ticket workflow:

- token-based sign-in and backend-enforced roles;
- employee ticket submission and own-ticket visibility;
- technician queue, assignment, priority overrides, status updates, work notes, escalation, resolution, closure, and reopening requests;
- audit activities and in-app notifications;
- category administration and basic report totals.

## Run locally

### Backend

```bash
cd backend
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py seed_demo
python manage.py runserver
```

The backend uses SQLite when `DATABASE_URL` is absent. Set `DATABASE_URL` to a PostgreSQL URL in deployment.

### Frontend

```bash
cd frontend
npm install
npm run dev
```

The browser app expects the API at `http://localhost:8000/api`; override it with `VITE_API_URL` when required.

Demo accounts created by `seed_demo`: `employee`, `technician`, `supervisor`, and `admin`; each uses password `ChangeMe123!`. Change or remove these accounts outside local development.

