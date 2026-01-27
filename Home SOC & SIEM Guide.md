# 🧠 Home SOC Lab — Network Visibility & Automation Layer

> **Goal:** Tie network activity, endpoint logs, and basic automation into a single, understandable SOC workflow.

---

### Phase 0: Assumed Baseline (Guaranteed)

✅ Secure VPN usage  
✅ Password manager + MFA  
✅ Virtualization fundamentals  
✅ Backup awareness  
✅ Security-first mindset  

> *This phase is assumed and not the focus of the project.*

---

### Phase 1: Network Mapping & Baseline

- [x] Create a **home network inventory**
- Device name
- IP address
- OS
- Role (workstation, VM, router, etc.)

- [x]  Perform an **initial Nmap scan**  
- Identify open ports and services
- Document findings as a baseline snapshot

- [x]  Save Nmap output for comparison  
- Purpose: detect future changes, not exploit systems

**Key Question:**  
> *If something changes on my network, would I notice?*

---

### Phase 2: Log Collection & Centralization (SIEM Introduction)

- [x]  Enable **Windows Event Logging**
- Authentication events (success/failure)
- Account activity
- System changes

- [x]  Enable **Linux authentication logs**
- SSH login attempts
- Privilege escalation events (`sudo`, `su`)

- [x]  Install and configure **Splunk Enterprise (SIEM)**
- Configure log inputs
- Verify ingestion from multiple systems
- Use consistent indexing and timestamps

- [x]  Install **Splunk Universal Forwarder**
- Forward Windows logs
- Forward Linux authentication logs

- [x]  Validate data in **Splunk Search & Reporting**
- Confirm logs are searchable
- Identify baseline event volume

**Key Question:**
> _Can I see important activity from multiple systems in one place using Splunk?_hase 2: Log Collection & Centralization

---

### Phase 3: Basic Detection & Correlation (Splunk Analysis)

- [x]  Identify key security-relevant events **in Splunk**
- Failed authentication attempts
- Successful logins
- Service restarts
- Network-related events

- [x]  Build a **basic Splunk dashboard**
- Authentication activity over time
- System events by host
- Login failures by source

- [ ]  Perform **manual correlation in Splunk**
- Network scan activity vs authentication attempts
- Time-based event clustering
- Cross-host behavior comparison

- [ ]  Apply basic filtering and search refinement
- Narrow searches by host, user, or time window
- Reduce noise to highlight signal

**Key Question:**
> _Can I turn raw logs in Splunk into meaningful security signals?_

---

### Phase 4: Network Awareness (Active Observation)

- [ ]  Run **periodic Nmap scans**
- Compare results to baseline
- Identify new or removed open ports

- [ ]  Document changes
- Expected vs unexpected
- Risk reasoning (not severity guessing)

- [ ]  Verify findings using logs
- Does network activity align with endpoint behavior?

**Key Question:**  
> *Do network changes match what my logs are telling me?*

---

### Phase 5: Automation (Python – Minimal & Intentional)

- [ ]  Write a **basic Python script** that:
- Parses Nmap output **or**
- Compares current scan to baseline **or**
- Flags new open ports or devices

- [ ]  Script output should be:
- Human-readable
- Short
- Explainable

- [ ]  Document:
- What problem the script solves
- Why automation helps SOC workflows

**Key Question:**  
> *Can I reduce repetitive analysis with simple automation?*

---

### Phase 6: SOC Analyst Perspective

- [ ]  Write a short **SOC-style summary**
- What data is being collected
- What is monitored
- What would trigger investigation

- [ ]  Include:
- One dashboard screenshot
- One example alert or finding
- One automation output

- [ ]  Keep documentation concise and skimmable

**Key Question:**  
> *If an employer skimmed this in 60 seconds, would they understand my thinking?*

- - -
# 📝 Here are some videos for projects!
### Build Your Own Cybersecurity Lab at Home (For FREE)
https://www.youtube.com/watch?v=izmCJlJEvQw

### Lets BUILD a FREE Cybersecurity SIEM Lab in UNDER 15 minutes | SOC ANALYST
https://www.youtube.com/watch?v=QT81wcuoRFY

### Splunk Tutorial for Beginners (Cyber Security Tools)
https://www.youtube.com/watch?v=3CiRs6WaWaU

- - -
## Project notes! :

## 📊 Nmap: Learning Recap (Project Context)
#### **1. Tool Familiarization & Objective**

