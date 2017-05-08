import json

# holds an imaginary balance and stuff
# serializes the data to wallet.json
# this object only stores the data for the balance
class SimWallet:
    def __init__(self):
        try:
            with open('wallet.json') as f:
                data = json.load(f)
                self._balance = data
        except EnvironmentError:
            with open('wallet.json', 'w') as f:
                f.write('{}')
                self._balance = {}


    # saves the current state of the wallet
    # lazy
    def save(self):
        with open('wallet.json', 'w') as f:
            f.write(json.dumps(self._balance))

    def set_currency(self, currency, value):
        self._balance[currency] = value
        self.save()

    def balance(self, currency):
        try:
            return self._balance[currency]
        except KeyError:
            return 0

    def pay(self, currency, amount):
        try:
            self._balance[currency] -= amount
            self.save()
        except KeyError:
            pass

    def receive(self, currency, amount):
        try:
            self._balance[currency] += amount
            self.save()
        except KeyError:
            pass
