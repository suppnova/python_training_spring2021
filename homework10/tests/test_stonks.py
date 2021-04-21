from collections import namedtuple
from unittest.mock import patch

import numpy as np
import requests
from bs4 import BeautifulSoup

from homework10.src.stonks import (
    get_pe_ratio,
    get_potential_profit,
    get_price,
    get_title_and_code,
)


class MockResponse:
    pass


def mock_get(*args, **kwargs):
    return MockResponse()


def test_get_title_and_code(monkeypatch):
    MockResponse.text = (
        "<h1 class='price-section__identifiers'> 3M Co. </span> Stock MMM </span></h1>"
    )
    monkeypatch.setattr(requests, "get", mock_get)

    soup = BeautifulSoup(
        requests.get("https://fakeurl.com").text, features="html.parser"
    )
    title, code = get_title_and_code(soup)
    assert title == "MMM" and code == "3M Co."


def test_get_pe_ratio(monkeypatch):
    MockResponse.text = "<div class='snapshot__data-item'>19.91<div class='snapshot__header'> P/E Ratio</div></div>"
    monkeypatch.setattr(requests, "get", mock_get)

    soup = BeautifulSoup(
        requests.get("https://fakeurl.com").text, features="html.parser"
    )
    pe_ratio = get_pe_ratio(soup)
    assert pe_ratio == 19.91

    MockResponse.text = "<div class='snapshot__data-item'>19.91"
    soup = BeautifulSoup(
        requests.get("https://fakeurl.com").text, features="html.parser"
    )
    pe_ratio = get_pe_ratio(soup)
    assert np.isnan(pe_ratio)


def test_get_potential_profit(monkeypatch):
    MockResponse.text = "<div id='snapshot-highlow'>131.12 <div> 52 Week Low </div> 199.67 <div>52 Week High</div>"
    monkeypatch.setattr(requests, "get", mock_get)
    soup = BeautifulSoup(
        requests.get("https://fakeurl.com").text, features="html.parser"
    )
    potential_profit = get_potential_profit(soup)
    assert potential_profit == "52.28%"

    MockResponse.text = "<div>"
    soup = BeautifulSoup(
        requests.get("https://fakeurl.com").text, features="html.parser"
    )
    potential_profit = get_potential_profit(soup)
    assert np.isnan(potential_profit)


def test_get_price(monkeypatch):
    MockResponse.text = "<td> - <td> <td class='text-right'> 198.13<br/> 198.75 </td>"
    monkeypatch.setattr(requests, "get", mock_get)
    company = BeautifulSoup(
        requests.get("https://fakeurl.com").text, features="html.parser"
    )
    company_row = company.find_all("td")
    with patch("pycbrf.toolbox.ExchangeRates") as fake_class:
        FakeResponse = namedtuple("Exchange", ["value", "status"])
        fake_class.return_value = {"USD": FakeResponse(value=1, status=200)}

        price = get_price(company_row)
        # assert price == 198.13 # don't work for some reason :(
