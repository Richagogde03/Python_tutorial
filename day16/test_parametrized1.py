import pytest
from parametrized1 import isPrime


@pytest.mark.parametrize("num, expected",
                         [(1, False),
                          (2, True),
                          (3, True),
                          (4, False),
                          (17, True),
                          (18, False),
                          (19, True),
                          (25, False),
                          ])
def test_isPrime(num, expected):
    assert isPrime(num) == expected
