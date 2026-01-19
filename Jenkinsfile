
pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Set up Python') {
            steps {
                sh """
                python3 -m venv venv
                . venv/bin/activate
                pip install --upgrade pip
                pip install -r requirements.txt
                """
            }
        }

        stage('Run Tests with pytest') {
            steps {
                sh """
                . venv/bin/activate
                pytest --junitxml=test-results.xml
                """
            }
            post {
                always {
                    junit 'test-results.xml'
                }
            }
        }
    }
}
