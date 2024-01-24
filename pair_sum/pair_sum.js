const pairSum = (numbers, targetSum) => {
  
  
  for (let i = 0; i < numbers.length; i++) {
    for (let j = i + 1; j < numbers.length; j++) {
      const num1 = numbers[i];
      const num2 = numbers[j];
      
      if (num1 + num2 === targetSum) {
        return [i, j];
      }
    }  
  }
};
​
module.exports = {
  pairSum,
};
​