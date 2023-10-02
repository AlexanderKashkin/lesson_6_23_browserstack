import allure
import config
from selene import browser
import requests


def allure_attach_browserstack_video(session_id):
    browserstack_session = requests.get(
        f'https://api.browserstack.com/app-automate/sessions/{session_id}.json',
        auth=(config.settings.LOGIN, config.settings.PASSWORD),
    ).json()
    print(browserstack_session)
    video_url = browserstack_session['automation_session']['video_url']

    allure.attach(
        '<html><body>'
        '<video width="100%" height="100%" controls autoplay>'
        f'<source src="{video_url}" type="video/mp4">'
        '</video>'
        '</body></html>',
        name='video recording',
        attachment_type=allure.attachment_type.HTML,
    )


def allure_attach_browserstack_screenshot():
    allure.attach(
            browser.driver.get_screenshot_as_png(),
            name='screenshot',
            attachment_type=allure.attachment_type.PNG
        )
