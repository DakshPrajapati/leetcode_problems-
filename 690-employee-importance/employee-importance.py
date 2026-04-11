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
        '''

        step 1 - we need to find id of the employee in tree 
        in case we dont find we can retuirn 0

        root value start 
        we can use deque

        q.append(emp[0])

        while q and we dont find id:
            q.apend(emp[0].children) #we can have check here as well 
            we find root:
                savve root
            we break 

        after getting val
        we can clear queue and start cal
        '''

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
            