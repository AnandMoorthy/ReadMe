#!groovy

node {
  try {
    stage 'Test'
      sh 'source /home/anand/Dev/virtual_env/readme/bin/activate'

    stage 'Deploy'
      sh 'python manage.py makemigraions'
      sh 'python manage.py migrate'
  }
  catch (err) {
    sh 'echo "Error Occured By Anand"'
  }
}
