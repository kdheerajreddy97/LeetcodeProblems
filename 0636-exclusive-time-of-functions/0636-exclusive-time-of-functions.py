# Approach: Stack; Best solution
# Time: O(n); Space: O(n)(res) + O(n/2)(For Stack as we append only start times)
class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        res = [0] * n
        mystack = []
        # Will be different for start time and end time
        last_execution = 0
        
        for log in logs:
            thread_id, typ, time = log.split(":")
            thread_id = int(thread_id)
            time = int(time)

            if typ == "start":
                # only if previous threads exists
                if mystack:
                    # update the execution time into the res
                    res[mystack[-1]] += time - last_execution
                # push to stack the current executed thread
                mystack.append(thread_id)
                # Since its a start thread last_execution will be updated with latest time for next thread
                last_execution = time
            else:  # end
                # "+1" as we count the end time as extra time # imp step
                res[mystack.pop()] += time - last_execution + 1
                # last_execution for next thread should start from next minute or second 
                last_execution = time + 1
        
        return res
