from add import adder

class TestAdd():
  def test_add(self):
    assert adder(1, 2) == 3
