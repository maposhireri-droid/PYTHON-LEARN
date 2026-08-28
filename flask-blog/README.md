# Learning Journey Blog (Flask)

A small Flask app that renders your CS learning journey as a "git log" —
each phase of learning shown as a commit you can click to expand.

## Run it locally

```bash
pip install -r requirements.txt
python app.py
```

Then open **http://127.0.0.1:5000** in your browser.

## Deploy it for free (pick one)

### Option A — Render.com (easiest, free tier)
1. Push this folder to a GitHub repo (you already have `PYTHON-LEARN` —
   you could add this as a new folder/repo).
2. Go to https://render.com → New → Web Service → connect your GitHub repo.
3. Set:
   - **Build command:** `pip install -r requirements.txt`
   - **Start command:** `gunicorn app:app`
4. Click Deploy. Render gives you a live `https://yourapp.onrender.com` URL.

### Option B — PythonAnywhere (good if you're on mobile)
1. Create a free account at https://www.pythonanywhere.com
2. Upload the files (or clone from GitHub) via their in-browser file manager.
3. Go to the **Web** tab → Add a new web app → Flask → point it at `app.py`.
4. Reload the app. You'll get a URL like `yourname.pythonanywhere.com`.

### Option C — Railway.app
1. https://railway.app → New Project → Deploy from GitHub repo.
2. Railway auto-detects the `Procfile` and deploys it.

## Files
- `app.py` — Flask entry point
- `templates/index.html` — the page
- `static/style.css` — styling
- `static/script.js` — typed-terminal effect + expand/collapse commits
- `requirements.txt`, `Procfile` — deployment config
