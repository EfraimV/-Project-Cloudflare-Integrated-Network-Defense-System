import requests

def block_ip_cf(ip):
    """Add malicious IP to Cloudflare firewall"""
    headers = {
        "Authorization": "Bearer YOUR_API_TOKEN",
        "Content-Type": "application/json"
    }
    payload = {
        "mode": "block",
        "configuration": {"target": "ip", "value": ip},
        "notes": "Blocked via automated NIDS"
    }
    response = requests.post(
        "https://api.cloudflare.com/client/v4/zones/YOUR_ZONE_ID/firewall/access_rules/rules",
        headers=headers,
        json=payload
    )
    return response.json()
