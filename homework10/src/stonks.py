""" Homework10
Ваша задача спарсить информацию о компаниях, находящихся в индексе S&P 500 с данного сайта: <br>
https://markets.businessinsider.com/index/components/s&p_500

Для каждой компании собрать следующую информацию:
* Текущая стоимость в рублях (конвертацию производить по текущему курсу, взятому с сайта [центробанка РФ]
(http://www.cbr.ru/development/sxml/))
* Код компании (справа от названия компании на странице компании)
* P/E компании (информация находится справа от графика на странице компании)
* Годовой рост/падение компании в процентах (основная таблица)
* Высчитать какую прибыль принесли бы акции компании (в процентах), если бы они были куплены на уровне 52 Week Low и
проданы на уровне 52 Week High (справа от графика на странице компании)

Сохранить итоговую информацию в 4 JSON файла:
1. Топ 10 компаний с самими дорогими акциями в рублях.
2. Топ 10 компаний с самым низким показателем P/E.
3. Топ 10 компаний, которые показали самый высокий рост за последний год
4. Топ 10 комппаний, которые принесли бы наибольшую прибыль, если бы были куплены на самом минимуме и проданы на самом
максимуме за последний год.
<br>Пример формата:
[
{
    "code": "MMM",
    "name": "3M CO.",
    "price" | "P/E" | "growth" | "potential profit" : value,
},
...
]
```
For scrapping you cans use `beautifulsoup4` <br>
For requesting `aiohttp`"""

import asyncio
import json
from datetime import datetime
from typing import Tuple, Union

import aiohttp as aiohttp
import pandas as pd
import requests
from bs4 import BeautifulSoup
from numpy import NaN
from pycbrf.toolbox import ExchangeRates

URL500 = "https://markets.businessinsider.com/index/components/s&p_500"

usd_course = ExchangeRates(str(datetime.now().date()))["USD"].value


def get_title_and_code(soup: BeautifulSoup) -> tuple[str, str]:
    title_code = soup.find("h1", {"class": "price-section__identifiers"}).text.split()
    return title_code[-1], " ".join(title_code[: title_code.index("Stock")])


def get_pe_ratio(soup: BeautifulSoup) -> float:
    ratios = soup.find_all("div", {"class": "snapshot__data-item"})
    for ratio in ratios:
        ratio_text = ratio.text
        if "P/E Ratio" in ratio_text:
            return float(ratio_text.split()[0].replace(",", ""))
    return NaN


def get_potential_profit(soup) -> Union[str, float]:
    highlow = soup.find_all("div", {"id": "snapshot-highlow"})
    if not highlow:
        return NaN
    highlow_text = highlow[0].text.split()
    indexes = [i - 1 for i, item in enumerate(highlow_text) if item == "52"]
    if indexes:
        week_low52, week_high52 = (
            float(highlow_text[i].replace(",", "")) for i in indexes
        )
        return str(round((week_high52 - week_low52) / week_low52 * 100, 2)) + "%"


def get_price(company_row) -> float:
    latest_price_str, _ = company_row[1].text.split()
    latest_price_float = float(latest_price_str.replace(",", ""))
    return round(float(usd_course) * latest_price_float, 2)


async def fetch_company_url(session, url) -> str:
    async with session.get(url) as response:
        return await response.text()


async def parse_company(session, company) -> Tuple[str, str, float, float, str, str]:
    company_row = company.find_all("td")
    href = company_row[0].find("a").get("href")
    price = get_price(company_row)
    _, one_year_growth = company_row[9].text.split()

    url = f"https://markets.businessinsider.com{href}"
    soup = BeautifulSoup(await fetch_company_url(session, url), features="html.parser")

    title, code = get_title_and_code(soup)
    pe_ratio = get_pe_ratio(soup)
    potential_profit = get_potential_profit(soup)

    return code, title, price, pe_ratio, one_year_growth, potential_profit


def create_json_file(file_name, content):
    with open(f"{file_name}.json", "w") as fi:
        res = content.to_json(orient="table", index=False)
        parsed = json.loads(res)["data"]
        fi.write(json.dumps(parsed, indent=4))


async def fetch_page(session, page) -> str:
    url = f"{URL500}{page}"
    async with session.get(url) as response:
        return await response.text()


async def get_pages_htmls(session, pages) -> tuple:
    tasks = []
    for page in pages:
        task = asyncio.create_task(fetch_page(session, page))
        tasks.append(task)
    htmls = await asyncio.gather(*tasks)
    return htmls


async def main():
    start = datetime.now()

    main_soup = BeautifulSoup(requests.get(URL500).text, features="html.parser")
    pages = [
        page.get("href")
        for page in main_soup.find("div", {"class": "finando_paging"}).find_all("a")
    ]

    async with aiohttp.ClientSession() as session:
        htmls = await get_pages_htmls(session, pages)

    async with aiohttp.ClientSession() as session:
        tasks = []
        for html in htmls:
            soup = BeautifulSoup(html, features="html.parser")
            table = soup.find("table", {"class": "table table-small"})
            companies = table.find_all("tr")[1:]
            for company in companies:
                task = asyncio.create_task(parse_company(session, company))
                tasks.append(task)
        await asyncio.gather(*tasks)
        df = pd.DataFrame()
        for task in tasks:
            df = df.append(
                pd.DataFrame(
                    [task.result()],
                    columns=[
                        "code",
                        "name",
                        "price",
                        "P/E",
                        "growth",
                        "potential profit",
                    ],
                ),
                ignore_index=True,
            )
    create_json_file("top10_most_expensive", df.nlargest(10, ["price"]))

    create_json_file("top10_lowest_pe_ratio", df.nsmallest(10, ["P/E"]))

    top_growth_idx = df["growth"].str.strip("%").astype(float).nlargest(10).index
    create_json_file("top_growth", df.loc[top_growth_idx])

    top_profit_idx = (
        df["potential profit"].str.strip("%").astype(float).nlargest(10).index
    )
    create_json_file("top_profit", df.loc[top_profit_idx])

    end = datetime.now()
    print(f"Program execute time: {end - start}")


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
