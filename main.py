from EmployeeFile import Employee
import pytest
import requests
def test_method():
    pageNumber = 1
    URL = "https://reqres.in/api/users?page="
    data = requests.get(URL + str(pageNumber)).json()
    total = data["total"]
    dataList = []
    while data["data"]:
        for i in range(len(data["data"])):
            dataList.append(Employee(int(data["data"][i]["id"]), data["data"][i]["email"],
                                     data["data"][i]["first_name"], data["data"][i]["last_name"],
                                     data["data"][i]["avatar"]))
        pageNumber = pageNumber + 1
        data = requests.get(URL + str(pageNumber)).json()
    assert len(dataList) == total+1, "there is a bug in your method"
