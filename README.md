# Python Cryptocurrency

This is a basic cryptocurrency that was coded in python. Purpose of this project was to teach fundamentals of cryptocurrency to my classmates.

## How to Install

**You should have MySql installed. I set it up with the full options and I used "root" as password and username**

1. Open a new terminal and type `pip install -r requirements.txt`

2. Open command prompt start MySql server by typing `mysql.server start`

    - **If you cannot start the server with this command instead try this.**

        - Type `dir mysqld.exe /s /p`
        - You should see something like this "Directory of C:\Program Files\MySQL\MySQL Server 8.0\bin"
        - Change directory with `cd` command. In this case `cd C:\Program Files\MySQL\MySQL Server 8.0\bin` If your directory is different you should enter it instead.
        - Then type `mysql.exe -u root -p` and enter your password.
        
3. After you succesfully started MySql server, type `CREATE DATABASE crypto;`

4. Type `USE crypto;`

5. Type `CREATE TABLE blockchain(number varchar(10), hash varchar(64), previous varchar(64), data varchar(100), nonce varchar(15));`

6. Run **app.py**

And it should be working. You can change the code as you wish to see what they effect how it works.



## Used Technologies

- Python
- HTML5
- MySQL
- Bootstrap5


### Credit

I used [this](https://www.youtube.com/watch?v=b41TVaLwhKc&list=PLtCKS3CuBDYV_Vyl1ZH2Je8gSdXfQf4e3) tutorial to help me code. So if you want detailed information you can check this tutorial out.
