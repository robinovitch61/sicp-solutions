import requests
from bs4 import BeautifulSoup
import pdfkit

base_url = "http://community.schemewiki.org/"
start_path = "?SICP-Solutions"

def get_links(url, prefix):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    links = [
        a["href"] for a in soup.find_all("a", href=True)
        if a["href"].startswith(prefix)
    ]
    return links

def get_content(links, base_url):
    content = ""
    for link in links:
        full_url = base_url + link
        print(full_url)
        response = requests.get(full_url)
        content += response.text + "\n\n"
    return content

def save_to_pdf(content, output_file="output.pdf"):
    pdfkit.from_string(content, output_file)

if __name__ == "__main__":
    start_page_url = base_url + start_path
    links = get_links(start_page_url, prefix="/?sicp-ex-")
    content = get_content(links, base_url)
    save_to_pdf(content)
    print("done!")

