from bs4 import BeautifulSoup


def parse_html(html_content):
    soup = BeautifulSoup(html_content, 'lxml')
    return soup


def extract_data(soup: BeautifulSoup):
    data = []
    for item in soup.select('a'):
        data.append({
            'title': item.get_text(),
            'link': item.get("href")
        })
    return data
