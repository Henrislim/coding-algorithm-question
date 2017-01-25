def mergesort(seq):
    if len(seq)<=1:
        return seq
    mid=int(len(seq)/2)
    left=mergesort(seq[:mid])
    right=mergesort(seq[mid:])
    return merge(left,right)