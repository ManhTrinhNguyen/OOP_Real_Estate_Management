from agent import Agent
from client import Client
from house import House
from aparment import Apartment 
from commercial import Commercial
from transaction import Transaction

class RealEstateAgency: 
  # Instances Attribute
  def __init__(self) -> None:
    self.agents = [] # A list of agents registered with the agency (list of Agent objects).
    self.clients = [] # A list of client registered with the agency (list of Client objects).
    self.properties = [] # A list of properties registered with the agency (list of Properties objects).
    self.tracsactions = [] # A list of transaction registered with the agency (list of Transaction objects).

  # Method Atrribute 
  def register_agent(self, agent):
    # Add new agent to the agency list
    self.agents.append(agent)
    return f"Agent {agent.name} registered"

  def register_client(self, client):
    # Add new client to agency list
    self.clients.append(client)
    return f"Client {client.name} registered"
  
  def add_property(self, property):
    # Add new property to agency list
    self.properties.append(property)
    return f"Property {property} added to the list"

  def create_transaction(self, transaction): # Creates and processes a transaction between an agent and a client.
    self.tracsactions.append(transaction)
    return transaction.process()
  
  def find_property(self, address): # Find property by its address
    # Loop properties list . 
    for property in self.properties:
      # If property's address == address provided
      if property.address == address:
        return property
      else:
        return f"We don't have the property in that specific address"
  
  def list_available_properties(self, property_type): # Lists all available properties filtered by type.
    # loop properties list .
    for property in self.properties:
      # If property's type == property type provided 
      if property.type == property_type:
        return property


agency = RealEstateAgency()

# Create Agent
agent1 = Agent(1, 'Tim')
agent2 = Agent(2, 'Kelly')
print(agency.register_agent(agent1))
print(agency.register_agent(agent2))

# Create Client 
client1 = Client(1, 'Lena')
client2 = Client(2, 'Lance')
print(agency.register_client(client1))
print(agency.register_client(client2))

# Add Properties 
house1 = House("123 Maple St", 300000, 3, 2, 5000)
apartment1 = Apartment("456 Oak St", 200000, 5, True)
commercial1 = Commercial("789 Pine St", 500000, "Retail", 10000)
print(agency.add_property(house1))
print(agency.add_property(apartment1))
print(agency.add_property(commercial1))

# Agent list a property 
print(agent1.list_property(house1))

# Client add interest in the property 
print(client1.add_interest(house1))
print(client2.add_interest(apartment1))

# Create and process a transaction
transaction1 = Transaction(1, agent1, client1, house1, 'Buy')
print(agency.create_transaction(transaction1))

# List all available properties 
print(agency.list_available_properties('House'))
print(agency.list_available_properties('Apartment'))