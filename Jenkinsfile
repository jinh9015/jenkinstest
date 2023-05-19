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
                        
                        // deployment.yaml 템플릿 파일 로드
                        def deploymentTemplatePath = "${env.WORKSPACE}/k8s-manifest-repo/deployment.yaml.template"
                        def deploymentTemplate = readFile(deploymentTemplatePath)
                        
                        // 이미지 태그 동적으로 적용
                        def updatedDeploymentYaml = deploymentTemplate.replaceAll('\\$DOCKER_USER_ID', DOCKER_USER_ID)
                                                                     .replaceAll('\\$BUILD_NUMBER', BUILD_NUMBER)
                        
                        // 동적으로 생성한 deployment.yaml 파일 저장
                        def deploymentYamlPath = "${env.WORKSPACE}/k8s-manifest-repo/deployment.yaml"
                        writeFile(file: deploymentYamlPath, text: updatedDeploymentYaml)
                        
                        // 레파지토리에 변경 사항을 커밋하고 푸시
                        dir("${env.WORKSPACE}/k8s-manifest-repo") {
                            sh 'git add deployment.yaml'
                            sh 'git commit -m "Update deployment.yaml"'
                            sh 'git push'
                        }
                    }
                }
            }
        }
    }
}

