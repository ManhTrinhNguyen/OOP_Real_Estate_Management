from property import Property 

class Commercial(Property):
  def __init__(self, address: str, price: float, bussiness_type: str, square_footage: float) -> None:
    super().__init__(address, price, type='Commercial', availability=True)
    self.bussiness_type = bussiness_type 
    self.square_footage = square_footage 

