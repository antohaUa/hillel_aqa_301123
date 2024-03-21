import pytest
from code.if_elif_else import min_from_four
from data.internal_data import min_4_data


@pytest.mark.internal
class TestInternalCode:

    @pytest.mark.parametrize("data_set, expected_result", min_4_data)
    def test_min_4_params(self, data_set, expected_result):
        result = min_from_four(*data_set) == 'z'
        assert result == expected_result, 'Wrong expected result'
