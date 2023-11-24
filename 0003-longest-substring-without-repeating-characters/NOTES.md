​//Concept: Sliding Window

//Time Spent on this question : 50 minutes

/*Algorithm or Steps

Unaanza ivi:

int right = 0; right < n; right++: Hii for-loop ina iterate through each character in the string s, with right serving as the pointer to mwisho ya the current substring yenye tunaexamine. n ni the length of the string s.

Processing Each Character:

char currentChar = s.charAt(right): For each iteration, chukua hio character kwa index yenye right iko.


Updating the Left Pointer:

if (charIndexMap.containsKey(currentChar)): Inaangalia kama the current character penye tuko tushaiona before. (and hence iko kwa HashMap).

left = Math.max(charIndexMap.get(currentChar) + 1, left): Kama hio character ishaonekana before, the left pointer inafaa ku-updatiwa. Unaiset to the position right after the last occurrence of the current character. ( .get() hufetch the value part of the HashMap's Key, value pair setup, for this case, the Integer with the index associated na the character we're looking at).

 However, to avoid moving left backward (which could include a repeated character in the current window), Math.max is used. Kuensure that left only moves to the right.


Updating HashMap and Calculating Max Length:

charIndexMap.put(currentChar, right): Hii line ina update the HashMap with the current character and its latest index. This is crucial because if the character is encountered again, we want to use its most recent index.
maxLength = Math.max(maxLength, right - left + 1): After potentially updating left and always updating the HashMap, the length of the current substring without repeating characters is right - left + 1. We compare this with maxLength to keep track of the longest such substring found so far.


Imagine the string s = "abba". We want to find the length of the longest substring without repeating characters.

We start with left = 0 and iterate over the string.

When right = 0, we have s.charAt(right) = 'a'. The character 'a' is not in the HashMap, so it gets added with its index (0). The substring is now "a".

When right = 1, s.charAt(right) = 'b'. Similarly, 'b' is added with index 1. The substring is "ab".

When right = 2, s.charAt(right) = 'b' again. This time, 'b' is already in the map, with the previous index 1. We set left to 1 + 1 = 2 (the position right after the last occurrence of 'b'). The substring considered now is "b", starting from the second 'b'.

When right = 3, s.charAt(right) = 'a'. 'a' is in the map with index 0. According to the rule, we should set left to 0 + 1 = 1. But left is already at 2 from the previous step.
If we move left back to 1, we would include a repeated character ('b') in our substring. To avoid this, we use Math.max(charIndexMap.get(currentChar) + 1, left), which results in left staying at 2. The substring remains "b".