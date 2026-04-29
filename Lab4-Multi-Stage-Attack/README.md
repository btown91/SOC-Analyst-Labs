SOC Lab 4 — Multi-Stage Attack Detection
🧠 Objective

Analyze web server logs to identify a multi-stage attack, including reconnaissance, brute force attempts, successful compromise, and post-authentication activity.

Title: SOC Lab Session 5

Summary: 
An external IP address (192.168.1.50) was observed performing an automated brute force attack against the login endpoint of the target system. The activity included multiple failed login attempts followed by a successful authentication. After gaining access, the attacker navigated to sensitive areas of the application, including administrative and configuration endpoints.

Another external IP address (192.168.1.77) was observed performing web reconnaissance by probing multiple common and hidden endpoints. These attempts resulted in repeated 404 responses, indicating unsuccessful enumeration of available resources.

Suspicious IP:  
192.168.1.50, 192.168.1.77

Evidence: 
- Multiple HTTP requests within seconds from 192.168.1.50, indicating automated behavior

- Repeated failed login attempts from 192.168.1.50:
    - POST /login → 401 (Unauthorized)

- Successful login observed from 192.168.1.50:
    - POST /login → 200 (Success)

- Access to sensitive endpoints from 192.168.1.50:
    - /dashboard
    - /admin/panel
    - /config

- Reconnaissance activity from separate IP 192.168.1.77:
    - Multiple requests to non-existent endpoints:
        - /admin
        - /admin/login
        - /secret
        - /hidden
    - All resulting in 404 (Not Found)

Using multiple URL expressions to attempt access to sensitive resources.

Analysis: 
The observed behavior is consistent with a multi-stage attack. The attacker (192.168.1.50) initially performed a brute force attack against the login page, as indicated by repeated 401 responses. The attacker was eventually successful in authenticating, as shown by a 200 response on the login endpoint.

Following successful authentication, the attacker accessed sensitive areas of the application, including the dashboard, admin panel, and configuration pages. This indicates post-authentication activity and potential system compromise.

A second IP address (192.168.1.77) was observed performing reconnaissance by attempting to locate hidden or administrative endpoints. The repeated 404 responses indicate that this attacker was unsuccessful in discovering valid resources.

Severity: High



Recommended Actions: 
- Block IP address 192.168.1.50 at the firewall
- Monitor and consider blocking IP address 192.168.1.77
- Implement account lockout policies after multiple failed login attempts
- Enforce strong password policies
- Deploy a Web Application Firewall (WAF) to detect and block reconnaissance activity
- Monitor access to sensitive endpoints such as /admin and /config
- Review system logs and configurations for any unauthorized changes



Timeline:

1. 192.168.1.10 accesses /index.html (normal activity)

2. 192.168.1.50 accesses /login page

3. 192.168.1.50 performs multiple failed login attempts:
    - POST /login → 401 (Unauthorized)

4. 192.168.1.50 successfully logs in:
    - POST /login → 200 (Success)

5. 192.168.1.50 accesses authenticated user area:
    - GET /dashboard → 200

6. 192.168.1.77 begins reconnaissance activity:
    - Attempts access to multiple endpoints:
        - /admin
        - /admin/login
        - /secret
        - /hidden
    - All requests return 404 (Not Found)

7. 192.168.1.50 accesses sensitive administrative endpoints:
    - GET /admin/panel → 200
    - GET /config → 200

8. 192.168.1.50 logs out:
    - GET /logout → 200
