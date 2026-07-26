import os
from pathlib import Path

import pytest

from core.browser_manager import BrowserManager


ARTIFACTS = Path("artifacts")
SCREENSHOTS = ARTIFACTS / "screenshots"
TRACES = ARTIFACTS / "traces"
VIDEOS = ARTIFACTS / "videos"

SCREENSHOTS.mkdir(parents=True, exist_ok=True)
TRACES.mkdir(parents=True, exist_ok=True)
VIDEOS.mkdir(parents=True, exist_ok=True)


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    setattr(item, "rep_" + report.when, report)


@pytest.fixture()
def page(request):

    playwright, browser = BrowserManager.launch_browser()

    context = browser.new_context(
        record_video_dir=str(VIDEOS)
    )

    context.tracing.start(
        screenshots=True,
        snapshots=True,
        sources=True
    )

    page = context.new_page()

    yield page

    test_name = request.node.name

    if request.node.rep_call.failed:

        page.screenshot(
            path=str(SCREENSHOTS / f"{test_name}.png"),
            full_page=True
        )

        context.tracing.stop(
            path=str(TRACES / f"{test_name}.zip")
        )

    else:

        context.tracing.stop()

    context.close()
    browser.close()
    playwright.stop()