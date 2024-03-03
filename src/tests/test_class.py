import pytest
from helper.helper_test import *

class TestSample:
    """
        This class is responsible to handle all of 
        The sample test cases.
    """

    def test_addition_success(self):
        result = sum(10,5)
        assert result == 15
    
    def test_check_json_data_success(self):
        data = {
            "name" : "Shuvo",
            "designation": "Senior Software Engineer"
        }
        result = check_json_data(data)
        assert result == "OK"
    

    def test_check_json_data_failed(self):
        data = [10,2,3]
        with pytest.raises(Exception):
            check_json_data(data)