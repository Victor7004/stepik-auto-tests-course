const sequenceSum = (begin, end) => {
  // BEGIN (write your solution here)
    if(begin===end)
           return begin;
    if(begin>end || begin === undefined || end === undefined)
        return NaN;
    return begin + sequenceSum(begin + 1, end);
  // END
};