To establish a baseline for the SOC Home Lab, I utilized **Nmap (via the Zenmap GUI)** to perform network discovery. The primary objective was to map the local network topology and identify active services that require monitoring within the SIEM (Splunk).
- **Learning Resource:** [Zenmap Lab Tutorial - Nmap/Zenmap Basics](https://www.youtube.com/watch?v=ayx8luaHk2c)
- **Methodology:** Initial testing was conducted against the `scanme.nmap.org` sandbox to verify Nmap output formats and service detection capabilities without exposing local infrastructure during the learning phase.
#### **2. Service Enumeration & Security Observations**

During testing, I observed a significant delta in open ports between the tutorial environment and live targets.
- **Discovery:** Identified nearly 1,000 scanned ports on the test target, with a high density of "Open" vs. "Closed/Filtered" states.
- **SOC Insight:** A high number of open ports increases the **Attack Surface**. In a production environment, this would trigger a "Hardening" task to close any non-essential services.

#### **3. Topology Mapping & Subnet Discovery**

I successfully executed a subnet scan (e.g., `192.168.1.0/24`) to generate a visual **Network Topology Map**.
- **Process:** Used CIDR notation to define the scan range, identifying all interconnected nodes (VMs, host machines, and gateway).
- **Data Sanitization (OPSEC):** For documentation purposes, all screenshots of the network topology have been sanitized. Public IP addresses and sensitive internal MAC addresses were redacted to maintain **Operations Security (OPSEC)** while still demonstrating network architectural knowledge.

## 📸 Example Visuals
<p align="center">
  <img src="images/Nmap%20Output%20Example%201.png" alt="Nmap Output Example 1" width="500"> 
</p>

<p align="center">
  <img src="images/Nmap%20Output%20Example%202.png" alt="Nmap Output Example 1" width="500"> 
</p>

*Example of Nmap Output.*

<p align="center">
  <img src="images/Nmap%20Topology%20Example.png" alt="Nmap Output Example 1" width="500"> 
</p>

*Example of My Network Topology.*

## 📊 Splunk: Learning Recap (Project Context)

> **Purpose:** Summarize Splunk concepts used in this project without repeating foundational explanations elsewhere. Originally discussed in the (link to other page) lab. 
### 🔹 Why Splunk Was Used
Splunk was selected to:
- Centralize logs from multiple systems
- Search and filter security-relevant events efficiently
- Visualize activity in a SOC-style dashboard

The focus was on **analysis and visibility**, not enterprise-scale deployment.

### 🔹 Core Concepts Applied
**Indexes**
- Logs are organized by type/source for efficient searching
- Separating data improves clarity and performance
**Events**
- Individual log entries (e.g., login attempt, system event)
- Used as the atomic unit for investigation
**Search & Filtering**
- Searches were crafted to isolate:
  - Authentication activity
  - System changes
  - Network-related indicators
- Emphasis on narrowing noise into actionable signals
**Time-Based Analysis**
- Events analyzed across time windows
- Helped identify spikes, anomalies, and patterns

### 🔹 Dashboard Design Philosophy
Dashboards were built to:
- Answer specific security questions quickly
- Reduce manual searching during investigation
- Highlight abnormal behavior rather than raw log volume
Panels focus on:
- Authentication trends
- Event frequency over time
- Notable security events

### 🔹 Alerts & Detection Logic
Simple alert logic was implemented to:
- Flag repeated failed logins
- Surface unusual activity patterns
- Support analyst triage rather than automated response

Alerts were intentionally conservative to avoid noise.

The goal was to demonstrate **analyst thinking**, not mastery of every Splunk feature.

### Notes continued...
 
#### Initial Goal
The goal was to follow a guided video walkthrough to install Splunk Enterprise and begin collecting Windows security logs for basic monitoring and detection.

Before installation, I spent time understanding what Splunk is and how it functions:
- Splunk is a **SIEM (Security Information and Event Management)** platform
- It centralizes logs from one or more systems
- It runs primarily through a **web interface**, not as a traditional desktop application
- Data collection and processing are handled separately from visualization

This understanding helped frame later troubleshooting decisions.

#### Following the Video (Initial Attempt)
I followed a YouTube tutorial to:
- Install **Splunk Enterprise** on Windows
- Install the **Universal Forwarder** on the same system
- Begin collecting Windows Event Logs

During this step, I ran into an issue where:
- Navigating to **Settings → Data Inputs → Local Event Log Collection** returned a **404 error**
- This blocked progress relative to the video and initially suggested a broken install

#### Investigation & Hypotheses
Several possibilities were considered:
- Incorrect forwarder architecture (32-bit vs 64-bit)
- Management ports misconfigured during installation
- Forwarder web UI being disabled by default
- Required Windows add-ons missing

At this point, Splunk Enterprise itself was confirmed to be accessible at:
http://localhost:8000

### Corrections & Key Fixes
The following actions resolved the issue:

- Installed **Splunk Add-on for Microsoft Windows**
- Confirmed that **Universal Forwarder does not use the web UI** for input configuration
- Restarted the forwarder **using an Administrator terminal**
- Verified that Splunk Enterprise was listening for forwarded data

Important realization:
> The 404 error was expected behavior when using a Universal Forwarder and not an actual failure.

### Validation of Success
Data ingestion was confirmed using SPL searches:

(spl)
index=*

### Corrections & Key Fixes
The following actions resolved the issue:

- Installed **Splunk Add-on for Microsoft Windows**
- Confirmed that **Universal Forwarder does not use the web UI** for input configuration
- Restarted the forwarder **using an Administrator terminal**
- Verified that Splunk Enterprise was listening for forwarded data

Important realization:
> The 404 error was expected behavior when using a Universal Forwarder and not an actual failure.

### Validation of Success
Data ingestion was confirmed using SPL searches:

(spl)
index=*
→ Returned a large volume of events, confirming indexing was active.

(spl)
index=* host=Solace
→ Returned thousands of events, confirming forwarding worked.

(spl)
index=main sourcetype=WinEventLog:Security
→ Returned security-related Windows events, confirming correct log collection.

At this point, the pipeline from **Windows → Universal Forwarder → Splunk Enterprise → Search** was fully functional. 

With reliable log data now flowing into Splunk, the next phase of the project is to identify meaningful security signals and visualize them through targeted dashboards.

## Defining Protection Goals

At this stage of the project, the focus shifts from data ingestion to **defining what I am actually trying to protect**. Before expanding the lab further, I established a set of clear priorities that guide what events are monitored and how they are visualized.

These priorities act as a scope boundary for the project and help keep the dashboard purposeful rather than noisy.

---

### Protection Priorities

**Primary concerns**
- Unauthorized logins (local or remote)
- Account misuse (bursts of failed authentication attempts)
- Unexpected system or service changes
- Network-related activity that _could_ indicate probing or scanning

**Explicitly out of scope**
- Advanced malware detection
- EDR-level telemetry
- Nation-state threat modeling
- Full packet inspection within Splunk

The goal is **visibility**, not exhaustive detection.

## Dashboard Design and Rationale

With these priorities defined, the next objective was to build a Splunk dashboard that surfaces relevant activity in a way that is simple, readable, and actionable.

Using guidance from ChatGPT, I designed a small set of focused panels that collectively provide situational awareness without overwhelming the viewer.

---
### Panel 1: Authentication Activity Over Time (Line Graph)

This panel visualizes authentication behavior over time, highlighting successful versus failed login attempts. It is primarily used to detect anomalies such as spikes in failures or unusual login patterns.

**Search used:**

`index=* sourcetype=WinEventLog:Security EventCode IN (4624, 4625) | eval Action=if(EventCode=4624,"Success","Failure") | timechart count by Action`

**Relevant Event Codes**
- `4624` — Successful login
- `4625` — Failed login

---

### Panel 2: Recent Security Events (Table)

This panel provides a human-readable view of recent security-relevant activity. Rather than aggregating data, it allows for quick inspection of individual events when investigating suspicious behavior.

**Search used:**
`index=* sourcetype=WinEventLog:Security | table _time host EventCode Account_Name Source_Network_Address | sort -_time`

- The table is limited to ~50 rows to balance visibility and readability.
- Fields are intentionally kept minimal to support fast triage.

---

### Panel 3: System Activity / Stability Events (Line Graph)

To avoid an authentication-only view, this panel tracks general system activity such as restarts and service-related events. It helps surface non-auth changes that may still be security-relevant.

**Search used:**
`index=* sourcetype=WinEventLog:System | timechart count`

This panel provides baseline awareness of system behavior over time.

---

## Overall Dashboard Observations

Building this dashboard highlighted how quickly complexity can grow in a centralized logging environment. Even with a single host, careful scoping and panel design are necessary to prevent information overload.

Below is a **sanitized example** of the completed dashboard (fields containing hostnames, usernames, timestamps, and network identifiers have been intentionally redacted):

<p align="center">
  <img src="images/Screenshot%20Two.png" alt="SOC Dashboard Example" width="500">
</p>

*Example packet capture used during traffic analysis.*
> _Fields containing hostnames, usernames, timestamps, and network identifiers have been intentionally redacted._


This dashboard centralizes Windows authentication and system events using Splunk Enterprise. It emphasizes rapid visibility into abnormal access patterns rather than deep forensic analysis.

### Key Takeaways and Future Improvements
- Improve dashboard readability and visual clarity
- Add basic alerting for abnormal authentication patterns
- Expand the lab by forwarding logs from an additional system
- Revisit this dashboard later with refined detection logic

---

## 📊 Splunk Universal Forwarder: Learning Recap (Project Context)

### Goal
Forward Linux authentication logs from an Ubuntu system into a central **Splunk Enterprise** instance running on a Windows 11 host, simulating a basic multi-host SOC logging environment.

---
## Initial Objective

After successfully ingesting **local Windows Event Logs** into Splunk Enterprise, the next objective was to:
- Expand visibility beyond a single endpoint
- Practice **centralized log aggregation**
- Introduce a **Splunk Universal Forwarder** to simulate realistic SOC data flow

Planned architecture:
- **Ubuntu Linux host → Windows Splunk Enterprise server**

---
## Installing the Universal Forwarder (Ubuntu)
- Downloaded the **Splunk Universal Forwarder for Linux (x64)** via terminal
- Installed under:
    ```
    /opt/splunkforwarder
    ```
- Accepted the Splunk license agreement
- Reached initial setup and credential configuration

### Setup Clarification

During installation, the setup process prompted for a username:
- Usernames containing spaces were rejected
- Learned this account is **local to the forwarder**, not tied to Splunk Enterprise credentials
- Re-ran setup using a valid username format

---
## First Forwarding Attempt (Failed)

Attempted to configure the Windows system as the receiving indexer:

```
sudo ./splunk add forward-server <WINDOWS_IP>:9997
```

### Result
- Command failed with a directory-related error

### Root Cause
- Command was executed from the wrong directory
- Learned that Splunk CLI commands must be run from:
    ```
    /opt/splunkforwarder/bin
    ```

---
## Directory Correction & Retest

After navigating to the correct directory, the command executed successfully — but log forwarding still failed.

At this point, attention shifted away from syntax and toward **network-level troubleshooting**.

---
## Network Connectivity Investigation

### Observations
- Ubuntu → Windows ping **failed**
- Windows → Ubuntu ping **succeeded**

### Interpretation
- Indicated **one-way network reachability**
- Suggested firewall, routing, or adapter-related issues rather than IP misconfiguration alone

---
## IP Address & Adapter Confusion

The Windows host had multiple active network adapters:
- VPN adapter
- Ethernet adapter
- Wi‑Fi adapter

### Key Findings

- VPN adapter IP was incorrectly used during initial setup
- Correct IP belonged to the **Wi‑Fi adapter**
- Both systems needed to be on the **same local network**

---
## Firewall & Port Review

Confirmed the following:
- VPN fully disabled
- Windows Firewall temporarily disabled during testing
- Splunk receiver port **9997** configured

Despite this, forwarding still failed — reinforcing that the issue was **network handling**, not Splunk configuration.

---
## Firewall Rule Breakthrough

Further testing revealed:
- Windows was blocking inbound TCP traffic on port **9997**
- ICMP (ping) behavior was misleading due to firewall rule differences

### Resolution
- Added an explicit **inbound Windows Firewall rule** allowing TCP traffic on port 9997

Immediately after:
- Ubuntu → Windows ping succeeded
- Network reachability confirmed

---
## Placeholder Syntax Error (Critical Discovery)
A subtle but impactful mistake was identified while reviewing earlier commands.

### Issue
Documentation examples used:

```
<WINDOWS_IP>
```

This placeholder was mistakenly entered **literally**.

### Incorrect
```
<192.168.x.x>
```

### Correct
```
192.168.x.x
```

Once corrected:
- Forward-server command succeeded instantly
- Connection established without further errors

---
## Successful Forwarder Configuration

Final commands executed on Ubuntu:

```
cd /opt/splunkforwarder/bin
sudo ./splunk add forward-server WINDOWS_IP:9997
sudo ./splunk enable boot-start
sudo ./splunk start
```

Log source added:

```
sudo ./splunk add monitor /var/log/auth.log
```

---
## Initial Validation (Splunk Enterprise)

Search executed on Windows Splunk server:

```
index=* host=<ubuntu_hostname>
```

### Result
- Linux authentication events successfully ingested
- Multi-host log collection confirmed

---
### Forwarding Validation Attempts
- Test events sent from Ubuntu
- Searches returned **no Linux events initially**
- Only Windows logs were visible

Conclusion: forwarder configuration existed, but delivery was inconsistent

---
## Forwarder Configuration Review

- Reviewed `outputs.conf` on Ubuntu
- Target IP and port 9997 confirmed
- Forwarder status showed:
    > configured but inactive forwards

Interpretation: target recognized, but connection not established

---
## Connectivity Testing
- Ping from Ubuntu to Windows initially failed
- Indicated a fundamental connectivity or firewall issue

---
## Receiver & Port Inspection
- Verified Splunk was listening on port 9997 using `netstat`
- External TCP tests failed despite listening port

Key insight:

> A listening port does not guarantee external reachability

---
## Firewall Isolation Testing
- Temporarily disabled Windows Firewall
- TCP connectivity tests immediately succeeded

Conclusion: Windows Firewall was the final blocking layer

---
## Permanent Firewall Resolution
- Created inbound and outbound TCP rules for port 9997
- Applied rules to all profiles (Domain, Private, Public)

Verification:

```
sudo splunk list forward-server
```

Result:

- Active forward connection confirmed

---
## End-to-End Log Verification

- Generated test event on Ubuntu:
    ```
    logger "SOC TEST EVENT SUCCESS"
    ```
- Event appeared in Splunk with correct:
    - Timestamp
    - Hostname
    - Message content

End-to-end pipeline confirmed:

**Ubuntu → Forwarder → Splunk Receiver → Search**

## 📸 Example Visuals

<p align="center">
  <img src="images/Screenshot%203.png" alt="SOC Forwarder Test Image One" width="500">
</p>

*Terminal from the Ubuntu Laptop.*

<p align="center">
  <img src="images/Screenshot%204.png" alt="SOC Forwarder Test Image Two" width="500">
</p>

*Splunk result on Windows Laptop.*

---

## Key Takeaways
- Network and firewall issues are more common than Splunk misconfiguration
- TCP testing is more reliable than ICMP for diagnosing forwarding problems
- Placeholder syntax in documentation must never be copied literally
- Process IDs change frequently — always verify active ownership
- Incremental testing prevents misdiagnosis
- Persistent documentation enables systematic problem isolation

---

## **SOC Lab Phase 2: Engineering the Telemetry Pipeline**

### **Summary of the Build & Troubleshooting Journey**

#### **1. The Connectivity Hurdle (Network Engineering)**

- **The Problem:** Initial communication between the Ubuntu Forwarder and the Windows Indexer failed. Pings were successful from Windows to Ubuntu, but blocked in reverse.
- **The Learning Process:** * Diagnosed the issue as a **Windows Firewall ICMP block** and a **Network Profile mismatch** (Public vs. Private).
    - **The Fix:** Manually configured inbound rules for **TCP 9997** and **ICMPv4**. Verified the fix by monitoring consistent ping "Echo Requests" on the Ubuntu terminal.

#### **2. Data Routing & Index Management**

- **The Problem:** Data was initially defaulting to the `main` index, creating a "noisy" environment where system logs and security logs were mixed.
    
- **The Learning Process:** * Discovered that Splunk monitors are persistent. Simply adding a new monitor wouldn't work because the file was already "locked" to the default index.
    - **The Fix:** Executed a "Remove and Replace" workflow. Used `splunk remove monitor` to clear the path, then re-mapped the source to a custom `linux_logs` index for better data segregation.

#### **3. Permission Blocks & Visibility**

- **The Problem:** The Universal Forwarder was connected, but reported 0 events from `/var/log/auth.log`.
- **The Learning Process:** * Identified a **Linux File Permission** conflict. The log file was restricted to root-only access (`600`), preventing the Splunk service from reading it.
    - **The Fix:** Adjusted permissions to `644` (Global Read), allowing the telemetry to flow while maintaining system stability.

#### **4. Overcoming Field Extraction Failures (Data Parsing)**

- **The Problem:** Standard Splunk searches for `user` and `command` returned no results in the dashboard panels, despite the raw data being present.
- **The Learning Process:** * Recognized that without specific Linux Add-ons, Splunk treats logs as "unstructured strings."
    - **The Fix:** Wrote **Custom Regular Expressions (Regex)** using the `rex` command to manually extract the `executing_user` and `cmd_run` fields. This ensured the dashboard could display meaningful charts regardless of the OS version.

## 📸 Example Visuals

<p align="center">
  <img src="images/Linux%20Dashboard.png" alt="Linux Dashboard Image" width="500">
</p>

_Dashboard for Authentication & Privilege Escalation Auditing._

---

### **Final Infrastructure State**

- **Host A (Windows):** Acting as the Central Indexer and SOC Dashboard.
- **Host B (Ubuntu):** Acting as the Target/Forwarder.
- **Security Capabilities:** Real-time visibility into **failed logins** (Brute Force detection) and **sudo execution** (Privilege Escalation monitoring).


---
This section is intentionally scoped to maintain clarity and prevent overextension while keeping the lab expandable for future learning.


