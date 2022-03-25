#!/usr/bin/python3
from brownie import CoinFlip, accounts

def deploy_CoinFlip(acct_idx=0):
   account = accounts[acct_idx]
   contract = CoinFlip.deploy({"from": account})
   return contract

def main(acct_idx=0):
   deploy_CoinFlip(acct_idx)