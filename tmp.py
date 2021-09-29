class Solution:
    def uniqueLetterString(self, s: str) -> int:
        l = len(s)
        if l == 0:
            return 0
        score = [0] * l
        score[0] = 1

        occurance = {}
        contribution = {}
        occurance[s[0]] = 0
        contribution[s[0]] = 1

        for i in range(l):
            if i == 0:
               continue
            cur_char = s[i]
            if cur_char not in occurance:
                score[i] = score[i-1] + (i + 1)
                contribution[cur_char] = i+1
                occurance[cur_char] = i
            else:
                score[i] = score[i-1] - (contribution[cur_char]) + (i - occurance[cur_char])
                occurance[cur_char] = i
                contribution[cur_char] = i - occurance[cur_char] + 1

        return sum(score)