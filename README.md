# 🛡️ SOC Home Lab — Network Visibility & Automation

**Goal:** Tie network activity, endpoint logs, and basic automation into a single, understandable SOC workflow.

---

## 🧭 Project Phases

This lab is structured into progressive phases to mirror how a SOC environment is built and reasoned about:

- **Phase 0:** Assumed security baseline (not the focus)
- **Phase 1:** Network mapping and baseline creation
- **Phase 2:** Log collection and centralization using a SIEM (Splunk)
- **Phase 3:** Detection, correlation, and dashboarding
- **Phase 4:** Network change awareness and validation
- **Phase 5:** Minimal automation using Python
- **Phase 6:** SOC analyst-style reporting and conclusions

---

## 🔍 Guiding Questions

The lab is built around key questions a SOC analyst would ask:

- If something changes on the network, would I notice?
- Can raw logs be turned into actionable security signals?
- If an employer skimmed this in 60 seconds, would they understand my thinking?

---

## 🛠️ Tools Used

- **Splunk Enterprise & Universal Forwarder**
- **Windows & Linux Event Logs**
- **Python (for minimal automation)**
- Network scanning tools (e.g., Nmap)
- Virtualized environments (VMware, VirtualBox, or similar)

---

## 📄 Notes & Detailed Lab Documentation

For full step-by-step details, task checklists, screenshots, reflections, and experiment results, see:

- [`Home SOC & SIEM Guide.md`](Home%20SOC%20%26%20SIEM%20Guide.md)

This is where all hands-on work, troubleshooting, and experiments are documented in detail.

---

## 📸 Example Visuals

<p align="center">
  <img src="images/Screenshot%20Two.png" alt="SOC Dashboard Example" width="500">
</p>

*Example packet capture used during traffic analysis.*

*Example Splunk dashboard from the lab.*

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

---

## Key Takeaways
- Network and firewall issues are more common than Splunk misconfiguration
- TCP testing is more reliable than ICMP for diagnosing forwarding problems
- Placeholder syntax in documentation must never be copied literally
- Process IDs change frequently — always verify active ownership
- Incremental testing prevents misdiagnosis
- Persistent documentation enables systematic problem isolation

---

This project reinforced real-world SOC troubleshooting patterns: ambiguous failures, layered blockers, and the importance of methodical validation over assumptions.



📝 *This lab evolves as I build new capabilities, refine processes, and deepen my SOC knowledge.*


