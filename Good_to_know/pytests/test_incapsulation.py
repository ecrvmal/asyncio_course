import sys
from pathlib import Path
sys.path.append(str(Path('').absolute().parent))
from incapsulation import Phone
import pytest

prod_data = ['one', 'two', 'three']
test_data = ['one', 'two', 'three']


def divide(a, b):
    return a / b

class TestPhone():
    def test_1(self):
        p = Phone()
        assert p.get_number() == "111-11-11"

    def test_2(self):
        p = Phone()
        assert type(p.get_number()) == str


    @pytest.mark.parametrize("a, b, expected_result", [(10,2,5), (30, -3, -10), (5, 2, 2.5)])
    def test_division_good(self,a,b,expected_result):
        assert divide(a, b) == expected_result

    def test_zero_division_error(self):
        with pytest.raises(ZeroDivisionError):
            divide(10, 0)

    def test_type_error(self):
        with pytest.raises(TypeError):
            divide(10, "2")

    @pytest.mark.parametrize("exception, divider",[(ZeroDivisionError, 0 ), (TypeError, '2')] )
    def test_division_error(self, exception, divider):
        with pytest.raises(exception):
            divide (10, divider)


# run:
# python D:/GB/pythonProject/asyncio/Out_of_course/test_incapsulation.py
#  python D:/GB/pythonProject/asyncio/Out_of_course/test_incapsulation.py::TestPhone
#  python D:/GB/pythonProject/asyncio/Out_of_course/test_incapsulation.py::TestPhone::test_1
