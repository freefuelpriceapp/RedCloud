"""
RedCloud Protocol – Full Pipeline Demo (Indexed Shards)
Encrypt → Real Reed-Solomon (50,20) → Lose 30 random shards → Reconstruct → Decrypt
"""

import random
from pathlib import Path
from shard_engine import RedCloudShardEngine, Shard

def run_demo(input_file: str = "sample_vault.txt", output_file: str = "recovered_vault.txt"):
    print("=== RedCloud Full Pipeline Demo (Indexed) ===\n")

    # 1. Create sample file if needed
    if not Path(input_file).exists():
        sample_content = (
            b"RedCloud DePIN – Lifetime Secure Storage Demo\n"
            b"This file was encrypted with AES-256-GCM, "
            b"sharded with true Reed-Solomon (50,20), "
            b"and successfully recovered after losing 30 shards."
        )
        with open(input_file, "wb") as f:
            f.write(sample_content)
        print(f"Created sample file: {input_file}")

    # 2. Read original
    with open(input_file, "rb") as f:
        original = f.read()
    print(f"Original size: {len(original)} bytes\n")

    engine = RedCloudShardEngine(data_shards=20, parity_shards=30)

    # 3. Encrypt
    ciphertext, key, nonce = engine.local_encrypt_payload(original)

    # 4. Create indexed shards
    shards = engine.create_shards(ciphertext)
    print(f"Created {len(shards)} indexed shards\n")

    # 5. Simulate real-world loss – keep 20 random shards
    surviving: list[Shard] = random.sample(shards, 20)
    print(f"Simulating loss of 30 shards – kept {len(surviving)} random shards\n")

    # 6. Reconstruct
    recovered_cipher = engine.reconstruct(surviving, original_cipher_length=len(ciphertext))

    # 7. Decrypt
    recovered = engine.decrypt_payload(recovered_cipher, key, nonce)

    # 8. Write recovered file
    with open(output_file, "wb") as f:
        f.write(recovered)

    # 9. Verify
    success = recovered == original
    print(f"Recovered file: {output_file}")
    print(f"Byte-for-byte match: {success}")
    print("============================================")

    if success:
        print("✅ SUCCESS – Data survived loss of 60% of the shards")
    else:
        print("❌ Reconstruction failed")

if __name__ == "__main__":
    run_demo()
