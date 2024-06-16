#!/usr/bin/env python3

import psutil, shutil

import emails


def check_cpu_usage(delay):
    """Check if CPU usage is over 80%."""
    cpu_usage = psutil.cpu_percent(delay)
    return cpu_usage > 80

def check_disk_usage():
    """Check if available disk space is less than 20%"""
    disk_usage = shutil.disk_usage("/")
    threshold = 0.8 * disk_usage.total
    return disk_usage.used > threshold

def check_memory():
    """Check if available memory is less than 100MB."""
    mem = psutil.virtual_memory()
    threshold = 100 * 1024 * 1024  # 100MB
    return mem.available < threshold

def check_hostname():
    """Check if localhost cannot be resolved to 127.0.0.1."""
    nic = psutil.net_if_addrs()
    return nic.get('lo')[0].address != '127.0.0.1'

def main():
    # Info
    delay = 60

    From = "automation@example.com"
    To = "student@example.com"
    Body = "Please check your system and resolve the issue as soon as possible."
    
    issues = []
    if check_cpu_usage(delay):
        issues.append("Error - CPU usage is over 80%")
    if check_disk_usage():
        issues.append("Error - Available disk space is less than 20%")
    if check_memory():
        issues.append("Error - Available memory is less than 100MB")
    if check_hostname():
        issues.append("Error - localhost cannot be resolved to 127.0.0.1")
    for Subject in issues:
        message = emails.generate_email(From, To, Subject, Body)
        emails.send_email(message)


if __name__ == "__main__":
    main()