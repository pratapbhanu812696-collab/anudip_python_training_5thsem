# 20 sample email addresses
emails = [
    "rahul123@gmail.com", "priya@outlook.com", "anuj@company.in", "invalid email@gmail.com",
    "amit@yahoo.com", "suresh.kumar@gmail.com", "neha@outlook.com", "wrong@domain@com",
    "पूजा@gmail.com", "vikas55@yahoo.com", "hr@company.in", "test.user@com",
    "rohit@gmail.com", "sneha@outlook.com", "info@company.in", "contact@yahoo.com",
    "sales@company.in", "user1@gmail.com", "user2@gmail.com", "admin@outlook.com"
]

invalid_emails = []
domain_counts = {}

print("="*60)
print("       EMAIL VALIDATION & DOMAIN ANALYTICS")
print("="*60)

for email in emails:
    # 1. Validation check
    has_space = " " in email
    dot_count = email.count(".")
    at_count = email.count("@")
    
    if at_count == 1 and dot_count >= 1 and not has_space:
        # Valid email structure: Extract parts
        parts = email.split("@")
        username = parts[0]
        domain_part = parts[1]
        
        if "." in domain_part:
            d_parts = domain_part.split(".")
            domain = domain_part
            extension = d_parts[-1]
            
            # Count digits and special characters in username
            digits = 0
            special = 0
            for char in username:
                if char.isdigit():
                    digits += 1
                elif not char.isalnum():
                    special += 1
            
            # Domain Analytics Tracking
            domain_counts[domain] = domain_counts.get(domain, 0) + 1
            
            print(f"Email: {email} [VALID]")
            print(f"  Username: {username} (Digits: {digits}, Special: {special})")
            print(f"  Domain: {domain}, Extension: .{extension}")
        else:
            invalid_emails.append(email)
    else:
        invalid_emails.append(email)

# Display Invalid Emails
print("\n" + "="*40)
print("            INVALID EMAILS")
print("="*40)
for inv in invalid_emails:
    print(f"X {inv}")

# Challenge: Domain Report
print("\n" + "="*40)
print("         CHALLENGE DOMAIN REPORT")
print("="*40)
for dom, count in domain_counts.items():
    print(f"{dom} -> {count} users")
print("="*40)
