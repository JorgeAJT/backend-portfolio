from testing.src import myname

def test_myname():
    res = myname("Jorge")

    assert res == "Jorge"
