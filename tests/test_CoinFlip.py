from brownie import CoinFlip, accounts, network, config
import scripts.header as header
from scripts.deploy_CoinFlip import deploy_CoinFlip
import numpy as np

def test_CoinFlip():
   # Try to find the latest deployment of a contract. If not found, maybe deploy
   try:
      contract_address = config["networks"][network.show_active()]["CoinFlip"]
      print(f"Found contract at address {contract_address}")
      contract = CoinFlip.at(contract_address)
   except:
      print(
            f"{network.show_active()} address not found."
      )
      # If the network is a local blockchain, deploy. Otherwise, ask the user to deploy it
      if network.show_active() in header.LOCAL_BLOCKCHAIN_ENVIRONMENTS:
         print("Deploying contract...")
         contract = deploy_CoinFlip()
         print("Done")
      else:
         assert False, f"The contract is not deployed to this non-local blockchain ({network.show_active()}). Please deploy and run again."
   # Now that we've found the contract, test access to flip function as well as test that the odds of winning are roughly 50/50
   guesses = np.ones(header.NUM_FLIPS_TO_TEST)
   numWins = 0
   for guess in guesses:
      tx = contract.flip(guess)
      numWins += tx.return_value
   winRate = numWins / header.NUM_FLIPS_TO_TEST
   print(f"The win rate of this test was {winRate}.")
   # The actual win rate should be within a certain deviation from the expected value
   assert abs(winRate - header.EXPECTED_WIN_RATE) <= header.ACCEPTABLE_DEV