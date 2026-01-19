
pipeline {
    agent any

    options {
        // Stop runaway builds
        timeout(time: 15, unit: 'MINUTES')
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Set up Python venv') {
            steps {
                sh '''
                    set -e
                    python3 -m venv .venv
                    . .venv/bin/activate
                    python -m pip install --upgrade pip
                    pip install -r requirements.txt
                '''
            }
        }

        stage('Run tests') {
            steps {
                sh '''
                    set -e
                    . .venv/bin/activate
                    pytest --junitxml=test-results.xml -q
                '''
            }
        }
    }

    post {
        always {
            // Show test results in Jenkins UI (if plugin available)
            junit allowEmptyResults: true, testResults: 'test-results.xml'
            // Keep logs/reports
            archiveArtifacts artifacts: 'test-results.xml', onlyIfSuccessful: false
        }
    }
}



