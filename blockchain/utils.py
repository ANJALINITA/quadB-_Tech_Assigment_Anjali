def print_blockchain(blockchain):
    for block in blockchain.chain:
        print(f"Block {block.index} [Hash: {block.hash}, Previous Hash: {block.previous_hash}, Nonce: {block.nonce}]")
        print(f"Transactions: {block.transactions}\n")