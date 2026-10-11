import pytest
import allure
from pathlib import Path

# ========================================================================
# PYTEST + PLAYWRIGHT TEST CONFIGURATION FILE
# ========================================================================

# ----------------------------------------------------------------------------
# STEP 1: HOOK TO TRACK TEST RESULTS (PASS/FAIL/SKIP)
# ----------------------------------------------------------------------------
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """
    Captures the test execution result after each lifecycle phase.
    This is checked later to decide whether to attach debugging artifacts.
    """
    outcome = yield
    report = outcome.get_result()
    setattr(item, f"rep_{report.when}", report)

# ----------------------------------------------------------------------------
# STEP 2: POST-TEST TELEMETRY ARTIFACT MANAGEMENT
# ----------------------------------------------------------------------------
@pytest.fixture(scope="function", autouse=True)
def manage_artifacts(request, page):
    """
    Hooks into the Playwright page lifecycle.
    Let the plugin handle background captures, and attach files to Allure on failure.
    """
    # Pass control immediately to your functional test case logic
    yield page
    
    # Teardown Phase: Evaluate test outcome status post-execution
    test_name = request.node.name
    test_failed = hasattr(request.node, "rep_call") and request.node.rep_call.failed
    
    if test_failed:
        print(f"📊 Test '{test_name}' failed. Attaching forensic evidence to Allure...")
        
        # 📸 1. Capture and attach screenshot if failure occurs
        screenshot_path = f"reports/screenshots/{test_name}.png"
        page.screenshot(path=screenshot_path)
        allure.attach.file(
            screenshot_path,
            name=f"{test_name}_screenshot",
            attachment_type=allure.attachment_type.PNG
        )
        
        # 🎥 2. Extract and attach recorded video asset if available
        video_path = page.video.path() if page.video else None
        if video_path and Path(video_path).exists():
            allure.attach.file(
                video_path,
                name=f"{test_name}_video",
                attachment_type=allure.attachment_type.WEBM
            )




