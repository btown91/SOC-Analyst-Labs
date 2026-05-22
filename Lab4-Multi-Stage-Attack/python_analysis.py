#!/usr/bin/env python3


# SOC Lab 4 - Multi-Stage Attack Detection


# File we are reading
log_file = "lab4_logs.txt"


# Dictionaries / lists to store findings
failed_logins = {}        # {IP: count}
successful_logins = []    # [IP, IP, ...]
recon_activity = {}       # {IP: [paths]}
sensitive_access = {}     # {IP: [paths]}


# Sensitive endpoints we care about
sensitive_paths = ["/dashboard", "/admin/panel", "/config"]


# Open the file
with open(log_file, "r") as file:

    # Go line by line
    for line in file:

        # Step 1: Split the line into "columns"
        parts = line.split()

        # Step 2: Extract data using index positions
        ip = parts[0]                         # IP address

        # These need .strip('"') because of quotes in the log
        method = parts[4].strip('"')          # "POST → POST
        path = parts[5].strip('"')            # /login" → /login

        status_code = parts[6]                # 200, 401, 404


        # -------------------------------
        # FAILED LOGIN DETECTION
        # -------------------------------
        if method == "POST" and path == "/login" and status_code == "401":

            # Count how many times each IP fails login
            failed_logins[ip] = failed_logins.get(ip, 0) + 1


        # -------------------------------
        # SUCCESSFUL LOGIN DETECTION
        # -------------------------------
        if method == "POST" and path == "/login" and status_code == "200":

            # Store IP that successfully logged in
            successful_logins.append(ip)


        # -------------------------------
        # RECON DETECTION (404 errors)
        # -------------------------------
        if status_code == "404":

            # Create list if IP not seen before
            if ip not in recon_activity:
                recon_activity[ip] = []

            # Store the path they tried
            recon_activity[ip].append(path)


        # -------------------------------
        # SENSITIVE ENDPOINT DETECTION
        # -------------------------------
        if path in sensitive_paths and status_code == "200":

            # Create list if IP not seen before
            if ip not in sensitive_access:
                sensitive_access[ip] = []

            # Store sensitive path accessed
            sensitive_access[ip].append(path)


# ---------------------------------------
# PRINT RESULTS
# ---------------------------------------

print("=== Failed Login Attempts ===")
for ip, count in failed_logins.items():
    print(f"{ip} had {count} failed login attempts")


print("\n=== Successful Logins ===")
for ip in successful_logins:
    print(f"{ip} successfully logged in")


print("\n=== Recon Activity ===")
for ip, paths in recon_activity.items():
    print(f"{ip} accessed invalid paths:")
    for path in paths:
        print(f"  - {path}")


print("\n=== Sensitive Endpoint Access ===")
for ip, paths in sensitive_access.items():
    print(f"{ip} accessed sensitive endpoints:")
    for path in paths:
        print(f"  - {path}")
