pipeline{
    agent any
    stages{
        stage('Build'){
            steps{
                echo 'Build Docker Image'
                bat "docker build -t mypythonflaskapp ."
            }
        }
        stage('Run'){
            steps{
                echo 'Run application in Docker Container'
                bat "docker rm -f mycontainer || exit 0"
                //forcibly removes the Docker container named mycontainer
                //if the container doesnot exist,this command will fail and 
                bat "docker run -d -p 5050:5050 --name mycontainer mypythonflaskapp"
            }
        }
    }
    post{
        success{
            echo 'Pipeline completed successfully!'
        }
        failure{
            echo 'Pipeline failed.please check the logs.'
        }
    }
}