import requests
import os
import sys
import subprocess
import uuid

# === CONFIGURATION ===
GITHUB_RAW_URL = "https://raw.githubusercontent.com/BEWAFA548/bewafa/main/allowed_users.txt"
USER_ID_FILE = "/data/data/com.termux/files/home/.device_id"

def get_user_id():
    """Return a unique identifier for the current user/device."""
    if os.path.exists(USER_ID_FILE):
        with open(USER_ID_FILE, 'r') as f:
            return f.read().strip()
    else:
        # Try to get Android ID (works in Termux with proper permissions)
        try:
            android_id = subprocess.check_output(
                ['settings', 'get', 'secure', 'android_id'],
                text=True
            ).strip()
            if android_id and android_id != "null":
                # Save it for future use
                with open(USER_ID_FILE, 'w') as f:
                    f.write(android_id)
                return android_id
        except:
            pass
        
        # Fallback: generate a random UUID
        new_id = str(uuid.uuid4())
        with open(USER_ID_FILE, 'w') as f:
            f.write(new_id)
        return new_id

def is_user_approved(user_id):
    """Download the allowed IDs list from GitHub and check membership."""
    try:
        response = requests.get(GITHUB_RAW_URL, timeout=10)
        response.raise_for_status()
        allowed_ids = set(line.strip() for line in response.text.splitlines() if line.strip())
        
        if not allowed_ids:
            print("[!] Allowed users list is empty. Access denied for everyone.")
            return False
            
        return user_id in allowed_ids
    except requests.RequestException as e:
        print(f"[!] Failed to fetch approval list: {e}")
        return False

def main():
    user_id = get_user_id()
    print(f"User ID: {user_id}")
    
    if is_user_approved(user_id):
        print("[✓] License valid – starting tool...")
        # === Yahan apna original tool ka code daalein ===
        # Jaise: import kingprince; kingprince.BNG_71_()
        # Ya fir apna khud ka functionality
    else:
        print("[✗] Unauthorized user. Access denied.")
        sys.exit(1)

if __name__ == "__main__":
    main()
