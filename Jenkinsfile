pipeline {
    agent any 
    // options {
    //     timeout(time: 1, unit: 'MINUTES')
    // }

    parameters{
        string(name: 'ENVIRONMENT', defaultValue: 'dev', description: "Value for the Environment")
        booleanParam(name: 'RUN_TESTS', defaultValue: false, description: "Boolean value to run tests")
    }

    environment {
        DB_ADDRESS = "192.168.1.9"
        USERNAME = "DB_USER_1"
        // SERVER_CREDS = credentials('server_creds')
        }
    // options {
    //     skipDefaultCheckout true
    // }
    stages {
        // Checkout Stage
        stage("Checkout Code") {
            steps {
                // sh "git clone https://github.com/amandev-x/Jenkins-flask-app.git"
                echo "The IP Address of the DB is ${DB_ADDRESS} and username is ${USERNAME}"
                // echo "My Creds: ${SERVER_CREDS}"
                // echo "Username: ${SERVER_CREDS_USR}"
                // echo "Password: ${SERVER_CREDS_PSW}"
                withCredentials([usernamePassword(
                    credentialsId: "server_creds",
                    usernameVariable: "myusername",
                    passwordVariable: "mypassword"
                )])
                {
                    sh '''
                    echo "Username is ${myusername}"
                    echo "Password is ${mypassword}"                   
                    '''
                }
            }
        }

        // Nesting stages
        stage('Lint') {
                    steps {
                       echo "Linting code"
                    }
        }

        stage('Test'){
            when {
                expression {
                    params.RUN_TESTS == true
                }
            }

            steps {
                echo "Running tests"
            }
        }

        stage("Build Stage") {
            steps {
                echo "Building the application..."
                echo "Commit: ${env.GIT_COMMIT}"
            }
        }

        stage("Paramters") {
            steps {
                echo "Running in ${params.ENVIRONMENT} environment"
            }
        }

        // // Build Stage
        // stage() 
    }
}