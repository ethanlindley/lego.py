from mongoengine import *
from .account import Account


class Database(object):
    def __init__(self):
        connect('lego-py', host='localhost', port=27017)
        self.accounts = []

    def register_account_client(self, username, password, banned, is_admin, account_id):
        account = Account(
            account_id=account_id,
            username=username,
            password=password,
            banned=banned,
            is_admin=is_admin
        )
        self.accounts.append(account)

    def register_account_db(self, username, password, banned, is_admin, account_id):
        account = Account(
            account_id=account_id,
            username=username,
            password=password,
            banned=banned,
            is_admin=is_admin
        )
        account.save()
