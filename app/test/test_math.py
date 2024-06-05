import pytest

from app.controllers.math import add_numbers 


@pytest.mark.parametrize('test_input, expected', [
                        (3, 9), (-3, -5), (0, 0), (0, 5), (1, 2)])
def test_add_numbers(test_input, expected):

    assert add_numbers(3, 9) == 12