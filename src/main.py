import network
import network.api.requests as requests


def main():
    is_server = input("Use server? ").lower().strip() == 'y'

    if is_server:
        port = int(input("Port: "))
        server = network.Server(port)
        server.run()

    else:
        ip, port = input("Info: ").split(':')
        client = network.Client(ip, int(port))

        username = input("Username: ")
        username_request = requests.Request("username", username, "Username")

        client.connect()
        client.send(username_request)


if __name__ == "__main__":
    main()
