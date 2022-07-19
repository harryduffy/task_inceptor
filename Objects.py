class Tasks:

    def __init__(self, num_jobs):
        self._jobs = []
        self._n = num_jobs

    def add_job(self, j):
        self._jobs.append(j)

    def add_edge(self, i, j):
        i.edges.append(j)
        j.edges.append(i)

class Job:

    def __init__(self, ID, level):
        self.ID = ID
        self.edges = []
        self.level = level
        self.state = 0

class Client:

    def __init__(self, client_name, num_jobs):
        self.client_name = client_name
        self.jobs = Tasks(num_jobs)

    def open_job(self, i):

        if self.check_parent(i):
            for j in self.jobs._jobs:
                if j.ID == i.ID:
                    j.state = 2
            return 1
        
        return 0

    def close_job(self, i):

        if i.state == 1:
            return 0

        i.state = 1
        
        return 1

    def check_parent(self, i):

        if 1 == i.level:
            return 1

        for j in self.jobs._jobs:
            if i.level - 1 == j.level:
                if 0 == j.state:
                    return 0

        return 1

# client = Client("Harry Duffy", 7)
# A = Job("A", 1)
# B = Job("B", 2)
# C = Job("C", 2)
# D = Job("D", 3)
# E = Job("E", 4)
# F = Job("F", 4)
# G = Job("G", 5)

# jobs = [A, B, C, D, E, F, G]

# for j in jobs:
#     client.jobs.add_job(j)

# #1/2
# client.jobs.add_edge(A, B)
# client.jobs.add_edge(A, C)
# client.jobs.add_edge(A, D)

# #2/3
# client.jobs.add_edge(B, E)
# client.jobs.add_edge(C, E)
# client.jobs.add_edge(D, F)

# #3/4
# client.jobs.add_edge(E, G)
# client.jobs.add_edge(F, G)

# # 0 = not started
# # 1 = complete
# # 2 = working on it

# client.open_job(A)
# client.open_job(B)
# client.open_job(G)

# for j in client.jobs._jobs:
#     print(j.ID, j.state)

# client.close_job(A)
# print()

# for j in client.jobs._jobs:
#     print(j.ID, j.state)

