from behave import fixture, use_fixture
from appium import webdriver
from appium.webdriver.webdriver import AppiumOptions
from dotenv import load_dotenv
from devices.android_capabilities import android_capabilities
from utils.api.auth.auth import Auth
import config as cfg


def update_capabilities(context):
    android_capabilities['appium:deviceName'] = context.device_id
    android_capabilities['appium:app'] = context.app_path


@fixture
def set_up_driver(context):
    """Connect to the Appium server and return a driver."""
    capabilities = {}
    capabilities.update(android_capabilities)

    if context.execution_mode == 'local':
        url = 'http://localhost:4723'
        appium_options = AppiumOptions()
        appium_options.load_capabilities(capabilities)
        context.driver = webdriver.Remote(command_executor=url, options=appium_options)
        context.driver.implicitly_wait(10)
    if context.execution_mode == 'remote':
        ...


def before_all(context):
    """
    Prepares the testing environment by loading necessary configurations and verifying required inputs.
    """
    load_dotenv(override=True)  # reload .env variables, overwriting any existing ones.
    context.access_token = Auth(cfg.ADMIN_USERNAME, cfg.ADMIN_PASSWORD).auth()
    context.platform = context.config.userdata.get('platform', '')
    context.device_id = context.config.userdata.get('device_id', '')
    context.app_path = context.config.userdata.get('app_path', '')
    context.execution_mode = context.config.userdata.get('execution_mode', 'local')
    context.env = context.config.userdata.get('env', 'qa')

    required_inputs = {
        'platform': context.platform,
        'device_id': context.device_id,
        'app_path': context.app_path
    }

    if context.config.userdata.get('execution_mode', 'local') != 'local':
        required_inputs['execution_mode'] = context.config.userdata.get('execution_mode')

    if context.config.userdata.get('env', 'qa') != 'qa':
        required_inputs['env'] = context.config.userdata.get('env')

    missing_inputs = [input_name for input_name, value in required_inputs.items() if not value]

    if missing_inputs:
        error_message = (
                "Missing necessary user inputs: " + ", ".join(missing_inputs) + ". "
                "Please provide all required inputs.\n"
                "Example: behave -D platform=android -D device_id=R5CT71Y78DJ -D app_path=/path/to/app.apk "
                "-D execution_mode=local"
        )
        raise Exception(error_message)

    update_capabilities(context)


def before_feature(context, feature):
    ...


def before_scenario(context, scenario):
    use_fixture(set_up_driver, context)
    ...


def after_scenario(context, scenario):
    ...


def after_feature(context, feature):
    ...


def before_step(context, step):
    ...


def after_step(context, step):
    pass


def after_all(context):
    pass
