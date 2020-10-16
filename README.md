# ciandt-challenge-python

#### A challenge to develop a Python API inside a Docker container responsible for manipulating a .txt file

---

## Overview:

The HR opens a request to IT for a creation of entries whenever an employee is hired or leaves the company. These entries interact with the payment system to update the information and are written in a text file.

This project consists in a development of a Python API responsible for writing lines in this text file, automating the process and saving time. A Shell Script to create and remove users on Linux also should be developed.

## Requirements:

* Python 3
* Flask
* uWSGI
* Docker
* Shell Script
* Linux

## API Design [app.py]:


The API receives the following information from the frontend: 

* Action (ADD or DISABLE)
* Name
* Login
* Password (encrypted in Base64)

With this information provided, the API should write to the data.txt file a line with the following pattern:

###### ADD EMPLOYEE:
```
ADD "Full name", "login", "password"
```
###### OR

###### REMOVE EMPLOYEE:
```
DISABLE "login"
```
The password must be decrypted in the data.txt file.

The text file may have multiple lines in the end of the day.

Some validations are required:

* The login cannot repeat on the same day (same text file), even with different actions (add/disable).
* Password must contain at least 10 characters
* Password must contain at least a number
* Password must contain at least a lowercase letter
* Password must contain at least an uppercase letter
* Error messages should be displayed in case of failures in the data validation

## Shell Script Design [user_import.sh]:

Read the data from the data.txt file and add or remove the respective users of each line in the Linux OS.

###### ADD USER:

```
sudo useradd -c FULL_NAME -m LOGIN_ID -p PASSWORD_ENCRYPTED_MD5
```

###### DEL USER:

```
sudo userdel -rf LOGIN_ID
```

The script should also rename the data.txt file to YYYYMMDD.bak after running the process above.

## Setup:
Create the path /scripts/python/ in the Linux host machine and place user_import.sh inside it:
```
sudo mkdir -p /scripts/python
```

To build the Docker image from a Dockerfile:
```
docker build -t ciandt-python-challenge .
```

To run this container after building the image:
```
docker run -d -p 8080:8080 -v /scripts/python:/scripts/python ciandt-python-challenge
```

It's recommended to use Postman to simulate the requests in the port 8080, but the command "curl" should work as well.

The API will generate the data.txt file in the folder /scripts/python/ where is accessible from the host machine.
