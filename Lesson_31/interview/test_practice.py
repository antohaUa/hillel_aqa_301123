"""
Task.

1*2 = 2
6*5 = 30
 Hello word!
    start test
    end test
Bye World!
"""
import pytest


class TestClass:

    @pytest.fixture(scope='class', autouse=True)
    def hello(self):
        print('\nHello word!')
        yield
        print('\nBye World!')

    @pytest.fixture(scope='function', autouse=True)
    def start_end_test(self):
        print('\nstart test')
        yield
        print('\nend test')

    def test_1(self):
        assert 1 * 2 == 2, 'Not equal'

    def test_2(self):
        assert 6 * 5 == 30, 'Not equal'
