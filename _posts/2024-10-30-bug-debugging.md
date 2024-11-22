# To Bug or Not To Bug

<br>

## Hello again.
<br>
If there is one thing you should know about me, it's that i'm a programmer, which means I design programs. Not necessarily your fancy games, or homework AIs, or the rockets that take astronauts to space. I'm a junior python developer, which means I solve your problems such as programs not running or even create my own when I have time to make your lives easier. 

<br>

But in any stage of a programmer's life, no matter how knowledgable you are, no matter how skilled you are, no matter how talented you are, you will encounter a problem one way or another. And as a programmer, it's your job to find these problems and root them out of your program to make it function again. These bugs, and by extension the program as a whole, can be anything. Any set of actions you perform is a program of sorts (horrible analogy, I know), and bugs could be anything that hinder the result or your ability to perform those actions properly. 

<br>

Debugging is a skill that applies not only to programmers, but real life as well. But for the sake of your time and simplicity, i'll be introducing you to the concept of debugging, and some debugging tools you may find while coding, what they mean, and what they are good for. 

<br>

## <ins>***What is debugging?***</ins>

Debugging refers to going through a set of steps, whether its a program or an event that happens in life, and breaking down each step to understand where a problem may have occured. Debugging in your daily life may vary from recounting your steps to remember where you may have lost something, to going through a recipe to find where you made a mistake. Debugging in coding is a little more complicated, since a lot of the time, excluding syntax errors, your code "doesn't work" because it's not doing what it's supposed to. 

<br>

These kinds of errors where your code doesn't do what it is supposed to are called "logic errors." As opposed to normal errors, Python won't recognize this error since the code is doing what it is told to do, you just didn't tell it to do the right thing. This kind of error is often difficult to track and fix since to you, who wrote the program, the code looks alright, but in reality, you miscoded the program and it is ultimately not performing the function you want it to perform.

<br>

For these errors, thankfully, there exists these things called debugging tools. You don't need to be a god tier programmer in order to understand and use these tools, and since most debugging tools are very similar to each other, hopefully I can give a quick guide on how to use debugging tools in programming and make you a better debugger.

<br>

## <ins>***Breakpoints and Steps***</ins>

Breakpoints will be one of the most quintessential tools when debugging as a programmer. This tool, and the others mainly apply to interpreted programming languages, as interpreted languages run line by line as opposed to running the entire file at once like other programming languages. In case you are wondering, interpreted languages include languages like Python, JavaScript, Ruby, etc.

<br>

So, what are breakpoints? If you are using a programming application such as Visual Studio Code, hovering your mouse to the left of a line of code will ask you if you want to add a breakpoint. Breakpoints are used when using a debugging tool, such as the PythonDebugger. I will be referring to the PythonDebugger for future reference since it is what I have the most experience with, but a lot of my points still apply to other program debuggers as well. When running the debugging tool the program will stop before executing the line where you placed the breakpoint.

<br>

In this example code, the red dots are breakpoints which will pause the code just before the line is executed:

<img src="/blog/images/BreakpointExamplePic.png">

Debugging Code:

<img src="/blog/images/OutputCodeExample.png">

Output (notice how the evaluation code does not immediately run after I enter my preference):

<img src="/blog/images/OutputExample.png">

<br>

### <ins>***Step Over***</ins>

This is important since the most other functions use these breakpoints to debug your program, which brings me to the next function you will most likely encounter: <ins>***Step Over***</ins>. 

Step Over (Visual Studio Code):

<img src="/blog/images/StepOver.png">

Step Over is a function that typically looks like an arrow jumping over a breakpoint symbol. Step over will run the code one line at a time. This tool is useful as it allows you to check your code one line at a time and evaluate any erros within it one line at a time. While it is more tedious then its counterpart, Continue, which will run the code as normal until the next breakpoint, it can prove to be far more useful as you gain more agency over where to stop and debug your code.

<br>

The following code may look scary, but all that is happening is that a function is created to evaluate user input, and a user input is taken, giving an output based on the user's input.

When this file is run in debugging mode, the code will stop at the breakpoint labled in the code. Using Step Over will then cause the code to run the line it is stopped at and freeze at the next line of code "choice = input("Enter preference: ")"
```python
#<--test.py-->#

#BR# stands for breakpoint.

'''Evaluation function.'''
def choice_eval(choice)
    if choice == "apples":
        print("Tasty.")
    elif choice == "bananas":
        print("Not a fan")
    else:
        print("Boring")


'''Question.'''
print("Do you like apples or bananas?") #BR#


'''Answer field.'''
choice = input("Enter preference: ")


'''Calling evaluation function.'''
choice_eval(choice)

print("End")
```

<br>

### <ins>***Step Into***</ins>

The next type of function you will most likely encounter is <ins>***Step Into***</ins>.

Step Into (Visual Studio Code):

<img src="/blog/images/StepInto.png">

Step Into often involves functions and containers of code. To be brief, functions can be imagined as containers that are created like this (remember to indent the code after the def line and don't use hashtags): 

```python
def name_of_function():
    #Code goes here
    #Blah Blah Blah
```

They are used to store blocks of code that can be easily reused by calling upon the function. Like so:

```python
name_of_function()
```

("name_of_function" is used as a placeholder name).

<br>

Step Into involves entering a function when you are stopped at the line where it is called to be used. This will take you up to where the function is defined so you can see each line of code being run within the function. To put simply, it continues the debugging process inside the function, instead of just performing the code within the function all at once and moving on. This is also useful when working with modules, as it will open up the file where the function or variable originates from and take you to the source (where the function/class/variable was created or defined).

<br>

In this example, using Step Into when the following code is highlighted during debugging will open up the file where this function was created.

```python
#<--test.py--># (Main File)

import testmodule

testmodule.testfunction()
```

Output:

```python
#<--testmodule.py--># (Module File)

def testfunction():
    #Example function code here.
```

<br>

### <ins>***Step Out***</ins>

Along with Step Into, there is also <ins>***Step Out***</ins>.

Step Out (Visual Studio Code):

<img src="/blog/images/StepOut.png">

To put simply, Step Out will exit the function source code you are currently in and run the rest of the function. This is used when a function looks good and you want to continue debugging the rest of the code, but the function is too long to parse through with Step Over, nor do you want to risk running into an error with Continue.

Using Step Out will return to the main python file you were debugging:

```python
#<--testmodule.py--># (Module File)

import testmodule

def testfunction():
    #Example function code here.
```

Output:

```python
#<--test.py--># (Main File)

testmodule.testfunction()

#End of file.
```

## <ins>***Conclusion***</ins>

Well then, I hope after all that you understand now what debugging is, and how it would be useful to you, as a programmer, or as anything else. To briefly recap, Step Over/Continue allows you to control the flow of your program as you debug, slowly going through the program line by line with Step Over, or jump from breakpoint to breakpoint with Continue. Step Into is used to enter functions, variables, or classes to see their source code, where they were created and the code they contain, allowing you to quickly navigate to code within a function and figure out whats wrong. Finally, Step Out is used to quickly exit a function/variable/class's source code and finish running that segments code, so you can move on with debugging quicker.

<br>

As I've mentioned before, debugging a problem is not just a programmer issue, but you can replicate these steps in day to day activities to solve problems easier in whatever you are doing. Step Over can be working through a problem step by step. Step Into/Step Out can be you looking at the nitty-gritty of certain complex problems to find out what exactly is wrong. Continue is you going from your house, to the bus station, to your school, to find where you left your keys. Anywhere in life, you can apply these steps to solve issues you may have. 

<br>

### <ins>***Never forget that, and happy debugging!***</ins>