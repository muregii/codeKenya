<!-- 

const count_vowels = (str) => {
    // create a variable to store the number of vowels
    let count = 0;
    // create a variable to store the vowels
    const vowels = "aeiou";
    // loop through the string
    for (let i = 0; i < str.length; i++) {
        // check if the current character is a vowel
        if (vowels.includes(str[i])) {
        // increment the count
        count++;
        }
    }
    // return the count
    return count;
}
    

// Test the function
const result = count_vowels("hello");
console.log(result); // 2 -->

## Challenge

Write a function that takes in a string and returns the number of vowels in that string.

## Approach

1. We have a function `count_vowels` that takes in a string as an argument.
2. We create a variable `count` to store the number of vowels.
3. We create a variable `vowels` to store the vowels.
4. We loop through the string and check if the current character is a vowel.
5. If it is, we increment the count.
6. We return the count.

## Example

```js
const result = count_vowels("hello");
console.log(result); // 2
```

## Explanation

```
    The string is "hello". It has 2 vowels, e and o.
```