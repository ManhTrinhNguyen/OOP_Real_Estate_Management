from property import Property 

class House(Property) :
  def __init__(self, address: str, price: float, num_bedrooms: int, num_bathrooms: int, lot_size: float):
    super().__init__(address, price, type='House', availability=True)
    self.num_bedrooms = num_bedrooms 
    self.num_bathrooms = num_bathrooms
    self.lot_size = lot_size 
