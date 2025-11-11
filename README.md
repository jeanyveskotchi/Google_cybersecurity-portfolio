# Cybersecurity Portfolio

A structured, GitHub-ready portfolio showcasing audit work, network analysis, incident response,
OS hardening, and automation completed while earning the Google Cybersecurity Professional Certificate.

> **Highlights**
> - Internal controls & compliance audit (PCI DSS, GDPR, SOC)
> - DNS/ICMP troubleshooting & network-layer analysis
> - SYN flood analysis with remediation (SYN cookies)
> - OS hardening & web malware investigation
> - DDoS response using the NIST CSF (Identify → Protect → Detect → Respond → Recover)
> - Removable media (USB) risk analysis
> - Python automation: maintain allow-list from a remove-list

## Repo Structure

```
cybersecurity-portfolio/
├─ 01-botium-audit/
├─ 02-network-layer/
├─ 03-network-attacks/
├─ 04-os-hardening/
├─ 05-nist-csf-response/
├─ 06-usb-vuln-analysis/
├─ 07-incident-journal/
├─ 08-python-allowlist/
├─ LICENSE
├─ README.md
└─ .gitignore
```

## How to Use

- Browse the folders for scoped READMEs describing each artifact.
- Run the Python automation example in `08-python-allowlist/`:

```bash
cd 08-python-allowlist
python update_allow_list.py
```

## Quick Start: Publish to GitHub

```bash
# rename the folder if you want
cd cybersecurity-portfolio
git init
git add .
git commit -m "feat: import cybersecurity portfolio"
git branch -M main
git remote add origin https://github.com/<YOUR-USER>/cybersecurity-portfolio.git
git push -u origin main
```

## Contact

- **Name:** Jean‑Yves Kotchi
- **Focus:** Cybersecurity, SOC analysis, network defense, automation
