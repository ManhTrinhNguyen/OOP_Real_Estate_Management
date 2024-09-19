class Agent: 
  def __init__(self, agent_id: int, name: str):
    self.agent_id = agent_id 
    self.name = name 
    self.properties_listed: dict = {} # List of properties listed by the agent (list of Property objects).

  def list_property(self, property): # Add property the properties list
    # If property is not yet in the list 
    if property not in self.properties_listed:
      # Add property to the list 
      self.properties_listed[property] = property.availability
      return f'Add property: {property} to property_listed'
    return f'Property {property} is already in the property_listed'
  
  def remove_property(self, property): # Remove property from the list 
    # If property is in the list 
    if property in self.properties_listed:
      # Delete that property 
      del self.properties_listed[property]
      return f'Removed {property}'
    