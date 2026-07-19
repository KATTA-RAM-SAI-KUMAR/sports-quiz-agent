from src.search import search_web

results = search_web("Latest Cricket World Cup news")

print(results)

for i, result in enumerate(results, start=1):
    print(f"\nResult {i}:")
    print(result)