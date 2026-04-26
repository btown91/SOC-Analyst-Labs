# Pattern Detection 
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

Steps Performed
---------------

1. Created the log file

Command:
nano lab2_access.log

Purpose:
Created a sample log file to simulate web server traffic for analysis.


2. Viewed the log file

Command:
cat lab2_access.log

Purpose:
Reviewed all entries to understand the structure and data before filtering.


3. Counted IP activity

Command:
awk '{print $1}' lab2_access.log | sort | uniq -c | sort -nr

Purpose:
Extracted IP addresses, counted occurrences, and identified the most active IPs.


4. Identified failed login attempts

Command:
grep "401" lab2_access.log

Purpose:
Filtered for HTTP 401 responses to detect repeated login failures.


5. Identified scanning behavior

Command:
grep "404" lab2_access.log

Purpose:
Filtered for HTTP 404 responses to detect requests to non-existent pages.


6. Investigated specific IPs

Commands:
grep "192.168.1.50" lab2_access.log
grep "192.168.1.77" lab2_access.log

Purpose:
Isolated activity from each suspicious IP to compare behavior and determine intent.




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
