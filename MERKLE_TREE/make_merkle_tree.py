import hashlib

# Helper function to calculate SHA256 hash
def sha256_hash(data):
    return hashlib.sha256(data.encode('utf-8')).hexdigest()

# Function to construct a Merkle Tree and print it as a tree structure
def construct_and_print_merkle_tree(transactions):
    # Step 1: Hash all transactions to form leaf nodes
    levels = []  # Store all levels of the tree
    current_level = [sha256_hash(tx) for tx in transactions]
    levels.append(current_level)

    while len(current_level) > 1:
        next_level = []
        for i in range(0, len(current_level), 2):
            # Pair adjacent hashes; if odd, duplicate the last one
            left = current_level[i]
            right = current_level[i + 1] if i + 1 < len(current_level) else current_level[i]
            # Combine and hash the pair
            combined_hash = sha256_hash(left + right)
            next_level.append(combined_hash)
        levels.append(next_level)  # Store the next level
        current_level = next_level  # Move up to the next level

    # The root hash is the single remaining hash
    root_hash = current_level[0]

    # Print the tree-like structure
    print("\nMerkle Tree:")
    for level in reversed(levels):  # Print from root to leaves
        print(" | ".join(level))

    return root_hash

# Example transactions
transactions = ["Tx1: Akash pays Satish 10", "Tx2: Ram pays Krishna 5", "Tx3: Sandeep pays Narendra 2", "Tx4: Sowjanya pays Manasa 10","Tx5: Gopi pays Durga 500"]
merkle_root = construct_and_print_merkle_tree(transactions)

print("Transactions:", transactions)
print("Merkle Root:", merkle_root)
