# python3

class dequeue:
    def __init__(self):
        self.queue = []

    def frontPush(self, val) :
        self.queue = [val, x for x in self.queue]
        
    def pushBack(self, val) :
        self.queue.append(val)


def max_sliding_window_naive(sequence, m):
    maximums = []
    for i in range(len(sequence) - m + 1):
        maximums.append(max(sequence[i:i + m]))

    return maximums

if __name__ == '__main__':
    n = int(input())
    input_sequence = [int(i) for i in input().split()]
    assert len(input_sequence) == n
    window_size = int(input())

    print(*max_sliding_window_naive(input_sequence, window_size))

