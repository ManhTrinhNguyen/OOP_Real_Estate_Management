class Agent: 
  def __init__(self, agent_id, name):
    self.agent_id = agent_id 
    self.name = name 
    self.properties_listed = {} # List of properties listed by the agent (list of Property objects).

  def list_property(self, property):
    if property not in self.properties_listed:
      self.properties_listed[property] = property.availability
      return f'Add property: {property} to property_listed'
    return f'Property {property} is already in the property_listed'
  
  def remove_property(self, property):
    if property in self.properties_listed:
      del self.properties_listed[property]
      return f'Removed {property}'
    
