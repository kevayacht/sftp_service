from datetime import datetime
import pysftp
import sys
import os


class SFTPClient:

    def __init__(self, server):
        self.con = None
        self.server = dict(
            host=server["host"],
            username=server["username"],
            password=server["password"],
            private_key=server["private_key"],
            private_key_pass=server["private_key_pass"],
        )

        self.root_dir = None

    def login(self):
        os.chdir(os.path.dirname(sys.argv[0]) or '.')

        current_date_time = datetime.now().date()
        print("Current date and time: " + str(current_date_time))
        print("host = [%s]\nusername = [%s]\nprivate_key = [%s]" % (
            self.server["host"], self.server["username"], self.server["private_key"]))

        try:
            with pysftp.Connection(**self.server) as con:
                print("Connection Established")
                self.root_dir = con.listdir()
                print("root dir = [%s]" % self.root_dir)

        except pysftp.ConnectionException as e:
            print("Connection Exception: %s" % e)

        finally:
            print(" Exit Connection")


def main():
    print("Start main function")
    server = {
        "host": "sftp_ip",
        "username": "sftp_username",
        "password": "password!",
        "private_key": "private_key.pem",
        "private_key_pass": "sftp_passphrase#"}
    client = SFTPClient(server)
    client.login()


if __name__ == '__main__':
    main()
