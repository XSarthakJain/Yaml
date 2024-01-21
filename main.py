import yaml
from pprint import pprint

with open('config.yaml','r') as file:
    config: dict = yaml.safe_load(file)
pprint(config,sort_dicts=False)