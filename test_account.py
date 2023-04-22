import pytest
from account import *

class Test:
    def setup_method(self):
        self.p1 = Account('John')

    def teardown_method(self):
        del self.p1

    def test_init(self):
        assert self.p1.get_name() == 'John'
        assert self.p1.get_balance() == 0

    def test_deposit(self):
        assert self.p1.get_balance() == 0
        assert self.p1.deposit(100) is True
        assert self.p1.deposit(-100) is False
        assert self.p1.deposit('1 Bazillion Coins') is False

    def test_withdraw(self):
        self.p1.deposit(1)
        assert self.p1.withdraw(1) is True
        assert self.p1.withdraw(2) is False
        assert self.p1.withdraw(-100) is False
        assert self.p1.withdraw('1 Bazillion Coins') is False



