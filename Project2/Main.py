import wikipediaapi

def wiki_explorer(query):
    wiki_wiki = wikipediaapi.Wikipedia('en')  # 'en' for English Wikipedia, change as needed

    page_py = wiki_wiki.page(query)

    if page_py.exists():
        print("Title:", page_py.title)
        print("Summary:", page_py.summary[:200])  # Display the first 200 characters of the summary
        print("URL:", page_py.fullurl)
        print("Categories:", ", ".join(page_py.categories.keys()))
    else:
        print("Page not found. Please try another query.")

if __name__ == "__main__":
    user_query = input("Enter your query: ")
    wiki_explorer(user_query)
