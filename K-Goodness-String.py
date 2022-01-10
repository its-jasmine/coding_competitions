


class Adas_String:
    def __init__(self, string, n, k):
        self.string = string
        self.n = n
        self.k = k
        self.good_i = []
        self.goodness_score = self.goodness()

    def goodness(self):
        score = 0
        for i in range(int(self.n/2)):
            if (self.string[i] != self.string[self.n - i - 1]):
                score += 1
                self.good_i.append(i)
        return score
    def min_op(self):
        if self.goodness_score == k:
            return 0
        elif self.goodness_score < k:
            return k - self.goodness_score
        elif self.goodness_score > k:
            return self.goodness_score - k
    def result(self, i):
        min = self.min_op()
        print(f"Case #{i}: {min}")


num_tests = int(input())
for i in range(num_tests):
    n, k = (int(j) for j in input().split())
    string = Adas_String(input(), n, k)
    string.result(i + 1)




'''
case 1: string already has goodness score of k
case 2: string has goodness score < k
case 3: string has goodness score > k
'''