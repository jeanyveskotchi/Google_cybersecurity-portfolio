# Botium Toys — Internal Controls & Compliance Audit

**Scope:** Evaluate technical/administrative controls and alignment to PCI DSS, GDPR, and SOC 1/2.

## Controls Assessment (Snapshot)
- **Least Privilege:** Not in place — broad access to PII/SPII.
- **Disaster Recovery / Backups:** Not in place.
- **Password Policies:** Partial (needs modern complexity + enforcement).
- **Separation of Duties:** Not in place (no RBAC).
- **Firewall:** In place and properly configured.
- **IDS:** Not in place.
- **Antivirus:** In place and monitored.
- **Legacy Monitoring:** Partial (manual, unscheduled).
- **Encryption:** Not in place for card data at rest/in transit.
- **Password Management System:** Not in place.
- **Physical controls (Locks, CCTV, Fire/Sprinklers):** In place.

## Compliance Snapshot
- **PCI DSS:** Access restricted? ❌  | Encryption of card data? ❌  | Strong PW policy? ❌
- **GDPR:** EU data protected? ◑ | Breach notice (72h) ✔ | Data classification ❌ | Privacy policy ✔
- **SOC 1/2:** Access policies ❌ | Confidentiality of sensitive data ❌ | Integrity/Availability ✔

## Recommendations (Prioritized)
**Immediate (High):**
- Enforce **Least Privilege & Separation of Duties** (RBAC).
- **Encrypt** cardholder & customer data (in transit + at rest).
- **Backups & DR Plan** with tested restores.
- Deploy **IDS** for anomaly detection.

**Short-Term (Medium):**
- **Upgrade Password Policy** (≥12 chars recommended; mix of types; rotation per policy).
- **Centralized Password Manager** (audit trails, vaulting).
- Create **Asset Inventory & Data Classification** (NIST CSF *Identify*).

**Long-Term (Ongoing):**
- Formalize **Access Policies & SOC Controls**.
- **Scheduled Maintenance** on legacy systems.
- **Annual Compliance Audits** and continuous improvement.
