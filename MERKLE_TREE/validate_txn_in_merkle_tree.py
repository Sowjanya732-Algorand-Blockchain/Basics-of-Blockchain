import hashlib

# Helper function to calculate SHA256 hash
def sha256_hash(data):
    return hashlib.sha256(data.encode('utf-8')).hexdigest()

# Function to validate a transaction in a Merkle Tree
def validate_transaction(transaction, merkle_root, merkle_path):
    """
    Validate a transaction using its Merkle Path.

    Args:
    - transaction (str): The transaction to validate.
    - merkle_root (str): The root hash of the Merkle Tree.
    - merkle_path (list): A list of tuples where each tuple contains:
      - The sibling hash.
      - A direction ('left' or 'right') indicating whether the sibling is on the left or right.

    Returns:
    - bool: True if the transaction is valid, False otherwise.
    """
    # Compute the hash of the transaction
    current_hash = sha256_hash(transaction)

    # Traverse the Merkle Path to compute the Merkle Root
    for sibling_hash, direction in merkle_path:
        if direction == 'left':
            current_hash = sha256_hash(sibling_hash + current_hash)
        elif direction == 'right':
            current_hash = sha256_hash(current_hash + sibling_hash)
        else:
            raise ValueError("Invalid direction in Merkle Path. Must be 'left' or 'right'.")

    # Compare the computed root with the given Merkle Root
    return current_hash == merkle_root

# Example Usage
if __name__ == "__main__":
    # Example transaction
    transaction = "Tx2: Ram pays Krishna 5"

    # Example Merkle Root (calculated previously)
    merkle_root = "b24e73c300a489afa5feff6cc1318bbe3ad37b215c034833bab7c9a31d9f0f6a"

    # Example Merkle Path for the transaction
    # Format: (sibling hash, direction)
    merkle_path = [
        ("71894e0b1bac665e17b9880f45a8e38bb791304c1831ec67528a0bdc0593fe3e", "left"),
        ("f8f50a5a393c27fdd4421dd6acf816933bc4c731ba21ddc79ef2c3029a1aa5f0", "right")
    ]

    # Validate the transaction
    is_valid = validate_transaction(transaction, merkle_root, merkle_path)
    print("Is the transaction valid?", is_valid)
