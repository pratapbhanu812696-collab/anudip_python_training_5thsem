# Student Resume Sample text data
resume_text = """
Name: Amit Sharma
Email: amit.sharma2026@gmail.com
Phone: +91-9876543210
Education: B.Tech in Computer Science Engineering
Skills: Python, SQL, React, Java, Python, Communication, Teamwork, SQL, React
Projects:
1. E-Commerce Platform using React and Python backend engine.
2. Smart Analytics Dashboard with SQL database storage layer.
Achievements:
Secured 1st rank in National Level Hackathon coding competition.
Excellent technical expertise and strong professional communication skills.
"""

# Counts
total_words = len(resume_text.split())
total_chars = len(resume_text)

# Extract Email and Phone manually using simple loop logic
words_list = resume_text.split()
emails_found = []
phones_found = []

for w in words_list:
    clean_w = w.strip(":,()")
    if "@" in clean_w and "." in clean_w:
        emails_found.append(clean_w)
    if "-" in clean_w and any(char.isdigit() for char in clean_w):
        phones_found.append(clean_w)

# Skill frequency report and duplicate skill check
predefined_skills = ["python", "sql", "react", "java", "communication", "teamwork"]
skill_counts = {}
duplicate_skills = []

word_freq = {}
most_freq_word = ""
max_word_count = 0

for w in words_list:
    clean_w = w.strip(":,.-0123456789").lower()
    if clean_w:
        # Track general word frequency
        word_freq[clean_w] = word_freq.get(clean_w, 0) + 1
        if word_freq[clean_w] > max_word_count:
            max_word_count = word_freq[clean_w]
            most_freq_word = clean_w
            
        # If it is a matching skill
        if clean_w in predefined_skills:
            skill_counts[clean_w] = skill_counts.get(clean_w, 0) + 1

# Identify duplicate skills
for skill, count in skill_counts.items():
    if count > 1:
        duplicate_skills.append(skill)

# Custom loop sorting to find top 5 keywords (without sorted())
keyword_list = []
for k, v in word_freq.items():
    keyword_list.append([k, v])

# Manual Bubble Sort Loop
n = len(keyword_list)
for i in range(n):
    for j in range(0, n-i-1):
        if keyword_list[j][1] < keyword_list[j+1][1]:
            keyword_list[j], keyword_list[j+1] = keyword_list[j+1], keyword_list[j]

# Find most frequent skill
most_freq_skill = ""
max_skill_c = 0
for s, c in skill_counts.items():
    if c > max_skill_c:
        max_skill_c = c
        most_freq_skill = s

# Print Analysis Dashboard
print("="*50)
print("             RESUME ANALYSIS REPORT")
print("="*50)
print(f"Total Words           : {total_words}")
print(f"Total Characters      : {total_chars}")
print(f"Emails Found          : {len(emails_found)} ({emails_found})")
print(f"Phone Numbers Found   : {len(phones_found)} ({phones_found})")
print(f"Total Skills Detected : {len(skill_counts)}")
print(f"Skill Frequency Report: {skill_counts}")
print(f"Duplicate Skills Found: {duplicate_skills}")
print(f"Most Frequent Skill   : {most_freq_skill.upper()}")
print(f"Most Frequent Word    : '{most_freq_word}' ({max_word_count} times)")

print("\nTop 5 Keywords:")
for i in range(min(5, len(keyword_list))):
    print(f" - {keyword_list[i][0].capitalize()}: {keyword_list[i][1]} times")
print("="*50)
