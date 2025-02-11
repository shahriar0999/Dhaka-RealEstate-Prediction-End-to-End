pipeline {
    agent any

    stages {
        stage('Checkout code') {
            steps {
                git url: "https://github.com/shahriar0999/end-to-end-house-price-prediction-dhaka.git", branch: "main"
                sh "ls -ltr"
                echo "successfully cloning the project repo"
            }
        }
        
        stage("Set Environment") {
            steps {
                sh "python3 -m pip install --break-system-packages -r requirements.txt"
                echo "✅ Successfully installed all required packages"
            }
        }
        
        stage("Test") {
            steps {
                sh "python3 -m pip install pytest"
                sh "pytest tests/test_main.py"
                echo "✅ Successfully passed all tests!"
            }
        }
    }
}
