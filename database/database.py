import os
from mongoengine import *
from cryptography.fernet import Fernet
from .account import Account


class Database(object):
    def __init__(self, key):
        if not os.path.exists('./resources/data'):
            os.makedirs('./resources/data/db')

        connect('lego-py', host='localhost', port=27017)  # TODO - setup config for server/db specific constants
        self.accounts = []
        self.get_accounts()

        self.key = Fernet(key)

    def get_accounts(self):
        # load the database and store account objects in a list 
        # that can be dynamically read across server instancess
        for account in Account.objects:
            self.accounts.append(account)

    def register_account_client(self, username='', password='', banned=False, is_admin=False):
        account = Account(
            account_id=len(self.accounts) + 1,
            username=username,
            password=self.key.encrypt(bytes(password, 'latin1')),
            banned=banned,
            is_admin=is_admin
        )
        print(account.password)
        self.accounts.append(account)

    def register_account_db(self, username='', password='', banned=False, is_admin=False):
        account = Account(
            account_id=Account.objects.count() + 1,
            username=username,
            password=self.key.encrypt(bytes(password, 'latin1')),
            banned=banned,
            is_admin=is_admin
        )
        account.save()
