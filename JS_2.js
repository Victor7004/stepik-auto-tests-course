const smallestDivisor = (num) => {
  const iter = (counter, acc) => {
    if (counter === 1) {
      return 1;
    }
      if (counter%acc===0) {
          return acc;
      }
    return iter(counter,acc+1);
  };
    return iter(num,2);
};
