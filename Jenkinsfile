pipeline {
    agent any 
    stages{
        stage('Install Docker'){
            steps{
                sh './scripts/ansible.sh'
            }        
        }
        stage('Test services'){
            steps{
                sh './scripts/test_services.sh'
            }
        }
        stage('Export Variables'){
            steps{
                sh './scripts/URI.sh'
            }
        }
        stage('Deploy services'){
            steps{
                sh './scripts/deploy.sh'
            }
        }
        stage('Update nodes as needed'){
            steps{
                sh 
            }
        }
        stage('Save artifact'){
            steps{
                sh './scripts/artifact.sh'
            }
        }
    }
                   
}
