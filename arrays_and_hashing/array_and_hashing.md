Two Sum
- Given the tareget, return the indexes of the pair that add up to it. 
- The trick here was the negative numbers
  -> I transformed the list in a dict, {x: index(x)}
  -> Then to find the second elem of the pair y in (x + y = target), I did y = target - x. 
     But in math x - y != y - x, so added a check for target = x + y, if didn't match I did y = x - target. 

Valid Anagrams
- For Valid Anagrams,
-> First Approach -> 2 strings → 2 lists → 2 dictionaries → compare
  Why this could have been better, cause don't need a list, can iterate a string. 
  Can have a single dict instead of double. For single dict, keep the keys as letters and values as count, add for one string and subtract for another, thus for each letter the value should be 0. If yes true else false. 
 
Contains Duplicate
- I used the 'set' of python, this was a very pythonic solution, I compared the len of the total letters, with the set of numbers to identify the uniqueness of each letter. 

Group Anagrams.
- The biggest learning here is that the keys of the dictionary are hashable and immutable. And as dict and list are mutable, strings and tuples are immutable and can be used as dict keys. With this newly found knowledge or could be categorized as forgotton knowledge, I was able to create a dict of anagrams with tuples representing the whole group of anagrams, in a single pass. 

Top K Frequent Elements
- I used buckets and GPT suggested Heap, so solution came in with MaxHeap
- MaxHeap uses Insertion and ExtractMax.
- Root has the highest value node, represent in Binary Tree, starting from left. 
- Each parent has two child, both are smaller than the parent and that's the whole logic
- For extract max you take of the zeroth index and put the last element at the front and then apply logic of swapping child w/ parent if child is greater than parent.