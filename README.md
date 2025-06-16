# 🎓 College Event Management System

A web-based platform designed to simplify and streamline the process of organizing and managing college events such as workshops, fests, and seminars. This system allows admins to efficiently handle events while offering students an easy way to browse, register, and track their participation.

---

## 🚀 Features

### 🔒 Admin Panel
- Create, update, and delete events
- Add event details: name, venue, date & time, availability (open to all or specific departments)
- Track student enrollments in real-time
- Generate and manage QR codes for event check-in

### 👩‍🎓 Student Dashboard
- Browse upcoming events with filters
- One-click registration for events
- View and manage personal enrollment history
- QR code-based check-in for hassle-free entry

---

## 🛠️ Tech Stack

### Frontend
- **React.js**
- **HTML5 & CSS3**
- **Responsive Design** for mobile and desktop views

### Backend
- **Python** with **Django** or **Flask**
- RESTful APIs for event and user management
- Secure user authentication and role-based access control

### Database
- **PostgreSQL** / **MySQL**
- Efficient data modeling for events, users, and registrations


---

## ⚙️ Installation & Setup

### Prerequisites
- Node.js & npm
- Python 3.x
- PostgreSQL or MySQL
- Git

### Steps

1. **Clone the Repository**
   ```bash
   git clone https://github.com/your-username/college-event-management.git
   cd college-event-management

 **Frontend Setup**
- cd frontend
- npm install
- npm start

**Backend Setup**
- cd backend
- pip install -r requirements.txt
- python manage.py runserver


**database Setup**

- Create your database and update credentials in the backend .env or settings.py

- Run migrations:
- python manage.py makemigrations
- python manage.py migrate

**Future Enhancements**
-Role-based notification system

-Email & SMS alerts for registered users

-Analytics dashboard for participation stats

-Integration with college authentication systems
