# BuzzFussion

BuzzFussion is a social media platform that allows users to share photos, interact with posts, and follow other users. This fullstack application is built using Django for the backend and a combination of HTML, CSS, and JavaScript for the frontend.

## Features

- **User Authentication**: Register, log in, and manage user profiles.
- **Search Functionality**: Search for other users by username.
- **Photo Upload**: Upload photos and add captions.
- **Post Interaction**: Like, comment on, and view posts.
- **Notifications**: Receive notifications for new messages and activities.
- **Responsive Design**: Mobile-friendly and responsive layout.

## Technologies Used

### Backend

- **Django**: A high-level Python web framework for building the backend.
- **SQLite/PostgreSQL**: Database management systems (configure in `settings.py`).
- **Django Rest Framework**: For building RESTful APIs (if applicable).

### Frontend

- **HTML/CSS**: Markup and styling of the web pages.
- **JavaScript**: For dynamic interactions and handling frontend logic.
- **Tailwind CSS**: Utility-first CSS framework for styling.
- **UIkit**: Lightweight framework for user interface components.
- **Font Awesome**: Icon set for visual elements.

### Deployment

- **Heroku/AWS**: Cloud platforms for deploying the application (configure deployment settings as needed).
- **Docker**: Containerize the application for consistent development and deployment (if used).

## Installation

### Prerequisites

- Python 3.x
- Node.js and npm (for frontend dependencies)
- Virtualenv (for Python virtual environment)

### Setup

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/Patrick4350/buzzFussion.git
   cd buzzfussion
   ```

2. **Create and Activate Virtual Environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows use `venv\Scripts\activate`
   ```

3. **Install Backend Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Apply Migrations**:
   ```bash
   python manage.py migrate
   ```

5. **Create a Superuser** (for admin access):
   ```bash
   python manage.py createsuperuser
   ```

6. **Run the Development Server**:
   ```bash
   python manage.py runserver
   ```

7. **Install Frontend Dependencies** (if applicable):
   ```bash
   npm install
   ```

8. **Build Frontend Assets** (if using a build process):
   ```bash
   npm run build
   ```

## Usage

- **Navigate to** `http://localhost:8000` to access the application locally.
- **Admin Panel**: Access the admin panel at `http://localhost:8000/admin` using the superuser credentials created earlier.

## API Endpoints

- **/api/posts/**: List and create posts.
- **/api/posts/{id}/**: Retrieve, update, or delete a specific post.
- **/api/users/**: List and create users.
- **/api/users/{id}/**: Retrieve, update, or delete a specific user.
- **/api/messages/**: List and send messages.

## Contributing

1. Fork the repository.
2. Create a feature branch (`git checkout -b feature/YourFeature`).
3. Commit your changes (`git commit -am 'Add new feature'`).
4. Push to the branch (`git push origin feature/YourFeature`).
5. Create a new Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact

- **Author**: [Patrick4350](https://github.com/Patrick4350)
- **Email**: pbofah1@gmail.com
