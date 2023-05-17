def component = [
    Preprocess: false,
    Hyper: false,
    Train: false,
    Test: false,
    Bento: false
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
                                def dockerUserId = "jinh9015"
                                def dockerUserPassword = "jcha1855()"
                                sh "docker tag ${var.toLowerCase()}:latest ${dockerUserId}/spaceship_pipeline_${var.toLowerCase()}:${BUILD_NUMBER}"
                                sh "docker login -u ${dockerUserId} -p ${dockerUserPassword}"
                                sh "docker push ${dockerUserId}/${var.toLowerCase()}:${BUILD_NUMBER}"
                            }
                        }
                    }
                }
            }
        }
    }
}

