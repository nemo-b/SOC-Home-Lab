# **🧠 Home SOC Lab: Network Visibility & Automation Layer**

> **Objective:** To bridge the gap between network activity, endpoint telemetry, and automated analysis within a unified SOC workflow.

---
## **📂 Project Roadmap & Progress**

### **Phase 0: Assumed Baseline (Guaranteed)**

_Focus: Foundation of a security professional._
- [x] **Secure VPN usage** (Encryption & Tunneling)
- [x] **Credential Management** (Password Manager + MFA)
- [x] **Virtualization Fundamentals** (Hypervisors & OS Isolation)
- [x] **Backup Awareness** (Data Integrity & Recovery)
- [x] **Security-First Mindset** (Principle of Least Privilege)

---
### **Phase 1: Environment Orchestration & Baseline Connectivity**

- [x] **Home Network Inventory:** Documented Device names, IPs, OS types, and Roles.
- [x] **Initial Nmap Baseline:** Identified open ports and services to map the "known good" state.
- [x] **Snapshot Documentation:** Captured Nmap output for future delta analysis.

> **Key Question:** _If something changes on my network, would I notice?_

---
### **Phase 2: Telemetry Pipeline & Data Ingestion Engineering**

- [x] **Endpoint Logging:** Enabled Windows Security Events and Linux `auth.log` monitoring.
- [x] **SIEM Deployment:** Installed and optimized Splunk Enterprise on a Windows 11 Indexer.
- [x] **Universal Forwarding:** Successfully routed cross-platform logs from Ubuntu and Windows.
- [x] **Data Validation:** Confirmed searchable indexing and timestamp accuracy across hosts.

> **Key Question:** _Can I see important activity from multiple systems in one place?_

---
### **Phase 3: Active Reconnaissance & Event Correlation**

- [x] **Security Signal Identification:** Isolated failed logins, service restarts, and sudo events.
- [x] **SOC Dashboard V1:** Visualized authentication trends and system stability metrics.
- [x] **Manual Correlation:** Cross-referenced Nmap scan timing with internal Splunk log spikes.
- [x] **Search Refinement:** Applied `rex` field extractions and filters to reduce "log noise."

> **Key Question:** _Can I turn raw logs into meaningful security signals?_

---
### **Phase 4: Detection Engineering & Behavioral Analytics**

- [x] **Advanced Alerting:** Configure Splunk triggers for Brute Force and Privilege Escalation.
- [x] **Network Delta Analysis:** Run periodic Nmap scans and compare results to Phase 1 baseline.
- [x] **Behavioral Profiling:** Does network activity align with expected endpoint behavior?

> **Key Question:** _Do network changes match what my logs are telling me?_

---
### **Phase 5: Automation (Python – Minimal & Intentional)**

- [x] **Python Integration:** Write a script to parse Nmap XML outputs or flag new ports.
- [x] **Automated Reporting:** Generate human-readable summaries of network changes.
- [x] **SOC Workflow Optimization:** Document how automation reduces analyst fatigue.

> **Key Question:** _Can I reduce repetitive analysis with simple automation?_

---
### **Phase 6: Professional Summary & SOC Portfolio**

- [ ] **Executive Reporting:** Draft a SOC-style summary for potential employers.
- [ ] **Evidence Gallery:** Finalize sanitized screenshots of dashboards and alerts.
- [ ] **Project Reflection:** Highlight the "Analyst Thinking" behind every technical choice.

> **Key Question:** _If an employer skimmed this for 60 seconds, would they understand my thinking?_

