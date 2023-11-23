from unittest.mock import Mock
from lib.CatFacts import CatFacts

def test_call_api_to_provide_1():
    
    fake_requester = Mock()
    fake_response = Mock()
    fake_requester.get.return_value = fake_response
    fake_response.json.return_value = {
        "fact":"Cats have about 130,000 hairs per square inch (20,155 hairs per square centimeter).",
        "length":83
        } 
    
    catfacts = CatFacts(fake_requester)
    result = catfacts.provide()
    assert result == "Cat fact: Cats have about 130,000 hairs per square inch (20,155 hairs per square centimeter)."

