class Account:
    """An account has a balance and a holder.

    >>> a = Account('John')
    >>> a.holder
    'John'
    >>> a.deposit(100)
    100
    >>> a.withdraw(90)
    10
    >>> a.withdraw(90)
    'Insufficient funds'
    >>> a.balance
    10
    """
    def __init__(self, account_holder):
        self.holder = account_holder
        self.balance = 0

    def deposit(self, amount):
        """Add amount to balance."""
        self.balance = self.balance + amount
        return self.balance

    def withdraw(self, amount):
        """Subtract amount from balance if funds are available."""
        if amount > self.balance:
            return 'Insufficient funds'
        self.balance = self.balance - amount
        return self.balance

def transfer(source, destination, amount):
    """Transfer amount between two accounts.

    >>> john = Account('John')
    >>> jack = Account('Jack')
    >>> john.deposit(100)
    100
    >>> jack.deposit(100000)
    100000
    >>> transfer(jack, john, 1000)
    'Transfer successful'
    >>> john.balance
    1100
    >>> jack.balance
    99000
    >>> transfer(john, jack, 10000)
    'Insufficient funds'
    >>> transfer(john, jack, 10)
    'Transfer successful'
    >>> john.balance
    1090
    >>> jack.balance
    99010
    """
    result = source.withdraw(amount)
    if type(result) == str:  # something went wrong
        return result
    else:
        destination.deposit(amount)
        return 'Transfer successful'

class Scam:
    """A scam account has a balance and a holder.

    >>> a = Scam('John')
    >>> a.holder
    'John'
    >>> a.deposit(100)
    102.0
    >>> a.withdraw(90)
    'We apologize for the delay'
    >>> a.withdraw(90)
    'We apologize for the delay'
    >>> a.balance
    102.0
    """
    def __init__(self, account_holder):
        self.holder = account_holder
        self.balance = 0

    def deposit(self, amount):
        """Add amount +2% to balance."""
        self.balance = self.balance + amount * 1.02
        return self.balance

    def withdraw(self, amount):
        """Subtract amount from balance if funds are available."""
        return 'We apologize for the delay'

def create(names):
    """Creates a dictionary of accounts, each with an initial deposit of 5.

    >>> accounts = create(['Alice', 'Bob', 'Charlie'])
    >>> accounts['Alice'].holder
    'Alice'
    >>> accounts['Bob'].balance
    5
    >>> accounts['Charlie'].deposit(10)
    15
    """
    result = {name: Account(name) for name in names}
    for a in result.values():
        a.deposit(5)
    return result
