class Solution:
    def isPalindrome(self, s: str) -> bool:
        string = [char for char in s if char.isalnum()]
        text = "".join(string).lower()
        n = len(text)
        i = 0;
        j = n - 1
        while i < j:
            if text[i] != text[j]:
                print(f"error in i: {text[i]}")
                print(f"error in j: {text[j]}")
                return False
            i += 1
            j -= 1

        return True


        