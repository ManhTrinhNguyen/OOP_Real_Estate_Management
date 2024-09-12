from property import Property 

class Apartment(Property): 
  def __init__(self, address: str, price: float, floor: int, has_elevator: bool) -> None:
    super().__init__(address, price, type='Apartment', availability=True)
    self.floor = floor 
    self.has_elevator = has_elevator
    
#apartment1 = Apartment("456 Oak Ave", 150000, 2, True)

