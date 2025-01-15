from testing.src import myname


def test_myname():
    res = myname("Jorge")
    assert res == "Jorge"


def test_myname_null():
    res = myname(None)
    assert res == "Not a valid name"


def test_myname_list():
    res_empty = myname([])
    res = myname(["Jorge"])
    assert res_empty == "Not a valid name"
    assert res == "Not a valid name"


def test_myname_tuples():
    res_empty = myname(())
    res = myname(("Jorge", ))
    assert res_empty == "Not a valid name"
    assert res == "Not a valid name"


def test_myname_dictionary():
    res_empty = myname({})
    res = myname({"name": "Jorge"})
    assert res_empty == "Not a valid name"
    assert res == "Not a valid name"
