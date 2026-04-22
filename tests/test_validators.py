from bot.validators import validate_symbol


def test_validate_symbol_placeholder():
    assert validate_symbol("BTCUSDT") is True