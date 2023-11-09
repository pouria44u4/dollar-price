def price_of_a_currency_getter(currency) -> str:
    from requests import get
    from bs4 import BeautifulSoup

    #--------------------------------------------------

    html = get(f'https://www.tgju.org/profile/price_{currency}')
    html = html.text
    soup = BeautifulSoup(html, 'html.parser')
    data_2 = f'{soup.find("h1", attrs={"class": "title"}).text} --> {soup.find("span", attrs={"data-col": "info.last_trade.PDrCotVal"}).text}'
    data_2 = data_2.replace('\n', '')
    return data_2