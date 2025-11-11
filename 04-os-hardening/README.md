# OS Hardening & Web Malware Investigation

**Threat:** Former employee brute-forced admin creds, injected JavaScript prompting an EXE download.
**Observations:** DNS resolves `yummyrecipesforme.com` → browser redirected to `greatrecipesforme.com`; port 80 used (HTTP).

## Root Causes
- Weak admin password (no MFA / lockouts).
- Plain **HTTP** allowed → easy manipulation/injection.
- Insufficient change control and file integrity monitoring.

## Remediation
- **MFA** + **account lockout** + **monitor login attempts**.
- Enforce **HTTPS** (HSTS; redirect HTTP→HTTPS).
- **WAF** and server-side **FIM** (e.g., AIDE, OSSEC; CMS integrity checks).
- Secrets rotation; audit admin accounts; SIEM detection for webdeface/redirects.

> Include sanitized PCAPs/screens or logs in this folder (optional).
