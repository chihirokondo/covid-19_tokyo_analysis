import requests


def get_and_store_csv():
    URL = "https://stopcovid19.metro.tokyo.lg.jp/data/130001_tokyo_covid19_patients.csv"
    response = requests.get(URL)
    with open('covid-19_tokyo.csv', mode='w') as f:
        f.write(response.text)


if __name__ == "__main__":
    get_and_store_csv()