"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        mapp = { }
        importance = {}
        for i in range(len(employees)):
            employee = employees[i]
            e_id, e_imp, e_subs = employee.id, employee.importance, employee.subordinates
            mapp[e_id] = e_subs
            importance[e_id] = e_imp
        
        q = deque()
        q.append(id)
        ans_imp = 0

        while q:
            employee = q.popleft()
            ans_imp += importance[employee]
            for child in mapp[employee]:
                q.append(child)
        
        return (ans_imp)
            