class Client: 
  def __init__(self, client_id: int, name: str) -> None:
    self.client_id = client_id
    self.name = name 
    self.properties_interested = []

  def add_interest(self, property): # Add interest in the interest property 
    # Check if property is yet interested 
    if property not in self.properties_interested:
      self.properties_interested.append(property)
      return f"Added properties_interested {property} to properties_interested list"
    return f"Properties_interested {property} is already in the list"
  
  def remove_interest(self, property): # Remove interest from the interest property 
    # Check if property is yet interested 
    if property in self.properties_interested:
      self.properties_interested.remove(property)
      return f"Removed {property}"

