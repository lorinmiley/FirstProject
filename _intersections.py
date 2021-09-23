
def funct(x):
    return x + 1

# content of test_class.py
class TestClass:
    def test_one(self):
        assert funct(3) == 5
    def test_two(self):
        assert funct(3) == 4