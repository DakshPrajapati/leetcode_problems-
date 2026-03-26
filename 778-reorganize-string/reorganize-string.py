class Solution:
    def reorganizeString(self, s: str) -> str:
        '''
            if there is way to find not possible
            cause if possible we can reconstruct using counter 
            
            [ 0 ] counter 
            [ 1 ] if one count > half of total len
            [ 2 ] max heap using counter with last used index 
            {
                a: 2, -2
                c: 2, -2
                d: 2, -2
                b: 4, -2      
            }
            
            [ 4 ] construction
            for i in range(len(s)):
                x = 
                if b[1] == i - 1:
                    y heappop()
                    ans = 
                ans           

        '''
        #[0] getting counts
        counts = Counter(s)
        
        #[1] impossible condition
        maxCount = max(counts.values())
        if maxCount > (math.ceil(len(s) / 2)):
            print(maxCount, len(s))
            return ""

        #[2] max heap construction
        heap = []
        for char in counts.keys():
            freq = counts[char]
            heapq.heappush(heap, (-freq, char, -2))


        #[3] ans string 
        ans = ''
        for i in range(len(s)):
            freqX, letterX, lastIdxX = heapq.heappop(heap)
            if lastIdxX == i - 1:
                freqY, letterY, lastIdxY = heapq.heappop(heap)
                ans = ans + letterY
                freqY += 1
                if freqY != 0:
                    heapq.heappush(heap,(freqY, letterY, i))
                heapq.heappush(heap,(freqX, letterX, lastIdxX))    
            else:
                ans = ans + letterX
                freqX += 1
                if freqX != 0:
                    heapq.heappush(heap,(freqX, letterX, i))
            
        return (ans)
        