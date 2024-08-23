class UserService {
  constructor(userRepository) {
    this.userRepository = userRepository;
  }
  async getUsers() {
    const users = await this.userRepository.getUsers();
    return users;
  }
  async addUser(user) {
    await this.userRepository.addUser(user);
  }
}
class UserRepository {
  async getUsers() {
    // get users from database
  }
  async addUser(user) {
    // add user to database
  }
}
// Creating instances of the classes
const userRepository = new UserRepository();
const userService = new UserService(userRepository);
// Using the userService object to get and add users
userService.getUsers();
userService.addUser({ name: "John", age: 25 });

// Another example

// emailSender.js
class EmailSender {
  constructor(emailService) {
    this.emailService = emailService;
  }

  async sendEmail(userEmail, emailContent) {
    const success = await this.emailService.sendEmail(userEmail, emailContent);
    return success;
  }
}

// emailService.js
class EmailService {
  async sendEmail(userEmail, emailContent) {
    // actually send the email to the user
    // return true if successful, false if failed
  }
}

// emailSender.test.js
const assert = require("assert");
const EmailSender = require("./emailSender");
const EmailService = require("./emailService");

describe("EmailSender", () => {
  it("should send email to user", async () => {
    // Create a mock EmailService that logs email content instead of sending the email
    const mockEmailService = {
      sendEmail: (userEmail, emailContent) => {
        console.log(`Email to ${userEmail}: ${emailContent}`);
        return true;
      },
    };

    const emailSender = new EmailSender(mockEmailService);

    const userEmail = "example@example.com";
    const emailContent = "Hello, this is a test email!";
    const success = await emailSender.sendEmail(userEmail, emailContent);

    assert.strictEqual(success, true);
  });
});
