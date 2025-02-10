from blockchain.blockchain import Blockchain
from blockchain.utils import print_blockchain

# Initialize blockchain
quadbtech_blockchain = Blockchain()

# Add blocks
quadbtech_blockchain.add_block(["Transaction 1"])
quadbtech_blockchain.add_block(["Transaction 2", "Transaction 3"])

# Print blockchain
print_blockchain(quadbtech_blockchain)

# Validate blockchain
print("Is blockchain valid?", quadbtech_blockchain.is_chain_valid())

# Tamper with the blockchain
quadbtech_blockchain.chain[1].transactions = ["Tampered Transaction"]
print("After tampering, is blockchain valid?", quadbtech_blockchain.is_chain_valid())