import sys
import os
# 将项目根目录添加到 Python 搜索路径
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from business_logic import add_spaces

def test_add_spaces():
    result = add_spaces("Hello", "World")
    assert result == "Hello World"
