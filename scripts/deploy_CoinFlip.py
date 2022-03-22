#!/usr/bin/python3
from brownie import accounts

def deploy_CoinFlip(acct_idx=None):
   account = accounts(acct_idx)
   account.deploy(CoinFlip)

def main(acct_idx=None):
   deploy_CoinFlip(acct_idx)