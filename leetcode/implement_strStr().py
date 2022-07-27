class Solution:
  def strStr(self, haystack: str, needle: str) -> int:
    size_needle = len(needle)
    a = size_needle

    if needle == None or haystack == None:
      return 0

    if needle in haystack:
      for i in range(len(haystack)):
        if haystack[i:a] == needle:
          return i
        a = a + 1

    else: #needle not in haystack
      return -1