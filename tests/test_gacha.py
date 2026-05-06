import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from business_logic import gacha_pull

def test_gacha_pull_basic():
    result = gacha_pull(100)
    assert 'five_star' in result
    assert 'four_star' in result
    assert 'three_star' in result
    total = result['five_star'] + result['four_star'] + result['three_star']
    assert total == 100

def test_gacha_pull_zero():
    result = gacha_pull(0)
    assert result == {'five_star': 0, 'four_star': 0, 'three_star': 0}
