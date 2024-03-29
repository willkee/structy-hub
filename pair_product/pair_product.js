const pairProduct = (numbers, targetProduct) => {
  for (let i = 0; i < numbers.length; i++) {
    const num = numbers[i];
    
    const multiplier = targetProduct / num;
    const isInt = Number.isInteger(multiplier);
    if (isInt) {
      // We're looking for the multiplier in the rest of the array
      const secondIdx = numbers.slice(i + 1).indexOf(multiplier)
      if (secondIdx !== -1) return [i, numbers.indexOf(multiplier)]
    }
  }
};
​
module.exports = {
  pairProduct,
};
​