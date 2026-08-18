"""
RedCloud – Simple Recovery Helper
Takes surviving shards + original key/nonce and reconstructs the file.
"""

from typing import List
from shard_engine import RedCloudShardEngine, Shard

def recover_from_shards(
    surviving_shards: List[Shard],
    key: bytes,
    nonce: bytes,
    original_cipher_length: int,
    output_path: str = "recovered_file.bin"
):
    engine = RedCloudShardEngine()
    
    print("Starting recovery...")
    recovered_cipher = engine.reconstruct(surviving_shards, original_cipher_length)
    plaintext = engine.decrypt_payload(recovered_cipher, key, nonce)
    
    with open(output_path, "wb") as f:
        f.write(plaintext)
    
    print(f"Recovered file written to: {output_path}")
    return plaintext
