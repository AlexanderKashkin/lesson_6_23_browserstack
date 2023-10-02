import os

import pytest
from appium.options.android import UiAutomator2Options
from selene import browser

import config
from utils import (allure_attach_browserstack_screenshot, allure_attach_browserstack_video)


@pytest.fixture(scope='function', autouse=True)
def mobile_management():
    options = UiAutomator2Options().load_capabilities({
        "platformName": config.settings.android_platform,
        "platformVersion": config.settings.android_version,
        "deviceName": config.settings.android_device,

        # Set URL of the application under test
        'app': config.settings.app_url,

        # Set other BrowserStack capabilities
        'bstack:options': {
            'projectName': config.settings.project_name,
            'buildName': config.settings.build_name,
            'sessionName': config.settings.session_name,

            # Set your access credentials
            "userName": os.getenv('LOGIN'),
            "accessKey": os.getenv('PASSWORD')
        }
    })

    browser.config.driver_remote_url = config.settings.browserstack_url
    browser.config.driver_options = options

    browser.config.timeout = float(os.getenv('timeout', '10.0'))

    yield
    allure_attach_browserstack_screenshot()
    session_id = browser.driver.session_id
    allure_attach_browserstack_video(session_id)
    browser.quit()
