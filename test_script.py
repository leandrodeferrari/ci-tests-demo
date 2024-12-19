import sys

def add(a, b):
    return a - b  # Probando que tire error

def test_add():
    try:
        assert add(2, 3) == 5
        assert add(-1, 1) == 0
        assert add(0, 0) == 0
        print("All tests passed!")
    except AssertionError:
        print("Test failed!")
        sys.exit(1)  # Código de error

if __name__ == "__main__":
    test_add()