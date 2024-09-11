import pytest
from task import task

@pytest.mark.parametrize(
    "input_value, expected_output",
    [
        (10000, {"Needs": 5000, "Wants": 3000, "Savings": 2000}),
        (50000, {"Needs": 25000, "Wants": 15000, "Savings": 10000}),
        (13450, {"Needs": 6725, "Wants": 4035, "Savings": 2690}),
        (25000, {"Needs": 12500, "Wants": 7500, "Savings": 5000}),
        (347100, {"Needs": 173550, "Wants": 104130, "Savings": 69420}),
    ]
)
def test_task(input_value, expected_output):
    assert task(input_value) == expected_output
