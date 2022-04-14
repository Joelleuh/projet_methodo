from lib import average, get_median
from main import class_average_median

def test_average():
    l1 = [0,10,20]
    result = average(l1)
    expected_result = 10
    assert result == expected_result

def test_get_median():
    l1 = [0,1,6,5]
    result = get_median(l1)
    expected_result = 3
    assert result == expected_result

def test_class_average_median():
    l2d = [[0,10,20], [18,20,22]]
    expected_average = 15
    expected_median = 15
    expected_result = (15,15)
    result = class_average_median(l2d)
    assert result == expected_result