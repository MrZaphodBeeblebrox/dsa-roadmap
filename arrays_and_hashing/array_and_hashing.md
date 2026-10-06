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
 