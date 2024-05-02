from lbox.example.logo import coffee

class TestLogo:

    def test_logo(self):
        result = coffee()
        assert result == "c[_]"