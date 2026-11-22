"""NaijaKit: Premium Python utilities for Nigerian developers, fintechs, and SMEs."""

__version__ = "0.2.0"

from .validators import identify_network, calculate_paystack_fee, is_valid_nin_or_bvn, is_valid_nuban
from .parsers import parse_bank_alert
from .locations import STATES, get_state_info

__all__ = [
    "identify_network",
    "calculate_paystack_fee",
    "is_valid_nin_or_bvn",
    "is_valid_nuban",
    "parse_bank_alert",
    "STATES",
    "get_state_info",
]