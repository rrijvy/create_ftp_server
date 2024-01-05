import socket
import subprocess


def get_local_ip():
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

        sock.connect(("8.8.8.8", 80))

        local_ip = sock.getsockname()[0]

        return local_ip
    except socket.error as e:
        print(f"Error: {e}")
        return None


def start_ftp_server():
    command = [
        "python",
        "-m",
        "pyftpdlib",
        "-p",
        "2121",
        "-i",
        get_local_ip(),
        "-d",
        r"E:\Tutorials",
        "-u",
        "root",
        "-P",
        "confirm000",
    ]

    try:
        subprocess.run(command, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    start_ftp_server()
