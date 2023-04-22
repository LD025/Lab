class Account:
    def __init__(self, name: str) -> None:
        self.__account_name = name
        self.__account_balance = 0

    def deposit(self, amount: float) -> True or False:
        """
        Function to add specified amount to account balance.
        :param amount: Amount to add to balance, should be a positive integer.
        :return: True if transaction successful, False if transaction failed.
        """
        if type(amount) != str and amount > 0:
            self.__account_balance += amount
            return True
        else:
            return False

    def withdraw(self, amount: float) -> True or False:
        """
        Function to withdraw specified amount from account balance.
        :param amount: Amount to remove from balance, should be a positive integer, and less than current account balance.
        :return: True if transaction successful, False if transaction failed.
        """
        if type(amount) != str and amount > 0:
            if amount > self.__account_balance:
                return False
            else:
                self.__account_balance -= amount
                return True
        else:
            return False

    def get_balance(self) -> float:
        """
        Function to get account balance amount.
        :return: Current account balance total.
        """
        return self.__account_balance

    def get_name(self) -> str:
        """
        Function to get name associated with account.
        :return: Name associated with account.
        """
        return self.__account_name