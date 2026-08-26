# Flask Blog

A simple, elegant blogging platform built with Flask.

## Features

- **Create Posts**: Write and publish new blog posts
- **View Posts**: Display all posts on the home page
- **Read Full Posts**: View individual blog posts
- **RESTful API**: JSON endpoints for programmatic access
- **Responsive Design**: Mobile-friendly interface
- **JSON Storage**: Posts stored in `posts.json` file

## Project Structure

```
flask_blog/
├── app.py                 # Main Flask application
├── requirements.txt       # Python dependencies
├── posts.json            # Blog posts database (auto-created)
├── templates/
│   ├── base.html         # Base template
│   ├── index.html        # Home page
│   ├── post.html         # Single post view
│   ├── create.html       # Create post form
│   └── 404.html          # Error page
└── static/
    └── style.css         # Stylesheet
```

## Installation

1. Navigate to the flask_blog directory:
   ```bash
   cd flask_blog
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Running the Blog

Start the Flask development server:

```bash
python app.py
```

The blog will be available at `http://localhost:5000`

## API Endpoints

- `GET /` - Home page with all posts
- `GET /post/<id>` - View a single post
- `GET /create` - Create post form
- `POST /create` - Submit new post
- `GET /api/posts` - Get all posts as JSON
- `GET /api/posts/<id>` - Get single post as JSON

## Features

### Home Page
- Displays all blog posts sorted by date (newest first)
- Posts shown as cards with excerpt
- Quick access to create new posts

### Create Post
- Simple form to create new blog posts
- Requires: Title and Content
- Optional: Author name
- Auto-saves with timestamp

### View Post
- Full post content display
- Shows title, author, and publication date
- Navigation back to home

### JSON API
- RESTful endpoints for integration with other applications
- Get posts programmatically

## Configuration

Edit these settings in `app.py`:

```python
app.config['SECRET_KEY'] = 'your-secret-key-here-change-in-production'
```

Change this to a secure random string for production.

## Data Storage

Posts are stored in `posts.json` with the following structure:

```json
[
  {
    "id": 1,
    "title": "First Post",
    "content": "Post content here...",
    "author": "Your Name",
    "date": "2026-08-25 10:30:45"
  }
]
```

## Customization

### Styling
Edit `static/style.css` to customize the look and feel.

### Templates
Modify templates in the `templates/` directory to change layout or add new features.

### Adding Features
Common extensions:
- User authentication
- Comments system
- Categories/tags
- Search functionality
- Database integration (SQLite, PostgreSQL, etc.)

## Deployment

For production deployment:

1. Set `debug=False` in `app.py`
2. Use a production WSGI server (Gunicorn, uWSGI)
3. Set a strong `SECRET_KEY`
4. Configure environment variables
5. Use a proper database instead of JSON

Example with Gunicorn:
```bash
pip install gunicorn
gunicorn -w 4 app:app
```

## License

Free to use for personal and commercial projects.
