from typing import Dict, List
import requests

from Config import config


class PyNotion:
    def __init__(self):
        pass

    def retrieve_databases(self, database: str):
        database_url = f"{config.notion_url}/{database}"
        response = requests.get(database_url, headers=config.headers)
        try:
            response.raise_for_status()
        except requests.exceptions.HTTPError as e:
            return "Error: " + str(e)

        json_obj = response.json()
        return json_obj

    def query_databases(
        self,
        database: str,
        filter: Dict = None,
        sorts: List = None,
        start_cursor: str = None,
        page_size: int = None,
    ):
        database_url = f"{config.notion_url}/{database}/query"
        payload = {"page_size": page_size}
        response = requests.post(database_url, headers=config.headers, data=payload)
        try:

            response.raise_for_status()
        except requests.exceptions.HTTPError as e:
            return "Error: " + str(e)

        json_obj = response.json()
        return json_obj


notion_obj = PyNotion()
# data = notion_obj.query_databases(config.databases["actions"])
data = notion_obj.query_databases(config.databases["actions"], page_size=20)

print(data)
