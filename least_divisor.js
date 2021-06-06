// BEGIN (write your solution here)
const smallestDivisor  = (n) => {
  let counter = 2;
    
  if (n < 1) {
    return NaN;
  } 
  if (n === 1) {
    return n ;
  }
while (n % counter) { 
    counter = counter + 1;
  }

  return counter;
}
// END
