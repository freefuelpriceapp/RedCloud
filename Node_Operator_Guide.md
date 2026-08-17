# RedCloud Protocol: Node Operator Guide v2.1.0-Core 🔴☁️

Welcome to the distributed infrastructure layer. By hosting a RedCloud storage edge node, you lease your idle hardware capacity to encrypt, shard, and secure global consumer data while earning native `$RCLOUD` network emissions.

---

## 🖥️ 1. Hardware Infrastructure Tiers

Select the operational blueprint that matches your hardware profiles and bandwidth constraints.

### Tier 1: Light Edge Node (Residential)
*   **Storage Capacity Pool:** 100 GB minimum available storage (SSD/NVMe preferred)
*   **Bandwidth Threshold:** 100 Mbps symmetric down/up speeds
*   **Target Profile:** Personal computers, home media servers, high-performance Raspberry Pi setups
*   **Network Protocol:** Edge cache storage arrays and rapid chunk content distribution loops

### Tier 2: Dedicated Node (Enterprise)
*   **Storage Capacity Pool:** 2.0 TB minimum dedicated hardware (NVMe PCIe array)
*   **Bandwidth Threshold:** 1.0 Gbps dedicated enterprise fiber pipeline
*   **Target Profile:** Dedicated server setups, data center racks, cloud-hosted virtual private servers (VPS)
*   **Network Protocol:** High-availability primary block validation, parity mapping matrix replication

---

## 🛠️ 2. Core Daemon Installation Pipeline

Follow these structural Linux command steps to download, verify, and initialize the system daemon layer.

### Step A: Download & Extract Runtime Assets
```bash
curl -sL https://red-cloud.online | tar -xz
cd rcloud-daemon-core
```

### Step B: Initialise Identity Ledger Settings
Run the initialization flag to generate your local node configuration parameters:
```bash
./rcloud-daemon --init
```

---

## 📝 3. Configuration Properties (`config.yaml`)

Your initialization routine compiles a local node layout. Customize your routing thresholds using this standard structural design:

```yaml
protocol: "RedCloud v2.1.0-Core"
identity:
  node_name: "UK-London-Edge-01"
  reward_wallet: "8f6FXoXtKE4hnNGFzxM7Xh9TrUUVnWqvN4EWANwLpump" # Your SPL Mint Target

allocation:
  storage_bytes_limit: 500000000000 # 500 GB Allocation Limit
  allocated_path: "/mnt/storage/rcloud-vault"

telemetry:
  heartbeat_interval_seconds: 30
  max_concurrent_connections: 256
```

---

## 📈 4. Programmatic Reward Emission Formulas

Node yield isn't arbitrary—it is calculated via deterministic network tracking metrics to ensure absolute resource proof transparency.

$$\text{Node Yield Weight } (W) = S_{\text{bytes}} \times U_{\text{time}} \times \left(\frac{100}{\text{Latency}_{\text{ms}}}\right)$$

*   **$S_{\text{bytes}}$:** Verified, cryptographically audited hardware capacity allocated to the network grid.
*   **$U_{\text{time}}$:** System uptime percentage calculated across ongoing 24-hour heartbeat cycles.
*   **$\text{Latency}_{\text{ms}}$:** Average round-trip time routing matrix fragments back to our aggregation layers.

All node yield tokens are derived directly from the **50% Protocol Staking Endowment Vault** funded continually by inbound Web2 fiat credit card storage transactions.

---

## 🚦 5. Execution & Lifecycle Validation

To launch your background storage host worker, boot the service daemon framework:

```bash
./rcloud-daemon --start --config=config.yaml
```
Verify your network synchronization tracking stats via the terminal window output:
```bash
./rcloud-daemon --status
```
