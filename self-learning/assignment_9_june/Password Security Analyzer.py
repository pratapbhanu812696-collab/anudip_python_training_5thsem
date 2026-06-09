# 15 sample passwords
passwords = [
    "Admin@123", "password", "Hello World 2026!", "CoolP@ss99", "qwerty",
    "Secure#45", "python", "MySecr3t!", "LetMeIn_7", "12345678",
    "SUPER@CHARGED1", "just_a_pwd", "NoDigitsHere!", "P1@s", "Valid_P@ss2026"
]

report = {"Strong": 0, "Medium": 0, "Weak": 0}

print("="*60)
print("             PASSWORD SECURITY REPORT")
print("="*60)

for pwd in passwords:
    u_count = 0
    l_count = 0
    d_count = 0
    s_count = 0
    v_count = 0
    c_count = 0
    has_space = "No"
    
    # Character counting loop
    for char in pwd:
        if char.isupper():
            u_count += 1
        if char.islower():
            l_count += 1
        if char.isdigit():
            d_count += 1
        if not char.isalnum() and char != " ":
            s_count += 1
        if char.isspace():
            has_space = "Yes"
            
        # Vowels and Consonants
        if char.lower() in "aeiou":
            v_count += 1
        elif char.lower() in "bcdfghjklmnpqrstvwxyz":
            c_count += 1

    # Frequency and repeated characters
    freq = {}
    repeated = []
    max_char_count = 0
    most_freq_char = ""
    for char in pwd:
        freq[char] = freq.get(char, 0) + 1
        if freq[char] > max_char_count:
            max_char_count = freq[char]
            most_freq_char = char
            
    for char, count in freq.items():
        if count > 1:
            repeated.append(char)

    # Determine Password Strength
    length = len(pwd)
    if length >= 8 and u_count > 0 and l_count > 0 and d_count > 0 and s_count > 0 and has_space == "No":
        strength = "Strong"
    elif length >= 6 and (u_count > 0 or l_count > 0) and d_count > 0:
        strength = "Medium"
    else:
        strength = "Weak"
        
    report[strength] += 1

    # Display individual result
    print(f"\nPassword: {pwd}")
    print(f"-> Length: {length} (Min 8 Check: {'Passed' if length>=8 else 'Failed'}), Has Space: {has_space}")
    print(f"-> Uppercase: {u_count}, Lowercase: {l_count}, Digits: {d_count}, Special: {s_count}")
    print(f"-> Vowels: {v_count}, Consonants: {c_count}")
    print(f"-> Repeated Characters: {repeated}")
    print(f"-> Most Frequent Character: '{most_freq_char}' (Appeared {max_char_count} times)")
    print(f"-> Strength: {strength}")
    print("-" * 40)

# Challenge Summary Report
print("\n" + "="*40)
print("          CHALLENGE SUMMARY REPORT")
print("="*40)
print(f"Total Passwords Analyzed : {len(passwords)}")
print(f"Strong Passwords         : {report['Strong']}")
print(f"Medium Passwords         : {report['Medium']}")
print(f"Weak Passwords           : {report['Weak']}")
print("="*40)
