class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        idxMap = {}
        for idx, val in enumerate(ingredients):
            idxMap[recipes[idx]] = idx
        
        canBeMade = set()
        seen = set()
        def dfs(root):
            if root in supplies or root in canBeMade:
                return True
            if root in seen:
                return False       
            if root in idxMap:
                seen.add(root)
                for c in ingredients[idxMap[root]]:
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
        