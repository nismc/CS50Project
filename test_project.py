from project import check_username_existence, check_credentials, save_credentials
import csv


def test_check_username_existence():
    existing_username = "nina"
    non_existing_username = "bob"
    assert check_username_existence(existing_username) is True
    assert check_username_existence(non_existing_username) is False


def test_check_credentials():
    username = "hello"
    password = "goodbye"
    assert check_credentials(username, password) is False


def test_save_credentials():
    username = "david"
    password = "harvard"
    save_credentials(username, password)
    with open("credentials.csv", mode="r") as csvfile:
        reader = csv.reader(csvfile)
        data = list(reader)
        assert [username, password] in data


test_save_credentials()
test_check_credentials()
test_check_username_existence()
