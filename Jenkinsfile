pipeline {
    agent any 

    environment{
        MYSQL_ROOT_PASSWORD = credentials('MYSQL_ROOT_PASSWORD')
       
    }

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
        stage('Save artifact'){
            steps{
                sh './scripts/artifact.sh'
            }
        }
    }
                   
}
