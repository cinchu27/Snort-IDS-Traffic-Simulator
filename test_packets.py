#!/usr/bin/env python3
"""
test_packets.py

A script to generate network traffic for testing Snort IDS rules.
This script sends TCP SYN packets to simulate a port scan and
a single SYN packet to test a basic detection rule.
"""

from scapy.all import IP, TCP, send
import time
from typing import List

def generate_port_scan(target_ip: str, target_ports: List[int]) -> None:
    """
    Generates a series of TCP SYN packets to multiple ports on a target IP
    to simulate a port scan.

    Args:
        target_ip (str): The IP address of the target machine.
        target_ports (List[int]): A list of destination ports to scan.
    """
    print(f"[*] Initiating simulated port scan on {target_ip}...")
    
    # Loop through the provided list of ports and send a SYN packet to each.
    for port in target_ports:
        # IP layer: specifies source and destination IPs.
        # TCP layer: specifies source and destination ports, and the 'S' flag.
        packet = IP(dst=target_ip) / TCP(dport=port, flags="S")
        
        # Send the packet and wait for a response (verbose=0 suppresses output).
        send(packet, verbose=0)
        print(f"    - Sent SYN packet to port {port}")
        time.sleep(0.1) # Small delay to avoid overwhelming the network.

    print("[*] Port scan simulation complete.")

def generate_single_syn(target_ip: str, target_port: int) -> None:
    """
    Generates a single TCP SYN packet to test a basic detection rule.

    Args:
        target_ip (str): The IP address of the target machine.
        target_port (int): The destination port for the SYN packet.
    """
    print(f"[*] Sending a single SYN packet to {target_ip}:{target_port}...")
    
    packet = IP(dst=target_ip) / TCP(dport=target_port, flags="S")
    send(packet, verbose=0)
    
    print("[*] Single SYN packet sent.")

if __name__ == "__main__":
    # --- Configuration ---
    # IMPORTANT: Replace this with the actual IP of your Snort sensor/VM.
    TARGET_IP = "192.168.1.20" 
    
    # A list of ports to scan, designed to trigger the threshold in the Snort rule.
    # The rule alerts on 5+ connections to ports 1-1024 within 10 seconds.
    PORTS_TO_SCAN = [22, 23, 80, 135, 443]
    
    # --- Execution ---
    try:
        # 1. Trigger the basic "SYN Packet Detected" rule.
        generate_single_syn(TARGET_IP, 80)
        
        # 2. Trigger the "Potential Port Scan" rule.
        generate_port_scan(TARGET_IP, PORTS_TO_SCAN)

    except KeyboardInterrupt:
        print("\n[!] Script interrupted by user.")
    except Exception as e:
        print(f"[!] An error occurred: {e}")
