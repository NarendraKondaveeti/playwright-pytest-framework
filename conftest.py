from pathlib import Path
import pytest

from core.browser_manager import BrowserManager

# ======================================================
# Artifact Folders
# ======================================================

ARTIFACTS = Path("artifacts")

SCREENSHOT_DIR = ARTIFACTS / "screenshots"
TRACE_DIR = ARTIFACTS / "traces"
VIDEO_DIR = ARTIFACTS / "videos"
LOG_DIR = ARTIFACTS / "logs"

SCREENSHOT_DIR.mkdir(parents=True, exist_ok=True)
TRACE_DIR.mkdir(parents=True, exist_ok=True)
VIDEO_DIR.mkdir(parents=True, exist_ok=True)
LOG_DIR.mkdir(parents=True, exist_ok=True)


# ======================================================
# Pytest Hook
# ======================================================

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):

    outcome = yield
    report = outcome.get_result()

    setattr(item, "rep_" + report.when, report)


# ======================================================
# Browser Fixture
# Launch Browser ONLY ONCE
# ======================================================

@pytest.fixture(scope="session")
def browser():

    print(f"Browser Fixture ID : {id(object())}")

    playwright, browser = BrowserManager.launch_browser()

    yield browser

    browser.close()
    playwright.stop()


# ======================================================
# Page Fixture
# New Context for Every Test
# ======================================================

@pytest.fixture(scope="function")
def page(browser, request):

    context = browser.new_context(

        record_video_dir=str(VIDEO_DIR)

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

            path=str(SCREENSHOT_DIR / f"{test_name}.png"),
            full_page=True

        )

        context.tracing.stop(

            path=str(TRACE_DIR / f"{test_name}.zip")

        )

    else:

        context.tracing.stop()

    context.close()