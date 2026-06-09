# News paragraph containing over 300 words
article = """
The digital revolution has completely transformed how modern human civilization operates on a daily basis. 
In recent years artificial intelligence and machine learning technologies have moved from simple labs 
into real world applications. Today smart machines power online search systems networks hospitals 
and driverless cars seamlessly. Millions of active software developers across the entire world are building 
creative updates to solve complex global problems efficiently. Python has emerged as the premier language 
for data science projects globally because it is simple to read and exceptionally powerful to execute. 
Students and professional experts find it easy to master programming when they start their core journey 
with easy syntax rules. However tech progress also introduces unique challenges regarding data privacy 
and cloud infrastructure security parameters. Cyber attacks are growing rapidly so we need stronger protection 
mechanisms across networks immediately. Every big enterprise corporation is heavily investing resources 
into securing user platforms and databases from malicious hackers. Educational institutions are transforming 
their curriculum systems to include advanced analytics and computer engineering modules. Young students 
must learn how to code data pipelines effectively before entering the highly competitive modern job market. 
Innovation never stops and those who update their skill sets continuously will always find great success 
in this tech ecosystem. Tomorrow belongs to smart automated workflows and sustainable green energy technology. 
Leaders should focus on ethical frameworks so that technology benefits every individual equally without bias. 
Let us build a highly collaborative global network to secure a brighter digital future for generations to come.
"""

# Clean and break text into words
words_list = article.split()
total_words = len(words_list)
total_chars = len(article)

# Sentences split by '.'
sentences_list = article.split(".")
# Remove empty strings at the end if any
sentences_count = 0
for s in sentences_list:
    if s.strip():
        sentences_count += 1

v_count = 0
c_count = 0
for char in article:
    if char.lower() in "aeiou":
        v_count += 1
    elif char.lower() in "bcdfghjklmnpqrstvwxyz":
        c_count += 1

# Word frequency analysis
word_freq = {}
total_word_len = 0
longest_word = ""
shortest_word = words_list[0]

for w in words_list:
    clean_w = w.strip(".,!?\"()").lower()
    if clean_w:
        total_word_len += len(clean_w)
        word_freq[clean_w] = word_freq.get(clean_w, 0) + 1
        
        # Longest / Shortest word checks
        if len(clean_w) > len(longest_word):
            longest_word = clean_w
        if len(clean_w) < len(shortest_word):
            shortest_word = clean_w

# Categories based on frequencies
only_once = []
more_than_5 = []
most_frequent_word = ""
max_word_count = 0

for w, count in word_freq.items():
    if count == 1:
        only_once.append(w)
    if count > 5:
        more_than_5.append(w)
    if count > max_word_count:
        max_word_count = count
        most_frequent_word = w

# Alphabet distribution check (words starting with each alphabet)
alphabet_counts = {}
for w in word_freq:
    first_letter = w[0]
    if first_letter.isalpha():
        alphabet_counts[first_letter] = alphabet_counts.get(first_letter, 0) + 1

# Output Processing
print("="*60)
print("             NEWS TEXT ANALYZER DASHBOARD")
print("="*60)
print(f"1. Total Characters : {total_chars}")
print(f"2. Total Words      : {total_words}")
print(f"3. Total Sentences  : {sentences_count}")
print(f"4. Vowels Count     : {v_count}, Consonants Count: {c_count}")
print(f"5. Longest Word     : '{longest_word}'")
print(f"6. Shortest Word    : '{shortest_word}'")
print(f"7. Words Appearing Only Once (First 10 shown): {only_once[:10]}")
print(f"8. Words Appearing More than 5 times         : {more_than_5}")
print(f"9. Alphabet Distribution Count               : {alphabet_counts}")

# Challenge Summary Report
print("\n" + "="*50)
print("         CHALLENGE TEXT SUMMARY REPORT")
print("="*50)
print(f"Total Words          : {total_words}")
print(f"Total Sentences      : {sentences_count}")
print(f"Average Word Length  : {total_word_len / total_words:.2f} characters")
print(f"Most Frequent Word   : '{most_frequent_word}' ({max_word_count} times)")
print(f"Vocabulary Size      : {len(word_freq)} unique words")
print("="*50)
