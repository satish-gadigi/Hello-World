# app.py
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, World from automation using below scenarios /n
This has been implemented by using my Mobile and PC. My PC has low configuration machine to implement devops so I am using my mobile which is high configurations to install Jenkins. Docker and Kubernetes can't run in mobile because docker build needs real linux kernal. So I have installed Docker and kuberenetes which ever require full linux support and these can be handled by machine with little slowness. /n

In Mobile:

1) Installed Termux(Mobile acts as linux machine with limited features).  
2) Inside Termux, installed open ssh so that i can access PC from mobile. /n
3) Installed jenkins and configured Nodes(with my PC wifi ip and linux credentials) and Pipeline  /n

In PC:

1) Since My PC is Windos, I have enabled WSL2 which acts as linux in windows.
2) Installed all required tools and softwares like ssh,java,git,docker,kubernetes(docker compose) etc
3) Write or pull Source code in PC built using docker then push to docker hub, finally run the docker to see outuput in local browser.

Steps:
    Write Jenkinsfile along with your source code in PC. Configure the jenkins pipeline (access jenkins in your mobile or in PC with ip)
Once the pipeline started to build, Initially connects the Node(PC) and then run Jenkinsfile steps. Steps includes that, 
pull code from git hub in PC's configured location
|
Builds the code
|
Docker hub login and Push the docker image to docker hub
|
Docker run
|
Access the app in local broser

This is how CI has been implemented except automatic trigger.


Next steps:
___________

-> Automatic integration setup while pushing the changes to github
-> Continuous Deploy

"
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
