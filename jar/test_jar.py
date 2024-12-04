import pytest
from jar import Jar

def test_init():
    # Test jar initialization with valid and invalid capacities
    jar = Jar()
    assert jar.capacity == 12  # Default capacity
    assert jar.size == 0  # Starts empty

    jar = Jar(5)
    assert jar.capacity == 5
    assert jar.size == 0

    # Invalid capacities should raise ValueError
    with pytest.raises(ValueError):
        Jar(-1)

    with pytest.raises(ValueError):
        Jar("not an integer")


def test_str():
    # Test string representation of the jar
    jar = Jar()
    assert str(jar) == ""  # Empty jar has no cookies

    jar.deposit(1)
    assert str(jar) == "🍪"  # One cookie

    jar.deposit(11)
    assert str(jar) == "🍪" * 12  # Full jar

    jar.withdraw(3)
    assert str(jar) == "🍪" * 9  # After removing cookies


def test_deposit():
    # Test depositing cookies into the jar
    jar = Jar(10)  # Create a jar with capacity 10
    jar.deposit(1)
    assert jar.size == 1

    jar.deposit(5)
    assert jar.size == 6

    # Depositing more than capacity should raise ValueError
    with pytest.raises(ValueError):
        jar.deposit(5)

    # Negative deposits should raise ValueError
    with pytest.raises(ValueError):
        jar.deposit(-1)


def test_withdraw():
    # Test withdrawing cookies from the jar
    jar = Jar()
    jar.deposit(5)

    jar.withdraw(2)
    assert jar.size == 3

    jar.withdraw(3)
    assert jar.size == 0  # Jar is empty after withdrawal

    # Withdrawing more than available should raise ValueError
    with pytest.raises(ValueError):
        jar.withdraw(1)

    # Negative withdrawals should raise ValueError
    with pytest.raises(ValueError):
        jar.withdraw(-1)
