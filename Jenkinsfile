pipeline {
    agent any

    stages {
        stage("Checkout") {
            steps {
                checkout scm
            }
        }

        stage("Build") {
            steps {
                script {
                    // Docker 빌드 실행
                    sh "docker build -t jinh9015/jenkinstest ."
                }
            }
        }

        stage("Tag and Push") {
            steps {
                withCredentials([usernamePassword(
                    credentialsId: 'DockerHub',
                    usernameVariable: 'DOCKER_USER_ID',
                    passwordVariable: 'DOCKER_USER_PASSWORD'
                )]) {
                    script {
                        env.DOCKER_USER_ID = DOCKER_USER_ID
                        env.DOCKER_USER_PASSWORD = DOCKER_USER_PASSWORD
                        sh 'docker tag jinh9015/jenkinstest:latest $DOCKER_USER_ID/jenkinstest:$BUILD_NUMBER'
                        sh 'docker login -u $DOCKER_USER_ID -p $DOCKER_USER_PASSWORD'
                        sh 'docker push $DOCKER_USER_ID/jenkinstest:$BUILD_NUMBER'
                    }
                }
            }
        }
    }
}

