class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        res = [0] * n
        mystack = []
        last_execution = 0
        
        for log in logs:
            thread_id, typ, time = log.split(":")
            thread_id = int(thread_id)
            time = int(time)

            if typ == "start":
                if mystack:
                    res[mystack[-1]] += time - last_execution
                mystack.append(thread_id)
                last_execution = time
            else:  # end
                res[mystack.pop()] += time - last_execution + 1
                last_execution = time + 1
        
        return res
