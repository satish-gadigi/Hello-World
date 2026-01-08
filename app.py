# app.py
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return """Hello, World from automation using below scenarios \n
This has been implemented by using my Mobile and PC. My PC has low configuration machine to implement devops so I am using my mobile which is high configurations to install Jenkins. Docker and Kubernetes can't run in mobile because docker build needs real linux kernal. So I have installed Docker and kuberenetes which ever require full linux support and these can be handled by machine with little slowness. \n\n

In Mobile:\n\n

1) Installed Termux(Mobile acts as linux machine with limited features).  \n
2) Inside Termux, installed open ssh so that i can access PC from mobile. \n
3) Installed jenkins and configured Nodes(with my PC wifi ip and linux credentials) and Pipeline  \n

In PC: \n\n

1) Since My PC is Windos, I have enabled WSL2 which acts as linux in windows. \n
2) Installed all required tools and softwares like ssh,java,git,docker,kubernetes(docker compose) etc\n
3) Write or pull Source code in PC built using docker then push to docker hub, finally run the docker to see outuput in local browser.\n\n

Steps:\n
    Write Jenkinsfile along with your source code in PC. Configure the jenkins pipeline (access jenkins in your mobile or in PC with ip)
Once the pipeline started to build, Jenkinsfiles triggered then executes the stages as per the below stages. \n\n

Initially connects the Node(PC) \n
|\n
pull code from git hub in PC's configured location\n
|\n
Builds the code\n
|\n
Docker hub login and Push the docker image to docker hub\n
|\n
Docker run\n
|\n
Access the app in local broser\n\n

This is how CI has been implemented except automatic trigger.\n\n\n


Next steps:\n
___________\n\n

-> Automatic integration setup while pushing the changes to github\n
Status:Implemented in this change\n\n

-> Continuous Deploy\n
Status: Yet to start\n\n

======
=========================================================================================================================================\n
Faced ssh issues in my PC so switched to PC only mode, excluding mobile setup from here onwards. Installed Jenkins in my PC and implementing now whole setup in PC \n"""

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
