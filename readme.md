# The Grinder Load Test Tutorial

Hi there! This is a tutorial with the purpose of giving a try to the  [Grinder Load Testing Framework](https://cossme.github.io/grinder/guide/getting-started.html) 

The project performs load tests on the **"SINGLE USER"** and **"LOGIN-SUCCESSFUL"** API endpoints on https://reqres.in

## Prerequisites
- **Java Installation**
	- Check if Java is installed on your machine:
	- Open **Command Prompt** and run `java --version`
	- If Java is not installed on your machine then download and install it from the link below:
https://www.java.com/en/download/
- **Grinder Installation**
	- Download the latest(4.0.0) GRINDER binary release from github via the link below:
https://github.com/cossme/grinder/releases/download/4.0.0/grinder-4.0.0-binary.zip
	- Extract `grinder-4.0.0-binary.zip` and move`grinder-4.0.0` folder into **`C:`** drive
	- You can take a look at the project in its GitHub Repository:
https://github.com/cossme/grinder
- **`JSON in Java(package org.json)` Library Installation**
	- [`JSON in Java (package org.json)`](https://github.com/stleary/JSON-java) library is required for dealing with JSON data.
	- Download [**`json-20220924.jar`**](https://repo1.maven.org/maven2/org/json/json/20220924/json-20220924.jar) file and move it into **`C:\grinder-4.0.0\lib`** folder in your system.
## Downloading And Running The Project in Windows
- Download and extract project folder.
- Open the folder and double click `start.cmd` file.
- If everyting is OK and there is no error on openning CMD windows; 
	- Go to [**`http://localhost:6373`**](http://localhost:6373) in your browser for "Web Console" UI. 
	- Go to **`Agents`** view and you have to see that 2 agents are running.
	- Go back to the **`Results`** view and click run button for starting load tests. 
		- On first click you may get an error message about distributed files but ignore it and click the run button again.
		
	- You can check the test results and reports on the UI.