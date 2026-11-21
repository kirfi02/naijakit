import re

PREFIXES = {
    "MTN": {"0703", "0706", "0803", "0806", "0810", "0813", "0814", "0816", "0903", "0906", "0913", "0916"},
    "Airtel": {"0701", "0708", "0802", "0808", "0812", "0901", "0902", "0904", "0907", "0912"},
    "Glo": {"0705", "0805", "0807", "0811", "0815", "0905", "0915"},
    "9mobile": {"0809", "0817", "0818", "0908", "0909"},
}

def identify_network(phone: str) -> dict:
    """Normalize a Nigerian phone number and identify its telecom network."""
    cleaned = re.sub(r"[\s\-+]", "", phone)
    if cleaned.startswith("234") and len(cleaned) == 13:
        cleaned = "0" + cleaned[3:]
    
    if not re.fullmatch(r"0\d{10}", cleaned):
        return {"valid": False, "normalized": None, "network": "Unknown"}
    
    prefix = cleaned[:4]
    network = next((net for net, prefs in PREFIXES.items() if prefix in prefs), "Other")
    return {"valid": True, "normalized": cleaned, "network": network}

def calculate_paystack_fee(amount_ngn: float) -> dict:
    """Calculate standard Nigerian Paystack local transaction fee (1.5% + NGN 100, capped at NGN 2000)."""
    flat_fee = 100.0 if amount_ngn >= 2500 else 0.0
    fee = min((0.015 * amount_ngn) + flat_fee, 2000.0)
    return {
        "amount": round(amount_ngn, 2),
        "fee": round(fee, 2),
        "net_settled": round(amount_ngn - fee, 2),
    }
