import string


class Solution(object):
    def myAtoi(self, s):
        if s == "" or (len(s) == 1 and s not in '0123456789') or (all(i not in '0123456789' for i in s)):
            return 0
        s = self.skip_spaces(s)
        char_changer = self.check_char(s)
        if char_changer == 0:
            return 0
        result = char_changer * int(self.delete_not_use_zero(s))
        if result < -2**31: return -2**31
        if result > 2**31-1: return 2**31-1
        return result

    @staticmethod
    def skip_spaces(s):
        i = 0
        while i < len(s) and s[i] == ' ':
            i += 1
        j = i + 1
        while j < len(s) and s[j] not in ' .-+':
            j += 1
        if j == i+1:
            return s
        return s[i:j+1]

    @staticmethod
    def check_char(s):
        for i in range(len(s)-1):
            if s[i] in '-.+' and s[i+1] not in '0123456789':
                return 0
        if s[0] in string.ascii_letters + '.':
            return 0
        if s[0] == '-':
            return -1
        return 1

    @staticmethod
    def delete_not_use_zero(s):
        f = False
        final = ''
        for i in s:
            if i in '-+. ' + string.ascii_letters and not f:
                continue
            if i in '-+. ' + string.ascii_letters and f:
                break
            if i in '0123456789' and not f:
                f = True
            final += i
        return final

s = Solution()
print(s.myAtoi("  +  413"))