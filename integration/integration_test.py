# To check if a number is prime.
# If it's prime, return true, otherwise, return false
# Create Date: 2024/6/7
# Author: Bin Hu

import pytest

# create a function to check if a number is prime.
def check_prime(i):
    if i == 1:
        return False
    if i == 2:
        return True
    for j in range(2, i-1):
        if i % j == 0:
            return False
    return True

# case 1: check if '13' is prime. make the case PASS as the requirement.
def test_case1_check_prime():
    assert check_prime(13) is True

# case 2: check if '17' is prime. make the case FAIL as the requirement.
def test_case2_check_prime():
    assert check_prime(17) is False


if __name__ == '__main__':
    pytest.main(['-s'])
