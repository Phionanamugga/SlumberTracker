🌙 SlumberTracking App
A full-stack Django sleep tracking application that helps users monitor their sleep patterns, track sleep debt, and visualize trends with interactive charts.
🚀 Built with clean architecture, REST API support, and production-ready deployment guidelines.

📍 Live Demo → SlumberTracking App (Demo credentials: demo@slumber.com / password123)

🎬 Preview
(Dashboard with charts, sleep debt calculation & weekly trends)

✨ Features
🔐 User Authentication (secure login/logout)
🛌 Track Sleep Sessions (bedtime, wake time, duration auto-calculated)

📊 Analytics Dashboard
Weekly sleep trends (Chart.js)
Best/Worst nights
Sleep debt calculator (vs 8h target)
Average duration

🌐 REST API for integrations (wearables, mobile apps)
🛠️ Admin Panel (manage users & sessions)
🚀 Deployment Ready (Docker + Gunicorn + Nginx + PostgreSQL)

🏗️ Tech Stack
Layer	Technology
Backend	Django 5, Django REST Framework
Frontend	HTML5, Chart.js
Database	SQLite (dev) → PostgreSQL (prod)
Auth	Django User Model
Dev Tools	Black, Ruff, pytest
Deployment	Docker, Gunicorn, Nginx

📦 Installation
git clone https://github.com/Phionanamugga/slumbertracking.git
cd slumbertracking
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
Setup .env:
SECRET_KEY=replace_me
DEBUG=1
ALLOWED_HOSTS=127.0.0.1,localhost
Run migrations & start server:
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
Visit 👉 http://127.0.0.1:8000/

📊 Example Analytics API
{
  "avg_sleep": 7.5,
  "best": 9.2,
  "worst": 4.3,
  "sleep_debt": 10.5,
  "trend": {
    "labels": ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"],
    "data": [7.2, 6.5, 8.0, 5.0, 7.8, 9.2, 6.0]
  }
}

✅ Tests
pytest
# or
python manage.py test
✔️ Models (sleep duration)
✔️ Views (CRUD sessions)
✔️ API endpoints
🚀 Deployment
docker build -t slumbertracking .
docker run -d -p 8000:8000 slumbertracking
Or manually:
python manage.py collectstatic
gunicorn config.wsgi:application --bind 0.0.0.0:8000

🌍 Why It Matters
Sleep fuels productivity.
SlumberTracking App = actionable insights → better rest → better performance.
This project showcases:
📐 Clean full-stack architecture
📊 Data-driven analytics
🛡️ Production practices
✅ Test-driven development

👩🏽‍💻 Author
Phiona Namugga
🎓 MSc Data Science, AI & Digital Business
📈 Data Science Apprentice @ ALX Africa
☁️ AWS Certified Cloud Practitioner


⭐ Recruiter Note
This is more than a tutorial app. It demonstrates:
End-to-end engineering (backend, frontend, analytics, deployment)
Scalable & modular design
Real-world problem solving (sleep optimization)
Professional polish (badges, tests, docs, visuals)
I built this to highlight the impact-driven engineering and analytical thinking I’d bring