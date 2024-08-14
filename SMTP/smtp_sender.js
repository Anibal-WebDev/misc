const net = require("node:net");

class SMTPSender {
  constructor() {
    this.sender = net.createConnection({ port: 2525 }, () => {
      console.log(
        "Connected to server on",
        this.sender.remoteAddress + ":" + this.sender.remotePort,
      );
      this.sender.on("data", (data) => {
        console.log(data.toString());
      });
    });
  }
  writeData(data) {
    this.sender.write(data);
  }

  close() {
    this.sender.end();
  }

  helo(domain) {
    this.writeData(`HELO ${domain}\r\n`);
  }

  mailFrom(reversePath) {
    this.writeData(`MAIL FROM: ${reversePath}\r\n`);
  }

  receiptTo(forwardPath) {
    this.writeData(`RCPT TO: ${forwardPath}\r\n`);
  }

  data() {
    this.writeData("DATA\r\n");
  }
}

const smtpSender = new SMTPSender();
smtpSender.mailFrom("<weirdohax@localhost>");
