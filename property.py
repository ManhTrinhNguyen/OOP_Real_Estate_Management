class Property:
  def __init__(self, address: str, price: float, type: str, availability: bool) -> None:
    self.address = address
    self.price = price 
    self.type = type 
    self.availability = availability 

  def __str__(self) -> str:
    return f"House address: {self.address}, Price: {self.price}, Type: {self.type}, Availability: {self.availability}"

  def mark_sold(self): 
    self.availability = False 
    return 'Sold'
  

  
