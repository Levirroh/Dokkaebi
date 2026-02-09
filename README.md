# 📱 Dokkaebi

A self-hosted automation server and command gateway designed to breathe new life into old Android devices. This project leverages the **Termux** environment to transform idle hardware into a secure, extensible remote control hub.

**Author:** [Levirroh](https://github.com/Levirroh)  
**Status:** In Development (MVP Phase)

---

## 🏗️ System Architecture

The project is built on a decoupled three-tier architecture:

1.  **Server (Backend):** Powered by **Python (FastAPI)** running inside Termux on the legacy Android device. It interacts with the Android system layer via `termux-api`.
2.  **Client (Frontend):** A modern **React + Vite** (PWA) dashboard for visual monitoring and remote execution.
3.  **Network & Security:** Secure tunneling via **Tailscale** for remote access without port forwarding, protected by **API Key** authentication.

---

## 🗺️ Feature Roadmap

This roadmap focuses on general utility, cybersecurity, and quality of life.

- [ ] **1. Telemetry Dashboard (System Health)** Real-time monitoring of battery status, CPU temperature, and storage. Includes a "Watchdog" safety system to suspend heavy processes if the temperature exceeds 45°C.

- [ ] **2. Remote Command Executor (CLI & UI)** A bridge to execute remote commands on a workstation or the Android server itself. Features include triggering automation scripts, PC Wake-on-LAN, or clearing system caches.

- [ ] **3. Smart Notification Bridge** A Web Push notification system that alerts your primary device whenever the server detects specific events (e.g., download complete, network downtime, or new device detected on Wi-Fi).

- [ ] **4. Centralized Remote Downloader** An API-driven service that receives URLs and downloads large files directly to the Android’s 64GB internal storage, freeing up space on your primary devices.

- [ ] **5. SMS & Communication Gateway** An API to send and read SMS messages remotely. Useful for handling 2FA codes or sending critical system alerts via cellular network when internet access is unavailable.

---

## 🚀 Getting Started (Coming Soon)

### Prerequisites
- Unknown

### Basic Setup
```bash
# Clone the repository
git clone [still not ready])

# Follow the setup guides in the /docs folder for Termux configuration
```


## Install:
front:
```npm install styled-components lucide-react axios ```

back:
```pip install fastapi uvicorn python-dotenv```

termux:
```pkg install termux-api```

