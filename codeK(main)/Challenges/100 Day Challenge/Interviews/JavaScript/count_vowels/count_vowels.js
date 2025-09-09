

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
console.log(result); // 2