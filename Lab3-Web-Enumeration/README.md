# SOC Lab 3 – Web Enumeration Detection

## Scenario
You are a SOC Analyst investigating web server logs to identify suspicious activity and determine if a security incident has occurred.

---

## Investigation Steps
```bash
tail access.log
grep "404" access.log
grep "403" access.log
awk '{print $1}' access.log | sort | uniq -c | sort -nr


Title: SOC Lab Session 3

Summary: An external IP address (10.10.14.8) was observed performing automated web enumeration against the target system. The activity involved probing multiple common administrative and sensitive endpoints in an attempt to identify exposed services or files

Suspicious IP:  10.10.14.8

Evidence: 
- Multiple HTTP requests within seconds, indicating automated behavior
- Requests originated from `curl`, suggesting command-line tooling
- Targeted sensitive endpoints including:
    - /admin
    - /login
    - /.env
    - /phpmyadmin
    - /wp-admin
    - /server-status
- HTTP response codes observed:
    - 404 (Not Found)
    - 403 (Forbidden)

Using multple URL expresessions to gain entry.

Analysis: The observed behavior is consistent with automated reconnaissance, specifically web directory enumeration. The attacker is attempting to identify accessible administrative interfaces or sensitive configuration files. The use of known high-value paths and rapid request frequency indicates malicious intent rather than legitimate user activity.

Severity: Medium

Recommended Actions: 
- Block IP address at firewall
- Monitor for repeated attempts from similar IP ranges
- Implement Web Application Firewall (WAF) rules to detect and block web enumeration attempts
- Review server configuration for exposed/misconfigured endpoints

# Key Findings
- Suspicious IP identified: 10.10.14.8
- Multiple requests to sensitive endpoints
- Evidence of automated behavior using curl


## Skills Demonstrated
- Log analysis (Apache access logs)
- Threat detection (web enumeration)
- Indicator identification (IP, endpoints, status codes)
- Incident analysis and reporting
- Defensive security recommendations



