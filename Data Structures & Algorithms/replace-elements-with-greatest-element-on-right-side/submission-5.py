class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        for n in range(len(arr)-1):
            largest = arr[n+1]
            for i in range(n+1, len(arr)):
                if arr[i] > largest:
                    largest = arr[i]

                else:
                    continue
            
            arr[n] = largest

    
        arr[-1] = -1
        return arr
                
                