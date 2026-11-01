"""Small, platform-independent addition helper."""

from decimal import Decimal, InvalidOperation


def _to_decimal(value: str) -> Decimal:
    # Support Arabic-Indic digits and Arabic decimal separator as well.
    normalized = value.strip().replace("٫", ".").replace("−", "-")
    if not normalized:
        raise ValueError("Please enter both numbers.")
    try:
        number = Decimal(normalized)
    except InvalidOperation as exc:
        raise ValueError("Please enter valid numbers.") from exc
    if not number.is_finite():
        raise ValueError("Please enter finite numbers.")
    return number


def add_numbers(first: str, second: str) -> str:
    """Return the exact decimal sum, formatted without redundant zeroes."""
    result = _to_decimal(first) + _to_decimal(second)
    if not result.is_finite():
        raise ValueError("Result is not finite.")
    formatted = format(result, "f")
    if "." in formatted:
        formatted = formatted.rstrip("0").rstrip(".")
    if formatted in ("-0", ""):
        return "0"
    return formatted
