"""
RedCloud Protocol – Full Pipeline Demo
Encrypt → Real Reed-Solomon (50,20) → Simulate loss of 30 shards → Reconstruct → Decrypt
"""

import os
from pathlib import Path
from shard_engine import RedCloudShardEngine

def run_demo(input_file: str = "sample_vault.txt", output_file: str = "recovered_vault.txt"):
    print("=== RedCloud Full Pipeline Demo ===\n")

    # 1. Create a sample file if it doesn't exist
    if not Path(input_file).exists():
        with open(input_file, "wb") as f:
            f.write(b"RedCloud DePIN – Lifetime Secure Storage Demo\nThis file was encrypted, sharded with true Reed-Solomon, and recovered after simulated node loss.")
        print(f"Created sample file: {input_file}")

    # 2. Read original
    with open(input_file, "rb") as f:
        original = f.read()
    print(f"Original file size: {len(original)} bytes\n")

    engine = RedCloudShardEngine(data_shards=20, parity_shards=30)

    # 3. Encrypt
    ciphertext, key, nonce = engine.local_encrypt_payload(original)

    # 4. Create shards
    shards = engine.create_shards(ciphertext)
    print(f"Created {len(shards)} shards\n")

    # 5. Simulate catastrophic loss – keep only 20 shards
    surviving_shards = shards[:20]
    print(f"Simulating loss of 30 shards – only {len(surviving_shards)} remain\n")

    # 6. Reconstruct
    recovered_cipher = engine.reconstruct(surviving_shards, original_length=len(ciphertext))

    # 7. Decrypt
    recovered = engine.decrypt_payload(recovered_cipher, key, nonce)

    # 8. Write recovered file
    with open(output_file, "wb") as f:
        f.write(recovered)

    # 9. Verify
    success = recovered == original
    print(f"Recovered file written to: {output_file}")
    print(f"Byte-for-byte match: {success}")
    print("====================================")

    if success:
        print("✅ Pipeline successful – data survived loss of 60% of shards")
    else:
        print("❌ Reconstruction failed")

if __name__ == "__main__":
    run_demo()
