from net.grinder.script import Test
from net.grinder.script.Grinder import grinder
from net.grinder.plugin.http import HTTPRequest
from org.json import JSONObject

user_id = 1
request = HTTPRequest(url="https://reqres.in")
test = Test(1, "Get User By Id").record(request)

class TestRunner:
    def __init__(self):
        grinder.statistics.delayReports=True

    def __call__(self):
        response = request.GET("/api/users/"+ str(user_id))
        jo = JSONObject(response.text)
        id = jo.getJSONObject("data").getInt("id")

        if id != user_id: 
            grinder.statistics.forLastTest.success = 0 
            grinder.logger.error("User ID is not valid: " + id)

    