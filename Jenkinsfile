pipeline {
    agent { label "crown" }
    environment {
        USERNAME= 'crownai'
        IMAGE_TAG = "${USERNAME}${env.BUILD_NUMBER}"
    }

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
                sh "apt install -y python3-pip"
                sh "apt install python3.12-venv"
                sh "python3 -m venv venv"
                sh ". venv/bin/activate && python3 -m pip install --upgrade pip && pip install -r requirements.txt"
                echo "✅ Successfully installed all required packages"
            }
        }
        
        stage("Test") {
            steps {
                sh ". venv/bin/activate && pytest tests/test_main.py"
                echo "✅ Successfully passed all tests!"
            }
        }

        stage('Login to docker hub') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'docker-cred', usernameVariable: 'DOCKERHUB_USERNAME', passwordVariable: 'DOCKERHUB_PASSWORD')]) {
                    sh "echo ${DOCKERHUB_PASSWORD} | docker login -u ${DOCKERHUB_USERNAME} --password-stdin"} 
                    echo 'Login successfully'
            }
        }

        stage("Build Docker Images") {
            steps {
                script{
                    // Build both FastAPI and Streamlit app images
                    sh """
                        docker-compose build
                        docker tag fastapi:latest $USERNAME/fastapi-app:$IMAGE_TAG
                        docker tag streamlit:latest $USERNAME/streamlit-app:$IMAGE_TAG
                    """
                }
            }
        }

        stage("Push Docker Images") {
            steps {
                sh "docker push $USERNAME/fastapi-app:$IMAGE_TAG"
                sh "docker push $USERNAME/streamlit-app:$IMAGE_TAG"
            }
        }

        stage('Pull Docker Images') {
            steps {
                sh "docker pull $USERNAME/fastapi-app:$IMAGE_TAG"
                sh "docker pull $USERNAME/fastapi-app:$IMAGE_TAG"
            }
        }

        stage("Run Docker Containers") {
            steps {
                sh 'docker-compose down'
                sh "docker-compose up -d"
            }
        }
    }
}
