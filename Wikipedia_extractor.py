# This is a function built to extract text from wikipedia pages

import wikipediaapi

def extract_text_from_wikipedia(page_title):
    # Create a Wikipedia API object
    wiki_api = wikipediaapi.Wikipedia('en')

    # Fetch the page using the provided page title
    page = wiki_api.page(page_title)

    # Extract content from page if page exists
    if page.exists():
        text = page.text
        print("Success!")
        return text
    else:
        print("Page not found, please choose an available page.")
        return None

page_title = "Suppot Vector Machines"
text = extract_text_from_wikipedia(page_title)
if text:
    print(text)
