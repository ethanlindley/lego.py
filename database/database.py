import os
from mongoengine import *
from cryptography.fernet import Fernet
from .account import Account


class Database(object):
    def __init__(self, key):
        if not os.path.exists('./database/data'):
            os.makedirs('./database/data/db')

        connect('lego-py', host='localhost', port=27017)  # TODO - setup config for server/db specific constants
        self.key = Fernet(key)
        
        self.accounts = []

    def register_account_client(self, username, password, banned, is_admin, account_id, characters):
        account = Account(
            account_id=account_id,
            username=username,
            password=self.key.encrypt(bytes(password)),
            banned=banned,
            is_admin=is_admin,
            characters=characters
        )
        self.accounts.append(account)

    def register_account_db(self, username, password, banned, is_admin, account_id, characters):
        account = Account(
            account_id=account_id,
            username=username,
            password=self.key.encrypt(bytes(password)),
            banned=banned,
            is_admin=is_admin,
            characters=characters
        )
        account.save()
