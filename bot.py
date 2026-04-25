import os, sys, time

# === CONFIGURATION ===
OWNER_ID = "02af9ef2-05e2-443c-b75c-1c738c2e1d96"

def clear():
    os.system('clear')
    print("\033[1;32m      PRINCE CLONING TOOL - OWNER PANGY BAZ\033[0m")
    print("\033[1;33m====================================================\033[0m")

def cloning_menu():
    print("\033[1;36m[1] FILE CLONING (M1/M2/M3)")
    print("[2] PUBLIC ID CLONING")
    print("[3] CREATE FILE / DUMP")
    print("[0] EXIT TOOL\033[0m")
    print("\033[1;33m====================================================\033[0m")
    
    choice = input("\033[1;37m[?] CHOOSE OPTION: \033[0m")
    
    if choice == '1':
        print("\n\033[1;32m[*] STARTING FILE CLONING...")
        file_path = input("[?] ENTER FILE PATH: ")
        print("\033[1;33m[*] CRACKING STARTED... PLEASE WAIT\033[0m")
        time.sleep(3)
        print("\033[1;31m[!] No IDs found. Make sure file exists.\033[0m")
    elif choice == '2':
        print("\033[1;32m[*] PUBLIC ID CLONING STARTING...\033[0m")
    else:
        sys.exit()

def main():
    clear()
    # Device ID match logic
    user_id = "02af9ef2-05e2-443c-b75c-1c738c2e1d96"
    
    if user_id == OWNER_ID:
        print(f"\033[1;32m[✓] LICENSE VALID: WELCOME BEWAFA\033[0m")
        print("\033[1;33m====================================================\033[0m")
        # Yahan menu call hoga
        cloning_menu()
    else:
        print("\033[1;31m[✗] ACCESS DENIED! CONTACT OWNER\033[0m")
        sys.exit()

if __name__ == "__main__":
    main()
