pipeline {
    agent { label 'lbl_agent_node' }

    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/satish-gadigi/Practice.git'
            }
        }

        stage('Build') {
            steps {
                sh 'docker build -t satishri/practice:${BUILD_NUMBER} .'
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
                    sh 'docker tag satishri/practice:${BUILD_NUMBER} satishri/practice:latest'
                    sh 'docker push satishri/practice:latest'
                }
            }
        }
    }
}