---
### **📝 Resource Library**
- **Build Your Own Cybersecurity Lab at Home:** [Watch Here](https://www.youtube.com/watch?v=izmCJlJEvQw)
- **SIEM Lab in Under 15 Minutes:** [Watch Here](https://www.youtube.com/watch?v=QT81wcuoRFY)
- **Splunk Beginner Tutorial:** [Watch Here](https://www.youtube.com/watch?v=3CiRs6WaWaU)

- - -
# **Phase 1: Environment Orchestration & Baseline Connectivity**
**Focus:** _Networking, VM/Hardware setup, and Firewall configuration._

---

## **📊 Nmap: Learning Recap (Project Context)**

### **1. Tool Familiarization & Objective**
To establish a baseline for the SOC Home Lab, I utilized **Nmap (via the Zenmap GUI)** to perform network discovery. The primary objective was to map the local network topology and identify active services that require monitoring within the SIEM (Splunk).
- **Learning Resource:** [Zenmap Lab Tutorial - Nmap/Zenmap Basics](https://www.youtube.com/watch?v=ayx8luaHk2c)
- **Methodology:** Initial testing was conducted against the `scanme.nmap.org` sandbox to verify Nmap output formats and service detection capabilities without exposing local infrastructure during the learning phase.

### **2. Service Enumeration & Security Observations**
During testing, I observed a significant delta in open ports between the tutorial environment and live targets.
- **Discovery:** Identified nearly 1,000 scanned ports on the test target, with a high density of "Open" vs. "Closed/Filtered" states.
- **SOC Insight:** A high number of open ports increases the **Attack Surface**. In a production environment, this would trigger a "Hardening" task to close any non-essential services.

### **3. Topology Mapping & Subnet Discovery**
I successfully executed a subnet scan (e.g., `192.168.1.0/24`) to generate a visual **Network Topology Map**.
- **Process:** Used CIDR notation to define the scan range, identifying all interconnected nodes (VMs, host machines, and gateway).
- **Data Sanitization (OPSEC):** For documentation purposes, all screenshots of the network topology have been sanitized. Public IP addresses and sensitive internal MAC addresses were redacted to maintain **Operations Security (OPSEC)** while still demonstrating network architectural knowledge.

---

## **📸 Example Visuals**

<p align="center">
  <img src="images/Nmap%20Output%20Example%201.png" alt="Windows Dashboard" width="500">
</p>

<p align="center">
  <img src="images/Nmap%20Output%20Example%202.png" alt="Windows Dashboard" width="500">
</p>

> _Example of Nmap Output._

<p align="center">
  <img src="images/Nmap%20Topology%20Example.png" alt="Windows Dashboard" width="500">
</p>

> _Example of My Network Topology._

---
# **Phase 2: Telemetry Pipeline & Data Ingestion Engineering**
**Focus:** _Universal Forwarder setup, Index creation, and log routing._

---
## **📊 Splunk: Learning Recap (Project Context)**

> **Purpose:** Summarize Splunk concepts used in this project without repeating foundational explanations elsewhere. Originally discussed in the (link to other page) lab.

### **🔹 Why Splunk Was Used**
Splunk was selected to:
- Centralize logs from multiple systems
- Search and filter security-relevant events efficiently
- Visualize activity in a SOC-style dashboard
The focus was on **analysis and visibility**, not enterprise-scale deployment.
### **🔹 Core Concepts Applied**
- **Indexes**
    - Logs are organized by type/source for efficient searching
    - Separating data improves clarity and performance
- **Events**
    - Individual log entries (e.g., login attempt, system event)
    - Used as the atomic unit for investigation
- **Search & Filtering**
    - Searches were crafted to isolate: Authentication activity, System changes, and Network-related indicators
    - Emphasis on narrowing noise into actionable signals
- **Time-Based Analysis**
    - Events analyzed across time windows
    - Helped identify spikes, anomalies, and patterns

### **🔹 Dashboard Design Philosophy**
Dashboards were built to:
- Answer specific security questions quickly
- Reduce manual searching during investigation
- Highlight abnormal behavior rather than raw log volume

**Panels focus on:**
- Authentication trends
- Event frequency over time
- Notable security events

### **🔹 Alerts & Detection Logic**
Simple alert logic was implemented to:
- Flag repeated failed logins
- Surface unusual activity patterns
- Support analyst triage rather than automated response

Alerts were intentionally conservative to avoid noise. The goal was to demonstrate **analyst thinking**, not mastery of every Splunk feature.

---

## **📂 Phase 2: Continued...**

### **Initial Goal**
The goal was to follow a guided video walkthrough to install Splunk Enterprise and begin collecting Windows security logs for basic monitoring and detection. Before installation, I spent time understanding what Splunk is and how it functions:
- Splunk is a **SIEM (Security Information and Event Management)** platform
- It centralizes logs from one or more systems
- It runs primarily through a **web interface**, not as a traditional desktop application
- Data collection and processing are handled separately from visualization

This understanding helped frame later troubleshooting decisions.

### **Following the Video (Initial Attempt)**
I followed a YouTube tutorial to:
- Install **Splunk Enterprise** on Windows
- Install the **Universal Forwarder** on the same system
- Begin collecting Windows Event Logs

During this step, I ran into an issue where navigating to **Settings → Data Inputs → Local Event Log Collection** returned a **404 error**. This blocked progress relative to the video and initially suggested a broken install.

### **Investigation & Hypotheses**
Several possibilities were considered:
- Incorrect forwarder architecture (32-bit vs 64-bit)
- Management ports misconfigured during installation
- Forwarder web UI being disabled by default
- Required Windows add-ons missing

At this point, Splunk Enterprise itself was confirmed to be accessible at: `http://localhost:8000`

---
## **🛠️ Corrections & Key Fixes**

The following actions resolved the issue:
- Installed **Splunk Add-on for Microsoft Windows**
- Confirmed that **Universal Forwarder does not use the web UI** for input configuration
- Restarted the forwarder **using an Administrator terminal**
- Verified that Splunk Enterprise was listening for forwarded data

> **Important realization:** The 404 error was expected behavior when using a Universal Forwarder and not an actual failure.

---
## **✅ Validation of Success**

Data ingestion was confirmed using SPL searches:

Code snippet:

```
index=*
```

_→ Returned a large volume of events, confirming indexing was active._

Code snippet:

```
index=* host=Solace
```

_→ Returned thousands of events, confirming forwarding worked._

Code snippet:

```
index=main sourcetype=WinEventLog:Security
```

_→ Returned security-related Windows events, confirming correct log collection._

At this point, the pipeline from **Windows → Universal Forwarder → Splunk Enterprise → Search** was fully functional. With reliable log data now flowing into Splunk, the next phase of the project is to identify meaningful security signals and visualize them through targeted dashboards.

---
## **🎯 Defining Protection Goals**

At this stage of the project, the focus shifts from data ingestion to **defining what I am actually trying to protect**. Before expanding the lab further, I established a set of clear priorities that act as a scope boundary and help keep the dashboard purposeful rather than noisy.
### **Protection Priorities**
- **Primary concerns:**
    - Unauthorized logins (local or remote)
    - Account misuse (bursts of failed authentication attempts)
    - Unexpected system or service changes
    - Network-related activity that _could_ indicate probing or scanning
- **Explicitly out of scope:**
    - Advanced malware detection
    - EDR-level telemetry
    - Nation-state threat modeling
    - Full packet inspection within Splunk

The goal is **visibility**, not exhaustive detection.

---
## **📊 Dashboard Design and Rationale**

Using guidance from ChatGPT, I designed a small set of focused panels that collectively provide situational awareness without overwhelming the viewer.

### **Panel 1: Authentication Activity Over Time (Line Graph)**

This panel visualizes authentication behavior over time, highlighting successful versus failed login attempts. It is primarily used to detect anomalies such as spikes in failures or unusual login patterns.

**Search used:** `index=* sourcetype=WinEventLog:Security EventCode IN (4624, 4625) | eval Action=if(EventCode=4624,"Success","Failure") | timechart count by Action`

**Relevant Event Codes:**
- `4624` — Successful login
- `4625` — Failed login

### **Panel 2: Recent Security Events (Table)**

This panel provides a human-readable view of recent security-relevant activity, allowing for quick inspection of individual events when investigating suspicious behavior.

**Search used:** `index=* sourcetype=WinEventLog:Security | table _time host EventCode Account_Name Source_Network_Address | sort -_time`
- The table is limited to ~50 rows to balance visibility and readability.
- Fields are intentionally kept minimal to support fast triage.
### **Panel 3: System Activity / Stability Events (Line Graph)**

To avoid an authentication-only view, this panel tracks general system activity such as restarts and service-related events.

**Search used:** `index=* sourcetype=WinEventLog:System | timechart count`

---

## **🧐 Overall Dashboard Observations**

Building this dashboard highlighted how quickly complexity can grow. Even with a single host, careful scoping is necessary to prevent information overload. Below is a **sanitized example** of the completed dashboard:

<p align="center">
  <img src="images/Windows%20Dashboard.png" alt="Windows Dashboard" width="500">
</p>

> _Fields containing hostnames, usernames, timestamps, and network identifiers have been intentionally redacted._

**Key Takeaways and Future Improvements:**
- Improve dashboard readability and visual clarity
- Add basic alerting for abnormal authentication patterns
- Expand the lab by forwarding logs from an additional system
- Revisit this dashboard later with refined detection logic

---

## **🚀 Future Work**

Planned next steps include:
- **Log Forwarding from a Secondary Host:** Deploy a Splunk Universal Forwarder on an additional system (Ubuntu) to simulate multi-host monitoring.
- **Refinement and Light Alerting:** Minor improvements to dashboard readability and the addition of basic alerts.
- **Transition to Network-Focused Analysis (Nmap):** Focus will shift to using Nmap to explore network discovery, later correlating findings with log data.

---

## **📊 Splunk Universal Forwarder: Ubuntu Integration**

### **Initial Objective**

After successfully ingesting local Windows logs, the next objective was to expand visibility:
- Practice **centralized log aggregation**
- Ubuntu Linux host → Windows Splunk Enterprise server

### Installing the Universal Forwarder (Ubuntu)
- Downloaded the **Splunk Universal Forwarder for Linux (x64)**
- Installed under: `/opt/splunkforwarder`
- Accepted the license and reached initial setup.

**Setup Clarification:** During installation, I learned the credentials entered are **local to the forwarder**, not tied to Splunk Enterprise. Usernames containing spaces were rejected; re-ran setup with a valid format.

### First Forwarding Attempt (Failed)

Attempted: `sudo ./splunk add forward-server <WINDOWS_IP>:9997`
- **Result:** Command failed with a directory-related error.
- **Root Cause:** Command was executed from the wrong directory. Learned that Splunk CLI commands must be run from: `/opt/splunkforwarder/bin`
### Network Connectivity Investigation
- Ubuntu → Windows ping **failed**
- Windows → Ubuntu ping **succeeded** Indicated **one-way network reachability**, suggesting firewall or adapter issues.
### IP Address & Adapter Confusion

The Windows host had multiple adapters (VPN, Ethernet, Wi-Fi).
- **Key Finding:** VPN adapter IP was incorrectly used. The correct IP belonged to the **Wi-Fi adapter**.
### Firewall & Port Review

Confirmed VPN was disabled and port **9997** was configured, yet forwarding still failed. This reinforced that the issue was **network handling**, not Splunk configuration.
### Firewall Rule Breakthrough
- **Resolution:** Added an explicit **inbound Windows Firewall rule** allowing TCP traffic on port 9997.
- **Result:** Ubuntu → Windows ping succeeded; network reachability confirmed.
### Placeholder Syntax Error (Critical Discovery)
A subtle mistake was identified: documentation placeholders like `<WINDOWS_IP>` were mistakenly entered **literally**.
- **Incorrect:** `<192.168.x.x>`
- **Correct:** `192.168.x.x`
### Successful Forwarder Configuration
Final commands executed on Ubuntu:

Bash

```
cd /opt/splunkforwarder/bin
sudo ./splunk add forward-server WINDOWS_IP:9997
sudo ./splunk enable boot-start
sudo ./splunk start
sudo ./splunk add monitor /var/log/auth.log
```

---

## **✅ End-to-End Log Verification**

- Generated test event on Ubuntu: `logger "SOC TEST EVENT"`
- Event appeared in Splunk with correct Timestamp, Hostname, and Message.

**Pipeline confirmed:** **Ubuntu → Forwarder → Splunk Receiver → Search**

### **Troubleshooting Journey Summary**

1. **Connectivity:** Resolved Windows Firewall ICMP block and Profile mismatch (Public/Private).
2. **Data Routing:** Used "Remove and Replace" to move logs from `main` to `linux_logs` index.
3. **Permissions:** Changed `/var/log/auth.log` from `600` to `644` to allow Splunk visibility.
4. **Field Extraction:** Wrote **Custom Regex (rex)** to extract `executing_user` and `cmd_run` from unstructured Linux strings.

|**Incident**|**Root Cause**|**Resolution**|**Learning Outcome**|
|---|---|---|---|
|**404 Web Error**|Universal Forwarders (UF) lack a Web UI by design.|Configured inputs via Splunk Enterprise and CLI.|Differentiated between "Indexer" and "Forwarder" capabilities.|
|**One-Way Ping**|Windows Firewall blocked ICMP requests on Public profile.|Explicitly allowed ICMPv4 and switched to Private profile.|Network profiles significantly impact peer-to-peer visibility.|
|**Inactive Forward**|TCP Port 9997 was blocked by Windows Defender.|Created an Inbound Rule for Port 9997 (All Profiles).|Listening services are useless if the host firewall drops the packets.|
|**Zero Events (Linux)**|Permission `600` on `auth.log` blocked the Splunk user.|Applied `chmod 644` to the authentication log file.|SIEM services must have granular read-access to target logs.|
|**Syntax Error**|Documentation placeholders (`<IP>`) were used literally.|Removed brackets and used raw IP address in CLI strings.|Verified that literal syntax vs. placeholder notation is a critical distinction.|
|**Blank Dashboard**|Splunk lacked the Linux TA for automatic field parsing.|Implemented `rex` (Regex) commands to manually extract data.|Manual field extraction (Regex) is a "Fail-Safe" for custom data.|

---
## **📸 Example Visuals**

<p align="center">
  <img src="images/Splunk%20Input%20from%20Ubuntu.png" alt="Windows Dashboard" width="500">
</p>

_Terminal from the Ubuntu Laptop._

<p align="center">
  <img src="images/Splunk%20Output%20from%20Ubuntu.png" alt="Splunk Output from Ubuntu" width="500">
</p>

_Splunk result on Windows Laptop._

<p align="center">
  <img src="images/Linux%20Dashboard.png" alt="Windows Dashboard" width="500">
</p>

_Final Dashboard for Authentication & Privilege Escalation Auditing._

---
## **💡 Key Takeaways**
- Network and firewall issues are more common than Splunk misconfiguration.
- TCP testing is more reliable than ICMP for diagnosing forwarding problems.
- Placeholder syntax in documentation must never be copied literally.
- Incremental testing prevents misdiagnosis and enables systematic isolation.

---
# **Phase 3: Active Reconnaissance & Event Correlation**
**Focus:** _Nmap scanning, cross-referencing logs, and time-syncing events._

---
## **🔍 Active Reconnaissance Simulation (Nmap)**

### **1. The Test Methodology**
To test the visibility of my new telemetry pipeline, I conducted an active **Nmap service discovery scan** from the Windows Indexer against the Ubuntu endpoint. This simulated the "Discovery" phase of a typical cyber attack.

### **2. Service Discovery & Port Analysis**
The scan yielded critical insights into the communication between my two hosts:
- **TCP Port 9997 (Identified):** Confirmed as the active "Data Plane" for the Splunk Universal Forwarder.
- **TCP Port 8089 (Identified):** Confirmed as the **Splunkd Management Port**.
- **Analysis:** I correlated this "network noise" with the internal Splunk processes. While 9997 handles the log stream, Port 8089 manages the command-and-control communication between the Indexer and the Forwarder. Seeing this in Nmap verified exactly which "doors" were open on my target.

---

## **🔗 Manual Event Correlation**

### **1. Observation & Timing**
I successfully synchronized network-level probes (the Nmap scan) with application-level logs (`auth.log`).

### **2. Validation of Pipeline Resilience**
By monitoring the Splunk responses in real-time as the scan was running, I verified that:
- Administrative actions on the Ubuntu machine were instantly indexed on the Windows host.
- The end-to-end telemetry pipeline is resilient, with accurately synchronized timestamps across different operating systems.

---

## **🛡️ Data Privacy & OPSEC (Operational Security)**

### **1. Standardized Redaction Strategy**
To prepare this lab for a professional portfolio, I implemented a strict data masking policy for all documentation.

### **2. Technical Reasoning**
I utilized **heavy Gaussian blurs** rather than solid black redaction boxes for several reasons:
- **Context Preservation:** It maintains the visual structure of the log files, showing the "shape" of the data without revealing the content.
- **PII Protection:** It effectively hides sensitive information such as Public IPs, MAC addresses, and private hostnames.
- **Professionalism:** This demonstrates a "Security-First" mindset, proving I can share my work publicly without violating operational security (OPSEC).

---
## **📸 Example Visuals**

<p align="center">
  <img src="images/Ubuntu%20Forwarder%20Active from%20Windows%20Nmap.png" alt="Windows Dashboard" width="500">
</p>

> **Description:** _Nmap Service Discovery: Identifying Splunkd Management (Port 8089) and Data Pipeline on Ubuntu Endpoint._

---
# **Phase 4: Detection Engineering & Behavioral Analytics**
**Focus**: Defining "The Malicious," creating SIEM triggers, and validating the telemetry loop.

---
## **🎯 Objective**
To move beyond passive log collection and establish an active monitoring posture. This phase focuses on creating logic that can differentiate between standard user activity and potential "Brute Force" attacks.
## **🛠️ The Engineering Process**

### **1. Signal Development (SPL)**
I developed a search query using **Splunk Processing Language (SPL)** to identify high-frequency authentication failures.
- **Query:** `index=linux_logs "Failed password" | stats count by user, src_ip | where count >= 3`
- **Technical Logic:** This search aggregates unstructured "Failed password" logs into structured counts, filtering for events where a single source attempts more than three failed logins within a specific window.
### **2. Orchestrating the "Live Fire" Test**
To validate the detection, I simulated a local Brute Force attack on the Ubuntu host:
- **Simulation:** `for i in {1..5}; do ssh localhost; done`
- **Result:** Verified the **Telemetry Pipeline** was healthy as the Splunk index updated in real-time, showing an event count jump from **17 to 25**.
### **3. Alert Configuration & Optimization**

To ensure the SOC is notified of this activity, I configured a **Scheduled Alert**:
- **Scheduling:** Implemented a **Cron Schedule** (`*/5 * * * *`) to run the detection engine every five minutes.
- **Time Window:** Configured a **15-minute look-back window** to ensure sufficient data overlap and capture all relevant events.
- **Actions:** Set the alert to trigger a **High Severity** event in the SIEM dashboard upon discovery.
## **🔍 Advanced Troubleshooting: The "Job Management" Audit**

During the validation phase, I encountered a scenario where search results were present, but UI notifications were delayed. I performed a deep-dive audit of the Splunk backend:
- **Diagnostic:** Navigated to the **Job Management** console to verify execution.
- **Finding:** Confirmed that the alert "Jobs" were executing successfully on the Cron schedule and returning the correct data hits.
- **Analyst Insight:** This troubleshooting step allowed me to verify that the **detection logic** was functional even when the **presentation layer** required adjustment—a crucial distinction for a SIEM Administrator.
## **📸 Example Visuals**
<p align="center">
  <img src="images/Linux%20Alert.png" alt="Windows Dashboard" width="500">
</p>

_The Linux alert in Alerts Tab._

<p align="center">
  <img src="images/Alert%20Event%20Output.png" alt="Windows Dashboard" width="500">
</p>

_Brute force Attempt Search with Results._

<p align="center">
  <img src="images/Alert%20Response%20Output.png" alt="Windows Dashboard" width="500">
</p>

_Brute force Alert Events._

---
# **Phase 5: Security Automation (Python Layer)**
**Focus:** _Scripting for post-incident response and automated compliance auditing._

---
## **🎯 Objective**
To reduce manual effort in the SOC by writing a Python script that audits the "Attack Surface" of the environment.
## **💻 Development & Implementation**

### **1. The "Port Watcher" Script**
I authored `port_scanner.py` using Python’s native `socket` library. The script was designed to perform a targeted scan of the Ubuntu endpoint to verify that critical service ports (SSH/Splunk) were in the expected state.
### **2. Troubleshooting the Environment**
During execution, I managed several "Real World" technical hurdles:
- **Pathing & Execution Aliases:** Resolved issues where Python wasn't recognized by the Windows shell by managing app execution aliases and installing a verified Python 3.13 environment.
- **Socket Error Handling:** Diagnosed and fixed a `socket.gaierror (Errno 11001)` by refining the IP address string and ensuring correct data types were passed to the `connect_ex` function.
## **🛡️ Post-Incident Analysis**
When the script ran, it correctly identified that **Port 22 (SSH)** was closed.
- **Analyst Insight:** Instead of seeing a "Closed" port as a failure, I documented it as a **successful audit**. It proved the script was accurately reflecting the state of the machine after a major system update, highlighting a need for "Service Health Monitoring" in the SOC.
## **📸 Example Visuals**

<p align="center">
  <img src="images/Python%20Port%20Scanner%20Example.png" alt="Windows Dashboard" width="500">
</p>

_Python Port Scanner Script in Use._

---
