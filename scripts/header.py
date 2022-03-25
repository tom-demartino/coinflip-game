from brownie import CoinFlip

NON_FORKED_LOCAL_BLOCKCHAIN_ENVIRONMENTS = ["hardhat", "development", "ganache"]
LOCAL_BLOCKCHAIN_ENVIRONMENTS = NON_FORKED_LOCAL_BLOCKCHAIN_ENVIRONMENTS + [
    "mainnet-fork",
    "binance-fork",
    "matic-fork",
]
CONTRACT_NAMES = ["CoinFlip"]
CONTRACT_CONTAINERS = [CoinFlip]

# Testing
NUM_FLIPS_TO_TEST = 1500
EXPECTED_WIN_RATE = 0.5
ACCEPTABLE_DEV = 0.05   # 5% deviation from expected value