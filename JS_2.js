//функция находящая наименьший делитель
const smallestDivisor = (num) => { //создаем функцию с названием
  const iter = (counter, acc) => { // создаем новую переменную iter
    if (counter === 1) { // прописываем первое условие 
      return 1;
    }
      if (counter%acc===0) { // прописываем второе условие
          return acc; // если делится без остатка возвращаем делитель 
      }
    return iter(counter,acc+1);// увеличиваем счетчик на 1
  };
    return iter(num,2);
};
