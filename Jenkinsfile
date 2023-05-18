pipeline {
    agent none

    stages {
        stage('Run Docker Build') {
            agent {
                kubernetes {
                    defaultContainer 'jnlp'
                    yaml """
                        apiVersion: v1
                        kind: Pod
                        metadata:
                          labels:
                            jenkins/jenkins-jenkins-agent: "true"
                            jenkins/label: "docker-build"
                          name: "docker-build-pod"
                          namespace: "jenkins"
                        spec:
                          containers:
                            - name: 'git'
                              image: 'alpine/git'
                              command: ['cat']
                              tty: true
                            - name: 'docker'
                              image: 'docker'
                              command: ['cat']
                              tty: true
                            - name: 'jnlp'
                              image: 'jenkins/inbound-agent:4.11-1'
                              args: ['$(JENKINS_URL)', '$(JENKINS_SECRET)', 'docker-build-pod']
                              resources:
                                requests:
                                  cpu: '100m'
                                  memory: '256Mi'
                              volumeMounts:
                                - mountPath: '/var/run/docker.sock'
                                  name: 'docker-sock'
                                - mountPath: '/home/jenkins/agent'
                                  name: 'workspace-volume'
                          volumes:
                            - name: 'docker-sock'
                              hostPath:
                                path: '/var/run/docker.sock'
                            - name: 'workspace-volume'
                              emptyDir: {}
                    """
                }
            }

            stages {
                stage('Setup') {
                    steps {
                        container('git') {
                            sh 'apk add --no-cache git'
                        }
                        container('docker') {
                            sh 'service docker start'
                            sleep 10
                            sh 'docker network create my-bridge-network'  // 네트워크 이름을 변경하여 생성
                        }
                    }
                }

                stage('Checkout') {
                    steps {
                        container('git') {
                            checkout scm
                        }
                    }
                }

                stage('Build') {
                    steps {
                        container('docker') {
                            script {
                                def appImage = docker.build("jinh9015/jenkinstest")
                            }
                        }
                    }
                }

                stage('Test') {
                    steps {
                        container('docker') {
                            script {
                                appImage.inside {
                                    sh 'npm install'
                                    sh 'npm test'
                                }
                            }
                        }
                    }
                }

                stage('Push') {
                    steps {
                        container('docker') {
                            script {
                                docker.withRegistry('https://registry.hub.docker.com', dockerHubCred) {
                                    appImage.push("${env.BUILD_NUMBER}")
                                    appImage.push("latest")
                                }
                            }
                        }
                    }
                }
            }
        }
    }
}

