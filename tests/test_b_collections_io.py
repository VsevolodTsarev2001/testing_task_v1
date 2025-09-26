import pytest
from src.b_collections_io import (
    unique_sorted, count_words, merge_dicts, find_max_pair, flatten,
    read_file, write_file, safe_get, top_n, chunk_list
)

# B-OSA TESTID: Kirjuta teste, et leida vigased funktsioonid!
# Järgmised 2 testi on näited - kirjuta ülejäänud testid ise!

def test_unique_sorted_basic():
    """Test unikaalsete sorteeritud arvude funktsiooni."""
    assert unique_sorted([3,1,2,2,3]) == [1,2,3]
    assert unique_sorted([]) == []
    assert unique_sorted([5,5,5]) == [5]

def test_count_words_basic():
    """Test sõnade loendamise funktsiooni."""
    text = "tere tere tulemast koju"
    out = count_words(text)
    assert out == {"tere": 2, "tulemast": 1, "koju": 1}

def test_merge_dicts_basic():
    """Test sõnastike ühendamise funktsiooni."""
    d1 = {'a': 1, 'b': 2}
    d2 = {'b': 3, 'c': 4}
    out = merge_dicts(d1, d2)
    assert out == {'a': 1, 'b': 3, 'c': 4}

    d1 = {'x': 1}
    d2 = {}
    out = merge_dicts(d1, d2)
    assert out == {'x': 1}

    d1 = {}
    d2 = {'y': 2}
    out = merge_dicts(d1, d2)
    assert out == {'y': 2}

def test_find_max_pair_basic():
    """Test maksimaalse paari leidmise funktsiooni."""
    assert find_max_pair([1, 2, 3, 3, 2, 1]) == (3, 2)
    assert find_max_pair([5]) == (5, 1)

    try:
        find_max_pair([])
    except ValueError as e:
        assert str(e) == "Tühja loendi maksimum ei ole defineeritud"

def test_flatten_basic():
    """Test lamedaks muutmise funktsiooni."""
    assert flatten([[1, 2], [3, 4], [5]]) == [1, 2, 3, 4, 5]
    assert flatten([[]]) == []
    assert flatten([[], [1, 2]]) == [1, 2]
    assert flatten([]) == []

def test_read_file_basic():
    """Test faili lugemise funktsiooni."""
    # Create a temporary file for testing
    path = 'test_file.txt'
    with open(path, 'w', encoding='utf-8') as f:
        f.write("Testi tekst.")
    
    out = read_file(path)
    assert out == "Testi tekst."

def test_write_file_basic():
    """Test faili kirjutamise funktsiooni."""
    path = 'test_write.txt'
    out = write_file(path, "Testi kirjutamine")
    assert out == len("Testi kirjutamine")

    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    assert content == "Testi kirjutamine"

def test_safe_get_basic():
    """Test sõnastiku võtme olemasolu kontrollimise funktsiooni."""
    d = {'a': 1, 'b': 2}

    assert safe_get(d, 'a') == 1
    assert safe_get(d, 'b') == 2
    assert safe_get(d, 'c', 'default') == 'default'
    assert safe_get(d, 'c') is None

def test_top_n_basic():
    """Test top-n arvu leidmise funktsiooni."""
    assert top_n([1, 2, 3, 4, 5], 3) == [5, 4, 3]
    assert top_n([5, 5, 5, 5], 2) == [5, 5]

    try:
        top_n([1, 2, 3], 0)
    except ValueError as e:
        assert str(e) == "n peab olema positiivne"

    try:
        top_n([1, 2, 3], 5)
    except ValueError as e:
        assert str(e) == "n ei tohi olla suurem kui loendi pikkus"

def test_chunk_list_basic():
    """Test listi tükkideks jagamise funktsiooni."""
    assert chunk_list([1, 2, 3, 4, 5], 2) == [[1, 2], [3, 4], [5]]
    assert chunk_list([1, 2, 3, 4, 5], 3) == [[1, 2, 3], [4, 5]]
    
    try:
        chunk_list([1, 2, 3], 0)
    except ValueError as e:
        assert str(e) == "Suurus peab olema positiivne"

    assert chunk_list([], 2) == []

# TODO: Kirjuta ülejäänud testid ise!
# Vihje: mõned funktsioonid on vigased - sinu testid peaksid need leidma!
