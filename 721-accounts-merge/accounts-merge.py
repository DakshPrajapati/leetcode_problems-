
class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        mailToName = {}
        parent = {}
        rank = {}
        
        for account in accounts:
            name = account[0]
            for email in account[1:]:
                mailToName[email] = name
                if email not in parent:
                    parent[email] = email
                    rank[email] = 0

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        
        def union(x, y):
            root_x, root_y = find(x), find(y)
            if root_x == root_y:
                return

            if rank[root_x] > rank[root_y]:
                parent[root_y] = root_x
            elif rank[root_y] > rank[root_x]:
                parent[root_x] = root_y
            else:
                parent[root_y] = root_x
                rank[root_x] += 1
        
        for account in accounts:
            root_mail = account[1]
            for email in account[2:]:
                union(root_mail, email)

        ans = defaultdict(list)
        for email in parent:
            root = find(email)
            ans[root].append(email)
        
        res = []
        for root, group in ans.items():
            name = mailToName[root]
            res.append([name] + sorted(group))
        
        return res