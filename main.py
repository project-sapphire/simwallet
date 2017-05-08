# the dopest python script of all time
# OF ALL TIME
# python3
from SimWallet import SimWallet

def main():
    x = SimWallet()
    x.set_currency('btc', 10.0)
    x.set_currency('xrp', 2.0)
    print(x.balance['btc'])
    print(x.balance['xrp'])


if __name__ == '__main__':
    main()
