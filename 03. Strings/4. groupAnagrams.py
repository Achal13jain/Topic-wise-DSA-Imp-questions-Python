#Group strings that are anagrams of each other.
# 🔹 Idea (Character Frequency Key)
# Anagrams have same character counts
# Use tuple of counts as key

def group_anagrams(words):
    groups = {}

    for word in words:
        count = [0] * 26

        # Count characters
        for ch in word:
            count[ord(ch) - ord('a')] += 1

        key = tuple(count)
        if key not in groups:
            groups[key] = []

        groups[key].append(word)

    return list(groups.values())
# Example usage

words = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(group_anagrams(words))
# Output: [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]
# Time Complexity: O(n * k) where n is number of words and k is max length of a word
# Space Complexity: O(n * k) for storing the grouped anagrams