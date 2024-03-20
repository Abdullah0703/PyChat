# Python Client-Server Chat Application

This is a simple client-server chat application implemented in Python using sockets. It allows communication between a server and multiple clients over a network.

## Features

- **Bi-directional Communication**: Both the server and clients can send and receive messages to and from each other.
- **Simple Interface**: The interface is text-based and simple to use.
- **Graceful Termination**: The conversation can be terminated gracefully by either the server or the client by sending the message "bye".

## Prerequisites

- Python 3.x

## Usage

1. **Start the Server**: Run the `server.py` script to start the server. It will listen for incoming connections on port 9999 of the localhost.

    ```bash
    python server.py
    ```

2. **Connect the Client**: Run the `client.py` script to connect a client to the server. You can run multiple instances of the client script to simulate multiple clients.

    ```bash
    python client.py
    ```

3. **Start Chatting**: Once the client is connected to the server, you can start exchanging messages. Enter your message at the prompt and press Enter to send it. You will receive messages from the other party.

4. **End the Conversation**: To end the conversation, type "bye" and press Enter. This will terminate the connection between the client and the server.

## Example

Here's an example of how to use the chat application:

1. Start the server:

    ```bash
    python server.py
    ```

2. Connect a client:

    ```bash
    python client.py
    ```

3. Exchange messages between the client and server:

    ```
    Server: Welcome to the chat room!
    client => Hello, server!
    Server: Hi there!
    client => How are you?
    Server: I'm doing well, thank you!
    client => bye
    ```

4. Terminate the conversation:

    ```
    Server: bye
    ```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---
