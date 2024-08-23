const { Readable, Transform, Writable } = require("stream");

// Define a Readable stream that emits an array of numbers
class NumberGenerator extends Readable {
  constructor(options) {
    super(options);
    this.numbers = [1, 2, 3, 4, 5];
  }

  _read(size) {
    const number = this.numbers.shift();
    if (!number) return this.push(null);
    this.push(number.toString());
  }
}

// Define a Transform stream that doubles the input number
class Doubler extends Transform {
  _transform(chunk, encoding, callback) {
    const number = parseInt(chunk, 10);
    const doubledNumber = number * 2;
    this.push(doubledNumber.toString());
    callback();
  }
}

// Define a Writable stream that logs the output
class Logger extends Writable {
  _write(chunk, encoding, callback) {
    console.log(`Output: ${chunk}`);
    callback();
  }
}

// Create instances of the streams
const numberGenerator = new NumberGenerator();
const doubler = new Doubler();
const logger = new Logger();

// Chain the streams together
numberGenerator.pipe(doubler).pipe(logger);
