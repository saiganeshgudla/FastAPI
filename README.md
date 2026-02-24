# 📋 Flask + Google Sheets Auth App

> A fun little web app that lets users **sign up & log in** — powered by **Flask** 🐍 and **Google Sheets** as the database! No heavy database setup needed. Just connect, code, and go! 🚀

---

## ✨ What Can It Do?

| Feature | Description |
|---|---|
| 🆕 **Sign Up** | Create a new account with a username & password |
| 🔑 **Log In** | Authenticate safely with hashed passwords |
| 🔒 **Secure Passwords** | Stored using PBKDF2-SHA256 hashing — never plain text! |
| 📊 **Google Sheets DB** | Your users live in a Google Sheet — no SQL needed! |
| 💬 **Flash Messages** | Friendly feedback messages for every action |

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| 🐍 Backend | Flask (Python) |
| 🔒 Auth | werkzeug password hashing |
| 📊 Database | Google Sheets via `gspread` |
| 🔑 API Auth | Google Service Account (OAuth2) |
| 🤫 Secrets | `python-dotenv` + `.env` file |

---

## 📁 Project Structure

```
📦 FastAPI/
├── 🐍 app.py                # Main Flask application
├── 🔒 credentials.json      # Google Service Account key (gitignored!)
├── 🤫 .env                  # Secret keys (gitignored!)
├── 🙈 .gitignore            # Keeps secrets safe from Git
├── 📦 requirements.txt      # All Python dependencies
├── 🎨 static/
│   └── style.css            # App styles
└── 📄 templates/
    ├── signup.html          # Signup page
    └── login.html           # Login page
```

---

## ⚙️ Getting Started

Follow these steps and you'll be up and running in no time! 🏃

### 1️⃣ Clone the repo
```bash
git clone https://github.com/your-username/your-repo.git
cd your-repo
```

### 2️⃣ Create a virtual environment
```bash
python3 -m venv venv
source venv/bin/activate       # 🍎 macOS/Linux
venv\Scripts\activate          # 🪟 Windows
```

### 3️⃣ Install dependencies
```bash
pip install -r requirements.txt
```

### 4️⃣ Set up Google Sheets API 📊

1. 🌐 Go to [Google Cloud Console](https://console.cloud.google.com/)
2. ➕ Create a new project → Enable **Google Sheets API** and **Google Drive API**
3. 👤 Create a **Service Account** → Download the JSON key
4. 📂 Rename it to `credentials.json` and drop it in the project root
5. 📋 Create a Google Sheet named **`FlaskUsers`** with columns: `username` | `password`
6. 📤 Share that sheet with the service account email (found under `client_email` in `credentials.json`)

### 5️⃣ Set up your `.env` file 🤫

Create a `.env` file in the root folder:
```env
FLASK_SECRET_KEY=your-strong-random-secret-key
```

> 💡 Need a secure key? Generate one instantly:
> ```bash
> python3 -c "import secrets; print(secrets.token_hex(32))"
> ```

### 6️⃣ Run the app! 🎉
```bash
python app.py
```

Open your browser and visit 👉 **[http://localhost:5000](http://localhost:5000)**

---

## 🔗 Available Routes

| Route | Method | What it does |
|---|---|---|
| `/` | GET | 🔄 Redirects to signup |
| `/signup` | GET, POST | 🆕 Register a new user |
| `/login` | GET, POST | 🔑 Log in an existing user |

---

## 🔐 Security Tips

- 🙈 `credentials.json` and `.env` are in `.gitignore` — **never commit them!**
- 🔒 Passwords are **always hashed** with PBKDF2-SHA256 before being stored
- 🎲 Your `FLASK_SECRET_KEY` should be a long, random string — keep it secret!
- ♻️ Rotate your Google Service Account key if you ever think it's been exposed

---

## 📦 Dependencies

```txt
flask
gspread
oauth2client
werkzeug
python-dotenv
```

Install them all in one shot:
```bash
pip install -r requirements.txt
```

---

## 🤝 Contributing

Got ideas to improve this? Feel free to fork it, tweak it, and open a PR! All contributions are welcome 💙

---

## 📄 License

Open-source and free to use. Do cool things with it! 🌟
