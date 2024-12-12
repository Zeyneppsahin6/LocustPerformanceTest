from locust import HttpUser, between, task


class WebsiteUser(HttpUser):
    wait_time = between(5, 15)

    @task
    def UserCreate(self):
        bodyPayLoad = {
          "id": 1234567,
          "username": "Zeynep2",
          "firstName": "Zeynep2",
          "lastName": "Şahin2",
          "email": "zeynepsahin@icloud.com",
          "password": "Abcdef123!2",
          "phone": "05378564326",
          "userStatus": 0
        }
        self.client.post("/v2/user", json=bodyPayLoad)

    @task
    def getUserInfo(self):
        self.client.get("/v2/user/zeynep3")

    @task
    def UserDelete(self):
        self.client.delete("/v2/user/Zeynep2")

    @task
    def UserUpdate(self):
        bodyPayLoad = {
          "id": 23422354,
          "username": "zeynep3",
          "firstName": "zeynep3",
          "lastName": "sahin3",
          "email": "zeynep@gmail.com",
          "password": "abc123xxx",
          "phone": "05346284928",
          "userStatus": 1
        }
        self.client.put("/v2/user/zeynep3", json=bodyPayLoad)
