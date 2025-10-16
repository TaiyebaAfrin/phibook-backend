# Phibook - Social Media Platform

Phibook is a modern social media platform built with Django REST Framework backend and React frontend, featuring user profiles, posts, authentication, and subscription plans.

## 🚀 Features

### Core Features

- **User Authentication** - Secure login/register system
- **User Profiles** - Customizable profiles with bios and profile images
- **Post Management** - Create, view, and interact with posts
- **Follow System** - Follow/unfollow other users
- **Like System** - Like and unlike posts
- **Search Functionality** - Find users and content
- **Responsive Design** - Mobile-friendly interface

### Subscription Plans

- **Basic Plan** - $9.99/month - Perfect for getting started
- **Pro Plan** - $19.99/month - Great for professionals
- **Enterprise Plan** - $49.99/month - For large organizations

## 🛠 Tech Stack

### Frontend

- **React** - Frontend framework
- **Chakra UI** - Component library
- **React Router** - Navigation
- **Axios** - API requests

### Backend

- **Django** - Web framework
- **Django REST Framework** - API development
- **SQLite** - Database (development)
- **Pillow** - Image processing
- **CORS Headers** - Cross-origin requests

## 📦 Installation

### Prerequisites

- Python 3.8+
- Node.js 14+
- npm or yarn

### Backend Setup

1. **Navigate to backend directory**

   ```bash
   cd backend
   ```

2. **Create virtual environment**

   ```bash
   # Windows
   python -m venv venv
   venv\Scripts\activate

   # Mac/Linux
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Run migrations**

   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Create superuser** (optional)

   ```bash
   python manage.py createsuperuser
   ```

6. **Start backend server**
   ```bash
   python manage.py runserver
   ```
   Backend runs on `http://localhost:8000`

### Frontend Setup

1. **Navigate to frontend directory**

   ```bash
   cd frontend
   ```

2. **Install dependencies**

   ```bash
   npm install
   ```

3. **Start development server**
   ```bash
   npm start
   ```
   Frontend runs on `http://localhost:3000`

## 🔧 Configuration

### Environment Variables

Create `.env` file in backend directory:

```env
DEBUG=True
SECRET_KEY=your-secret-key-here
ALLOWED_HOSTS=localhost,127.0.0.1
```

### API Endpoints

| Method | Endpoint                  | Description          |
| ------ | ------------------------- | -------------------- |
| POST   | `/api/register/`          | User registration    |
| POST   | `/api/login/`             | User login           |
| POST   | `/api/logout/`            | User logout          |
| GET    | `/api/user/profile/`      | Get user profile     |
| PUT    | `/api/user/update/`       | Update user profile  |
| GET    | `/api/posts/`             | Get all posts        |
| POST   | `/api/posts/create/`      | Create new post      |
| POST   | `/api/follow/<username>/` | Follow/unfollow user |

## 🎯 Usage

### Authentication

1. Register a new account at `/register`
2. Login with your credentials at `/login`
3. Access protected routes after authentication

### Creating Posts

1. Navigate to `/create/post`
2. Write your post content
3. Submit to share with the community

### User Profiles

- Visit `/username` to view any user's profile
- Follow/unfollow users
- View posts from users you follow

### Subscriptions

- Navigate to `/subscriptions` to view available plans
- Click "Subscribe Now" to redirect to payment provider
- Test payment URLs are provided for development

## 📁 Project Structure

```
phibook-sm/
├── backend/
│   ├── manage.py
│   ├── requirements.txt
│   └── your_django_app/
│       ├── models.py
│       ├── views.py
│       ├── urls.py
│       └── serializers.py
└── frontend/
    ├── public/
    ├── src/
    │   ├── components/
    │   ├── routes/
    │   ├── contexts/
    │   ├── api/
    │   └── constants/
    └── package.json
```

## 🚀 Deployment

### Backend Deployment

```bash
# Collect static files
python manage.py collectstatic

# Set DEBUG=False in production
# Use production database (PostgreSQL recommended)
# Configure allowed hosts
```

### Frontend Deployment

```bash
# Build for production
npm run build

# Deploy build folder to static hosting
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🐛 Troubleshooting

### Common Issues

1. **Pillow not installed**

   ```bash
   pip install Pillow
   ```

2. **CORS errors**

   ```bash
   pip install django-cors-headers
   ```

3. **Migration issues**

   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

4. **Node modules issues**
   ```bash
   npm install
   rm -rf node_modules package-lock.json
   npm install
   ```

## 📞 Support

For support, please open an issue in the GitHub repository or contact the development team.

---

**Note**: This is a development version. For production use, ensure proper security measures, environment configuration, and database setup.
