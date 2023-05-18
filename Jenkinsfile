def dockerHubRegistry = "docker.io"

pipeline {
    agent any

    environment {
        DOCKER_USER_ID = credentials('jinh9015').username
        DOCKER_USER_PASSWORD = credentials('jinh9015').password
    }

    stages {
        stage('Clone Repository') {
            steps {
                checkout([$class: 'GitSCM',
                          branches: [[name: '*/main']],
                          userRemoteConfigs: [[url: 'https://github.com/jinh9015/jenkinstest.git']]])
            }
        }
        
        stage('Build and Push Docker Image') {
            steps {
                dir('jenkinstest') {
                    withCredentials([usernamePassword(credentialsId: 'jinh9015', usernameVariable: 'DOCKER_USER_ID', passwordVariable: 'DOCKER_USER_PASSWORD')]) {
                        script {
                            sh "docker login -u ${DOCKER_USER_ID} -p ${DOCKER_USER_PASSWORD} ${dockerHubRegistry}"
                            sh "docker-compose -f docker-compose.yaml build"
                            sh "docker tag jinh9015/jenkinstest:${env.BUILD_NUMBER} ${dockerHubRegistry}/jinh9015/jenkinstest:${env.BUILD_NUMBER}"
                            sh "docker push ${dockerHubRegistry}/jinh9015/jenkinstest:${env.BUILD_NUMBER}"
                        }
                    }
                }
            }
        }
    }
}

