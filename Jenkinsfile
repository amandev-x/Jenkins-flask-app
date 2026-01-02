pipeline {
    agent any 
    // options {
    //     skipDefaultCheckout true
    // }
    stages {
        // Checkout Stage
        stage("Checkout Code") {
            environment {
            DB_ADDRESS = "192.168.1.9"
            USERNAME = "DB_USER_1"
            }

            steps {
                // sh "git clone https://github.com/amandev-x/Jenkins-flask-app.git"
                echo "The IP Address of the DB is ${DB_ADDRESS} and username is ${USERNAME}"
            }
        }

        stage("Build Stage") {
            steps {
                echo "Building the application..."
                echo "The IP Address of the DB is ${DB_ADDRESS} and username is ${USERNAME}"
            }
        }

        // // Build Stage
        // stage() 
    }
}