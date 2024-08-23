class House {
  constructor(builder) {
    this.bedrooms = builder.bedrooms;
    this.bathrooms = builder.bathrooms;
    this.kitchens = builder.kitchens;
    this.garages = builder.garages;
  }
}
class HouseBuilder {
  constructor() {
    this.bedrooms = 0;
    this.bathrooms = 0;
    this.kitchens = 0;
    this.garages = 0;
  }
  setBedrooms(bedrooms) {
    this.bedrooms = bedrooms;
    return this;
  }
  setBathrooms(bathrooms) {
    this.bathrooms = bathrooms;
    return this;
  }
  setKitchens(kitchens) {
    this.kitchens = kitchens;
    return this;
  }
  setGarages(garages) {
    this.garages = garages;
    return this;
  }
  build() {
    return new House(this);
  }
}
const house1 = new HouseBuilder()
  .setBedrooms(3)
  .setBathrooms(2)
  .setKitchens(1)
  .setGarages(2)
  .build();
console.log(house1); // Output: House { bedrooms: 3, bathrooms: 2, kitchens: 1, garages: 2 }

// example 2

class Person {
  constructor(name, age, email, phoneNumber) {
    this.name = name;
    this.age = age;
    this.email = email;
    this.phoneNumber = phoneNumber;
  }
}
class PersonBuilder {
  constructor() {
    this.name = "";
    this.age = 0;
    this.email = "";
    this.phoneNumber = "";
  }
  withName(name) {
    this.name = name;
    return this;
  }
  withAge(age) {
    this.age = age;
    return this;
  }
  withEmail(email) {
    this.email = email;
    return this;
  }
  withPhoneNumber(phoneNumber) {
    this.phoneNumber = phoneNumber;
    return this;
  }
  build() {
    return new Person(this.name, this.age, this.email, this.phoneNumber);
  }
}
// Example usage
const person1 = new PersonBuilder()
  .withName("Alice")
  .withAge(30)
  .withEmail("alice@example.com")
  .build();
const person2 = new PersonBuilder()
  .withName("Bob")
  .withPhoneNumber("555-1234")
  .build();
