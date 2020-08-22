pipeline {
    agent any 
    stages{
        stage('Install Docker'){
            steps{
                sh './scripts/install_docker.sh'
            }        
        }
        stage('Test services'){
            steps{
                sh 'echo "This is where we will test"'
            }
        }
        stage('Deploy services'){
            steps{
                sh './scripts/deploy.sh'
            }
        }
    }
                   
}
