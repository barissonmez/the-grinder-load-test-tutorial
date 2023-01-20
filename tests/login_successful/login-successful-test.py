from net.grinder.script import Test
from net.grinder.script.Grinder import grinder
from net.grinder.plugin.http import HTTPRequest
from HTTPClient import NVPair
from org.json import JSONObject
from java.lang import System

user_login_token = "QpwL5tke4Pnpja7X4"
request = HTTPRequest(url="https://reqres.in")
test = Test(2, "Login Successful").record(request)

class TestRunner:
    def __init__(self):
        grinder.statistics.delayReports=True

    def __call__(self):

        headers = [
            NVPair("Content-Type", "application/json"),
            NVPair('Charset', 'UTF-8'),
        ]

        payload = JSONObject({"email": "eve.holt@reqres.in", "password": "cityslicka"})

        response = request.POST("/api/login", str(payload), headers)
        
        jo = JSONObject(response.text)
        token = jo.getString("token")

        if token != user_login_token: 
            grinder.statistics.forLastTest.success = 0 
            grinder.logger.error("Token is not valid: " + token)
    