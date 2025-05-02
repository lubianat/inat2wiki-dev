## How to set up locally on your machine

1. **Clone the repo**  
   ```bash
   git clone https://github.com/lubianat/inat2wiki-new.git
   cd inat2wiki-new
   ```

2. **Create & activate venv**  
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate   # on Windows: .venv\Scripts\activate
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
   Then open <http://127.0.0.1:5000> in your browser.

5. **Run tests**  
   ```bash
   pytest --cov=app --cov-report=term-missing

## Compatible Python/Flask versions

Created with:

```
Python 3.12.3
Flask 3.1.0
Werkzeug 3.1.3
```

## Linter/Formatter used

The code is linted with [black](https://github.com/psf/black). 

## Ticket management

Tickets are being tracked on GitHub. ICode may be moved to https://gitlab.wikimedia.org in the future and tickets to Phabricator.

## Documentation

--> Where does documentation live? --> Still not figured out

## Testing

Testing is being done using pytest. Trying to get  _good_, but not necessarily 100% coverage. 

## Commit policy 

Commits try to follow https://www.conventionalcommits.org/en/v1.0.0-beta.2. Following that make releases a bit clearer and eables using semantic release.


## Release schedule

The code uses [`python-semantic-release`](https://python-semantic-release.readthedocs.io/en/latest/) for managing releases.

## Documentation

On-wiki documentation is hosted on https://commons.wikimedia.org/wiki/Commons:INat2Wiki.