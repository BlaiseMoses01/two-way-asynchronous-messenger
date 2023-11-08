# Two Way Asynchronous Messenger

Ths is a two way client/server messenger app developed in Python using socket programming

## Description

This program was developed during my CSCE416: Introduction to Computer Networks Course. Following an example by my professor of a one way messenger app in which a server displayed messages from a connected client, we were tasked with creating a two way asychronous messenger in which the client would also display messsages from the server. I achieved this using socket programming and a turn-based looping structure.

## Getting Started

### Dependencies
* Python, any version should work but I recommend the latest

### Installing

* clone the repo using the command: 
```
git clone  https://github.com/BlaiseMoses01/two-way-asynchronous-messenger.git
```
Alternatively you can download the repo as a zip from the link in the above command, and extract the files locally.

### Executing program

* Running the Program

* Step 1: Open the cloned repo in a console window or your IDE of choice

* Step 2: Launch the server using the below command 
```
python TwoWayMesgServer.py <PORTNUMBER>
```
replace <PORTNUMBER> with a value, any should work . In my demo, I use "111", just remember the value you choose as you will need it later when launching the client. 

If you completed this step correctly , the console should display "waiting for a client..."

* Step 3: In a separate terminal window , launch the client with the below command

```
python TwoWayMesgServer.py <SERVERNAME> <SERVERPORT>
```
SERVERNAME should be localhost unless you renamed, and SERVERPORT is whatver value you used for <PORTNUMBER> while completing step 2

If done correctly , the client window should display "Connected to Server at ( <SERVERNAME>, <SERVERPORT>).

This should get the application up and running , send messages between the two terminals as much as needed, and one completed use CNTRL^D on Mac or CNTRL^Z + # on Windows in either terminal, which will disconnect the sockets and terminate the program.

## Help
If you are having trouble getting the two terminals to connnect , remember that you MUST launch the server first and you must use the same portnumber in both commands, otherwise the client will fail to connect.
## Authors

Contributors names and contact info
[Blaise Moses](blaisemoses2001@gmail.com)

## License
This project is licensed under the Apache License

## Acknowledgments
I would like to acknowledge my CSCE416 professor , Nelakuditi Srihari, for the written and coded examples in class that allowed me to understand the structure and syntax enough to complete this project.