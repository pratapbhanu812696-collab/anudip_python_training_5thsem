# 20 Sample Chat Messages
messages = [
    "Hello everyone welcome to the Python workspace",
    "This is an awesome and clean environment",
    "Can anyone help me with this simple string question?",
    "Python is great",
    "Yes",
    "Let us complete this mini assignment today itself",
    "Excellent work done by the whole development team",
    "Data science is the future of modern technology",
    "Keep learning every single day to grow fast",
    "We need to focus on building logic without shortcuts",
    "Amazing",
    "Please check your email notification for updates",
    "Coding is fun and very rewarding too",
    "Artificial intelligence is changing the entire world completely",
    "Do you love programming in Python language?",
    "Keep it up",
    "Hard work always pays off in the end",
    "Success demands continuous effort and absolute dedication",
    "Consistency is the ultimate key to master any hard skill",
    "Goodbye"
]

total_words_all = 0
longest_msg = ""
shortest_msg = messages[0]
global_word_freq = {}

print("="*60)
print("           CHAT MESSAGE ANALYTICS")
print("="*60)

for msg in messages:
    words = msg.split()
    word_count = len(words)
    char_count = len(msg)
    total_words_all += word_count
    
    # Track Longest/Shortest messages
    if len(msg) > len(longest_msg):
        longest_msg = msg
    if len(msg) < len(shortest_msg):
        shortest_msg = msg

    v_count = 0
    c_count = 0
    longest_word = ""
    shortest_word = words[0] if words else ""
    vowel_words = []
    long_words = []
    local_word_freq = {}

    for word in words:
        # Clean word from punctuation if any
        clean_word = word.strip("?,.").lower()
        
        # Word Frequency Track
        local_word_freq[clean_word] = local_word_freq.get(clean_word, 0) + 1
        global_word_freq[clean_word] = global_word_freq.get(clean_word, 0) + 1
        
        # Longest/Shortest word
        if len(clean_word) > len(longest_word):
            longest_word = clean_word
        if len(clean_word) < len(shortest_word):
            shortest_word = clean_word
            
        # Words starting with vowel
        if clean_word and clean_word[0] in "aeiou":
            vowel_words.append(word)
            
        # Words longer than 5 chars
        if len(clean_word) > 5:
            long_words.append(word)

    # Vowels and Consonants in message
    for char in msg:
        if char.lower() in "aeiou":
            v_count += 1
        elif char.lower() in "bcdfghjklmnpqrstvwxyz":
            c_count += 1

    # Find repeated words in this message
    repeated_words = [w for w, c in local_word_freq.items() if c > 1]

    print(f"\nMessage: \"{msg}\"")
    print(f"-> Words: {word_count}, Characters: {char_count}")
    print(f"-> Vowels: {v_count}, Consonants: {c_count}")
    print(f"-> Longest Word: '{longest_word}', Shortest Word: '{shortest_word}'")
    print(f"-> Words starting with Vowel: {vowel_words}")
    print(f"-> Words > 5 Characters: {long_words}")
    if repeated_words:
        print(f"-> Repeated Words: {repeated_words}")

# Find most frequent word overall
most_freq_word = ""
max_freq = 0
for w, c in global_word_freq.items():
    if c > max_freq:
        max_freq = c
        most_freq_word = w

# Challenge Report
print("\n" + "="*50)
print("            CHALLENGE SUMMARY REPORT")
print("="*50)
print(f"Most Frequently Used Word : '{most_freq_word}' ({max_freq} times)")
print(f"Longest Message           : \"{longest_msg}\"")
print(f"Shortest Message          : \"{shortest_msg}\"")
print(f"Average Words Per Message : {total_words_all / len(messages):.2f}")
print("="*50)
