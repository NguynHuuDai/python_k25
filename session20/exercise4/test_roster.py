import unittest
from main import calculate_actual_pay


class TestCalculateActualPay(unittest.TestCase):

    def test_active_player(self):
        player = {
            "player_id": "P01",
            "name": "Faker",
            "role": "Mid Lane",
            "salary": 5000.0,
            "status": "Active"
        }

        self.assertEqual(
            calculate_actual_pay(player),
            5000.0
        )

    def test_benched_player(self):
        player = {
            "player_id": "P03",
            "name": "Ruler",
            "role": "ADC",
            "salary": 6000.0,
            "status": "Benched"
        }

        self.assertEqual(
            calculate_actual_pay(player),
            3000.0
        )


if __name__ == "__main__":
    unittest.main()
