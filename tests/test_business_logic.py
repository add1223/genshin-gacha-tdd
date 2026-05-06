from business_logic import add_spaces

def test_add_spaces():
    """测试 add_spaces 函数是否正确拼接两个字符串"""
    result = add_spaces("Hello", "World")
    assert result == "Hello World"
