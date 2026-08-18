# RedCloud Protocol v2.1.0-Core

Client-side AES-256-GCM encryption + true Reed-Solomon (50,20) erasure coding for decentralized storage.

**Pay once. Store forever. Zero corporate tracking.**

## Quick Start

```bash
git clone https://github.com/freefuelpriceapp/RedCloud.git
cd RedCloud
pip install reedsolo cryptography
python shard_engine.py          # basic self-test
python demo_full_pipeline.py    # full encrypt → shard → lose 30 → recover demo
