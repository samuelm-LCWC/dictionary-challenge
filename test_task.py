import pytest
from task import task

def test_1():
    expected = {"Needs": 5000, "Wants": 3000, "Savings": 2000}
    result = task(10000)
    assert expected == result

def test_2():
    expected = {"Needs": 25000, "Wants": 15000, "Savings": 10000}
    result = task(50000)
    assert expected == result

def test_3():
    expected = {"Needs": 6725, "Wants": 4035, "Savings": 2690}
    result = task(13450)
    assert expected == result

def test_4():
    expected = {"Needs": 12500, "Wants": 7500, "Savings": 5000}
    result = task(25000)
    assert expected == result

def test_5():
    expected = {"Needs": 173550, "Wants": 104130, "Savings": 69420}
    result = task(347100)
    assert expected == result