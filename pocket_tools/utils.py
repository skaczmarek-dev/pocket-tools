import json
import logging

def jprint(obj):
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)

def setup_logging():
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')