from getFileBytesYandexDisk import getFileBytesYandexDisk

import configparser

config = configparser.ConfigParser()
config.read("config.ini")

public_key = config["Settings"]["public_key"]
path = config["Settings"]["path"]


def downloadFileSchedule():
    fileBytes = getFileBytesYandexDisk(public_key)
    with open(path, 'wb') as f:
        f.write(fileBytes)


if __name__ == "__main__":
    downloadFileSchedule()