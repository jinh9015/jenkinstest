def component = [
    Preprocess: true,
    Hyper: true,
    Train: true,
    Test: true,
    Bento: true
]

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
                    component.each { entry ->
                        stage("${entry.key} Build") {
                            if (entry.value) {
                                def var = entry.key
                                sh "docker-compose build ${var.toLowerCase()}"
                            }
                        }
                    }
                }
            }
        }

        stage("Tag and Push") {
            steps {
                script {
                    component.each { entry ->
                        stage("${entry.key} Push") {
                            if (entry.value) {
                                def var = entry.key
                                withCredentials([usernamePassword(
                                    credentialsId: 'jinh9015',
                                    usernameVariable: 'DOCKER_USER_ID',
                                    passwordVariable: 'DOCKER_USER_PASSWORD'
                                )]) {
                                    sh "docker tag spaceship_pipeline_${var.toLowerCase()}:latest ${DOCKER_USER_ID}/spaceship_pipeline_${var.toLowerCase()}:${BUILD_NUMBER}"
                                    sh "docker login -u ${DOCKER_USER_ID} -p ${DOCKER_USER_PASSWORD}"
                                    sh "docker push ${DOCKER_USER_ID}/spaceship_pipeline_${var.toLowerCase()}:${BUILD_NUMBER}"
                                }
                            }
                        }
                    }
                }
            }
        }
    }
}

