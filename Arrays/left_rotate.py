def reverseArr(self, arr, a, b):
        while a <= b:
            arr[a], arr[b] = arr[b], arr[a]
            a += 1
            b -= 1
def leftRotate(self, arr, k, n):
    k = k%n
    # temp = []
    # for i in range(n):
    #     j = i+k
    #     if j >= n:
    #         j = j-n
    #     temp.append(arr[j])
    # for i in range(n):
    #     arr[i] = temp[i]
    
    self.reverseArr(arr, 0, k-1)
    self.reverseArr(arr, k, n-1)
    self.reverseArr(arr, 0, n-1)