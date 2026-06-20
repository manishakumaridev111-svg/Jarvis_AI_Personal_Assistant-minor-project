from ddgs import DDGS

def search(query):
    try:
        with DDGS() as ddgs:
            results = list(ddgs.text(query, max_results=3))
            if results:
                output = ""
                for r in results:
                    output += r['body'] + " "
                return output.strip()
            else:
                return "No results found."
    except Exception as e:
        return f"Search error: {e}"

if __name__ == "__main__":
    query = input("Search: ")
    result = search(query)
    print(f"Result: {result}")
