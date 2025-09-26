import pytest
from src.c_module import BankAccount, fibonacci, prime_factors, moving_average, normalize_scores

# C-OSA TESTID: Kirjuta teste, et leida vigased funktsioonid!
# Järgmised 2 testi on näited - kirjuta ülejäänud testid ise!

# Näited ülesandest:
def test_fibonacci_small():
    assert [fibonacci(i) for i in range(6)] == [0,1,1,2,3,5]
    assert fibonacci(10) == 55

def test_prime_factors_basic():
    assert prime_factors(12) == [2,2,3]
    assert prime_factors(97) == [97]

# Testid BankAccount klassile
def test_bankaccount_init_and_balance():
    acc = BankAccount("Alice", 100)
    assert acc.balance() == 100
    acc2 = BankAccount("Bob")
    assert acc2.balance() == 0

def test_bankaccount_init_invalid():
    with pytest.raises(ValueError):
        BankAccount("", 50)
    with pytest.raises(ValueError):
        BankAccount(123, 50)
    with pytest.raises(ValueError):
        BankAccount("Alice", -10)

def test_bankaccount_deposit():
    acc = BankAccount("Alice", 100)
    acc.deposit(50)
    assert acc.balance() == 150
    with pytest.raises(ValueError):
        acc.deposit(0)
    with pytest.raises(ValueError):
        acc.deposit(-10)

def test_bankaccount_withdraw():
    acc = BankAccount("Alice", 100)
    acc.withdraw(30)
    assert acc.balance() == 70
    with pytest.raises(ValueError):
        acc.withdraw(0)
    with pytest.raises(ValueError):
        acc.withdraw(-5)
    with pytest.raises(ValueError):
        acc.withdraw(1000)  # rohkem kui kontol on

def test_bankaccount_transfer_to():
    acc1 = BankAccount("Alice", 100)
    acc2 = BankAccount("Bob", 50)
    acc1.transfer_to(acc2, 40)
    assert acc1.balance() == 60
    assert acc2.balance() == 90
    with pytest.raises(ValueError):
        acc1.transfer_to("not a bank account", 10)
    with pytest.raises(ValueError):
        acc1.transfer_to(acc2, 0)
    with pytest.raises(ValueError):
        acc1.transfer_to(acc2, -5)
    with pytest.raises(ValueError):
        acc1.transfer_to(acc2, 1000)  # rohkem kui saldo

# Testid fibonacci funktsioonile
def test_fibonacci_invalid():
    with pytest.raises(ValueError):
        fibonacci(-1)

def test_fibonacci_large():
    # lihtsalt kontrollida, et arvutus õnnestub ja ei kuku kokku (rekursiooni tõttu mitte väga suur)
    assert fibonacci(5) == 5
    assert fibonacci(7) == 13

# Testid prime_factors funktsioonile
def test_prime_factors_invalid():
    with pytest.raises(ValueError):
        prime_factors(1)
    with pytest.raises(ValueError):
        prime_factors(0)
    with pytest.raises(ValueError):
        prime_factors(-10)

def test_prime_factors_composite():
    assert prime_factors(18) == [2,3,3]
    assert prime_factors(100) == [2,2,5,5]

# Testid moving_average funktsioonile
def test_moving_average_basic():
    vals = [1,2,3,4,5]
    assert moving_average(vals, 1) == [1,2,3,4,5]
    assert moving_average(vals, 2) == [1.5,2.5,3.5,4.5]
    assert moving_average(vals, 3) == [2.0,3.0,4.0]
    assert moving_average(vals, 5) == [3.0]

def test_moving_average_invalid():
    with pytest.raises(ValueError):
        moving_average([1,2,3], 0)
    with pytest.raises(ValueError):
        moving_average([1,2,3], -1)
    assert moving_average([1,2], 3) == []

# Testid normalize_scores funktsioonile
def test_normalize_scores_basic():
    scores = [0, 50, 100]
    normalized = normalize_scores(scores)
    assert normalized == [0.0, 0.5, 1.0]

def test_normalize_scores_invalid():
    with pytest.raises(ValueError):
        normalize_scores([-1, 50])
    with pytest.raises(ValueError):
        normalize_scores([50, 101])
    with pytest.raises(ValueError):
        normalize_scores([13, 150])

# TODO: Kirjuta ülejäänud testid ise!
# Vihje: mõned funktsioonid on vigased - sinu testid peaksid need leidma!
