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

def tables_merge(dsu, id_values, dest_id, source_id):
    if dest_id != source_id:
        final_dest_id = dsu.find(dest_id)
        final_source_id = dsu.find(source_id)
        if final_dest_id != final_source_id:
            id_values[final_dest_id] += id_values[final_source_id]
            id_values[final_source_id] = 0
            dsu.union(final_dest_id, final_source_id)
        return id_values[final_dest_id]
    return id_values[dest_id]
                 
def inp_as_it_list():
    return list(map(int, input().split(' ')))

def main():
    tables_n, requests_m = inp_as_it_list()
    initial_tables_sizes = inp_as_it_list()
    dsu = DSU(tables_n)
    ids = { dsu.make_set(val): val for index, val in enumerate(initial_tables_sizes) }
    max_table_size = max(initial_tables_sizes)
    while requests_m > 0:
        dest, source = inp_as_it_list()
        max_table_size = max(max_table_size, tables_merge(dsu, ids, dest, source))
        print(max_table_size)
        requests_m -= 1

main()
                