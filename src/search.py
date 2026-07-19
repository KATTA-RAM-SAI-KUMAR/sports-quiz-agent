from ddgs import DDGS

def search_web(query):
    snippets = []

    with DDGS() as ddgs:
        results = ddgs.text(query, max_results=5)

        for result in results:
            snippets.append(result["body"])

    return snippets