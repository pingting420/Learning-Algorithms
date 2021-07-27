class Solution:
    def getImportance(self, employees, id: int):
        mp = {employee.id : employee for employee in employees}
        def dfs(id):
            employee = mp[id]
            total = employee.importance + sum(dfs(subId) for subId in employee.subordinates)
            return total
        return dfs(id)