## 🧠 Home SOC Lab — Network Visibility & Automation Layer

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

- [ ] Create a **home network inventory**
- Device name
- IP address
- OS
- Role (workstation, VM, router, etc.)

- [ ]  Perform an **initial Nmap scan**  
- Identify open ports and services
- Document findings as a baseline snapshot

- [ ]  Save Nmap output for comparison  
- Purpose: detect future changes, not exploit systems

**Key Question:**  
> *If something changes on my network, would I notice?*

---

### Phase 2: Log Collection & Centralization (SIEM Introduction)

- [ ]  Enable **Windows Event Logging**
- Authentication events (success/failure)
- Account activity
- System changes

- [ ]  Enable **Linux authentication logs**
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


- [ ]  Enable **Windows Event Logging**
- Authentication events
- Account activity
- System changes

- [ ]  Enable **Linux authentication logs**
- SSH attempts
- Privilege escalation events

- [ ]  Forward logs to a **central log platform**
- Focus on consistency, not volume

**Key Question:**  
> *Can I see important activity from multiple systems in one place?*

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
## Future Work

This project is approaching a stable stopping point for its initial scope. The current focus is on finalizing the Splunk dashboard and documenting the lab in a way that clearly demonstrates intent, design decisions, and learned concepts.

Planned next steps include:
- **Log Forwarding from a Secondary Host**  
    Deploy a Splunk Universal Forwarder on an additional system to simulate multi-host monitoring. This will allow the dashboard to transition from a single-machine view to a more realistic SOC-style setup, while reinforcing how centralized logging scales in practice.
- **Refinement and Light Alerting**  
    Minor improvements to dashboard readability and the possible addition of basic alerts (e.g., authentication failure spikes) to move from passive monitoring toward actionable visibility.
- **Transition to Network-Focused Analysis (Nmap)**  
    Once the Splunk portion is finalized, focus will shift to learning and using **Nmap** to explore network discovery and scanning techniques. Findings from Nmap will later be correlated with log data concepts learned in this project.

This section is intentionally scoped to maintain clarity and prevent overextension while keeping the lab expandable for future learning.
