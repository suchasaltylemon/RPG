import api
import ctypes
lib = ctypes.windll.LoadLibrary("src/DLL/lib.dll")

import asyncio

c_mult = lib["Multiply"]
res = c_mult(ctypes.c_int(4), ctypes.c_int(4))


name_request = api.net.requests._BaseRequest("Timmy", "name")

def create_server(port=7092):
    server = api.net.Server(port)

    return server


def create_client(ip, port=7092):
    client = api.net.Client(ip, port)

    return client


async def main():
    if input("Use server? y/n ").lower().strip() == 'y':
        server = create_server()

    else:
        client = create_client()


    print()



if __name__ == "__main__":
    asyncio.run(main())
