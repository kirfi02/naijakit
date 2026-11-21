import unittest
import naijakit

class TestNaijaKit(unittest.TestCase):
    def test_network_identifier(self):
        res = naijakit.identify_network("+234 803 123 4567")
        self.assertTrue(res["valid"])
        self.assertEqual(res["network"], "MTN")

    def test_paystack_fee(self):
        res = naijakit.calculate_paystack_fee(15000)
        self.assertEqual(res["fee"], 325.0)
        self.assertEqual(res["net_settled"], 14675.0)

    def test_bank_alert_parser(self):
        alert = "Credit Alert! Acct: 012****890 Amt: NGN 25,500.00 Desc: POS Transfer"
        res = naijakit.parse_bank_alert(alert)
        self.assertEqual(res["type"], "CREDIT")
        self.assertEqual(res["amount_ngn"], 25500.0)
        self.assertTrue(res["is_valid_credit"])

if __name__ == "__main__":
    unittest.main()
