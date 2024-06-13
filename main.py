from utils import fetch_url
from utils.parse import parse_html, extract_data
from utils.save import save_to_csv


def main():
    print("starting")
    url = "https://google.com/"
    html_content = fetch_url(url)
    soup = parse_html(html_content)
    data = extract_data(soup)
    save_to_csv(data, "output.csv")


if __name__ == "__main__":
    main()
