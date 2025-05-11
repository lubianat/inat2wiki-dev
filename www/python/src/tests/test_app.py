import os
import sys
import pytest

# ensure the parent directory (src) is on sys.path so app.py can be imported
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import app as myapp
from app import app


@pytest.fixture
def client():
    app.testing = True
    return app.test_client()


def test_index(client):
    response = client.get("/")
    assert response.status_code == 200


def test_parse_obs_supported(monkeypatch, client):
    # Prepare dummy observation data with a supported license
    dummy_obs = {
        "id": 42,
        "taxon": {"min_species_taxon_id": 42, "name": "TestTaxon"},
        "photos": [
            {"url": "http://example.com/image_square.jpg", "license_code": "cc-by"}
        ],
    }
    # Monkey-patch external dependencies
    monkeypatch.setattr(myapp, "request_observation_data", lambda oid: dummy_obs)
    monkeypatch.setattr(myapp, "lookup_id", lambda taxon_id, prop, default="": "Q42")
    monkeypatch.setattr(
        myapp, "get_commons_url", lambda obs, photo, oid: "http://upload"
    )

    # Call the parse_obs route
    response = client.get("/parse/42")
    assert response.status_code == 200
    html = response.data.decode("utf-8")
    # Should show modified URL and upload button
    assert "image_original.jpg" in html
    assert '<a href="http://upload"' in html
    assert "License: cc-by" in html
    # QID and taxon name should appear
    assert "Q42" in html
    assert "TestTaxon" in html


def test_parse_obs_unsupported(monkeypatch, client):
    # Prepare dummy observation data with an unsupported license
    dummy_obs = {
        "id": 99,
        "taxon": {"min_species_taxon_id": 99, "name": "OtherTaxon"},
        "photos": [
            {"url": "http://example.com/img_square.jpg", "license_code": "cc-by-nc"}
        ],
    }
    # Monkey-patch external dependencies
    monkeypatch.setattr(myapp, "request_observation_data", lambda oid: dummy_obs)
    monkeypatch.setattr(myapp, "lookup_id", lambda taxon_id, prop, default="": "")
    monkeypatch.setattr(
        myapp, "get_commons_url", lambda obs, photo, oid: "License not supported"
    )

    # Call the parse_obs route
    response = client.get("/parse/99")
    assert response.status_code == 200
    html = response.data.decode("utf-8")
    # Should show placeholder text for unsupported license
    assert "License not supported" in html
    # No upload button should be rendered
    assert '<a href="http://upload"' not in html
    # Taxon name and observation id should appear
    assert "Observation 99" in html
    assert "OtherTaxon" in html


def test_parse_obs_missing_geojson(monkeypatch, client):
    """
    Observation 279 666 022 has 'geojson': null and currently crashes.
    The view should render a page and fall back gracefully.
    """
    dummy_obs = {
        "id": 279666022,
        "taxon": {"min_species_taxon_id": 999, "name": "GeojsonlessTaxon"},
        "geojson": None,  # <-- culprit
        "photos": [
            {
                "url": "http://example.com/img_square.jpg",
                "license_code": "cc-by",
                "id": 1234,
            }
        ],
        "user": {
            "id": 5678,
            "login": "TestUser",
            "name": "Test User",
        },
        "place_guess": "Test Place",
        "observed_on": "2023-01-01",
    }

    # stub network / helpers
    monkeypatch.setattr(myapp, "request_observation_data", lambda oid: dummy_obs)
    monkeypatch.setattr(myapp, "lookup_id", lambda tid, prop, default="": "")

    resp = client.get("/parse/279666022")
    assert resp.status_code == 200
