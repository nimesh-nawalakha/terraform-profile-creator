from webscrapper_service import scrape_terraform_documentation

# URL of the webpage you want to scrape
url = 'https://registry.terraform.io/providers/hashicorp/azurerm/latest/docs/resources/databricks_workspace'

# Call the web scraper function
if __name__ == "__main__":
    li_texts = scrape_terraform_documentation(url)
    for text in li_texts:
        print(text)