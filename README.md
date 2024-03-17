<center>
<img src="https://s9.gifyu.com/images/SUYDt.gif" width ="1200" height="500">
</center>
<h1>What´s a command interpreter?</h1>
<p>A command interpreter, often referred to as a shell, is a program that interprets and executes commands entered by the user. It provides a command-line interface (CLI) through which users can interact with the operating system or other software applications.

The command interpreter takes the commands entered by the user, parses them, and then executes the appropriate actions based on those commands. It serves as an intermediary between the user and the underlying system, allowing users to perform various tasks such as managing files, running programs, configuring system settings, and more.

Command interpreters come in different forms and have various features depending on the operating system and the specific shell being used. Examples of command interpreters include the Bash shell on Unix-like systems, Command Prompt on Windows, and PowerShell, which is also available on Windows but offers more advanced features than Command Prompt.</p>


<h1>Execution 💻</h1>

- Your shell should work like this in interactive mode:


```python
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF help quit

(hbnb)
(hbnb)
(hbnb) quit
$
```
- But also in non-interactive mode:

```python
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
```

<center>
- An example of its use
<img src="![test](https://s9.gifyu.com/images/SUYXg.gif)">
</center>

<br>

<center>
<p>Brayan Salazar</p>
<a href="https://www.linkedin.com/in/brayan-salazar-perdomo-07a4321b1/">
  <img src="https://static-00.iconduck.com/assets.00/linkedin-icon-2048x2048-ya5g47j2.png" width="50">
</a>

<a href="https://github.com/BrayanSalazar14">
 <img src="https://1000logos.net/wp-content/uploads/2021/05/GitHub-logo.png" width="100">
</a>


<footer><img src="https://media4.giphy.com/media/coxQHKASG60HrHtvkt/giphy.gif?cid=6c09b952ij868emdkh0ihkk1yud54rfc1ypkvyoigqyacq7r&ep=v1_internal_gif_by_id&rid=giphy.gif&ct=g"></footer>