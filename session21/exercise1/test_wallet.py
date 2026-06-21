import unittest
from main import (
    validate_amount,
    check_balance,
    InvalidAmountError,
    InsufficientBalanceError
)


class TestWallet(unittest.TestCase):

    def test_deposit_success(self):
        self.assertTrue(validate_amount(100000))

    def test_transfer_insufficient_balance(self):
        with self.assertRaises(InsufficientBalanceError):
            check_balance(100000, 200000)

    def test_invalid_amount(self):
        with self.assertRaises(InvalidAmountError):
            validate_amount(-1000)


unittest.main()
