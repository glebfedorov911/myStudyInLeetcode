class Solution  :
    def convert(self, s, numRows):
        index = 0
        new_s = [[] for _ in range(numRows)]
        f1 = True
        f2 = False
        for let in s:
            new_s[index].append(let)
            if index+1 != numRows and f1:
                index += 1
                if index == numRows-1:
                    f1 = False
                    f2 = True
            elif index-1 >= 0 and f2:
                index -= 1
                if index == 0:
                    f1 = True
                    f2 = False
        return ''.join([''.join(i) for i in new_s])


sol = Solution()
print(sol.convert("PAYPALISHIRING", 3))