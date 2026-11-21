import re

def parse_bank_alert(message: str) -> dict:
    """Extract transaction type, NGN amount, account snippet, and credit status from a Nigerian bank alert."""
    text = " ".join(message.split())
    
    tx_type = "UNKNOWN"
    if re.search(r"\b(CR|Credit|credited|received)\b", text, re.IGNORECASE):
        tx_type = "CREDIT"
    elif re.search(r"\b(DR|Debit|debited|sent)\b", text, re.IGNORECASE):
        tx_type = "DEBIT"
        
    # Match NGN, ₦, or standalone N before digits (never matching 'n' inside words)
    amount_match = re.search(r"(?:NGN|₦|(?<![a-zA-Z])N)\s?([\d,]+(?:\.\d{1,2})?)", text, re.IGNORECASE)
    amount = float(amount_match.group(1).replace(",", "")) if amount_match else None
    
    acct_match = re.search(r"\b(\d{2,4}[\*xX]{3,6}\d{2,4})\b", text)
    account = acct_match.group(1) if acct_match else None
    
    return {
        "type": tx_type,
        "amount_ngn": amount,
        "account": account,
        "is_valid_credit": tx_type == "CREDIT" and amount is not None and amount > 0
    }
