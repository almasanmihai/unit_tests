from app.mini_calc import MiniCalc
import pytest


class TestMiniCalc:
    def setup_method(self):
        print('This will run first')
        self.calc1 = MiniCalc(3, 5)

    def teardown_method(self):
        print('This will run last')

    def test_sum(self):
        assert self.calc1.sum() == 8, 'sum is not working'

    def test_subtract(self):
        assert self.calc1.subtract() == -2, 'subtract is not working'

    @pytest.mark.skip
    def test_multiply(self):
        assert self.calc1.multiply() == 15, 'multiply is not working'

    def test_division(self):
        assert self.calc1.division() == 0.6, 'division is not working'

    def test_custom_sum(self):
        assert self.calc1.custom_sum(5, 6) == 10, 'custom_sum not working'

    @pytest.mark.parametrize(
        ('c', 'd', 'expected'),
        [
            (1, 2, 3),
            (2, 3, 5),
            (5, 5, 11)
        ]
    )
    def test_custom_sum_param(self, c, d, expected):
        assert self.calc1.custom_sum(c, d) == expected
