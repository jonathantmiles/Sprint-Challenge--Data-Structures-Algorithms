Add your answers to the questions below.

1. What is the runtime complexity of your `depth_first_for_each` method?

    it checks each element in the tree twice, once for left node, secondly for right node. So I'd say it's:

    O(n) (simplified from O(2n))

2. What is the space complexity of your `depth_first_for_each` function?

    it at most holds one element for the height of the tree in memory (or with an extra 'None' object at the end)

    O(h) (where h is the height of the tree, simplified from O(h+1))

3. What is the runtime complexity of your `breadth_first_for_each` method?

4. What is the space complexity of your `breadth_first_for_each` method?

5. What is the runtime complexity of your `heapsort` function?

    O(n) (from O(2n) since it adds each element once to the heap, then a second time from the heap to the returned list)

6. What is the space complexity of the `heapsort` function? Recall that your implementation should return a new array with the sorted data. What would be the space complexity if your function instead altered the input array?

    O(n) from O(2n) since it holds two arrays in memory of equal sizes

    if I altered the input array instead it would be a strict 0(n)
