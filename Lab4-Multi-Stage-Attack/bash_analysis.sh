#!/bin/bash

echo "=== Failed Login Attempts ==="
grep 'POST /login" 401' lab4_logs.txt | awk '{print $1}' | sort | uniq -c

echo -e "\n=== Successful Logins ==="
grep 'POST /login" 200' lab4_logs.txt | awk '{print $1}'

echo -e "\n=== Recon Activity ==="
grep ' 404' lab4_logs.txt | awk '{print $1, $6}' | sed 's/"//g'

echo -e "\n=== Sensitive Endpoint Access ==="
grep -E '/dashboard|/admin/panel|/config' lab4_logs.txt | grep ' 200'
