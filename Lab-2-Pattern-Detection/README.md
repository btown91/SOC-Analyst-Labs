SOC Lab 2 — Pattern Detection (Easy Mode)

Objective
---------
Analyze web server logs to identify suspicious behavior such as:
- Brute force login attempts
- Reconnaissance (scanning)
- Automated activity


Log Overview
------------
The log file contains:
- IP Address
- Timestamp
- Request Type (GET / POST)
- Status Codes:
    200 → Success
    401 → Unauthorized (login failure)
    404 → Page not found


Analysis Performed
------------------

1. Most Active IPs
------------------
192.168.1.50 → 4 requests
192.168.1.77 → 4 requests

Both IPs show the highest activity in the log.


2. Brute Force Detection
-----------------------
IP Address: 192.168.1.50

Behavior:
- Repeated POST requests to /login
- Status Code: 401 (Unauthorized)

This indicates repeated failed login attempts.

Total Failed Attempts: 4

Conclusion:
This is consistent with a brute force attack.


3. Reconnaissance / Scanning Detection
-------------------------------------
IP Address: 192.168.1.77

Behavior:
- Multiple GET requests
- All responses return 404 (Not Found)

Pages accessed:
- /admin
- /admin/login
- /admin123
- /secret

Conclusion:
This indicates directory enumeration or scanning for hidden endpoints.


4. Behavior Comparison
---------------------
192.168.1.77:
- GET requests
- 404 responses
- Testing multiple endpoints
→ Reconnaissance activity

192.168.1.50:
- POST requests
- 401 responses
- Repeated login attempts
→ Brute force attack


5. Timeline of Activity
----------------------
Time Range:
13:55 → 13:56

Observations:
- Requests occur within seconds
- Very consistent timing between attempts

Conclusion:
Activity is likely automated.


Final Assessment
----------------
Two suspicious IP addresses were identified:

192.168.1.77:
- Performing reconnaissance
- Attempting to discover valid pages

192.168.1.50:
- Performing brute force login attempts
- Attempting unauthorized access

Both IPs should be flagged as malicious:
- One represents the reconnaissance phase
- One represents the attack phase


Key Takeaways
-------------
- 401 errors indicate failed login attempts
- 404 errors indicate probing or scanning
- Repeated activity from a single IP is suspicious
- Fast, consistent timing suggests automation
- Attacks often occur in phases (recon → attack)


End of Report
