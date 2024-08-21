const numbers = [1, 2, 3, 4, 5];

// To remove elements,
// .pop() to remove from the end
// .splice() to remove from the middle
// .shift() to remove from the beginning

// NOTE: \n within a string stands for newline,

const lastElement = numbers.pop();
console.log(`lastElement: ${lastElement}\n`); // lastElement: 5
console.log(numbers);

const firstElement = numbers.shift();
console.log(`firstElement: ${firstElement}`); // firstElement: 1
console.log(numbers);

// 1st arg is the index to start from
// 2nd arg is the number of elements to remove
const middleElement = numbers.splice(1, 1);
console.log(`middleElement: ${middleElement}`); // middleElement: 3
console.log(numbers);
