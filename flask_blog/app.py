from flask import Flask, render_template, request, jsonify
from datetime import datetime
import json
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key-here-change-in-production'

# Path to store blog posts
POSTS_FILE = 'posts.json'

def load_posts():
    """Load all blog posts from JSON file"""
    if os.path.exists(POSTS_FILE):
        with open(POSTS_FILE, 'r') as f:
            return json.load(f)
    return []

def save_posts(posts):
    """Save blog posts to JSON file"""
    with open(POSTS_FILE, 'w') as f:
        json.dump(posts, f, indent=2)

@app.route('/')
def home():
    """Home page - display all blog posts"""
    posts = load_posts()
    # Sort posts by date (newest first)
    posts.sort(key=lambda x: x['date'], reverse=True)
    return render_template('index.html', posts=posts)

@app.route('/post/<int:post_id>')
def view_post(post_id):
    """View a single blog post"""
    posts = load_posts()
    post = next((p for p in posts if p['id'] == post_id), None)
    if post is None:
        return render_template('404.html'), 404
    return render_template('post.html', post=post)

@app.route('/create', methods=['GET', 'POST'])
def create_post():
    """Create a new blog post"""
    if request.method == 'POST':
        posts = load_posts()
        new_id = max([p['id'] for p in posts], default=0) + 1
        
        new_post = {
            'id': new_id,
            'title': request.form.get('title'),
            'content': request.form.get('content'),
            'author': request.form.get('author', 'Anonymous'),
            'date': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        }
        
        posts.append(new_post)
        save_posts(posts)
        
        return jsonify({'success': True, 'id': new_id})
    
    return render_template('create.html')

@app.route('/api/posts')
def api_posts():
    """API endpoint to get all posts"""
    posts = load_posts()
    posts.sort(key=lambda x: x['date'], reverse=True)
    return jsonify(posts)

@app.route('/api/posts/<int:post_id>')
def api_post(post_id):
    """API endpoint to get a single post"""
    posts = load_posts()
    post = next((p for p in posts if p['id'] == post_id), None)
    if post is None:
        return jsonify({'error': 'Post not found'}), 404
    return jsonify(post)

@app.errorhandler(404)
def not_found(error):
    """Handle 404 errors"""
    return render_template('404.html'), 404

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
