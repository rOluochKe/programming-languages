// Another loop in JavaScript is the do-while loop.
// This differs from the traditional while-loop as
// it will execute the statements within the code block,
// and then evaluate the condition after.

// This means that a do-while loop is guaranteed to execute at least once.
let i = 0;
do {
  console.log(i);

  i++;
} while (i < 10);

// Infinite loops will cause your program to crash.
// You want to ensure within your loops that you are progressively
// getting closer to your condition being false as to termiante the loop.
