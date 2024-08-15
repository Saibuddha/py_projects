import sys
import webbrowser


# Dictionary of categories with associated URLs
sites_cat = {
    "nodes": ["https://app.getgrass.io/dashboard", "https://app.nodepay.ai/dashboard"],
    "adtasks": ["https://app.galxe.com/quest/spaces/all", "https://www.intract.io/"]
}

# Function to open a list of URLs in the web browser
def open_websites(urls):
    for url in urls:
        print(f"Opening: {url}")
        webbrowser.open(url)

if __name__ == "__main__":
    # Check if a command-line argument is provided
    if len(sys.argv) < 2:
        print("Error: Please provide a category name (e.g., 'nodes' or 'adtasks').")
    else:
        set_name = sys.argv[1]  # Get the category name from command-line argument
        urls = sites_cat.get(set_name)  # Retrieve the URLs for the given category
        
        if urls:
            open_websites(urls)  # Open the URLs in the web browser
        else:
            print(f"Error: Category '{set_name}' not found.")
