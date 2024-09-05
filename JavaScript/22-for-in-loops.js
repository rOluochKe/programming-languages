// We typically use for-loops to iterate over an array.

// We also have another loop known as the for-in loop
// which is used to iterate over the keys of a JavaScript object.

// A JavaScript object is a data type that allows you to store key-value pairs.

const course = {
  name: "JavaScript for Beginners",
  duration: 3,
  setions: 7,
};

console.log(course.name);
console.log(course["duration"]);
console.log(course.sections);

// We could also iterate over the keys with the for-in loop.
for (const key in course) {
  console.log(course[key]);
}

console.log("================================================");

// In the case when we are simply looping over the elements of an array.
// If we aren't utilizing the index variable, then we have a cleaner syntax.

let numbers = [1, 2, 3, 4, 5, 6, 7];

for (const number of numbers) {
  console.log(number);
}
