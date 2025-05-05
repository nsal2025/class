from netmiko import ConnectHandler
from datetime import datetime

# Define your SSH username
username = "admin"  

# VLANs to create
vlans_to_create = [
    {"vlan_id": 110, "vlan_name": "New VLAN"},
]

# List of EXOS switches in Access Closet 1
devices = [
    {
        "device_type": "extreme_exos",
        "ip": "10.10.1.22",
        "name": "User_Network"
    },
    {
        "device_type": "extreme_exos",
        "ip": "10.10.1.24",
        "name": "Local_Switch"
    },
    {
        "device_type": "extreme_exos",
        "ip": "10.10.1.30",
        "name": "IT_Network"
    },
    {
        "device_type": "extreme_exos",
        "ip": "10.10.1.31",
        "name": "MGMT_Network"
    },
    {
        "device_type": "extreme_exos",
        "ip": "10.10.1.32",
        "name": "ACCT_Network"
    }
]

def create_vlans(device, username):
    try:
        print(f"Connecting to {device['name']} at {device['ip']}...")

        conn = ConnectHandler(
            device_type=device["device_type"],
            ip=device["ip"],
            username=username,
            use_keys=True,
            key_file="~/.ssh/RSA_Key"  
        )
     
        print(f"Creating VLANs on {device['name']}...")
        for vlan in vlans_to_create:
            vlan_cmd = f"create vlan {vlan['vlan_name']} tag {vlan['vlan_id']}"
            conn.send_config_set([vlan_cmd])
            print(f"✔ Issued: {vlan_cmd}")

        conn.disconnect()
        print("=" * 60 + "\n")

    except Exception as e:
        print(f"[ERROR] Could not connect to {device['name']} at {device['ip']}: {e}")

if __name__ == "__main__":
    print("EXOS VLAN Creation Script (SSH Key Auth Only)")
    print(f"Run Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")

    for device in devices:
        create_vlans(device, username)
