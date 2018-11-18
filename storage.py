import json

class Storage:

    def save(filename, data):
        with open(filename, 'w') as file:  
            json.dump(data, file, ensure_ascii=False)

    def load(filename):
        with open(filename) as file:  
            data = json.load(file)
        return data