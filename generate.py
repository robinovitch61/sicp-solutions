import requests
from bs4 import BeautifulSoup
import pdfkit
from pypdf import PdfMerger

base_url = "http://community.schemewiki.org/"
start_path = "?SICP-Solutions"

merger = PdfMerger()

def get_links(url, prefix):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    links = [
        base_url + a["href"] for a in soup.find_all("a", href=True)
        if a["href"].startswith(prefix)
    ]
    return links

if __name__ == "__main__":
    print("starting")
    links = get_links(base_url + start_path, prefix="/?sicp-ex-")
    print(f"found {len(links)} links")
    output_pdfs = []
    for start in range(0, len(links), 50):
        output = f"output_{start}-{start+50}.pdf"
        try:
            pdfkit.from_url(links[start:start+50], output, options={"enable-local-file-access": ""})
        except:  # sometimes exits with ProtocolUnknownError, seems ignorable
            pass
        merger.append(output)
        print(output)
    merger.write("output.pdf")
    merger.close()
    print("done!")

