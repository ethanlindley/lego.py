import os
from mongoengine import *
from .account import Account


class Database(object):
    def __init__(self, salt):
        if not os.path.exists('./resources/data'):
            os.makedirs('./resources/data/db')

        connect('lego-py', host='localhost', port=27017)  # TODO - setup config for server/db specific constants
        self.accounts = []
        self.get_accounts()

        self.salt = salt

    def get_accounts(self):
        # load the database and store account objects in a list 
        # that can be dynamically read across server instancess
        for account in Account.objects:
            self.accounts.append(account)

    def register_account_db(self, username='', password='', banned=False, is_admin=False):
        account = Account(
            account_id=Account.objects.count() + 1,
            username=username,
            password=password,  # TODO - fix hashing of passwords in db
            banned=banned,
            is_admin=is_admin
        )
        account.save()
        self.accounts.append(account)
