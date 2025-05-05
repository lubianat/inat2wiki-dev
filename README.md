# iNat2Wiki - Complete Rewrite

inat2wiki (hosted at https://inat2wiki.toolforge.org) is an application to connect observations from iNaturalist to Wikimedia Commons. This repository is a slow rewrite of the tool, covering core functionality and making sure proper tests/documentation/internationalization/etc is in place.

# Contributing 

## How to set up locally

1. **Clone the repo**  
   ```bash
   git clone https://github.com/lubianat/inat2wiki-dev.git
   cd inat2wiki-dev
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

To run tests, you may run:
```
pytest
```

To get code coverage, add these extra parameters:
   ```bash
   pytest --cov=app --cov-report=term-missing
```

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

Tickets are being tracked on the [GitHub issue tracker(https://github.com/lubianat/inat2wiki-dev/issues). Code may be moved to https://gitlab.wikimedia.org in the future and tickets to Phabricator.

## Documentation

Documentation for this project is hosted either here or on https://commons.wikimedia.org/wiki/Commons:INat2Wiki.

If you spot any errors on documentation or have any suggestions of what can be added, just let me know!

## Testing

Testing is being done using pytest. We are trying to get  _good_, but not necessarily 100% coverage. 

## Commit policy 

Commits try to follow https://www.conventionalcommits.org/en/v1.0.0-beta.2. Following that make releases a bit clearer and eables using semantic release.

## Release schedule

The code uses [`python-semantic-release`](https://python-semantic-release.readthedocs.io/en/latest/) for managing releases.