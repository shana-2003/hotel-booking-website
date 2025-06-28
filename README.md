# 🍽️ Hotel Table Booking Website

This is a Django-based web application that allows users to **book tables at a hotel restaurant**, view the **menu card**, and check out the **top deals of the day**. It provides a smooth, user-friendly experience for restaurant reservations.

---

## 🌟 Features

- 🔒 **Secure Table Booking System**  
  Customers can easily book a table by filling out a form with their details.

- 📜 **Dynamic Menu Card**  
  The restaurant's full menu is displayed beautifully and can be updated from the backend.

- 💸 **Top Deals of the Day**  
  Daily or special limited-time deals are highlighted on the homepage.



---

## 🛠️ Technologies Used

- **Frontend**: HTML, CSS, Bootstrap  
- **Backend**: Python, Django  
- **Database**: SQLite (default Django database, easy to migrate to MySQL/PostgreSQL)  
- **Templating**: Django Template Language  
- **Static Files**: Managed using Django's static files system

---

## 🚀 Getting Started

### Prerequisites

- Python 3.x
- pip (Python package manager)
- Django

## 📂 Folder Structure

django_course/
├── django_tutorial/
│ ├── settings.py
│ ├── urls.py
│ ├── asgi.py
│ ├── wsgi.py
│ ├── __init__.py

├── home/
│ ├── models.py
│ ├── views.py
│ ├── urls.py
│ ├── admin.py
│ ├── apps.py
│ ├── forms.py
│ ├── tests.py
│ └── templates/
│ ├── base.html
│ ├── booking.html
│ └── confirm.html
│ ├── deals.html
│ ├── menu.html
│ ├── about.html
│ ├── contact.html
├── static/
│ └── css/
│ └── images
│ └── js
└── manage.py

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/hotel-table-booking.git
   cd hotel-table-booking
   
