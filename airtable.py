import logging
import requests
import os


def post(karma_data):
    airtable_base_id = os.getenv("AIRTABLE_BASE_ID")
    airtable_table_name = os.getenv("AIRTABLE_TABLE_NAME")
    airtable_api_key = os.getenv("AIRTABLE_API_KEY")

    url = f"https://api.airtable.com/v0/{airtable_base_id}/{airtable_table_name}"
    headers = {
        "Authorization": f"Bearer {airtable_api_key}",
        "Content-Type": "application/json"
    }

    records = []
    for user in karma_data["users"]:
        record = {
            "fields": {
                "Name": user,
                "Description": karma_data["reason"],
                "Points": karma_data["karmas"]
            }
        }
        records.append(record)

    data = {"records": records}

    # Send POST request to Airtable
    response = requests.post(url, headers=headers, json=data)
    if response.status_code == 200:
        logging.debug("Karma data posted to Airtable successfully.")
    else:
        logging.debug((
            f"Failed to post to Airtable. Status code: {response.status_code}"
        ))
