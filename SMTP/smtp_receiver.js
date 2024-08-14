const net = require("node:net");

class SMTPreceiver {
  constructor() {
    this.receiver = net.createServer((socket) => {
      console.log(
        "Server started on",
        socket.address()["address"] + ":" + socket.address()["port"],
      );
      socket.on("data", (data) => {
        console.log(data.toString());
        socket.write("250 OK\r\n");
      });
      socket.on("end", () => {
        console.log("Connection closed");
      });
    });
  }
  start(port, host, backlog) {
    this.receiver.listen(port, host, backlog);
  }
}

const smtpReceiver = new SMTPreceiver();
smtpReceiver.start(2525, "localhost", 5);
