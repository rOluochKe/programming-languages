// Define a prototype object
const prototype = {
  greeting: "Hello",
  sayHello: function () {
    console.log(this.greeting + " World!");
  },
  clone: function () {
    return Object.create(this);
  },
};
// Create a new object by cloning the prototype
const newObj = prototype.clone();
// Modify the new object's properties
newObj.greeting = "Hola";
// Call the sayHello method of the new object
newObj.sayHello(); // Output: Hola World!

// another example

// Define a prototype object for caching data
const cachePrototype = {
  data: {},
  getData: function (key) {
    return this.data[key];
  },
  setData: function (key, value) {
    this.data[key] = value;
  },
  clone: function () {
    const cache = Object.create(this);
    cache.data = Object.create(this.data);
    return cache;
  },
};
// Create a cache object by cloning the prototype
const cache = cachePrototype.clone();
// Populate the cache with some data
cache.setData("key1", "value1");
cache.setData("key2", "value2");
cache.setData("key3", "value3");
// Clone the cache to create a new cache with the same data
const newCache = cache.clone();
// Retrieve data from the new cache
console.log(newCache.getData("key1")); // Output: value1
// Modify data in the new cache
newCache.setData("key2", "new value");
// Retrieve modified data from the new cache
console.log(newCache.getData("key2")); // Output: new value
// Retrieve original data from the original cache
console.log(cache.getData("key2")); // Output: value2
