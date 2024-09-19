import sys 
sys.path.insert(1, '/Users/trinhnguyen/Documents/Meta-Certificate/Python/object-oriented-programing/OOP_Real_Estate_Management')
from aparment import Apartment

class Test_Apartment:
  def setup_method(self, method): # Setup method run at the beginning of each tesgt
    print(f'Running method {method}')
    self.apartment1 = Apartment("456 Oak Ave", 150000, 2, True)

  def test_apartment(self):
    # Apartment should have 2 floor 
    assert self.apartment1.floor == 2
    # Apartment should have price at 150000
    assert self.apartment1.price == 150000
    # Apartment should be available 
    assert self.apartment1.availability == True
    # Apartment address 
    assert self.apartment1.address == "456 Oak Ave"

    