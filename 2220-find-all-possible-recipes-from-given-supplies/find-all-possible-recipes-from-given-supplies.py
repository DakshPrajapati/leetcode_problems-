class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        adjMap = {}
        for idx, val in enumerate(ingredients):
            adjMap[recipes[idx]] = val
        
        canBeMade = set()
        seen = []

        def dfs(root):
            if root in supplies or root in canBeMade:
                return True
            if root in seen:
                return False       
            if root in adjMap:
                for c in adjMap[root]:
                    seen.append(root)
                    if not dfs(c):
                        seen.remove(root)
                        return False
                    seen.remove(root)
                canBeMade.add(root)    
                return True
            return False

        for r in recipes:
            if r not in canBeMade:
                dfs(r)
    
        return list(canBeMade)
        