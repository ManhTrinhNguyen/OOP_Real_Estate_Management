import sys 
sys.path.insert(1, '/Users/trinhnguyen/Documents/Meta-Certificate/Python/object-oriented-programing/OOP_Real_Estate_Management')
from commercial import Commercial 

class Test_Comercial: 
  # Setup method 
  def setup_method(self, method): # Setup method run at beginning of each test
    print(f'Running method {method}')
    self.comercial = Commercial("789 Pine St", 500000, "Retail", 10000)

  def test_comercial(self):
    # Should have price at 500000 
    assert self.comercial.price == 500000
    # Should have bussiess_type as Retial 
    assert self.comercial.bussiness_type == 'Retail'
    # Should have squarefoot at 10000
    assert self.comercial.square_footage == 10000
    # Address 
    assert self.comercial.address == "789 Pine St"
