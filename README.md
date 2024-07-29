# Drip ChainLink CCIP-BNM Token On any Testnet

## Supported Networks


```sh
- Ethereum
- polygon
- optimism
- arbitrum
- avalanche
- base
```

## Usage

1. Import or generate new accounts in ape. This script is assuming you have an account named `ctf` with necessary gas & fees required for each chain. Ex. for Ethereum you should have enough sepolia ETH, for polygon amoy should have enough MATIC etc.

2. Run

```sh
# for eth sepolia
ape run scripts/get_tokens.py --network :sepolia 
```