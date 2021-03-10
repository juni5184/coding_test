import re


class Solution:
    def myAtoi(self, s: str) -> int:
        # 1
        s = s.lstrip()

        answer = 0
        if s != "":
            # 2,3,4
            if s[0] == '-' and len(s) > 1:
                if s[1].isdigit():
                    answer = 0 - int((re.findall("\d+", s))[0])

            elif s[0] == '+' and len(s) > 1:
                if s[1].isdigit():
                    answer = int((re.findall("\d+", s))[0])

            elif s[0].isdigit():
                answer = int(re.findall("\d+", s)[0])
            else:
                answer = 0

        # 5
        if answer > (2 ** 31) - 1:
            answer = (2 ** 31) - 1
        elif answer < -(2 ** 31):
            answer = -(2 ** 31)

        return answer


