import sys
sys.path.insert(1, '/Users/trinhnguyen/Documents/Meta-Certificate/Python/object-oriented-programing/OOP_Real_Estate_Management')

from property import Property

class Test_Property: 
  def setup_method(self, method): # Setup Method run at the beginning of each Test 
    print(f"Setting up metohd {method}")
    self.property1 = Property('123 st', 199000, 'House', True)

  def test_mark_sold(self):
    # Mark property as sold 
    assert self.property1.mark_sold() == 'Sold'
    # Availabiltity should return False 
    assert self.property1.availability == False 