#LEARN FLASK VIA THIS PROJECT. FLASK:a popular, lightweight Python web framework that provides the essential tools to build web applications and APIs. -The project entails a POS system called MY DUKA. -run the terminal on VSCODE and type pip install flask -after running,"pip install flask" -install pip install psycopg2-binary -After installing the above packages -have the files:database.py,main.py -Open sqlpowershell to open ur database. -Create a new database in sql shell called myduka_db

1.create database myduka_db; 2.connect to myduka_db database \c myduka_db 3.Run the following commands to create tables //products table CREATE TABLE products ( id SERIAL PRIMARY KEY, name VARCHAR(100) NOT NULL, buying_price NUMERIC(20, 2) NOT NULL CHECK (buying_price >= 0), selling_price NUMERIC(20, 2) NOT NULL CHECK (selling_price >= 0) );

//stock table CREATE TABLE stock ( id SERIAL PRIMARY KEY, pid INTEGER NOT NULL REFERENCES products(id) ON DELETE CASCADE, stock_quantity INTEGER NOT NULL CHECK (stock_quantity >= 0), created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP );

//sales table CREATE TABLE sales ( id SERIAL PRIMARY KEY, pid INTEGER NOT NULL REFERENCES products(id) ON DELETE CASCADE, quantity INTEGER NOT NULL CHECK (quantity > 0), created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP );

                          WEBSERVER
// WEBSERVER:A web server is a combination of computer hardware and software that stores website files (HTML, CSS, images, JS) and delivers them to users via a browser using HTTP/HTTPS. It acts as a digital librarian, receiving, processing, and responding to client requests to display website content.

                          WEB HOSTING
//WEB HOSTING:Web hosting is a service that provides secure, internet-connected server space to store website files (HTML, CSS, images, data), making them accessible to users worldwide 24/7. It acts as the "home" for a website, allowing browsers to request and display site content instantly. Hosting providers handle server maintenance, security, and uptime.(Renting a server to deploy resources and make them available to the internet)

                          I.P ADDRESS
//I.P ADDRESS:An IP (Internet Protocol) address is a unique numerical label assigned to every device connected to a computer network that uses the Internet Protocol for communication. It acts as a digital identifier or "mailing address" for computers, phones, and IoT devices, allowing them to send/receive data, locate each other, and communicate over local networks or the internet.(A unique number that identifies a number or a network.)(A unique number that identifies a device on the internet.)

                        DOMAIN NAME
//DOMAIN NAME:A domain name is the unique, human-friendly address used to locate a website on the internet, acting as an easy-to-remember alias for a complex numerical IP address. Examples include google.com or wikipedia.org, which users type into browsers to reach specific web servers.(Human friendly name for us to access an ip address.)

                        U.R.L
//URL:A URL (Uniform Resource Locator) is the unique, web-based address for a specific resource on the internet, such as a website, image, or file. Acting like a digital, functional address, it tells a browser how to locate and display information.

It typically consists of a protocol (e.g., https), a domain name (e.g., example.com), and a file path(specific resource u want to access),port(where a service is running). (Full address of a resource on the internet.)

                     HTTP/HTTPS
//HTTP (Hypertext Transfer Protocol) and HTTPS (HTTP Secure) are protocols for transmitting data between a web browser and a server. HTTP sends data in plain text, leaving it vulnerable to interception, whereas HTTPS uses SSL/TLS encryption to secure data, providing confidentiality, integrity, and authentication.

HTTPS is essential for protecting sensitive user information and boosts SEO.

                 **INTRODUCTION TO PSYCOPG2.**
-Simply a POSTGRESQL driver or adapter used to connect python to a POSTGRES database. -It needs to know the SERVER,DATABSE,PORT,USERNAME AND PASSWORD. -python is connected to a POSTGRES database by psycopg2,using the function:#psycopg2.connect() 1.HOST:on what server is the database hosted.

local host:my local device(laptop or computer),it uses 127.0.0.1 2.PORT:exactly where the Postgres service is running on my server. -5432 is the default port for the POSTGRES SERVICE 3.USER:username used to authenticate or identify who is accessing your database. 4.PASSWORD:The password attached to the username,to authenticate oneself before using POSTGRES services. 4.DB NAME:what database are u connecting to. cur:an object used to perform database operations. it performs the following:CRUD operations(create,Read,Update,Delete data)
DB OPERATIONS -insert two products in SQLSHELL.
