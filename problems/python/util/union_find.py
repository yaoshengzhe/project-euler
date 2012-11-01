
class UnionFind:

    def __init__(self, capacity):

        self.validate(capacity)
        self.capacity = capacity
        self.table = [i for i in range(capacity)]
        self.weights = [1 for i in range(capacity)]

    def validate(self, capacity):
        if capacity < 1:
            raise Exception("table size should larger than 0")

    def find(self, index):
        root = index
        while self.table[root] != root:
            root = self.table[root]
        return root

    def union(self, i, j):
        a, b = self.find(i), self.find(j)
        if self.weights[a] > self.weights[b]:
            self.table[b] = a
            self.weights[a] += self.weights[b]
        else:
            self.table[a] = b
            self.weights[b] += self.weights[a]


if __name__ == '__main__':
    union_find = UnionFind(10)
    print union_find.table
    union_find.union(1, 2)
    print union_find.table
    union_find.union(1, 3)
    print union_find.table

