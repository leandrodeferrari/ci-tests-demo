def add(a, b):
    return a + b

def test_add():
    print("Testing add function...")

    # Primera prueba
    result = add(2, 3)
    print(f"Expected 5, got {result}")
    assert result == 5, f"Test failed for add(2, 3), expected 5 but got {result}"

    # Segunda prueba
    result = add(-1, 1)
    print(f"Expected 0, got {result}")
    assert result == 0, f"Test failed for add(-1, 1), expected 0 but got {result}"

    # Tercera prueba
    result = add(0, 0)
    print(f"Expected 0, got {result}")
    assert result == 0, f"Test failed for add(0, 0), expected 0 but got {result}"

    print("All tests passed!")

if __name__ == "__main__":
    test_add()