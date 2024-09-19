class Transaction:
  # Instances Attribute 
  def __init__(self, transaction_id: int, agent, property, transaction_type, client) -> None:
    self.transaction_id = transaction_id # Unique identifier for the transaction (integer)
    self.agent = agent # The agent involved in the transaction (an Agent object). 
    self.property = property # The property involved in the transaction (a Property object).
    self.transaction_type = transaction_type # Type of transaction ("buy", "sell", "rent").
    self.client = client # The client involved in the transaction (a Client object).

  # Method 
  def process(self):
    # If the property available -> mark as sold . 
    if self.property.availability:
      self.property.mark_sold()
      return f"Transaction {self.transaction_id}: {self.transaction_type} of {self.property} by {self.client.name} through {self.agent.name} completed."
    return f"Transaction {self.transaction_id} failed: {self.property} is not available."
  