import json
import requests
import logging
from .utils import jprint

API_ENDPOINT_GET = "https://getpocket.com/v3/get"
HEADERS = {'Content-Type': 'application/json; charset=UTF-8', 'X-Accept': 'application/json'}

def get_pocket_data(settings_file, output_file):

    """
    Fetch data from the Pocket API based on the provided settings file and write output to a JSON file.
    
    Args:
        settings_file (str): Path to the JSON settings file.
        output_file (str): Path to the JSON output file.
    """
    try:
        with open(settings_file, 'r') as f:
            settings = json.load(f)

        # response = requests.get(API_ENDPOINT_GET, headers=HEADERS, json=settings)
        response = requests.get(API_ENDPOINT_GET, settings)

        if response.status_code == 200:
            logging.info(f"Data fetched successfully from {settings_file}")

            # Pretty print response
            jprint(response.json())

            # Save response to a file
            with open(output_file, 'w') as o:
                json.dump(response.json(), o, indent=4)
        else:
            logging.error(f"Failed to fetch data: {response.status_code} - {response.text}")

    except Exception as e:
        logging.error(f"Error occurred: {e}")
