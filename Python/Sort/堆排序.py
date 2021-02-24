class Solution:
    def heapSort(self, nums):
        self.heapfy(nums)
        for i in range(len(nums) - 1):
            self.extractMax(nums, 0, len(nums) - i)

    def heapfy(self, nums):
        for i in range(len(nums) // 2 - 1, -1, -1):
            self.siftDown(nums, i, len(nums))

    def siftUp(self, heap, pos):
        if pos == 0:
            return
        parent = pos // 2 - 1
        if heap[parent] < heap[pos]:
            heap[parent], heap[pos] = heap[pos], heap[parent]
            self.siftUp(heap, parent)

    def siftDown(self, heap, pos, size):
        left = 2 * pos + 1
        right = 2 * pos + 2
        target = left
        if target >= size:
            return
        if right < size and heap[right] > heap[target]:
            target = right
        if heap[target] > heap[pos]:
            heap[pos], heap[target] = heap[target], heap[pos]
            self.siftDown(heap, target, size)

    def extractMax(self, heap, start, end):
        heap[start], heap[end - 1] = heap[end - 1], heap[start]
        self.siftDown(heap, start, end - 1)


if __name__ == "__main__":
    S = Solution()
    nums = [4, 2, 3, 1, 5, 1]
    S.heapSort(nums)
    print(nums)
