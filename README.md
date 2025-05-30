# 🛠️ PC Forge – Custom PC Builder Web App

**PC Forge** is a full-stack web platform for building custom PCs, managing inventory, and processing customer orders. Designed with flexibility, performance, and user clarity in mind, it supports multiple user roles—including customers, employees, and administrators—with dynamic CRUD operations, part compatibility validation, and real-time order workflows.

---

## 🚀 Key Features

- 🔧 **PC Builder Tool**  
  Guides users in building compatible PCs by selecting from a curated set of components (CPU, GPU, PSU, etc.). The system ensures all selections work together and adds the entire build directly to the cart.

- 🛒 **Live Cart & Seamless Checkout**  
  Users can add items or full builds to a cart and checkout with ease.

- 👤 **Role-Based Access Control**  
  - **Customers** can browse parts, use the builder, place orders, and track them via their profile.  
  - **Employees** can log in to view, claim, and update the status of customer orders.  
  - **Administrators** can do everything employees can *plus*:  
    - Create, edit, or remove products  
    - Manage user accounts (employees & customers)  
    - View analytics  
    - Moderate customer messages via a message center

- 📊 **Analytics Dashboard**  
  Admins get insight into site activity, user engagement, and performance metrics.

- 🔍 **Smart Filters**  
  Users can filter parts by price, manufacturer, or compatibility to quickly find what fits their budget and build.

- 🎨 **Interactive Product Highlights**  
  Standout parts (like GPUs) feature interactive exploded views, offering a detailed, educational look at internal hardware components.

- 🌐 **Responsive UI**  
  Built using Tailwind CSS and Bootstrap for a clean look across devices.

---

## 🧰 Tech Stack

| Layer         | Technology                      |
|---------------|----------------------------------|
| **Frontend**  | HTML5, Tailwind CSS, Bootstrap, JavaScript |
| **Backend**   | Django (Python), Node.js (async services) |
| **Database**  | SQLite (dev) / PostgreSQL-ready |
| **Other**     | Django REST Framework, Trello (agile), GitHub, DigitalOcean

---

## 📁 Project Structure

```
pcforge/
├── backend/
│   ├── manage.py
│   ├── pcforge/                 # Django project core
│   └── components/             # Part management and APIs
│       ├── models.py
│       ├── views.py
│       ├── serializers.py
│       └── admin.py
├── frontend/
│   ├── templates/
│   │   ├── index.html          # Homepage / PC Builder
│   │   ├── cart.html
│   │   ├── profile.html
│   │   ├── dashboard_admin.html
│   │   └── dashboard_employee.html
│   └── static/
│       ├── css/                # Tailwind, Bootstrap
│       └── js/                 # Cart logic, filtering, animations
├── uploads/                    # Order-related user uploads (ignored by Git)
├── resume-parser-env/          # Python virtual environment (ignored)
└── README.md
```

---

## 💡 How It Works

1. Customers select components through the PC Builder or catalog
2. Compatibility checks ensure valid part combinations
3. Cart stores build; users place orders and track them
4. Employees view & process orders through a dedicated dashboard
5. Admins manage products, users, analytics, and support messages

---

## 🛠️ Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/pcforge.git
cd pcforge
```

### 2. Create and activate a virtual environment

```bash
python -m venv venv
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Migrate and run

```bash
python manage.py migrate
python manage.py runserver
```

Visit `http://127.0.0.1:8000` to access the platform.

---

## 🌐 Live Demo

> http://134.122.115.119/

---

## 📦 Future Improvements

- Payment gateway integration (e.g., Stripe or PayPal)  
- Part benchmarking and side-by-side comparisons  
- Save/load custom builds per user  
- Admin analytics with interactive charts (Plotly, Chart.js)  
- Dark mode toggle

---

## 📸 Screenshots

> *(Add images of PC Builder, dashboards, or exploded GPU animation)*

---

## 👨‍💻 Authors

Zaayan, Bobby, Evan, Josue, Ethan  
**Course:** COSC 3339-01  
**Date:** 5/7/2025

---
