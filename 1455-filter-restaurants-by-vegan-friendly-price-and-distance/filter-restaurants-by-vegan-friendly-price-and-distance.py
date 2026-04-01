class Solution:
    def filterRestaurants(self, restaurants: List[List[int]], veganFriendly: int, maxPrice: int, maxDistance: int) -> List[int]:
        '''
        1- Time Optimized
            > Delay sort as back as possible
            > Filter first based on vegan, dist, price
            > Then sort at the end based on rating (not increasing)
        
            [-] store filtered list somewhere 

        2- Space Optimized 

            > we sort first 
            > then return only which matches conditions
            > wont matter much since we cant paginate results to save network cost 
            > time consupmption v.v.high (nlogn but n >> previousN)

        '''    

        def isValid(x):
            
            idx, rating, ifVegan, price, dist = x

            if veganFriendly == 1 and ifVegan != 1:
                return False
            
            if price > maxPrice:
                return False

            if dist > maxDistance:
                return False 

            return True 

        candidates = []
        
        for r in restaurants:
            if isValid(r):
                candidates.append([r[0],r[1]])

        candidates.sort(key=lambda x: (x[1], x[0]))
        return [x[0] for x in candidates][::-1]