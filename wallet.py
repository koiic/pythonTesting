
class InsufficientFund(Exception):
  pass

class Wallet(object):

  def __init__(self, initialAmount = 0):
    self.balance = initialAmount

  def add_cash(self, amount):
    self.balance += amount

  def spend_cash(self, amount):
    if(self.balance < amount):
      raise InsufficientFund('Not enough available to spend {}'.format(amount))
    self.balance -= amount

