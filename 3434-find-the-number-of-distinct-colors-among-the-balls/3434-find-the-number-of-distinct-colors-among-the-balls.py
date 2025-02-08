# class Solution:
#     def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
#         n = len(queries)
#         color_count = {}
#         balls_map = [0] * (limit + 1)
#         res = [0] * n

#         for i in range(n):
#             ball, color = queries[i]

#             if balls_map[ball] != 0:
#                 prev = balls_map[ball]
#                 color_count[prev] -= 1

#                 if color_count[prev] == 0:
#                     del color_count[prev]

#             balls_map[ball] = color

#             if color in color_count:
#                 color_count[color] += 1
#             else:
#                 color_count[color] = 1

#             res[i] = len(color_count)

#         return res


class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        n = len(queries)
        color_count = {}
        balls_map = {}
        res = [0] * n

        for i in range(n):
            ball, color = queries[i]

            if ball in balls_map:
                prev = balls_map[ball]
                color_count[prev] -= 1

                if color_count[prev] == 0:
                    del color_count[prev]

            balls_map[ball] = color

            if color in color_count:
                color_count[color] += 1
            else:
                color_count[color] = 1

            res[i] = len(color_count)

        return res
            






        