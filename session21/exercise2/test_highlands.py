import unittest

from pos_logic import (
    calculate_total,
    add_to_order,
    InvalidQuantityError
)


class TestHighlandsPOS(unittest.TestCase):

    def test_calculate_total(self):
        mock_order = [
            {
                "code": "P1",
                "quantity": 2
            },
            {
                "code": "F1",
                "quantity": 1
            }
        ]

        result = calculate_total(
            mock_order
        )

        self.assertEqual(
            result,
            125000
        )

    def test_invalid_quantity(self):

        mock_order = []

        with self.assertRaises(
            InvalidQuantityError
        ):
            add_to_order(
                mock_order,
                "P1",
                -1
            )


if __name__ == "__main__":
    unittest.main()
