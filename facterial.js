//вычесляем фактериал через цикл for
const factorial = (n) => {
  let result  = 1;

  // initialization↓    condition↓     update↓
  for (let counter = 1; counter <= n; counter++) {
    result *= counter;
  }

  return result;
}
