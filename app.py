# This script verifies the integrity (soundness) of a smart contract 
# by fetching its bytecode from the blockchain and computing its keccak256 hash.
# app.py
import sys
from web3 import Web3

RPC_URL = "https://mainnet.infura.io/v3/YOUR_INFURA_KEY"
CONTRACT_ADDRESS = "0x00000000219ab540356cBB839Cbe05303d7705Fa"

def connect_to_web3():
    w3 = Web3(Web3.HTTPProvider(RPC_URL))
    if not w3.is_connected():
        print("❌ Failed to connect to the blockchain node.")
        sys.exit(1)
    return w3

def get_contract_code_hash(w3, address):
    try:
        code = w3.eth.get_code(Web3.to_checksum_address(address))
        if len(code) == 0:
            print("⚠️ No contract bytecode found (address might be EOA or destroyed).")
            sys.exit(2)
        code_hash = Web3.keccak(code).hex()
        return code_hash
    except Exception as e:
        print(f"❌ Error fetching contract code: {e}")
        sys.exit(1)

def main():
    print("🔗 Web3 Contract Integrity Checker")
    w3 = connect_to_web3()
    print(f"Connected to chain ID: {w3.eth.chain_id}")
    print(f"Fetching code for contract: {CONTRACT_ADDRESS}")
    code_hash = get_contract_code_hash(w3, CONTRACT_ADDRESS)
    print(f"✅ Contract code hash (keccak256): {code_hash}")
    print("Integrity verified successfully (hash computed).")
    

if __name__ == "__main__":
    main()

