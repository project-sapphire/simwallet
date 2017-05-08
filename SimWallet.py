import json

# holds an imaginary balance and stuff
# serializes the data to wallet.json
# this object only stores the data for the balance
class SimWallet:
    def __init__(self):
        try:
            with open('wallet.json') as f:
                data = json.load(f)
                self.balance = data
        except EnvironmentError:
            with open('wallet.json', 'w') as f:
                f.write('{}')
                self.balance = {}


    # saves the current state of the wallet
    # lazy
    def save(self):
        with open('wallet.json', 'w') as f:
            f.write(json.dumps(self.balance))

    def set_currency(self, currency, value):
        self.balance[currency] = value
        self.save()


    def balance(self, currency):
        if self.balance[currency] == None:
            return 0
        else:
            return self.balance[currency]

    def pay(self, currency, amount, address):
        pass

    def receive(self, currency, amount, address):
        pass
