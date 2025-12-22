<div align="center">

  <div>

  <!-- Shields.io Info -->
  [![Python](https://img.shields.io/badge/python-3.9+-blue)](#)
  ![GitHub repo size](https://img.shields.io/github/repo-size/denv3rr/network-explorer)
  ![GitHub Created At](https://img.shields.io/github/created-at/denv3rr/network-explorer)
  ![Last Commit](https://img.shields.io/github/last-commit/denv3rr/network-explorer)
  ![Issues](https://img.shields.io/github/issues/denv3rr/network-explorer)
  ![License](https://img.shields.io/github/license/denv3rr/network-explorer)
  ![Website](https://img.shields.io/website?url=https%3A%2F%2Fseperet.com&label=seperet.com)

  <!-- OS Icons -->
  <img width="32" alt="image" src="https://github.com/user-attachments/assets/3b32cddc-c6c6-4acc-b2de-d01b30e5613d" />
  <img width="32" alt="image" src="https://github.com/user-attachments/assets/af8dec60-cab6-4c1a-8ea3-9cb2d75e8516" />
  <img width="32" alt="image" src="https://github.com/user-attachments/assets/df923ccd-dd6a-4b86-9864-2c5d6cea4e4a" />

  </div>
  
</div>

<br><br>

<div align="center">

<div align="center">
  <a href="https://seperet.com">
    <img width="100" src=https://github.com/denv3rr/denv3rr/blob/main/IMG_4225.gif/>    
  </a>
</div>

  [About](#about) |
  [Features](#features) |
  [Quick Start](#quick-start) |
  [Manual Installation](#manual-installation) |
  [Specific Usage](#specific-usage) |
  [Logs](#logs) |
  [Troubleshooting](#troubleshooting) |
  [seperet.com](https://seperet.com)
  
</div>

---

## About

A Python tool for quick **network and host security assessment**.

---

## Features

- **Main Menu**
  - Launch without flags or arguments to access a user-friendly menu.
- **Wi-Fi scanning**
  - Lists visible networks, channels, BSSIDs, signal strength, and optional BSSID/IP geolocation.
- **Port scanning**
  - **Top TCP** (Fast), **Full Connect**, and **UDP** (Payload Probe) modes.
- **Bluetooth scanning**
  - Discovers nearby BLE devices with RSSI signal strength and metadata (using `bleak`).
- **OS security checks**
  - Detects Firewall status and Antivirus presence on Windows, Linux, and macOS.
- **Network metadata scanning**
  - Identifies connection type (Wired/Wi-Fi), local identity, public IP, ISP, ASN, and geographic info.
- **Outbound testing (Web/DNS)**
  - Safe by default with very low request rate; optional active probing with explicit warning/acknowledgement.
  - External OSINT (RDAP, DNS-over-HTTPS, GeoIP) only when `--external` is enabled.
- **Full Scan mode**
  - One-click execution of all modules with intelligent defaults.

---

## Quick Start

Run:

```bash
git clone https://github.com/denv3rr/network-explorer.git
cd network-explorer
python run.py
```

---

## Manual Installation

### **1. Check Requirements**

- **Python 3.9+**
- Modules auto-installed at runtime via `requirements.txt` (you may be prompted). See <a href="#quick-start">Quick Start</a> above.
  - Set `NEX_AUTO_INSTALL=1` to allow auto-install without prompts.
  - `requests`
  - `ifaddr`
  - `texttable`
  - `bleak`
  - `colorama`

- or install with this command before running:

```bash
pip install -r requirements.txt
```

### **2. Clone or Download**

- Clone

  - ```bash
    git clone https://github.com/denv3rr/network-explorer.git
    cd network-explorer
    ```
- Download
  
    - `.zip`:  [network-explorer-main](https://github.com/denv3rr/network-explorer/archive/refs/heads/main.zip)

### **3. Run**
  
```bash
python run.py
```

---

## Specific Usage

### **Basic commands**

| Action | Command |
|--------|----------|
| Quick Start | `python run.py` |
| Run all modules | `python run.py --all` |
| Wi-Fi scan only | `python run.py --wifi` |
| Port scan (top) | `python run.py --ports` |
| Port scan (custom range) | `python run.py --ports 1-2000` |
| Port scan profile | `python run.py --ports --profile aggressive` |
| Port scan rate limit | `python run.py --ports --rate 200` |
| Network metadata (wired support) | `python run.py --network` |
| OS security check | `python run.py --os` |
| Bluetooth scan | `python run.py --bluetooth` |
| Outbound testing (safe, low-rate) | `python run.py --outbound example.com` |
| Outbound testing with OSINT | `python run.py --outbound example.com --external` |
| Outbound testing (active) | `python run.py --outbound example.com --outbound-active --active-ok` |
| Outbound testing with rate limit | `python run.py --outbound example.com --outbound-rate 5` |
| Outbound active requires ack | `--active-ok` must be supplied to proceed |
| Allow external lookups | `python run.py --network --external` |
| Skip confirmation prompts | `python run.py --all --yes` |
| Wi-Fi diagnostic dump | `python run.py --wifi --wifi-diag` |
| Specify Wi-Fi interface | `python run.py --wifi --wifi_interface "Wi-Fi"` |

## Flags

### Safe vs Active
- **Safe mode**: Minimal, low-rate requests and passive checks only.
- **Active mode**: Sends additional probes (paths/methods); requires `--outbound-active` and `--active-ok`.

### FAQ

**Does safe mode avoid touching the target?**  
Safe mode still makes low-rate HTTP/DNS requests to the target; it is designed to be low-impact, not invisible.

**How do I enable external OSINT?**  
Use `--external` to allow RDAP, DNS-over-HTTPS, and GeoIP lookups.

**Why do I need `--active-ok`?**  
Active probing can trigger alerts or violate acceptable use; explicit acknowledgement is required.

### General
- `--external`: Allow external lookups (public IP, MAC vendor, OSINT).
- `--yes`: Skip confirmation prompts.
- `--json <file>`: Write full results to a JSON file.

### Port Scanning
- `--ports [start-end]`: Run port scan (default `1-1024` when provided).
- `--profile safe|normal|aggressive`: Port scan profile.
- `--rate <ports/sec>`: Rate limit ports/sec per host.
- `--timeout <seconds>`: Socket timeout.
- `--workers <count>`: Worker threads.
- `--no-banner`: Skip banner grabbing.

### Wi-Fi
- `--wifi`: Run Wi-Fi scan.
- `--wifi_interface "<name>"`: Specify Wi-Fi interface.
- `--wifi-diag`: Print diagnostic netsh output.
- `--geo`: Enable Wi-Fi geolocation (requires `--external`).

### Outbound Testing
- `--outbound [target]`: Run outbound testing (safe by default).
- `--outbound-active`: Enable active outbound probing (requires acknowledgement).
- `--active-ok`: Acknowledge active probing risk to proceed.
- `--outbound-rate <req/sec>`: Rate limit outbound requests (defaults to low-rate safe mode).

### Deprecated
- `--outbound-aggressive`: Deprecated alias for `--outbound-active`.
- `--aggressive-ok`: Deprecated alias for `--active-ok`.
| Save JSON report | `python run.py --all --json results.json` |
| Disable colors | `python run.py --all --no-color` |
| Silent mode | `python run.py --all --silent` |

---

## Logs

- Logs are automatically written to the `logs/` directory.
- Files follow timestamp format:
  ```
  NEX_YYYYMMDD_HHMMSS.log
  ```
- Old logs (>7 days) are automatically pruned.

---

## Troubleshooting

| Issue | Fix |
|-------|-----|
| **Wi-Fi scan shows “No Wi-Fi data.”** | Ensure Wi-Fi adapter is enabled and, on Windows, run as **Administrator** with **Location Services ON**. |
| **No results on wired connection** | Use `--network` to retrieve public IP and geolocation via IP-based lookup. |
| **Permission errors (Linux/macOS)** | Run with `sudo` if needed for raw socket access. |

---

[COMMENT]: <LOGO*****************************************>
<div align="center">
  <a href="https://seperet.com">
    <img src=https://github.com/denv3rr/denv3rr/blob/main/IMG_4225.gif/>    
  </a>
</div>

