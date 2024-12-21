# Two Approaches:
# 1. Heaps
# 2. Bucket Sort or HashMap
class Solution:
    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> List[int]:
        map = {}
        m = len(bikes)
        n = len(workers)
        for i in range(len(workers)):
            for j in range(len(bikes)):
                dist = self.calculate_dist(workers[i], bikes[j])
                if dist in map:
                    map[dist].append((i,j))
                else:
                    map[dist] = [(i,j)]
        
        bikes_visited = set()
        workers_visited = set()
        res = [-1] * n
        for key in sorted(map.keys()):
            for val in map[key]:
                worker = val[0]
                bike = val[1]
                if worker not in workers_visited and bike not in bikes_visited:
                    res[worker] = bike
                    workers_visited.add(worker)
                    bikes_visited.add(bike)

        return res
                

        





    def calculate_dist(self, worker, bike):
        x = abs(worker[0] - bike[0])
        y = abs(worker[1] - bike[1])
        return x + y

        