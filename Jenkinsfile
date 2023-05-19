pipeline {
    agent any

    stages {
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
                ), usernamePassword(
                    credentialsId: 'github_token',
                    usernameVariable: 'GITHUB_USERNAME',
                    passwordVariable: 'GITHUB_TOKEN'
                )]) {
                    script {
                        env.DOCKER_USER_ID = DOCKER_USER_ID
                        env.DOCKER_USER_PASSWORD = DOCKER_USER_PASSWORD
                        env.GITHUB_USERNAME = GITHUB_USERNAME
                        
                        // k8s-manifest-repo 디렉토리가 이미 존재하는지 확인 후 삭제
                        def workspacePath = "${env.WORKSPACE}/k8s-manifest-repo"
                        if (fileExists(workspacePath)) {
                            sh "rm -rf ${workspacePath}"
                        }
                        
                        // Git 레파지토리 클론
                        git branch: 'main', url: 'https://github.com/jinh9015/k8s-manifest-repo.git'
                        
                        // deployment.yaml 템플릿 파일 로드
                        def deploymentTemplatePath = "${workspacePath}/deployment.yaml.template"
                        def deploymentTemplate = readFile(deploymentTemplatePath)
                        
                        // 이미지 태그 동적으로 적용
                        def updatedDeploymentYaml = deploymentTemplate.replaceAll('\\$DOCKER_USER_ID', DOCKER_USER_ID)
                                                                     .replaceAll('\\$BUILD_NUMBER', BUILD_NUMBER)
                        
                        // 동적으로 생성한 deployment.yaml 파일 저장
                        def deploymentYamlPath = "${workspacePath}/deployment.yaml"
                        writeFile(file: deploymentYamlPath, text: updatedDeploymentYaml)
                        
                        // 업데이트된 파일을 레파지토리에 커밋하고 푸시
                        dir(workspacePath) {
                            sh 'git add deployment.yaml'
                            sh 'git commit -m "Update deployment.yaml"'
                            sh 'git push origin main'
                        }
                    }
                }
            }
        }
    }
}

