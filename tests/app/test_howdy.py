from app import howdy

def test_say_howdy() -> None:
    expected = "Well howdy, Zackelynn"
    result = howdy.say_howdy("Zackelynn")
    assert result == expected
