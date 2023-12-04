import os

import pytest


def pytest_configure(config):
    config.addinivalue_line(
        "markers", "skip_ci: skip tests on CI systems like GitHub Actions"
    )


def pytest_collection_modifyitems(config, items):
    if os.getenv("GITHUB_ACTIONS") == "true":
        skip_marker = pytest.mark.skip(reason="Skipping this test on Github Actions")
        for item in items:
            if "skip_ci" in item.keywords:
                item.add_marker(skip_marker)
