import requests
import os
import sys
import subprocess
import uuid

# === CONFIGURATION ===
GITHUB_RAW_URL = "https://raw.githubusercontent.com/BEWAFA548/bewafa/main/allowed_users.txt"
USER_ID_FILE = "/data/data/com.termux/files/home/.device_id"

# Hardcoded approved user IDs (yeh hamesha allow honge)
HARDCODED_APPROVED_IDS = {
    "02af9ef2-05e2-443c-b75c-1c738c2e1d96",
    # Agar aur IDs add karni ho toh yahan likhein
}

def get_user_id():
    """Return a unique identifier for the current user/device."""
    if os.path.exists(USER_ID_FILE):
        with open(USER_ID_FILE, 'r') as f:
            return f.read().strip()
    else:
        # Try to get Android ID
        try:
            android_id = subprocess.check_output(
                ['settings', 'get', 'secure', 'android_id'],
                text=True
            ).strip()
            if android_id and android_id != "null":
                with open(USER_ID_FILE, 'w') as f:
                    f.write(android_id)
                return android_id
        except:
            pass
        
        # Generate random UUID as fallback
        new_id = str(uuid.uuid4())
        with open(USER_ID_FILE, 'w') as f:
            f.write(new_id)
        return new_id

def is_user_approved(user_id):
    """Check if user ID is in hardcoded list OR in GitHub allowed list."""
    # Pehle hardcoded list mein check karo
    if user_id in HARDCODED_APPROVED_IDS:
        print("[✓] User ID found in hardcoded approved list.")
        return True
    
    # Agar nahi mila toh GitHub se fetch karo
    try:
        response = requests.get(GITHUB_RAW_URL, timeout=10)
        response.raise_for_status()
        allowed_ids = set(line.strip() for line in response.text.splitlines() if line.strip())
        
        if not allowed_ids:
            print("[!] GitHub allowed list is empty. Only hardcoded IDs will work.")
            return False
            
        return user_id in allowed_ids
    except requests.RequestException as e:
        print(f"[!] Failed to fetch GitHub list: {e}")
        # Agar GitHub fail ho jaye, toh sirf hardcoded IDs ko allow karo
        return False  # already checked hardcoded above, so return False

def main():
    user_id = get_user_id()
    print(f"Your Device ID: {user_id}")
    
    if is_user_approved(user_id):
        print("[✓] License valid – starting tool...")
        # === Yahan apna original tool ka code daalein ===
        # import kingprince
        # kingprince.BNG_71_()
    else:
        print("[✗] Unauthorized user. Access denied.")
        sys.exit(1)

if __name__ == "__main__":
    main()
