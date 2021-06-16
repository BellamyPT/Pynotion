import requests

TOKEN = "YOUR TOKEN"
DATABASE_ID = "YOUR DB ID"
NOTION_URL = "https://api.notion.com/v1/databases"


class Pynotion:
    def __init__(self):
        pass

    def query_databases(self):
        database_url = f"{NOTION_URL}/{DATABASE_ID}"
        headers = {
            "Authorization": f"Bearer {TOKEN}",
            "Notion-Version": "2021-05-13",
            "Content-Type": "application/json",
        }
        print(database_url)
        response = requests.request("GET", database_url, headers=headers)
        try:
            response.raise_for_status()
        except requests.exceptions.HTTPError as e:
            return "Error: " + str(e)

        json_obj = response.json()
        return json_obj


nsync = Pynotion()
data = nsync.query_databases()
print(data)
print(type(data))
