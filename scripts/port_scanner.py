import socket
from datetime import datetime

# --- CONFIGURATION ---
# Replace this with your Ubuntu Laptop's IP address
TARGET_IP = "192.168.x.x" 
# The "Baseline" ports we expect to be open
BASELINE_PORTS = {22: "SSH", 8089: "Splunk Management", 9997: "Splunk Data"}

def scan_network():
    print(f"--- SOC Automation: Scanning {TARGET_IP} ---")
    print(f"Scan started at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
    
    for port, service in BASELINE_PORTS.items():
        # Create a connection attempt
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1) # Wait 1 second for a response
        
        result = s.connect_ex((TARGET_IP, port))
        
        if result == 0:
            print(f"[OK] Port {port} ({service}) is OPEN.")
        else:
            print(f"[ALERT] Port {port} ({service}) is CLOSED or UNREACHABLE!")
        
        s.close()
    print("\n--- Scan Complete ---")

if __name__ == "__main__":
    scan_network()