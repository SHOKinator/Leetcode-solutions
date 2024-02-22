class Solution:
    def reverse(self, x: int) -> int:
        negative = False
        if x < 0:
            x *= -1
            negative = True

        if x > 2**31 - 1:
            return 0

        x = str(x)
        x_list = list(x)
        x_list.reverse()
        x = ''.join(x_list)
        x = int(x) + 0

        if negative == True:
            x *= -1

        if x > 2**31 - 1 or x < -2**31:
            return 0
        return x
