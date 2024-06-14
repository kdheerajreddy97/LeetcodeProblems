class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        letter_logs = []
        digit_logs = []
        
        for log in logs:
            log_new = log.split()
            if log_new[1].isalpha():
                letter_logs.append(log)
            else:
                digit_logs.append(log)
        
        for i in range(len(letter_logs)):
            for j in range(i + 1, len(letter_logs)):
                log1 = letter_logs[i]
                log2 = letter_logs[j]
                
                content1 = log1.split()[1:]
                content2 = log2.split()[1:]
                identifier1 = log1.split()[0]
                identifier2 = log2.split()[0]
                
                if (content1 > content2) or (content1 == content2 and identifier1 > identifier2):
                    letter_logs[i], letter_logs[j] = letter_logs[j], letter_logs[i] 
            
        
        return letter_logs + digit_logs
                
                
        