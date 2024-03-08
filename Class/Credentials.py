from dotenv import load_dotenv
import os

class Credenciales():
    load_dotenv()
    def venv_data():
        key = os.environ.get("Api_key")
        model = os.environ.get("model")
        page = os.environ.get("pag")
        promt = os.environ.get("Promt")
        print(page)
        return key, model, page, promt