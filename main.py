# Author: Miguel Toledano.
import os

import requests

BASE_URL = "https://api.github.com"
GH_TOKEN = os.getenv("INPUT_GITHUB_TOKEN")
GH_REPO = os.getenv("INPUT_REPOSITORY")
PR_NUMBER = os.getenv("INPUT_PR_NUMBER")


def make_request(method: str, url: str, body: dict = None) -> int:
    """
    Method to make dynamic requests, in this case will be used for
    make requests to the github api with differents HTTP Methods.
    :param method: An HTTP Method
    :param url: The url to make the request
    :param body: A dictionary with the necessary data to send in body
    :return: The status code of the request.
    """
    format_token = f"token {GH_TOKEN}"

    headers = {
        "Accept": "vnd.github.v3+json",
        "Authorization": format_token
    }
    response = requests.request(
        method=method,
        url=url,
        json=body,
        headers=headers
    )
    
    return response.status_code


def get_modifications() -> int:
    """
    Method to get the additions and deletions from
    a pull request.
    :return: `int` Total additions + deletions.
    """
    modifications = 0

    url = f"{BASE_URL}/repos/{GH_REPO}/pulls/{PR_NUMBER}"

    response = make_request(
        method="GET",
        url=url
    )

    json_response = response.json()

    additions = json_response.get("additions", 0)
    deletions = json_response.get("deletions", 0)

    modifications = additions + deletions

    return modifications


def get_label(modifications: int) -> str:
    """
    Method to get the label based on the modifications
    :modifications: Total modifications number.
    :return: The label string.
    """
    # TODO: Improve this part

    if modifications <= 10:
        return "SIZE/XS"
    elif modifications > 10 and modifications <= 100:
        return "SIZE/S"
    elif modifications > 100 and modifications <= 250:
        return "SIZE/M"
    elif modifications > 250 and modifications <= 500:
        return "SIZE/L"
    elif modifications > 500 and modifications <= 1000:
        return "SIZE/XL"
    else:
        return "Pull Request too big, please split it."


def add_label(label: str) -> int:
    """
    Method to set a label to an specific pull request.
    :param label: The label to set.
    :return:
    """
    body = {
        "labels": [label]
    }

    url = f"{BASE_URL}/repos/{GH_REPO}/issues/{PR_NUMBER}"

    response = make_request(
        method="PATCH",
        url=url,
        body=body
    )

    return response.status_code


def main():
    """
    Main function that executes and is like an interface to interact with the other methods.
    """
    modifications = get_modifications()
    label = get_label(modifications)
    add_label(label)


if __name__ == "__main__":
    main()
