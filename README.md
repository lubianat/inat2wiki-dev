# 🌿 iNat2Wiki - Complete Rewrite

![Flask](https://img.shields.io/badge/Flask-3.1.0-blue)
[![Code Style: Black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
![i18n](https://img.shields.io/badge/i18n-Babel-green)
[![Last Commit](https://img.shields.io/github/last-commit/lubianat/inat2wiki-dev.svg)](https://github.com/lubianat/inat2wiki-dev/commits/main)

> 🌱 **inat2wiki** is a tool that connects iNaturalist observations to Wikimedia Commons.  
> 🔧 This repo is a full rewrite focused on clean code, testing, documentation, and internationalization.

Hosted at: [https://inat2wiki-dev.toolforge.org](https://inat2wiki-dev.toolforge.org)

The original version of the tool can be found at: [https://inat2wiki.toolforge.org](https://inat2wiki.toolforge.org).

The core logic is managed at the Python module [inat2wiki](https://github.com/lubianat/inat2wiki-module).

---

## 🧑‍💻 Contributing

### 🔧 Local Development Setup

1. **Clone the repo**
   ```bash
   git clone https://github.com/lubianat/inat2wiki-dev.git
   cd inat2wiki-dev
   ```

2. **Create & activate virtual environment**
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate  # Windows: .venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install --upgrade pip
   pip install -r www/python/src/requirements.txt
   ```

4. **Run the app**
   ```bash
   export FLASK_APP=www/python/src/app.py
   export FLASK_ENV=development
   flask run
   ```
   Open [http://127.0.0.1:5000](http://127.0.0.1:5000) in your browser.

5. **Run tests**
   ```bash
   pytest
   ```

   To check coverage:
   ```bash
   pytest --cov=app --cov-report=term-missing
   ```

---

### 🐍 Python / Flask Versions

Built with:
- Python `3.12.3`
- Flask `3.1.0`
- Werkzeug `3.1.3`

---

### 🧹 Code Style

- Formatter: [**Black**](https://github.com/psf/black)

---

### 🌐 Internationalization (i18n)

- Uses **Babel** with configuration in `babel.cfg`
- Translations live in `www/python/src/translations/`
- Default template: `messages.pot`

---

### 📋 Issue Tracking

Issues are tracked on the [GitHub issue tracker](https://github.com/lubianat/inat2wiki-dev/issues).  
We may migrate code to [Wikimedia GitLab](https://gitlab.wikimedia.org) and issues to **Phabricator** in the future.

---

### 📚 Documentation

Project docs are available:
- In this repo
- On [Commons:INat2Wiki](https://commons.wikimedia.org/wiki/Commons:INat2Wiki)

Feel free to suggest improvements or corrections!

---

### 🧪 Testing Philosophy

- Tests live in `www/python/src/tests/`
- Run with `pytest`
- Aiming for **good coverage**, not necessarily 100%

---

### 📝 Commit Policy

We follow [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0-beta.2/)  
➡ Helps with clarity and supports automatic releases.

---

### 🚀 Release Process

Releases are managed using [`python-semantic-release`](https://python-semantic-release.readthedocs.io/en/latest/)

---

## 👥 Contributors

Thanks to everyone who helps build, test, and maintain this tool!

| Name | Role |
|------|------|
| [@lubianat](https://github.com/lubianat) | Creator & Maintainer |

> Want to contribute? Open an issue, send a PR, or just suggest improvements!

---

_This project is released under [The Unlicense](LICENSE)._
