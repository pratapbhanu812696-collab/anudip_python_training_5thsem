def count_sentiments(reviews):
    excellent = 0
    good = 0
    average = 0
    poor = 0
    
    for r in reviews:
        if "excellent" in r:
            excellent += 1
        elif "good" in r:
            good += 1
        elif "average" in r:
            average += 1
        elif "poor" in r:
            poor += 1
            
    print(f"Excellent Reviews: {excellent}")
    print(f"Good Reviews: {good}")
    print(f"Average Reviews: {average}")
    print(f"Poor Reviews: {poor}")

# Yeh wala function missing tha ya galat jagah tha:
def most_common_word(reviews):
    all_words = []
    for r in reviews:
        all_words.extend(r.split())
        
    most_common = max(all_words, key=all_words.count)
    return most_common

def longest_review(reviews):
    longest = ""
    for r in reviews:
        if len(r) > len(longest):
            longest = r
    return longest

def reviews_with_keyword(reviews, keyword):
    print(f"Reviews containing '{keyword}':")
    for r in reviews:
        if keyword in r:
            print(r)

# --- Main Program Execution ---
reviews = [
    "excellent movie",
    "average story",
    "excellent acting",
    "poor direction",
    "excellent visuals",
    "poor screenplay",
    "good music",
    "excellent climax",
    "average performance",
    "good cinematography"
]

# 1. Count Sentiments
count_sentiments(reviews)

# 2. Most Common Word
print(f"Most Common Word:\n{most_common_word(reviews)}")

# 3. Longest Review
print(f"Longest Review:\n{longest_review(reviews)}")

# 4. Reviews with Keyword
reviews_with_keyword(reviews, "excellent")
