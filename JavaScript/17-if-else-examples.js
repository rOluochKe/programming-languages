// Implement a function that accepts two numbers and returns the maximum number.

function max(num1, num2) {
  return num1 >= num2 ? num1 : num2;
}

// Implement a function to accept a number.
// Then return "FizzBuzz" if divisible by 3 and 5.
// Or return "Fizz" if only divisible by 3.
// Or return "Buzz" if only divisible by 5.
// Or return the original number if not divisible by 3 or 5

function fizzBuzz(num) {
  if (typeof num !== "number") return num;

  if (num % 3 === 0 && num % 5 === 0) return "FizzBuzz";
  else if (num % 3 === 0) return "Fizz";
  else if (num % 5 === 0) return "Buzz";
  else return num;
}

let number = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];

function displayEvenNumbers(number) {
  for (const num of number) {
    if (num % 2 === 0) console.log(num);
  }
}

function displayOddNumbers(number) {
  for (const num of number) {
    if (num % 2 !== 0) console.log(num);
  }
}
