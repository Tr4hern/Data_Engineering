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
                git([url:'https://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@github.com/Tr4hern/Data_Engineering.git/',branch:'release'])
            bat "git push origin release"
            }
        }
    }
}