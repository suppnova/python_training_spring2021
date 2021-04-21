import pytest

from homework11.src.hw2 import Order, elder_discount, morning_discount


def test_order_morning_discount():
    order = Order(100, morning_discount)
    assert order.final_price() == 75


def test_order_elder_discount():
    order = Order(100, elder_discount)
    assert order.final_price() == 90


def test_wrong_price():
    with pytest.raises(ValueError):
        Order(-1, elder_discount)
