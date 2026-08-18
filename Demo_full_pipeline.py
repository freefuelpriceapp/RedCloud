"""
RedCloud Protocol – Complete End-to-End Pipeline Demo
Encrypt → Shard (indexed) → Distribute → Save recovery package → Simulate loss → Recover
"""

import json
import random
import os
from pathlib import Path
from shard_engine import RedCloudShardEngine, Shard
from infrastructure_bridge import RedCloudInfrastructureBridge

def save_recovery_package(key: bytes, nonce: bytes, cipher_length: int, manifest: list, package_path: str = "recovery_package.json"):
    """Save everything needed for later recovery (except the shards themselves)."""
    package = {
        "key_hex": key.hex(),
        "nonce_hex": nonce.hex(),
        "original_cipher_length": cipher_length,
        "manifest": manifest
    }
    with open(package_path, "w") as f:
        json.dump(package, f, indent=2)
    print(f"Recovery package saved → {package_path}")

def run_complete_demo(input_file: str = "sample_vault.txt"):
    print("=== RedCloud Complete Pipeline Demo ===\n")

    # 1. Prepare sample file
    if not Path(input_file).exists():
        content = (
            b"RedCloud DePIN – Lifetime Secure Storage\n"
            b"This file demonstrates full client-side encryption, "
            b"Reed-Solomon (50,20) sharding, distribution, and recovery "
            b"after losing 60% of the shards."
        )
        with open(input_file, "wb") as f:
            f.write(content)
        print(f"Created: {input_file}")

    with open(input_file, "rb") as f:
        original = f.read()
    print(f"Original size: {len(original)} bytes\n")

    # 2. Encrypt
    engine = RedCloudShardEngine(data_shards=20, parity_shards=30)
    ciphertext, key, nonce = engine.local_encrypt_payload(original)

    # 3. Create indexed shards
    shards = engine.create_shards(ciphertext)
    print(f"Created {len(shards)} indexed shards\n")

    # 4. Distribute (sandbox by default)
    bridge = RedCloudInfrastructureBridge()
    manifest = bridge.distribute_shards(shards)

    # 5. Save recovery package (key + nonce + manifest)
    save_recovery_package(key, nonce, len(ciphertext), manifest)

    # 6. Simulate real-world failure – keep only 20 random shards
    surviving = random.sample(shards, 20)
    print(f"\nSimulating catastrophic loss: only {len(surviving)} shards remain\n")

    # 7. Recover
    recovered_cipher = engine.reconstruct(surviving, original_cipher_length=len(ciphertext))
    recovered = engine.decrypt_payload(recovered_cipher, key, nonce)

    # 8. Write recovered file
    output_file = "recovered_vault.txt"
    with open(output_file, "wb") as f:
        f.write(recovered)

    # 9. Verify
    success = recovered == original
    print(f"\nRecovered file → {output_file
