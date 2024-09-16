import requests
from bs4 import BeautifulSoup


def scrape_website(url):
    # Send a GET request to the URL
    response = requests.get(url)

    # Check if request was successful
    if response.status_code == 200:
        # Parse the HTML content of the webpage
        soup = BeautifulSoup(response.content, 'html.parser')

        # Extract text content from the webpage
        text_content = soup.get_text()

        # Print the text content in a structured format
        print("Text Content:")
        print("=" * 50)
        print(text_content)
        print("=" * 50)
        with open('output.txt', 'w', encoding='utf-8') as file:
            file.write(text_content)
    else:
        print("Failed to retrieve data from the URL.")


# Example usage:
url = input("Enter the URL to scrape: ")
# scrape_website(url)



def scrape_websites(url, output_file):
    # Send a GET request to the URL
    response = requests.get(url)

    # Check if request was successful
    if response.status_code == 200:
        # Parse the HTML content of the webpage
        soup = BeautifulSoup(response.content, 'html.parser')

        # Extract specific data from the webpage
        data = []
        for paragraph in soup.find_all('p'):
            data.append(paragraph.text.strip())
        # for heading in soup.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6']):
            # data.append(heading.text.strip())

        # Write the extracted data to a text file with structured formatting
        with open(output_file, 'w', encoding='utf-8') as file:
            file.write("Extracted Data:\n")
            # file.write("=" * 50 + "\n")
            for item in data:
                file.write(item + "\n")
                # file.write("-" * 50 + "\n")
            # file.write("=" * 50 + "\n")
        print("Data has been written to", output_file)
    else:
        print("Failed to retrieve data from the URL.")
scrape_websites(url,'output.txt')