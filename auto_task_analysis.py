class DSU:

    def __init__(self, size):
        self.ids = 1
        self.parent = [-1] * (size + 1)
        self.rank = [0] * (size + 1)

    def make_set(self, elem):
        _id_ = self.ids
        self.ids += 1
        self.parent[_id_] = _id_
        self.rank[_id_] = 0
        return _id_

    def find(self, num):
        if num != self.parent[num]:
            self.parent[num] = self.find(self.parent[num])
        return self.parent[num]

    def union(self, num1, num2):
        num1_id, num2_id = self.find(num1), self.find(num2)
        if num1_id == num2_id: return num1_id
        self.parent[num2_id] = num1_id

def inp_as_it_list():
    return list(map(int, input().split(' ')))

def main():
    vars_n, equations_e, unequations_d = inp_as_it_list()
    dsu = DSU(vars_n)
    for i in range(1, vars_n + 1):
        dsu.make_set(i)
    result = 1
    while equations_e > 0:
        var1, var2 = inp_as_it_list()
        dsu.union(var1, var2)
        equations_e -= 1
    while unequations_d > 0:
        var1, var2 = inp_as_it_list()
        if dsu.find(var1) == dsu.find(var2):
            result = 0
            break
        unequations_d -= 1
    print(result)

main()