"""NaijaKit: Essential Python utilities for Nigerian developers and businesses."""

__version__ = "0.1.0"

from .validators import identify_network, calculate_paystack_fee
from .parsers import parse_bank_alert

__all__ = ["identify_network", "calculate_paystack_fee", "parse_bank_alert"]
