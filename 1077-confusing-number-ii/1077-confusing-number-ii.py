class Solution:
    def confusingNumberII(self, n: int) -> int:
        # Creating the Mapping for the 180 degree rotation
        rotate = {
            '0': '0',
            '1': '1',
            '6': '9',
            '8': '8',
            '9': '6'
        }

        count = 0

        def is_confusing(num_str):
            # Reverse the number and then find the rotate[reversed] which gives the consufing number
            rotated = []

            reversed = num_str[::-1]

            for i in range(len(reversed)):
                rotated.append(rotate[reversed[i]])
            confusing_str = ''.join(rotated)
            # if not equal then its a confusing number
            return confusing_str != num_str

        def dfs(num_str):
            nonlocal count
            if num_str != "":
                value = int(num_str)
                # if value > n:
                #     return
                if value != 0 and is_confusing(num_str):
                    count += 1
            

            # For loop based recursion
            for num in rotate:
                if num_str == "" and num == '0':
                    continue
                
                new_str = num_str + num
                value = int(new_str)
                if value > n:
                    break
                dfs(new_str)
        
        dfs("")
        return count
