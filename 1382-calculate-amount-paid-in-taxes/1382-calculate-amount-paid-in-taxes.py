# Time Complexity: O(n); Space: O(1)
class Solution:
    def calculateTax(self, brackets: List[List[int]], income: int) -> float:

        tax = min(income , brackets[0][0]) * brackets[0][1] / 100.0
        if income == 0: return 0

        print(tax)
        if len(brackets[0]) == 1 or income < brackets[0][0]:
            return tax
        for i in range(1, len(brackets)):
            if income > brackets[i][0]:
                tax += (brackets[i][0] - brackets[i-1][0]) * brackets[i][1] /100.0
                print(tax)
            else:
                tax += (income - brackets[i-1][0]) * brackets[i][1] / 100.0

                print(tax)
                break
        return tax
