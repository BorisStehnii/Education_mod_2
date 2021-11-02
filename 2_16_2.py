'''
Implement 2 classes, the first one is the Boss and the second one is the Worker.

Worker has a property 'boss', and its value must be an instance of Boss.

You can reassign this value, but you should check whether the new value is Boss.
Each Boss has a list of his own workers.
You should implement a method that allows you to add workers to a Boss.
You're not allowed to add instances of Boss class to workers list directly via access to attribute,
use getters and setters instead!

You can refactor the existing code.
'''

import random


class Boss:

    def __init__(self, name: str, company: str):
        self.id_ = random.randint(0, 100)
        self.name = name
        self.company = company
        self._workers = []

    @property
    def workers_(self):
        workers = self._workers
        return workers

    @workers_.setter
    def workers_(self, worker):
        self._workers.append(worker)

    def __repr__(self):
        return f"{self.name} {self.id_}"


class Workers:

    def __init__(self, name: str, company: str):
        self.id_ = random.randint(0, 100)
        self.name_worker = name
        self._company = company
        self._boss = None

    def __repr__(self):
        return f"{self.name_worker} {self.id_}"

    @property
    def worker_boss(self):
        boss = self._boss
        return boss

    @worker_boss.setter
    def worker_boss(self, boss):
        if isinstance(boss, Boss):
            self._boss = boss
            Boss.workers_ = Workers

    @worker_boss.deleter
    def worker_boss(self):
        self._boss = None


bor = Workers("Boris", "AMC")
vik = Boss("Viktor", "AMC")
bor.worker_boss = vik
print(bor.worker_boss)
print(vik.workers_)

