# Explore India - Tourism & Destination Portal

A full-featured Django web application for discovering tourist destinations across India (Goa, Kerala, Rajasthan, Himachal, Andaman), filtering by states and seasonal packages, discovering hotels/restaurants, and managing user profiles with Cloudinary media integration.

## 🌟 Key Features
- **Destination Explorer**: Browse destinations filtered by state (Kerala, Goa, Rajasthan, etc.) and season (Honeymoon, Summer, Winter).
- **Search Functionality**: Instant keyword search for destinations across title and description fields.
- **Hotels & Restaurants**: Detailed listings of hotels, prices, and dining specialities.
- **User Authentication & Profiles**: Login, registration, password change, and Cloudinary profile picture uploads.
- **Responsive UI Design**: Built with Bootstrap 5, FontAwesome, and standard Django template inheritance (`base.html`).

## 🛠️ Tech Stack
- **Backend**: Python 3, Django 4.1
- **Database**: SQLite3
- **Media Storage**: Cloudinary API
- **Frontend**: HTML5, CSS3, JavaScript, Bootstrap 5, FontAwesome
- **Form Handling**: Django Crispy Forms (Bootstrap 5)

## 🚀 Setup & Installation

1. **Clone the Repository**
   ```bash
   git clone https://github.com/SewakMeghwal/Explore-India-Tourist.git
   cd Explore-India-Tourist
   ```

2. **Install Dependencies**
   ```bash
   pip install django cloudinary django-crispy-forms crispy-bootstrap5
   ```

3. **Run Database Migrations**
   ```bash
   cd goa_pro
   python manage.py migrate
   ```

4. **Run the Development Server**
   ```bash
   python manage.py runserver
   ```
   Access the application at `http://127.0.0.1:8000/`.

## 🧪 Running Tests
```bash
python manage.py test
```

## ✒️ Author
**Ajeet Kumar** & **Sewak Meghwal**
