import yaml


class Config:
    def __init__(self, config_file):
        with open(config_file) as f:
            data = yaml.load(f, Loader=yaml.FullLoader)
        self.token = data["token"]
        self.databases = data["databases"]
        self.notion_url = data["notion_url"]
        self.headers = {
            "Authorization": f"Bearer {data['token']}",
            "Notion-Version": "2021-05-13",
            "Content-Type": "application/json",
        }


config = Config("config.yml")
