from src.database import load_data, search_data

load_data()

results = search_data("Cricket")

print(results)