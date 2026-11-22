[![PyPI version](https://shields.io)](https://pypi.org)

# NaijaKit 🇳🇬

**Essential, zero-dependency Python utilities for Nigerian developers, fintechs, and local businesses.**

Built by **Ukasha M. I. Kirfi** in Bauchi, Nigeria.

## Features (v0.1.0)
- **Telecom Network Identifier:** Normalize Nigerian phone numbers (`+234` or `080...`) and detect MTN, Airtel, Glo, or 9mobile.
- **Paystack Fee Calculator:** Accurately compute local NGN transaction fees and net settlement amounts.
- **Bank Alert Parser:** Extract transaction type (`CREDIT`/`DEBIT`), exact NGN amounts, and masked account numbers from Nigerian bank SMS alerts.

## Quickstart
```python
import naijakit

print(naijakit.identify_network("+234 803 123 4567"))
# {'valid': True, 'normalized': '08031234567', 'network': 'MTN'}

print(naijakit.calculate_paystack_fee(15000))
# {'amount': 15000, 'fee': 325.0, 'net_settled': 14675.0}

print(naijakit.parse_bank_alert("Credit Alert! Acct: 012****890 Amt: NGN 25,500.00"))
# {'type': 'CREDIT', 'amount_ngn': 25500.0, 'account': '012****890', 'is_valid_credit': True}
```
