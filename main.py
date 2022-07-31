from EmployeeFile import Employee
import pytest
import requests
def test_validate_total_number_with_returned_data():
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
    assert len(dataList) == total, "there is a bug in your method"
def testPostUser():
    data = {
            "name": "morpheus",
            "id": "358",
            }
    URL = "https://reqres.in/api/users"
    response = requests.post(URL, data)
    getStatusCode = response.status_code
    assert getStatusCode == 201, "operation create failed"
    getName = response.json()
    assert data["name"] == getName["name"], "there is a problem with sending data"
# check respinse 201
# check name exists in response
    getSingleUserURL = "https://reqres.in/api/users/"+data["id"]
    response = requests.get(getSingleUserURL).status_code
    assert response != 404, "the post operation fail"
