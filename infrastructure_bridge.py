"""
RedCloud Protocol v2.1.0-Core
Infrastructure Bridge – Lighthouse / IPFS / Filecoin Orchestration Layer
Now fully compatible with indexed Shard objects
"""

import os
import json
import tempfile
from typing import List, Dict, Optional
from shard_engine import Shard

try:
    from lighthouseweb3 import Lighthouse
    LIGHTHOUSE_AVAILABLE = True
except ImportError:
    LIGHTHOUSE_AVAILABLE = False

class RedCloudInfrastructureBridge:
    def __init__(self, api_key: Optional[str] = None):
        self.api_key = api_key or os.getenv("LIGHTHOUSE_API_KEY")
        
        if self.api_key and LIGHTHOUSE_AVAILABLE:
            print("[Bridge] Connecting to live Lighthouse network...")
            self.client = Lighthouse(token=self.api_key)
            self.mode = "live"
        else:
            print("[Bridge] Running in sandbox / simulation mode")
            self.client = None
            self.mode = "sandbox"

    def distribute_shards(self, shards: List[Shard]) -> List[Dict]:
        """
        Takes a list of indexed Shard objects and distributes them.
        Returns a routing manifest with CIDs (real or simulated).
        """
        print(f"\n[Orchestration] Distributing {len(shards)} indexed shards...")
        routing_manifest = []

        with tempfile.TemporaryDirectory() as temp_dir:
            for shard in shards:
                # Package index + data together
                payload = {
                    "protocol": "RedCloud v2.1.0",
                    "shard_index": shard.index,
                    "data_hex": shard.data.hex()
                }

                temp_path = os.path.join(temp_dir, f"rcloud_shard_{shard.index:02d}.json")
                with open(temp_path, "w") as f:
                    json.dump(payload, f)

                if self.client and self.mode == "live":
                    try:
                        result = self.client.upload(temp_path)
                        cid = result.get("Hash") or result.get("cid")
                        status = "Committed"
                        address = f"https://gateway.lighthouse.storage/ipfs/{cid}"
                    except Exception as e:
                        print(f"  → Upload failed for shard {shard.index}: {e}")
                        cid = None
                        status = "Failed"
                        address = None
                else:
                    # Realistic simulated CID
                    cid = f"QmRedCloudSim{shard.index:04d}{os.urandom(8).hex()[:16]}"
                    status = "Simulated"
                    address = f"https://gateway.lighthouse.storage/ipfs/{cid}"

                routing_manifest.append({
                    "shard_index": shard.index,
                    "cid": cid,
                    "status": status,
                    "address": address
                })

                if shard.index < 5 or shard.index >= len(shards) - 2:
                    print(f"  → Shard {shard.index:02d} | {status} | {cid}")

        print(f"[Orchestration] Distribution complete – {len(routing_manifest)} entries in manifest\n")
        return routing_manifest

# Quick test
if __name__ == "__main__":
    from shard_engine import RedCloudShardEngine

    print("=== Infrastructure Bridge Test ===\n")

    engine = RedCloudShardEngine()
    sample = b"RedCloud Infrastructure Bridge Test Payload"
    ciphertext, key, nonce = engine.local_encrypt_payload(sample)
    shards = engine.create_shards(ciphertext)

    bridge = RedCloudInfrastructureBridge()  # sandbox by default
    manifest = bridge.distribute_shards(shards)

    print(f"Manifest contains {len(manifest)} routed shards")
    print("First 3 entries:")
    for entry in manifest[:3]:
        print(f"  {entry}")
