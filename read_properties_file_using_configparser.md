# How to read properties file in Python using configparser?

Sample Property file
First of all we will create a sample property file and add the properties. Here is sample example of properties file:

# Database Configuration

[db]
db_url=jdbc:mysql://localhost:3308/mydb
user=root
password=mypass

Here is the screen  shot of the properties file:

![image](https://user-images.githubusercontent.com/18412583/194212428-075b794c-d443-46d4-b3eb-09812a254100.png)

Installing configparser
```
pip install configparser
```

Reading properties file in Python using configparser
```
import configparser

config = configparser.ConfigParser()
config.read('db.properties')

db_url=config.get("db", "db_url")
user=config.get("db", "user")
password=config.get("db", "password")

print(db_url)
print(user)
print(password)
```

![image](https://user-images.githubusercontent.com/18412583/194212594-86ef4f73-569c-49bf-9ee6-972d8a82b813.png)

Here is the output of the program:

$ python readprop.py 
jdbc:mysql://localhost:3308/mydb
root
mypass
