import json

class JsonGenerator:
    def __init__(self, filename: str):
        self.filename = filename + ".json"

    def generate(self, data):
        with open(self.filename, 'w') as out:
            out.write(json.dumps(data))