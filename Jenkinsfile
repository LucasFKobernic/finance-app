
pipeline {
    agent {
        docker {
            image 'python:3.11-slim'   // or 3.12-slim
            args '-u root'             // lets us install system deps if needed
        }
    }

    stages {
        stage('Checkout') {
            steps { checkout scm }
        }

        stage('Install deps') {
            steps {
                sh '''
                  pip install --upgrade pip
                  pip install -r requirements.txt
                '''
            }
        }

        stage('Test') {
            steps {
                sh 'pytest --junitxml=test-results.xml'
            }
            post {
                always {
                    junit 'test-results.xml'
                }
            }
        }
    }
}

