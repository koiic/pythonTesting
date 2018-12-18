import pytest

from wallet import  Wallet, InsufficientFund


@pytest.fixture
def empty_wallet():
  ''' Returns empty wallet '''
  wallet = Wallet()
  return wallet

@pytest.fixture
def wallet():
  ''' Return initial balance of wallet '''
  return Wallet(20)

@pytest.fixture
def my_wallet():
  ''' Returna Wallet instance with a Zero balance '''
  return Wallet()


def test_default_initial_amount(empty_wallet):
  assert empty_wallet.balance == 0


def test_initial_amount(wallet):
  assert wallet.balance == 20

def test_wallet_add_cash(wallet):
  wallet.add_cash(200)
  assert wallet.balance == 220

def test_wallet_spend_cash(wallet):
    wallet.spend_cash(10)
    assert wallet.balance == 10

def test_spend_cash_raises_exception_on_insufficient_fund(empty_wallet):
  with pytest.raises(InsufficientFund):
    empty_wallet.spend_cash(100)


@pytest.mark.parametrize("earned,spent,expected", [
    (30, 10, 20),
    (20, 2, 18),
])
def test_transaction(my_wallet, earned, spent, expected):
  my_wallet.add_cash(earned)
  my_wallet.spend_cash(spent)
  assert my_wallet.balance == expected


