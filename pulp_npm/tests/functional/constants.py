# coding=utf-8
"""Constants for Pulp Npm plugin tests."""
from urllib.parse import urljoin

from pulp_smash.constants import PULP_FIXTURES_BASE_URL
from pulp_smash.pulp3.constants import (
    BASE_PUBLISHER_PATH,
    BASE_REMOTE_PATH,
    BASE_REPO_PATH,
    CONTENT_PATH,
)

# FIXME: list any download policies supported by your plugin type here.
# If your plugin supports all download policies, you can import this
# from pulp_smash.pulp3.constants instead.
# DOWNLOAD_POLICIES = ["immediate", "streamed", "on_demand"]
DOWNLOAD_POLICIES = ["immediate"]

# FIXME: replace 'unit' with your own content type names, and duplicate as necessary for each type
NPM_CONTENT_NAME = "npm.unit"

# FIXME: replace 'unit' with your own content type names, and duplicate as necessary for each type
NPM_CONTENT_PATH = urljoin(CONTENT_PATH, "npm/units/")

NPM_REMOTE_PATH = urljoin(BASE_REMOTE_PATH, "npm/npm/")

NPM_REPO_PATH = urljoin(BASE_REPO_PATH, "npm/npm/")

NPM_PUBLISHER_PATH = urljoin(BASE_PUBLISHER_PATH, "npm/npm/")

# FIXME: replace this with your own fixture repository URL and metadata
NPM_FIXTURE_URL = urljoin(PULP_FIXTURES_BASE_URL, "npm/")
"""The URL to a npm repository."""

# FIXME: replace this with the actual number of content units in your test fixture
NPM_FIXTURE_COUNT = 3
"""The number of content units available at :data:`NPM_FIXTURE_URL`."""

NPM_FIXTURE_SUMMARY = {NPM_CONTENT_NAME: NPM_FIXTURE_COUNT}
"""The desired content summary after syncing :data:`NPM_FIXTURE_URL`."""

# FIXME: replace this with the location of one specific content unit of your choosing
NPM_URL = urljoin(NPM_FIXTURE_URL, "")
"""The URL to an npm file at :data:`NPM_FIXTURE_URL`."""

# FIXME: replace this with your own fixture repository URL and metadata
NPM_INVALID_FIXTURE_URL = urljoin(PULP_FIXTURES_BASE_URL, "npm-invalid/")
"""The URL to an invalid npm repository."""

# FIXME: replace this with your own fixture repository URL and metadata
NPM_LARGE_FIXTURE_URL = urljoin(PULP_FIXTURES_BASE_URL, "npm_large/")
"""The URL to a npm repository containing a large number of content units."""

# FIXME: replace this with the actual number of content units in your test fixture
NPM_LARGE_FIXTURE_COUNT = 25
"""The number of content units available at :data:`NPM_LARGE_FIXTURE_URL`."""
