# RedCloud Protocol – Node Operator Guide  
**v2.1.0-Core** 🔴☁️

Thank you for your interest in running a RedCloud edge node.

RedCloud is currently in active development. This guide reflects the **current architecture** and the intended path for community node operators. Some components (full daemon binary, automated emissions, production rewards) are still being completed.

---

## Current Status (August 2026)

| Component                    | Status          | Notes                                      |
|-----------------------------|-----------------|--------------------------------------------|
| Client-side encryption      | ✅ Live         | AES-256-GCM                                |
| Reed-Solomon (50,20)        | ✅ Live         | Real implementation with indexing          |
| Infrastructure bridge       | ✅ Live (sandbox + live ready) | Lighthouse / IPFS / Filecoin     |
| Node daemon binary          | ⏳ In progress  | Coming in next phases                      |
| Automated $RCLOUD emissions | ⏳ Planned      | Will be funded by consumer vault purchases |
| Production rewards          | ⏳ Planned      | Tied to verified storage + uptime          |

---

## Vision for Node Operators

You will be able to contribute spare storage and bandwidth from:
- Home PCs / NAS
- Mini-PCs / Raspberry Pi class devices
- Dedicated servers / VPS

In return, once the emissions system is live, you will earn $RCLOUD based on:
- Verified storage capacity provided
- Uptime
- Successful shard serving / retrieval performance

---

## Hardware Recommendations (Target)

### Light Edge Node (Residential)
- 100 GB+ free storage (SSD preferred)
- 50–100 Mbps stable connection
- Always-on or high-uptime device

### Standard / Dedicated Node
- 1 TB+ storage
- 500 Mbps – 1 Gbps connection
- Preferably static IP or good dynamic DNS

---

## Current Way to Participate

While the full node daemon is under development, you can already:

1. Clone the repository  
   ```bash
   git clone https://github.com/freefuelpriceapp/RedCloud.git
   cd RedCloud
