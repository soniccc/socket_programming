#!/usr/bin/env python3

# import argparse
import socket

# parser = argparse.ArgumentParser(description="Choose to be a Client or Server")
# parser


def chat_choice():
    # print("Please enter you choice to be a server or client: ")
    # print("ENTER: server or client")
    name = input("Do you want to be a Server or Client? ")

    if name.casefold() == "server":
        print("You are a Server")
        server()
    elif name.casefold() == "client":
        print("You are a Client")
        client()
    elif name.casefold() != "client" or "server":
        print("Sorry you have input incorrectly....")


def server():

    def send_text(sending_socket, text):
        text = text + "\n"
        data = text.encode()
        sending_socket.send(data)

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(("0.0.0.0", 8081))
    server_socket.listen(5)
    print("SERVER MESSAGE: Server is waiting... waiting for a new message... yea...")
    connection_socket, address = server_socket.accept()
    print("SERVER MESSAGE: Client has connected!!")
    send_message = "RECEIVED MESSAGE: Hello, thanks for connecting"
    send_data = send_message.encode()
    send_text(connection_socket, "what the fuck man!!")
    # connection_socket.send(send_data)

    while True:
        recv_data = connection_socket.recv(1024)
        if not recv_data:
            break
        else:
            recv_message = recv_data.decode()
            print(recv_message)
        # connection_socket.send(recv_data)

    server_socket.close()


def client():
    server_ipadd = input("Please enter the IP Address of the Chat Server: ")
    message_status = True
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    send_message = input("Please enter the message you wish to send: ")
    client_socket.connect((server_ipadd, 8081))

    while message_status:
        # print("LOCAL MESSAGE: Made my connection baby!!")
        # send_message = "RECEIVED MESSAGE: Hello, thanks for letting me, the client, connect!!"
        send_data = send_message.encode()
        client_socket.send(send_data)
        check_msg = input("Do you have any more messages? (y/n): ")
        if check_msg == 'y':
            send_message = input(
                "Please enter the message you wish to send: ")
        elif check_msg == 'n':
            message_status = False
            break
        else:
            print("You have not entered y/n. Please try again")

    while True:
        recv_data = client_socket.recv(1024)
        # if not recv_data:
        if check_msg == 'n':
            break
        else:
            recv_message = recv_data.decode()
            print(recv_message)
        # client_socket.send(send_data)

    client_socket.close()


if __name__ == '__main__':
    chat_choice()
