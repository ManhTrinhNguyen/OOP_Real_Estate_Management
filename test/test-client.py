import sys 
sys.path.insert(1, '/Users/trinhnguyen/Documents/Meta-Certificate/Python/object-oriented-programing/OOP_Real_Estate_Management')

from client import Client 
from property import Property

class Test_Client: 
  # Setup 
  def setup_method(self, method): # Setup method run at the beginning of each test
    print(f'Running Method {method}')
    self.client1 = Client(1, 'Lena')
    self.property1 = Property('123 st', 199000, 'House', True)

  def test_client(self):
    # should have name is Lena 
    assert self.client1.name == 'Lena'
    # should have id is 1 
    assert self.client1.client_id == 1
    # Add properties interested 
    assert self.client1.add_interest(self.property1) == f'Added properties_interested {self.property1} to properties_interested list'
    # Add properties-interested list should have len is 1
    assert len(self.client1.properties_interested) == 1
    # Add the property that already in the list 
    assert self.client1.add_interest(self.property1) == f'Properties_interested {self.property1} is already in the list'
    # Remove property from the list 
    assert self.client1.remove_interest(self.property1) == f'Removed {self.property1}'

   