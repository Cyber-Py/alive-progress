# A progress bar made using [alive-progress](https://pypi.org/project/alive-progress/) 
> Beginners may not understand the things that are written on the [PyPI](https://pypi.org) page.

Have you ever wanted a progress bar for your program? Maybe just to make the program look more real, or for a real purpose? [alive-progress](https://pypi.org/project/alive-progress/) is with you.

See it for yourself (Video was used from their [PyPI page](https://pypi.org/project/alive-progress)):

[progress bar in motion (the original one)](https://warehouse-camo.ingress.cmh1.psfhosted.org/6b8999cc32e07fc1c5cb5154d94e0db61b9a1fdb/68747470733a2f2f7261772e67697468756275736572636f6e74656e742e636f6d2f7273616c6d65692f616c6976652d70726f67726573732f6d61737465722f696d672f7072696e742d686f6f6b2e676966)
***
[alive-progress](https://pypi.org/project/alive-progress/) has a wide variety of progress bars, like `bubbles`, or `circles`. They even this extra feature called spinners: the part that is in front of the bar. 

## How to use the module:

First and foremost, the most obvious thing, is to import the module. It doesn't matter if you use `pip install alive-progress` (Note: If you are going to go into the shell and use pip, you should use `pip install --upgrade pip ` first, because if you don't, it might show this warning:
```
WARNING: You are using pip version 19.3.1; however, version 21.1.3 is available.
You should consider upgrading via the 'pip install --upgrade pip' command.
``` 
, but this may only be applicable during the time this tutorial was created), or if you install the package/module through the built-in function in [replit.com](https://replit.com):

![image](https://storage.googleapis.com/replit/images/1624890889094_c8b0f991b490e118ecc39d7af48a7555.png)

or just simply auto-import: `import alive-progress` or `from alive-progress import *`, where `*` represents the functions/whatever you want to import (Note: the `*` is actually a real thing in python: it imports all of the functions into your program. These are called star-imports).

BUT, this is how you ues the module:

I would recommend using `from alive_progress import alive_bar, config_handler`.
but you can also use `from alive_progress import *`. We also need `sleep()` from `time`, and `randint` from `random`:

```py
from alive_progress import alive_bar, config_handler
from time import sleep
from random import randint
```

Now, if yu were wanting to use this progress bar multiple times in your program, you could define it, which is what I did. 

So, we define our function, with some parameters: `amount = 1000, starting_string = 'Initializing...', bar = 'bubbles', spinner = 'classic'`. 

An explanantion of all the parameters:
  
    amount: the amount needed to end the progress bar
  
    starting_string: the string that is going to be printed out on 0
  
    bar: the type of bar that will used in the progress bar
    
    spinner: the tpye of spinner that will be used in the progress bar

And an explanantion with examples:


***amount*** is the amount it will show. In this example, it is 615/**1000**
`<●●●●●●●●●●●●●●●●●●●●●●●●○               > - 615/1000 [62%] in 8s (74.7/s, eta: 5s)`

our ***starting_string*** is the string it will show on startup (The default is `Initializing...`):

`on 0: Initializing...`

`<●●●●●●●●●●●●●●●●●●●●●●●●○               > - 615/1000 [62%] in 8s (74.7/s, eta: 5s)
`

***bar*** is the type of bar that will be used, which is the circles, but it is actually called `bubbles`.

And spinner is the part after the ending of the bar, `>`. Right now it's just a hyphen, but if you see it in motion, it looks cool!

***

Ok, so let's put all of this in our function(I named mine bar, but you could name it anything):
```py
def bar(amount = 1000, starting_string = 'Initializing...', bar = 'bubbles', spinner = 'classic'):
```
Now, we put this peice of code after it:

```py
  config_handler.set_global(bar = bar, spinner = spinner)
  count = 0
  with alive_bar(amount) as bar:
    for i in range(amount):
      if count == 0:
        print(starting_string)
        count += 1
      elif i % randint(100, 700) == 0 and count != 0:
        print('We ran into an internal error... Please Wait')
        sleep(randint(1, 5))
        print('Error Fixed.')
      sleep(0.01)
      Bar()
```

Now I will explain all of these.

So `config_handler.set_global(bar = bar, spinner = spinner)` is the customzition function used to customize the bar and spinner: the reason it says `bar = bar` and `spinner = spinner` is because the first one is the actual parameter for the `config_handler.set_global()` function, and the second one is actually our parameters in our function.

I will explain `count` later on...

And now we have `with`.

You should be COMPLETELY confused as to what this is (Unless you know this or you googled it without reading ~~my very hard-to-understand~~ explanation of it). `with` is a keyword that is used to run as many functions as you want at the same time. PLEASE google it EVEN if you reade my explanantion; mine is not good. ~~Everyone starts complementing me that my explanantion is good XD~~

So `alive_Bar()` is actually the function used to make the bar, but we use it as `bar`. How do we do that? `as`. Simple. Just place `as bar` in front of the `alive_bar(amount)` function and you can use it as `Bar()` (But most probably only in the `with` statement).

Now, our `for` loop is for the bar, so that the bar actually moves. So we need to make the `range` for the `for` loop the same as the `amount`, or else the `for` loop will go on even after the `amount` is reached.

The `if` statement is so that it prints a certain statement at on 0, and not at a different time. This is why we needed `count`.We use count to track how many times the program has printed anything (But not print how many times).

So we find out if `count` = 0. If it is, it will print `Initializing...`, and add a 1 to count so it won't print out that statement again. 

Our `elif` statement will print out the other statements.

We do `elif`, then `i % randint(100, 700) == 0` so that it will do a random number, and then we will get i, the number we are at (**615**/1000), and divide it by the random number we generated and then we put `and count != 0` so that it only prints out when `count` does not equal 0.

It will print `We ran into an internal error... Please Wait`, or whatever statement you want to use. Then it will randomly generate a number between 1 and 5 using `sleep(randint(1, 5))`. After that it will print`Error Fixed.`, or again, whatever atatement you want.

Finally, we do `sleep(0.01)` to make the bar look like it is moving, or else the bar won't move: it will skip to the end!

And the last part, `Bar()`, which is actually `alive_bar(amount)`. Remember how we did that using `as`?

We have this right now:
```py
from alive_progress import alive_bar, config_handler
from time import sleep
from random import randint

def bar(amount = 1000, starting_string = 'Initializing...', bar = 'bubbles', spinner = 'classic'):
  '''
  amount: the amount needed to end the progress bar\n
  startin_string: the string that is going to be printed out on 0\n
  bar: the type of bar that will used in the progress bar\n
  spinner: the tpye of spinner that will be used in the progress bar
  '''
  config_handler.set_global(bar = bar, spinner = spinner)
  count = 0
  with alive_bar(amount) as Bar:
    for i in range(amount):
      if count == 0:
        print(starting_string)
        count += 1
      elif i % randint(100, 700) == 0 and count != 0:
        print('We ran into an internal error... Please Wait')
        sleep(randint(1, 5))
        print('Error Fixed.')
      sleep(0.01)
      Bar()
```
The part after we define the function is called a `docstring`. These are used to help you while you code, like when you forgot a parameter. If you hover your cursor over the funnction we defined, it would show this:

![image](https://storage.googleapis.com/replit/images/1624894795676_d0531b4aee94fbcca515177bfe423260.png)

Now, the last we need to do is call the function we created, and voila! A fully functioning [progress bar](https://warehouse-camo.ingress.cmh1.psfhosted.org/6b8999cc32e07fc1c5cb5154d94e0db61b9a1fdb/68747470733a2f2f7261772e67697468756275736572636f6e74656e742e636f6d2f7273616c6d65692f616c6976652d70726f67726573732f6d61737465722f696d672f7072696e742d686f6f6b2e676966)!

And I almost forgot!

If you want to see the bars and spinners they have to offer, just do `from alive_progress import show_bars(), show_spinners()`
***
> Please excuse all the grammar/spelling mistakes, I finished this really quickly.

> This code also has color and the tutorial does not, it is because I added the color after I made the tutorial.
***
## Hope you benefit from this tutorial!
