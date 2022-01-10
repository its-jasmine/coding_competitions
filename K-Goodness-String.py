


class Adas_String:
    def __init__(self, string, n, k):
        self.string = string
        self.n = n
        self.k = k
        self.goodness_score = self.goodness()
    
    # Returns goodness score of string
    def goodness(self):
        score = 0
        for i in range(int(self.n/2)):
            if (self.string[i] != self.string[self.n - i - 1]): 
                score += 1
        return score
    
    # Determines minimum number of operations to acheive desired goodness score of k
    def min_op(self):
        if self.goodness_score == k: 
            return 0
        elif self.goodness_score < k:
            return k - self.goodness_score
        elif self.goodness_score > k:
            return self.goodness_score - k
        
    # Responsible for output in requested format    
    def result(self, i):
        min = self.min_op()
        print(f"Case #{i}: {min}")

num_tests = int(input())
for i in range(num_tests):
    n, k = (int(j) for j in input().split())
    string = Adas_String(input(), n, k)
    string.result(i + 1)



