# To Bug or Not To Bug

<br>

### Hello again.
<br>
If there is one thing you should know about me, it's that i'm a programmer, which means I design programs. Not necessarily your fancy games, or homework AIs, or the rockets that take astronauts to space. I'm a junior python developer, which means I solve your problems such as programs not running or even create my own when I have time to make your lives easier. 

<br>

But in any stage of a programmer's life, no matter how knowledgable you are, no matter how skilled you are, no matter how talented you are, you will encounter a problem one way or another. And as a programmer, it's your job to find these problems and root them out of your program to make it function again. These bugs, and by extension the program as a whole, can be anything. Any set of actions you perform is a program of sorts (horrible analogy, I know), and bugs could be anything that hinder the result or your ability to perform those actions properly. 

<br>

Debugging is a skill that applies not only to programmers, but real life as well. But for the sake of your time and simplicity, i'll be introducing you to the concept of debugging, and some debugging tools you may find while coding, what they mean, and what they are good for. 

<br>

### <ins>***What is debugging?***</ins>

Debugging refers to going through a set of steps, whether its a program or an event that happens in life, and breaking down each step to understand where a problem may have occured. Debugging in your daily life may vary from recounting your steps to remember where you may have lost something, to going through a recipe to find where you made a mistake. Debugging in coding is a little more complicated, since a lot of the time, excluding syntax errors, your code "doesn't work" because it's not doing what it's supposed to. 

<br>

These kinds of errors where your code doesn't do what it is supposed to are called "logic errors." As opposed to normal errors, Python won't recognize this error since the code is doing what it is told to do, you just didn't tell it to do the right thing. This kind of error is often difficult to track and fix since to you, who wrote the program, the code looks alright, but in reality, you miscoded the program and it is ultimately not performing the function you want it to perform.

<br>

For these errors, thankfully, there exists these things called debugging tools. You don't need to be a god tier programmer in order to understand and use these tools, and since most debugging tools are very similar to each other, hopefully I can give a quick guide on how to use debugging tools in programming and make you a better debugger.

<br>

### <ins>***Breakpoints and Steps***</ins>

Breakpoints will be one of the most quintessential tools when debugging as a programmer. This tool, and the others mainly apply to interpreted programming languages, as interpreted languages run line by line as opposed to running the entire file at once like other programming languages. In case you are wondering, interpreted languages include languages like Python, JavaScript, Ruby, etc.

<br>

So, what are breakpoints? If you are using a programming application such as Visual Studio Code, hovering your mouse to the left of a line of code will ask you if you want to add a breakpoint. Breakpoints are used when using a debugging tool, such as the PythonDebugger. I will be referring to the PythonDebugger for future reference since it is what I have the most experience with, but a lot of my points still apply to other program debuggers as well. When running the debugging tool the program will stop before executing the line where you placed the breakpoint.

<br>

In this example code, the red dots are breakpoints which will pause the code just before the line is executed:

<img src="/blog/images/BreakpointExamplePic.png">

Debugging Code:

<img src="/blog/images/OutputCodeExample.png">

Output:

<img src="/blog/Images/OutputExample.png">

<br>

This is important since the most other functions use these breakpoints to debug your program. Which brings me to the next function you will most likely encounter: Step Over. Step Over is a function that typically looks like an arrow jumping over a breakpoint symbol. Step over will run the code as normal until it encounters another breakpoint. This tool is useful when you place breakpoints in front of or after sections of code that carry out specific functions, so that you can use Step Over to see if each sections of code works properly or not.