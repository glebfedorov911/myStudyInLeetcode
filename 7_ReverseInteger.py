class Solution:
    def reverse(self, x):
        x_string = str(x)
        if x_string[0] == '-':
            res = -1 * int(x_string[1:][::-1])
        else:
            res = int(x_string[::-1])
        
        if -2**31 <= res <= 2**31-1:
            return res
        return 0