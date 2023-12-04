import configparser
import os
from typing import Optional

# ------------------------------------------------------------------------
# ZeroLink Settings
# ------------------------------------------------------------------------

# Depending on the OS read the zerolink config file from the right place
if os.name == "nt":
    CONFIG_FILE = os.path.join(os.environ["APPDATA"], "zerolink", "config")
elif os.name == "posix":
    CONFIG_FILE = os.path.join(os.environ["HOME"], ".config", "zerolink", "config")
elif os.name == "darwin":
    CONFIG_FILE = os.path.join(
        os.environ["HOME"], "Library", "Application Support", "zerolink", "config"
    )
else:
    raise SystemError(f"Unsupported OS: {os.name}")

# default_server_url = "https://api.zerolink.io"
default_server_url = "http://localhost:8000"

# default_ssl = True

default_config = f"""
[default]
api_key = null
api_prefix = /api
api_version = v1
server_url = {default_server_url}
debug = false
use_ssl = true
enable_aws = false
"""

default_section = "default"


# Create the config file if it doesn't exist
def create_config() -> None:
    """
    Creates the config file if it doesn't exist.
    """
    if not os.path.exists(CONFIG_FILE):
        os.makedirs(os.path.dirname(CONFIG_FILE), exist_ok=True)
        with open(CONFIG_FILE, "w") as f:
            f.write(default_config)
    else:
        # print(f"Config file already exists: {CONFIG_FILE}")
        return


def get_config() -> configparser.ConfigParser:
    """
    Returns the config file as a ConfigParser object.
    """
    create_config()
    config = configparser.ConfigParser()
    config.read(CONFIG_FILE)
    return config


def get_config_path() -> str:
    """
    Returns the path to the config file.
    """
    return CONFIG_FILE


def get_config_var(var: str) -> str:
    """
    Returns the value of the config variable.
    """
    config = get_config()
    return config[default_section].get(var)


def write_config_var(var: str, value: str):
    """
    Writes the config variable to the config file.
    """
    config = get_config()
    config[default_section][var] = value
    with open(CONFIG_FILE, "w") as f:
        config.write(f)


def write_api_key(api_key: str):
    """
    Writes the api key to the config file.
    """
    config = get_config()
    config["default"]["api_key"] = api_key
    with open(CONFIG_FILE, "w") as f:
        config.write(f)


def read_api_key() -> Optional[str]:
    """
    Reads the api key from the config file.
    """
    # Use the environment variable if it exists
    api_key_var = os.environ.get("ZEROLINK_API_KEY")
    # Else read the api key from the config file
    if api_key_var:
        return api_key_var
    else:
        config = get_config()
        return config["default"].get("api_key")


# ------------------------------------------------------------------------
# Config Variables
# ------------------------------------------------------------------------

# Read the config file
config = get_config()

# Set the api key from the config file
api_key = config[default_section].get("api_key")
api_prefix = config[default_section].get("api_prefix")
api_version = config[default_section].get("api_version")
server_url = config[default_section].get("server_url")
debug = config[default_section].getboolean("debug")
use_ssl = config[default_section].getboolean("use_ssl")
enable_aws = config[default_section].getboolean("enable_aws")
enterprise = server_url != default_server_url

# ------------------------------------------------------------------------
# AWS Config Variables
# ------------------------------------------------------------------------

aws_credentials_file = os.path.join(os.environ["HOME"], ".aws", "credentials")
aws_config_file = os.path.join(os.environ["HOME"], ".aws", "config")

aws_region = None
aws_access_key_id = None
aws_secret_access_key = None

if enable_aws:
    if os.path.exists(aws_credentials_file):
        # Read the aws credentials file if it exists
        aws_config = configparser.ConfigParser()
        aws_config.read(aws_credentials_file)
        aws_access_key_id = aws_config["default"]["aws_access_key_id"]
        aws_secret_access_key = aws_config["default"]["aws_secret_access_key"]

    if os.path.exists(aws_config_file):
        # Read the aws config file if it exists
        aws_config = configparser.ConfigParser()
        aws_config.read(aws_config_file)
        aws_region = aws_config["default"]["region"]
