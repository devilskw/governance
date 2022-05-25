import json

class JsonReader:
    def __init__(self, filename: str):
        self.filename = filename + ".json"

    def read(self):
        json_object = {}
        with open(self.filename, 'r') as file:
            json_object = file.write(json.loads(data))
        return json_object