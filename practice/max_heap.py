class MaxHeap:
    def __init__(self) -> None:
        self.heap: list = []

    def insert(self, elem: tuple):
        self.heap.append(elem)
        index = len(self.heap) - 1

        if len(self.heap) == 1:
            return self.heap

        if len(self.heap) == 2:

            if self.heap[0][1] < self.heap[1][1]:
                self.heap = [self.heap[1], self.heap[0]]
            
            return self.heap
            

        while index != 0 and self.heap[(index - 1)//2][1] < self.heap[index][1]:
            parent_index = (index - 1)//2
            self.heap[index], self.heap[parent_index] = self.heap[parent_index], self.heap[index]
            index = parent_index

        return self.heap

    def extract_max(self):
        if len(self.heap) == 0:
            return None

        max_val = self.heap[0]

        if len(self.heap) == 1:
            self.heap = []
            return max_val

        if len(self.heap) == 2:
            self.heap = self.heap[1:]
            return max_val

        self.heap[0] = self.heap[-1]
        self.heap.pop()

        parent_index = 0
        while 2*parent_index + 1 < len(self.heap):
            child_1_index = 2*parent_index + 1
            child_2_index = 2*parent_index + 2
            parent_has_2_child = False

            if 2*parent_index + 2 < len(self.heap):
                parent_has_2_child = True

            replace_index = child_1_index
            if parent_has_2_child and self.heap[child_1_index][1] < self.heap[child_2_index][1]:
                replace_index = child_2_index

            if self.heap[replace_index][1] > self.heap[parent_index][1]:
                self.heap[replace_index], self.heap[parent_index] = self.heap[parent_index], self.heap[replace_index]
                parent_index = replace_index

            else:
                break

        return max_val



    def __str__(self) -> str:
        return str(self.heap)
    

def main():
    heap = MaxHeap()
    for _tuple in [(3, 1), (1, 1), (0, 2)]:
        heap.insert(_tuple)

    print(heap)
    for i in range(3):
        heap.extract_max()
        print(heap)

if __name__ == '__main__':
    main()