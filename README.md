# web3-integrity-checker
This project verifies the **integrity** and **soundness** of smart contracts deployed on Ethereum or other Web3-compatible chains.  
It fetches the contract bytecode from the blockchain and computes its **keccak256 hash**, helping developers verify that the deployed contract matches the expected code.

This concept aligns with **soundness principles** used in projects like **Aztec** (zero-knowledge privacy), **Zama** (homomorphic encryption), and other cryptographically secure Web3 frameworks.

## Repository Structure
- **app.py** — Python script that checks the contract code hash.  
- **README.md** — Documentation and usage instructions.

## Requirements
- Python 3.8 or newer  
- Internet connection  
- An Ethereum RPC endpoint (e.g., Infura or Alchemy)

## Installation
1. Clone this repository:
   git clone https://github.com/YOUR_USERNAME/web3-integrity-checker.git  
2. Navigate to the folder:
   cd web3-integrity-checker  
3. Install dependencies:
   pip install web3  

## Configuration
Edit the following variables in **app.py**:
- `RPC_URL`: your Ethereum node provider URL (Infura, Alchemy, or local node).  
- `CONTRACT_ADDRESS`: the smart contract address to verify.

## Usage
Run the script:
   python3 app.py

The output will show:
- Network connection status  
- Chain ID  
- Contract address  
- Bytecode hash  

Example:
🔗 Web3 Contract Integrity Checker  
Connected to chain ID: 1  
Fetching code for contract: 0x00000000219ab540356cBB839Cbe05303d7705Fa  
✅ Contract code hash (keccak256): 0x8a8a9b6c7f3f6c9b44a99a9d5e41ab8bb5d66a3a5e04afcb9e8c9e7776e2b3d9  
Integrity verified successfully (hash computed).  

## Expected Result
If the contract exists, you will receive a hash confirming that bytecode retrieval succeeded.  
If the address is invalid or empty, the script alerts you accordingly.

## Notes
- Works with any EVM-compatible network.  
- You can compare the printed hash with your deployment build hash to confirm correctness.  
- Can be integrated into CI pipelines for smart contract integrity checks.

## License
MIT License

## Suggested Repository Name
**web3-integrity-checker**
---
### 🔮 Future Improvements
- CLI interface with more network support  
- Docker image for automated integrity verification  
- Integration with Aztec and Zama frameworks  
