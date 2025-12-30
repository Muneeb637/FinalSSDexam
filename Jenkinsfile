pipeline {
    agent any
    
    parameters {
        // String parameter
        string(name: 'APP_VERSION', defaultValue: '1.0.0', description: 'Application version to build')
        
        // Choice parameter (dropdown)
        choice(name: 'ENVIRONMENT', choices: ['development', 'staging', 'production'], description: 'Target environment')
        
        // Boolean parameter (checkbox)
        booleanParam(name: 'RUN_TESTS', defaultValue: true, description: 'Run tests during build')
        
        // Text parameter (multi-line)
        text(name: 'BUILD_NOTES', defaultValue: '', description: 'Build notes or comments')
    }
    
    environment {
        // Build information
        BUILD_NUMBER = "${env.BUILD_NUMBER}"
        BUILD_ID = "${env.BUILD_ID}"
        BUILD_TIMESTAMP = "${new Date().format('yyyy-MM-dd HH:mm:ss')}"
        
        // Workspace information
        WORKSPACE_PATH = "${env.WORKSPACE}"
        
        // Use parameters in environment
        NODE_ENV = "${params.ENVIRONMENT}"
        APP_VERSION = "${params.APP_VERSION}"
        PYTHON_VERSION = '3.9'
    }
    
    options {
        // Keep only the last 10 builds
        buildDiscarder(logRotator(numToKeepStr: '10'))
        // Timeout after 10 minutes
        timeout(time: 10, unit: 'MINUTES')
    }
    
    stages {
        stage('Checkout') {
            steps {
                echo 'Checking out code from repository...'
                echo "Build Number: ${BUILD_NUMBER}"
                echo "Build Timestamp: ${BUILD_TIMESTAMP}"
                echo "Workspace: ${WORKSPACE_PATH}"
                echo "App Version: ${params.APP_VERSION}"
                echo "Environment: ${params.ENVIRONMENT}"
                checkout scm
            }
        }
        
        stage('Setup Python') {
            steps {
                echo 'Setting up Python environment...'
                bat '''
                    python --version
                    pip --version
                '''
            }
        }
        
        stage('Install Dependencies') {
            steps {
                echo 'Installing Python dependencies...'
                bat '''
                    pip install -r requirements.txt
                '''
            }
        }
        
        stage('Build') {
            steps {
                echo 'Building the Flask application...'
                echo "Environment: ${NODE_ENV}"
                echo "Build ID: ${BUILD_ID}"
                echo "Building version: ${params.APP_VERSION}"
                bat '''
                    echo Flask app structure verified
                    dir
                    python -m py_compile app.py
                '''
            }
        }
        
        stage('Test') {
            when {
                expression { params.RUN_TESTS == true }
            }
            steps {
                echo 'Running tests...'
                echo "Testing with Build Number: ${BUILD_NUMBER}"
                bat '''
                    pytest test_app.py -v --tb=short || python -m pytest test_app.py -v --tb=short
                '''
            }
            post {
                always {
                    echo 'Test stage completed'
                }
            }
        }
        
        stage('Archive') {
            steps {
                echo 'Archiving build artifacts...'
                echo "Archiving from: ${WORKSPACE_PATH}"
                echo "Version: ${params.APP_VERSION}"
                archiveArtifacts artifacts: '*.py', fingerprint: true
                archiveArtifacts artifacts: 'requirements.txt', fingerprint: true
            }
        }
    }
    
    post {
        always {
            echo 'Pipeline completed. Cleaning up...'
            echo "Final Build Number: ${BUILD_NUMBER}"
            echo "Build Notes: ${params.BUILD_NOTES}"
        }
        success {
            echo 'Pipeline succeeded! ✅'
        }
        failure {
            echo 'Pipeline failed! ❌'
        }
    }
}
