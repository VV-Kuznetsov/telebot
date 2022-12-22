import importlib
import os, sys

def load_config():
    conf_name = os.environ.get("TG_CONF")
    if conf_name is None:
        conf_name = "dev"
    try:
        return importlib.import_module("settings.{}".format(conf_name))
    except(TypeError, ValueError, ImportError):
        print("Invalid config \"{}\"".format(conf_name))
        sys.exit(1)
