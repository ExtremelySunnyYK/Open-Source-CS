# python3
"""
Learning Objective: Apply priority queues to schedule jobs on processors

How to apply priority queue to simulate processing jobs in the required order? 

Remember to consider the case when several threads become free simultaneously.

"""
"""
Test case


"""

import heapq

class JobQueue:
    def read_data(self):
        self.num_workers, m = map(int, input().split())
        self.jobs = list(map(int, input().split()))
        assert m == len(self.jobs)

    def write_response(self):
        for worker_id,start_time in self.result:
          print(worker_id,start_time) 

    def assign_jobs(self):
        # TODO: replace this code with a faster algorithm.
        self.assigned_workers = [None] * len(self.jobs)
        self.start_times = [None] * len(self.jobs)
        next_free_time = [0] * self.num_workers
        for i in range(len(self.jobs)):
          next_worker = 0
          for j in range(self.num_workers):
            if next_free_time[j] < next_free_time[next_worker]:
              next_worker = j
          self.assigned_workers[i] = next_worker
          self.start_times[i] = next_free_time[next_worker]
          next_free_time[next_worker] += self.jobs[i]

    #Thread class
    class Worker:
        def __init__(self,id,release_time=0):
            self.id = id
            self.release_time = release_time
            
        #returns the job that has finished. If 2 or more job are free, returns the priority one
#        def __cmp__(self,other):
#            if self.release_time == other.release_time:
#                return self.id < other.id
#            return self.release_time < other.release_time
        
        #require comparison dunder due to priorityq.pop()
        
        def __lt__(self, other):
            if self.release_time == other.release_time:
                return self.id < other.id
            return self.release_time < other.release_time

        def __gt__(self, other):
            if self.release_time == other.release_time:
                return self.id > other.id
            return self.release_time > other.release_time

        
    def fast_job(self):
        self.result = []
        self.workerq = []
        
        #creates a list for workers
        for i in range(self.num_workers):
            self.workerq.append(self.Worker(i))
        
        
        #appends result
        for job in self.jobs:
            worker = heapq.heappop(self.workerq)
            self.result.append((worker.id,worker.release_time))
            worker.release_time += job
            heapq.heappush(self.workerq,worker)
            
    
    
    def solve(self):
        self.read_data()
        #self.assign_jobs()
        self.fast_job()
        self.write_response()

if __name__ == '__main__':
    job_queue = JobQueue()
    job_queue.solve()

