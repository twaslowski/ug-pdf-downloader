import yaml
import re


# Takes a config path in the pattern of confa.confb.confc and returns its entry from the config.yml file
def get_config_element(path):
    args = re.split('\.', path)
    sub_conf = read_config()
    for arg in args:
        sub_conf = sub_conf[arg]
    return sub_conf


def read_config():
    with open('../config.yml') as file:
        return yaml.safe_load(file)
