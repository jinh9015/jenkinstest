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
                    // Docker 설치 확인
                    def dockerInstallation = tool 'docker'
                    if (dockerInstallation == null) {
                        dockerInstallation = tool(name: 'docker', type: 'org.jenkinsci.plugins.docker.commons.tools.DockerTool')
                    }

                    // Docker 설치
                    if (dockerInstallation == null) {
                        def dockerTool = 'docker'
                        def dockerVersion = 'latest'
                        def dockerHome = env.WORKSPACE + '/.docker'
                        def dockerUrl = "https://get.docker.com/"

                        dockerInstallation = dockerTool.installations.find {
                            it.getName() == dockerTool && it.getProperties().get("DockerInstallationDescriptor").getHome() == dockerHome
                        }

                        if (dockerInstallation == null) {
                            dockerInstallation = dockerTool.installations.find {
                                it.getName() == dockerTool
                            }
                        }

                        if (dockerInstallation == null) {
                            dockerInstallation = dockerTool.installations.find {
                                it.getProperties().get("DockerInstallationDescriptor").getHome() == dockerHome
                            }
                        }

                        if (dockerInstallation == null) {
                            dockerInstallation = dockerTool.installations.find {
                                it.getProperties().get("DockerInstallationDescriptor").getUrl() == dockerUrl
                            }
                        }

                        if (dockerInstallation == null) {
                            dockerInstallation = dockerTool.installations.find {
                                it.getProperties().get("DockerInstallationDescriptor").getVersion() == dockerVersion
                            }
                        }

                        if (dockerInstallation == null) {
                            def installer = new DockerInstaller(dockerTool)
                            installer.install()
                            dockerInstallation = dockerTool.installations.find {
                                it.getName() == dockerTool
                            }
                        }
                    }

                    // Docker 빌드 실행
                    sh "${dockerInstallation}/bin/docker build -t jinh9015/jenkinstest ."
                }
            }
        }

        stage("Tag and Push") {
            steps {
                withCredentials([usernamePassword(
                    credentialsId: 'jinh9015',
                    usernameVariable: 'DOCKER_USER_ID',
                    passwordVariable: 'DOCKER_USER_PASSWORD'
                )]) {
                    script {
                        sh "docker tag jinh9015/jenkinstest:latest ${DOCKER_USER_ID}/jenkinstest:${BUILD_NUMBER}"
                        sh "docker login -u ${DOCKER_USER_ID} -p ${DOCKER_USER_PASSWORD}"
                        sh "docker push ${DOCKER_USER_ID}/jenkinstest:${BUILD_NUMBER}"
                    }
                }
            }
        }
    }
}

