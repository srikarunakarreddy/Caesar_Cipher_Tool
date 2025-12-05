# ---------------------------------------------------------
# Project: Caesar Cipher Encryption/Decryption Tool
# By Sri Karunakar Reddy Avuthu
# Tech Stack: Python (Variables, Loops, Conditionals)
# Description: A tool to encrypt messages, decrypt them, 
# and brute-force hack encoded messages.
# ---------------------------------------------------------

# Alphabet size is constant
ALPHABET_SIZE = 26

# ASCII Art Banner for visual appeal in the terminal
print("------------------------------------------------")
print("   C Y B E R   S E C U R I T Y   T O O L   ")
print("          CAESAR CIPHER ENGINE             ")
print("------------------------------------------------")

while True:
    # 1. Main Menu Options
    print("\nSelect a mode:")
    print("1. Encrypt a message")
    print("2. Decrypt a message")
    print("3. Brute Force (Hack) a message")
    print("4. Exit")
    
    mode = input("Enter choice (1/2/3/4): ")

    if mode == '4':
        print("Exiting tool. Goodbye!")
        break

    elif mode == '1' or mode == '2':
        text = input("\nEnter your message: ")
        
        valid_key = False          # Validating integer input for the key
        while not valid_key:
            shift_input = input("Enter shift key (0-25): ")
            if shift_input.isdigit():
                shift = int(shift_input)
                valid_key = True
            else:
                print("Invalid key. Please enter a number.")

        result_text = ""
        
        if mode == '2':            # For decryption, we reverse the shift
            shift = -shift

        for char in text:          # Loop through every character in the user's text
            if char.isalpha():     # Check if it's a letter
                start_index = 65 if char.isupper() else 97    # Get the ASCII start point (65 for 'A', 97 for 'a')
                
                """Math: Convert char to 0-25 range -> Add shift -> Modulo 26 -> Convert back
                ord(char) gets the ASCII number
                chr(num) gets the character from the number"""
                original_pos = ord(char) - start_index
                new_pos = (original_pos + shift) % ALPHABET_SIZE
                new_char = chr(start_index + new_pos)
                
                result_text += new_char
            else:
                result_text += char       # Keep symbols/spaces/numbers exactly as they are
        
        print(f"\nResult: {result_text}")

    elif mode == '3':
        message_to_hack = input("\nEnter the encrypted message to hack: ")
        print("\n--- ATTEMPTING BRUTE FORCE ATTACK ---")
        
        for key_attempt in range(1, 26):    # Loop through every possible key (1 to 25)
            hacked_text = ""
            
            """Decrypt logic using the current key_attempt
            Since we are hacking (decrypting), we subtract the key"""
            shift = -key_attempt
            
            for char in message_to_hack:
                if char.isalpha():
                    start_index = 65 if char.isupper() else 97
                    
                    original_pos = ord(char) - start_index
                    new_pos = (original_pos + shift) % ALPHABET_SIZE
                    new_char = chr(start_index + new_pos)
                    
                    hacked_text += new_char
                else:
                    hacked_text += char
            
            # Print every attempt so the user can visually find the right one
            print(f"Key #{key_attempt}: {hacked_text}")

    else:
        print("Invalid selection. Please choose 1, 2, 3, or 4.")