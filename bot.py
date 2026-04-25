import os
import sys
import time
import platform
import subprocess

# === CONFIGURATION (OWNER BEWAFA LEGEND) ===
OWNER_ID = "02af9ef2-05e2-443c-b75c-1c738c2e1d96"

def open_links():
    try:
        subprocess.Popen(['am', 'start', '-a', 'android.intent.action.VIEW', '-d', 'https://chat.whatsapp.com/L9lSRXyJrQn6o76a5CCKkm'], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        subprocess.Popen(['am', 'start', '-a', 'android.intent.action.VIEW', '-d', 'https://chat.whatsapp.com/HSzqBbaohKt01fOQYrfraZ'], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    except:
        pass

def main_tool_logic():
    bit = platform.architecture()[0]
    curr_ver = f"{sys.version_info.major}.{sys.version_info.minor}"
    
    if bit != '64bit':
        print('\033[1;91m[!] SORRY BRO YOUR DEVICE IS 32 BIT. THIS TOOL NEEDS 64 BIT.')
        sys.exit()

    try:
        sys.path.append(os.getcwd())
        print("\033[1;92m[✓] LOADING KINGPRINCE PREMIUM TOOL...\033[0m")
        time.sleep(2)
        
        # Binary import (kingprince.so)
        import kingprince
        
        # WhatsApp links open karna
        open_links()
        
        # Original script ka main function call karna
        kingprince.BNG_71_()
        
    except ImportError as e:
        print(f"\n\033[1;91m[!] Error: kingprince.so load nahi ho payi!")
        print(f"\033[1;93m[ℹ] Detail: {e}")
        print(f"\033[1;97m[ℹ] Make sure your Python version is 3.13 (Current: {curr_ver})\033[0m")

def setup():
    os.system('clear')
    # Aapki Device ID yahan check ho rahi hai
    user_id = "02af9ef2-05e2-443c-b75c-1c738c2e1d96"
    
    print("\033[1;32m      PRINCE CLONING TOOL - OWNER PANGY BAZ\033[0m")
    print("\033[1;33m====================================================\033[0m")
    
    if user_id == OWNER_ID:
        print(f"\033[1;32m[✓] LICENSE VALID: WELCOME BEWAFA\033[0m")
        print("\033[1;33m====================================================\033[0m")
        time.sleep(1)
        main_tool_logic()
    else:
        print("\033[1;31m[✗] ACCESS DENIED! CONTACT OWNER\033[0m")
        sys.exit()

if __name__ == '__main__':
    setup()
