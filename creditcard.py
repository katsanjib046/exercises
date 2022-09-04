class CreditCard:
    """A Consumer Credit Card"""
    def __init__(self,customer,bank,acnt,limit):
        """Create a new Credit Card instance.

        The Initial balance is zero.

        customer: Name of a customer (eg. Sanjib Katuwal)
        bank: the name of the bank (eg. Wells Fargo)
        acnt: the account number (eg. 5012 3456 4839 3453)
        limit: credit limit (measured in dollars)
        """
        self._customer = customer
        self._bank = bank
        self._acnt = acnt
        self._limit = limit
        self._balance = 0

    def get_customer(self):
        """Returns name of the customer"""
        return self._customer

    def get_bank(self):
        """Returns name of the bank"""
        return self._bank

    def get_account(self):
        """Returns account number"""
        return self._acnt

    def get_limit(self):
        """Returns credit limit"""
        return self._limit

    def get_balance(self):
        """Returns balance"""
        return self._balance

    def charge(self, price):
        """
        Charge given price to a credit card, assuming it has sufficient credit limit

        Returns True if charge was processed, else returns False
        """
        if price + self._balance > self._limit:
            return False
        else:
            self._balance += price
            return True

    def make_payment(self, amount):
        """
        Process Customer payment that reduces the balance
        """
        self._balance -= amount


class PredatoryCreditCard(CreditCard):
    """A class for predatory credit card which extends the class of credit card to include interests and fees"""

    def __init__(self, customer, bank, acnt, limit, apr):
        """
        Create a predatory credit card instance.
        The initial balance is zero.
        customer:   Name
        bank:       Name of the bank
        acnt:       Account Number
        limit:      Credit limit (is a number)
        apr:        APR (eg. 0.1 for 10%)
        """
        super().__init__(customer, bank, acnt, limit)
        self._apr = apr

    def charge(self, price):
        """
        Charge given price to the credit card, if the limit is sufficient
        Return True, if charge was processed
        Retur False and assess $5 if charge was denied
        """
        success = super().charge(price) #calling inherited method
        if not success:
            self._balance += 5 # adding penalty
        return success # return success to the caller

    def process_month(self):
        """ Assess monthly interests to the outstanding balance"""
        if self._balance > 0:
            # if positive balance, conver apr to multiplicative factor
            monthly_factor = pow(1 + self._apr, 1/12)
            self._balance *= monthly_factor

####### Testing #########
if __name__ == "__main__":
    wallet = []
    wallet.append(CreditCard("SK","WF Checking","1234",5000))
    wallet.append(CreditCard("SK","WF Savings","2345", 10000))
    wallet.append(CreditCard("SK","WF General", "3456",10000))

    for val in range(1,17):
        wallet[0].charge(val)
        wallet[1].charge(2*val)
        wallet[2].charge(3*val)

    for c in range(3): 
        print("Customer = ", wallet[c].get_customer()) 
        print("Bank = ", wallet[c].get_bank())
        print("Account = ", wallet[c].get_account()) 
        print("Limit = ", wallet[c].get_limit()) 
        print("Balance = ", wallet[c].get_balance()) 
        while wallet[c].get_balance( ) > 100: 
            wallet[c].make_payment(100)
        print( "New balance = ", wallet[c].get_balance())
        print()
