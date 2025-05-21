from collections import defaultdict

class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        # Step 1: Preprocess s
        char_indices = defaultdict(list)
        for i, ch in enumerate(s):
            char_indices[ch].append(i)

        # Custom binary search: first index in arr > target
        def binary_search(arr, target):
            left, right = 0, len(arr)
            while left < right:
                mid = (left + right) // 2
                if arr[mid] <= target:
                    left = mid + 1
                else:
                    right = mid
            return left  # could be out of bounds

        # Step 2: Check if word is subsequence
        def is_subsequence(word):
            prev_index = -1
            for ch in word:
                if ch not in char_indices:
                    return False
                pos = binary_search(char_indices[ch], prev_index)
                if pos == len(char_indices[ch]):
                    return False
                prev_index = char_indices[ch][pos]
            return True

        # Step 3: Count valid subsequences
        count = 0
        for word in words:
            if is_subsequence(word):
                count += 1
        return count
