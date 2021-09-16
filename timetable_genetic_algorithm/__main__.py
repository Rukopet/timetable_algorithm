import sys


# def main():
#     async def handle(request):

def console_main():
    len_argv = len(sys.argv)
    if len_argv > 3:
        raise AttributeError(f'Incorrect argv len; your len={len_argv - 1}; need 2 or 1')
    elif len_argv == 3:
        ...
    elif len_argv == 2:
        ...


def server_main():
    print(11)
    ...


if __name__ == "__main__":
    if len(sys.argv) > 1:
        console_main()
    else:
        server_main()
