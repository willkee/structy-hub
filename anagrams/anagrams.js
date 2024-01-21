const anagrams = (s1, s2) => {
  const hashMap = {}
  for (let i = 0; i < s1.length; i++) {
    const letter = s1[i];
    hashMap[letter] ? hashMap[letter]++ : hashMap[letter] = 1
  }
  
  for (let i = 0; i < s2.length; i++) {
    const letter = s2[i];
    
    if (!hashMap[letter] || hashMap[letter] === 0) return false;
    hashMap[letter]--;
  }
  
  for (const letter in hashMap) {
    if (hashMap[letter] !== 0) return false
  }
  return true
};
​
module.exports = {
  anagrams,
};
​