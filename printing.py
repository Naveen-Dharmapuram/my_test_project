import algo

def naveen_print():
    print("testing the printing.py")
    assert True

def inc(x):
    print("in x")
    return x + 1

def test_answer():
    print(" in test_answer")
    assert inc(3) == 5
