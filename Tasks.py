class Tasks:

    def __init__(self, num_jobs):
        self._jobs = [None] * num_jobs
        self._n = num_jobs

class Job:

    def __init__(self, ID):
        self.ID = ID
        self.edges = []

class Client:

    def __init__(self, client_name, num_jobs):
        self.client_name = client_name
        self._jobs = Tasks(num_jobs)

    def open_job(self, i):

        # check if parent is complete
        pass

    def close_job(self, i):

        if i > self._n or i < 0:
            return 0

        self._jobs[i] = 0
        
        return 1

    def check_parent(self, i):

        # 2n+1

        return 1