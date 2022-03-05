pipeline {
    agent any
    stages {
        stage('Building') {
            steps {
                bat "docker-compose build"
            }
        }
        stage('Pushing into Release') {
            steps {
                git([url:'https://github.com/Tr4hern/Data_Engineering.git/',branch:'release'])
            bat "git push origin release"
            }
        }
    }
}