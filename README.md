# Automated Server Log Anomaly Scanner & Threat Detection

A lightweight Python security scanner that analyzes server access logs line-by-line using regular expressions to detect OWASP Top 10 web application attacks and automate firewall remediation.

## Features
- **Multi-Vector Detection Engine:**
  - **SQL Injection (SQLi):** `UNION SELECT`, `' OR '1'='1`, `OR 1=1`, `--`.
  - **Cross-Site Scripting (XSS):** `<script>`, `onerror=`, `javascript:`.
  - **Path Traversal / Local File Inclusion (LFI):** `../../`, `/etc/passwd`.
  - **Malicious Vulnerability Scanners:** `sqlmap`, `nikto`.
  - **Brute Force Detection:** Aggregates repeated `401 Unauthorized` status codes per IP with threshold alerting.
- **Severity Scoring:** Classifies attacks as `CRITICAL`, `HIGH`, or `MEDIUM`.
- **SIEM Export:** Dumps structured incidents into `incident_report.json` for SOC ingestion.
- **Automated Remediation:** Generates `block_attackers.sh` with `iptables` drop rules to instantly mitigate threats.

## Quickstart

### Run the Security Scanner
```bash
python scanner.py
```

### Inspect Generated Outputs
1. **SIEM JSON Log:**
   ```bash
   cat incident_report.json
   ```
2. **Automated Firewall Remediation Script:**
   ```bash
   cat block_attackers.sh
   ```

## Demo Video
- [YouTube Demo Video](https://youtu.be/MFEk9VR_X4M)

## Verification Code
`WTC-7JV6NBLA`
