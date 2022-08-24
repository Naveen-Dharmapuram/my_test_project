import algo

def test_area():
    output = algo.area_of_rectangle(2,5)
    assert output == 10
 
def test_perimeter():
    output = algo.perimeter_of_rectangle(2,5)
    assert output == 14

def naveen_print():
    print("testing the printing.py")
    assert True

def inc(x):
    print("in x")
    return x + 1

def test_answer():
    print(" in test_answer")
    assert inc(3) == 5
