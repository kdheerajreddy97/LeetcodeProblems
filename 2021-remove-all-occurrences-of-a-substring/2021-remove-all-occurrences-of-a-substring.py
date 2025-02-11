class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        stack = []
        part_length = len(part)

        for char in s:
            stack.append(char)

            if len(stack) >= part_length and self.check_match(stack, part, part_length):

                for i in range(part_length):
                    stack.pop()

        return "".join(stack)

    def check_match(self, stack, part, part_length):
        last = []
        stack_len = len(stack) - 1
        for i in range(part_length):
            last.append(stack[stack_len - i])
        
        last_str = "".join(last[::-1])

        return last_str == part





        