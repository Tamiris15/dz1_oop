class TextFile:
    def __init__(self, filename):
        self.filename = filename
        self.content = ""
    
    def write(self, data):
        self.content = data
        print(f"Записываем в файл {self.filename}: {data}")
    
    def read(self):
        print(f"Читаем из файла {self.filename}")
        return self.content if self.content else "Файл пуст"

class Database:
    def __init__(self, dbname):
        self.dbname = dbname
        self.data = {}
    
    def write(self, data):
        if isinstance(data, dict):
            self.data.update(data)
            print(f"Записываем в базу {self.dbname}: {data}")
        else:
            print("Ошибка: в базу данных можно записывать только словари")
    
    def read(self):
        print(f"Читаем из базы {self.dbname}")
        return self.data if self.data else "База данных пуста"

class NetworkResource:
    def __init__(self, url):
        self.url = url
        self.last_request = None
    
    def write(self, data):
        self.last_request = ("POST", data)
        print(f"Отправляем POST-запрос на {self.url}: {data}")
    
    def read(self):
        if self.last_request and self.last_request[0] == "POST":
            print(f"Получаем ответ от {self.url} на запрос: {self.last_request[1]}")
            return f"Ответ от {self.url}"
        else:
            print(f"Получаем данные с {self.url}")
            return f"Данные с {self.url}"

# DON'T TOUCH UNDER THE LINE
#______________________________________________________________
def process_data(data_source, data=None):
    if data:
        data_source.write(data)
    return data_source.read()

text_file = TextFile("document.txt")
database = Database("users.db")
network = NetworkResource("http://example.com/api")

print(process_data(text_file, "Новый текст"))
print(process_data(database, {"name": "Иван", "age": 25}))
print(process_data(network, "POST data"))
