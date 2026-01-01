pipeline {
    agent { label 'lbl_agent_node' }

    stages {
        stage('Checkout') {
            steps {

        checkout([$class: 'GitSCM',
            branches: [[name: '*/main']],
            userRemoteConfigs: [[url: 'https://github.com/satish-gadigi/Hello-World.git']]
        ])
    }
}
               // git 'https://github.com/satish-gadigi/Hello-World.git'
            
        

        stage('Build') {
            steps {
                sh 'docker build -t satishri/hello-world:${BUILD_NUMBER} .'
            }
        }

        stage('Push') {
            steps {
                withCredentials([usernamePassword(
                    credentialsId: 'dockerhub-creds',
                    usernameVariable: 'DOCKER_USER',
                    passwordVariable: 'DOCKER_PASS'
                )]) {
                    sh 'echo $DOCKER_PASS | docker login -u $DOCKER_USER --password-stdin'
                    sh 'docker tag satishri/hello-world:${BUILD_NUMBER} satishri/hello-world:latest'
                    sh 'docker push satishri/hello-world:latest'
                }
            }
        }
    }
}
