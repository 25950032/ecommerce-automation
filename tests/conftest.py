
import os
import pytest
import allure


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        page = item.funcargs.get("page")

        if page:
            os.makedirs("reports/screenshots", exist_ok=True)

            screenshot_path = (
                f"reports/screenshots/{item.name}.png"
            )

            page.screenshot(
                path=screenshot_path,
                full_page=True
            )

            allure.attach.file(
                screenshot_path,
                name="Screenshot on failure",
                attachment_type=allure.attachment_type.PNG
            )
