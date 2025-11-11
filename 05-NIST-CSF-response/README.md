# NIST CSF — DDoS (ICMP Flood) Response

**Summary:** Unconfigured firewall allowed ICMP flood → 2 hours outage. After-action implemented:
- ICMP rate-limits + source IP verification
- Network monitoring & IDS/IPS

## CSF Functions

**Identify:** Map affected services, document misconfig as risk, add to risk register.  
**Protect:** Firewall rules; disable non-critical services during events; config review & training.  
**Detect:** Netflow/baselines; IDS/IPS tuned for ICMP anomalies; centralized logs.  
**Respond:** Contain with ACLs; comms plan; postmortem + playbook updates.  
**Recover:** Restore services; tabletop exercises; periodic reviews & continuous improvement.
