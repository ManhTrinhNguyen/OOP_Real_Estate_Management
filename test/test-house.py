import sys
sys.path.insert(1, '/Users/trinhnguyen/Documents/Meta-Certificate/Python/object-oriented-programing/OOP_Real_Estate_Management')

from house import House

class Test_House:
  def setup_method(self, method): # Set up method run at beginning of each test
    print(f'Run {method}')
    self.house1 = House("123 Maple St", 300000, 3, 2, 5000)

  def test_house1(self):
    # Number of bedrooms should be 3 
    assert self.house1.num_bedrooms == 3
    # Number of bathrooms should be 2
    assert self.house1.num_bathrooms == 2
    # Price should be 300000
    assert self.house1.price == 300000