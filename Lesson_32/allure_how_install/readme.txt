In addition to installed plugin and  pytest module
You need to go "Manage Jenkins" -> "Tools"
Click there "Add Allure Commandline" and type "allure" into "Name" field
Then apply config

After job run you will see in logs smth like
#-----------------
...
[Pipeline] allure
Unpacking https://repo1.maven.org/maven2/io/qameta/allure/allure-commandline/2.27.0/allure-commandline-2.27.0.zip to /var/jenkins_home/tools/ru.yandex.qatools.allure.jenkins.tools.AllureCommandlineInstallation/allure on Jenkins
...

#--------------------