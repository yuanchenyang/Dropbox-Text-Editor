# Welcome To HackJam3.0

## Thanks to Kurt Spindler for this AWESOME write up

This is a Your First Hack (YFH) project. It's a full proposal for what to do during your first hackathon - from start to finish. You'll build your very first web application. And not a dumb one either, but a web application that has some seriously awesome functionality, and you could absolutely use day-to-day. This YFH is to create a web-based Dropbox text editor. When you finish this project, you'll have:

* learned about OAuth, a way for you to securely use other applications (like Dropbox) without having your users give away their username and password.
* connected your application with the Dropbox API, allowing your application to act exactly like any application that Dropbox creates themselves.
* created a fully functional web application that other people can use by visiting it's URL.
* learned a ton of Python and HTML.
* learned how to use several 3rd party libraries to make your job easier and your project more robust.
* kicked some serious ass!

Now, let's get started!

## 0. Before You Start (Read This!)

First of all, the most important thing you should take away from this tutorial: don't be afraid to ask. Or be afraid and do it anyway, whichever works for you. Take away that message and you're done reading. That's it, you're done, go have fun hacking! If you're still reading, here's the idea: development is fundamentally about problem solving. And problems are difficult - otherwise they wouldn't be problems. With all the problems that constantly crop up when you're programming, the only hope you have to tackle all the challenges is to ask for assistance from time to time. When your Python program isn't working, ask the person next to you if s/he has any experience with pdb, the Python debugger. When your database just won't do what you tell it to do, walk up to that group of people chatting by the boxes of pizza and ask if any of them know some SQL-fu. And keep asking till you get the answers you're looking for. Don't be afraid to post your questions to Stack Overflow. And finally, share what you learn. Somebody else probably isn't as brave as you and didn't ask the questions they had. So, tell the person next to you when you learn how to write your first Hello World web application using the Bottle framework in Python. Face it, that's freakin' awesome, and the person next to you is going to learn about something they didn't even know was cool.

Now that you're pumped up to get started, here are some quick tips for when you hit your first roadblocks.

 - Ask other people around the room, or the group of people already chatting, or anyone else. What I said before, not kidding!
 - Ask Google. It has the right answers a lot of the time.
 - If you've asked several people and are getting stuck, consider asking one of these awesome people for help:
 <table><tr><td><img src="http://inst.eecs.berkeley.edu/~cs61a-rj/bootstrap/img/pic3.jpg" width="200" height="auto"></td>
 <td><img src="http://a2.sphotos.ak.fbcdn.net/hphotos-ak-snc7/305492_10150364954364573_516544572_7885545_1515202994_n.jpg" width="200" height="auto"></td>
 <td><img src="http://inst.eecs.berkeley.edu/~cs61a-rb/sharad.jpg" width="200" height="auto"></td>
 <td><img src="https://fbcdn-sphotos-f-a.akamaihd.net/hphotos-ak-ash3/558869_10150602046071008_351142091_n.jpg" width="200" height="auto"></td>
 <td><img src="http://inst.eecs.berkeley.edu/~cs61a-rk/steve.jpeg" width="200" height="auto"></td>
 <td><img src="https://fbcdn-sphotos-g-a.akamaihd.net/hphotos-ak-snc7/392436_3656152635417_1850008030_n.jpg" width="200" height="auto"></td>
 </tr><tr><td>Richie Zeng</td><td>Nelson Zhang</td><td>Sharad Vikram</td><td>Peter Gao</td><td>Steve Yadlowsky</td><td>Vaishaal Shankar</td></tr></table>

You'll need to install Python (3.X please!). If you've never used Python before and you've had something missing in your life, Python is probably the answer. If so, go download and install Python. That's step 1 for the project. Go!

## 1. Learn Python

Hopefully, you remember some of your Python from 61A. If you've forgotten a bit, head over to the [official Python tutorial](http://docs.python.org/tutorial/) (It's amazing!), and refresh your memory.


Important things you'll use from 61A:

1. Decorators! Remember when we slap ```@main```  or ```@interact``` or ```@trace``` above our ```def```? This is a use of higher order functions, where we basically get to add some hidden functionality to whatever function we want. We'll use this in the future to create our web server.
2. Mutable data structures (i.e. lists and dictionaries). As you'll soon learn, Dropbox looovvvvvesss to return data in the form of dictionaries.
3. Dot notation. Remember when you did ```words.append("hello")``` and other list operations? Well that period indicates that we're doing an operation specific to the words list. You'll be doing a lot of operations on objects with this "dot notation."

## 2. Learn Bottle (web server)

Bottle.py is a library for Python to make websites _extremely_ quickly. Install it (download "bottle.py" by clicking the link or using wget), and then write a Hello World from the [Bottle tutorial](http://bottlepy.org/docs/dev/tutorial.html).

## 3. Add Dropbox authentication

Dropbox is a wonderful company for any number of reasons - not least of which because they provide you with a fantastic Python library to use their services. Check it out at [their site](https://www.dropbox.com/developers). That being said, there's a lot of stuff on that site, so here are a few hotspots to check out.

1. Dropbox keeps a record of your app to ensure security. You'll first need to create an app with Dropbox in order to use their services. Go [here](https://www.dropbox.com/developers/apps) to create your app on Dropbox.
2. You'll need the Dropbox Python library. I included it in the Github files to make your life a bit easier, but feel free to install it yourself using pip or from Dropbox's website if you want the satisfaction of doing everything yourself.
3. Check out the example that Dropbox uses, either in the zip that you downloaded from Dropbox, or from the dropbox-examples folder from this Github. Open up web_upload_example.py and put in the two authentication keys Dropbox gave you - the app_key and the app_secret. Run their demo using `python web_upload_example.py` and see what functionality it provides. Now, take a look at the actual file, and try to figure out what Dropbox did to build their application. Parts of this example are actually going to form the first pages of your application, so pay special attention to the login page!

## 4. Start Building Your Web App!

Alright, so here's where we get down and dirty and actually start to build your web app. You're gonna have to start writing some of your own code here. Also, it's gonna start becoming a bit more free form, so feel free to try things that might not work, make mistakes, and generally be willing to try things until they work. You're discovering how to build stuff, so expect that you'll get a bit frustrated sometimes, but just keep on going, because the end result is gonna be awesome. Don't give up!

Start with a new version of the bottle.py Hello World application. Just to make discussion easier, call this file `app.py`. Modify it to be a web page with a single link, at first just to Dropbox's homepage. Make sure this web page works fine by running the Bottle server and visiting the web page. Now, just add one thing before continuing. Add an `import dropbox` line at the top of `app.py`, and make sure it still works. You'll need the Dropbox library installed for this to work. 

Once you've done that, start looking at how Dropbox's example website does the authentication on it's `/login` page. You're going to need to add all the same features to your bottle application. A few hints: The host is the base of the URL you're on. For the URL `http://www.dropbox.com/myfile`, the host is `www.dropbox.com`. Notice for most of your bottle development, your host has probably been `localhost:8080` (or maybe some other port). The dropbox example finds the name of the host using `self.host`. In bottle, you'll use `bottle.request.headers['host']`. I'd also copy the `get_session()` and `get_client()` functions into your python file. It will make your life a bit easier.

For reference, here is the Dropbox login page.

    sess = get_session()
    request_token = sess.obtain_request_token()
    TOKEN_STORE[request_token.key] = request_token
    
    callback = "http://%s/callback" % (self.host)
    url = sess.build_authorize_url(request_token, oauth_callback=callback)
    prompt = """Click <a href="%s">here</a> to link with Dropbox."""
    return prompt % url 

The reason this page is a bit complicated is because it holds the OAuth (the way Dropbox verifies users) logic for the application. It first creates a key for the user's session, this user's single visit, or session, to your website. Your website then asks Dropbox to verify that user for the duration of their session, and asks you to provide a callback URL that the Dropbox website will bring your user to once they've finished logging in to Dropbox.

You're going to want all this same logic: storing their session token, providing a callback URL, and building the string that creates the webpage for your bottle application. You should also construct a new route and function for `/callback`, which is the URL you want Dropbox to return you to. This page should also include the same logic as `callback_page()` in the Dropbox example. Try to make it work!

## 4. Status Check

Awesome job. So, just a status check, you should now have a basic website, consisting of two pages. The first should present a login link to the user. When that pages loads, it should be doing all the same OAuth work in the background that the Dropbox example does. After the user clicks on that link and goes to Dropbox, Dropbox should redirect the user to a new webpage, call it `/callback`, which should store the data returned from Dropbox, just like the Dropbox example does. Feel free to print out some data on the page for verification. 

If you've made it this far, take a minute to give yourself a huge pat on the back. You've mastered OAuth, creating a web server, using 3rd party libraries, and integrated with Dropbox. Damn good job.

## 5. Make the /viewfiles page

Alright, so now we want to do something with the Dropbox integration. Let's make a simple view of all our files. To do this, you should use a templating engine called [mustache](mustache.github.com). It's incredibly powerful, and beautiful as well. Everything is expressed with variable names surrounded by mustaches. {{like this}}. Read about that until you're a little comfortable with it. Then add this line to the top of `app.py`: `import pystache2`. The pystache2.py file is available at this project's Github page. Create a new route in your bottle file to test out using the templates, and get yourself a little comfortable with it. There's documentation on pystache2 within the `pystache2.py` file.

Now, let's make the `/viewfiles` page. Create this route and function in bottle.

First, we're going to need some data to populate the page with. Within the function for this page, we're going to need to query the Dropbox servers for the list of files in a directory. Check out the following code I wrote.

    access_token_key = bottle.request.get_cookie('access_token_key') #gets the access_token_key from the user's cookies
    access_token = TOKEN_STORE[access_token_key] #gets the actual access_token from the server's cache `TOKEN_STORE` based on the key on the previous line
    client = get_client(access_token) #get_client, the function from the Dropbox example code
    context = client.metadata('.') #client.metadata is the Dropbox library call to get the list of files in the directory. You should look at the documentation of the Dropbox Python library to confirm this.

For now, just have this webpage return `str(context)` and confirm that you're getting the data correctly. If you are, congratulations. Get another big pat on the back, and keep going!

You need to present this data in a more readable fashion - this is where the templates come in. Make a template `viewfiles.mustache`. It should have a mustache section (remember, in mustache, a section is a group that gets repeated or otherwise treated in a special way.) that will display something for every file within a directory. My version displays the name and the date modified, and wraps it within a HTML table. You should look at the keys of the context dictionary to figure out the names of variables you can use in your template.

Once that template is up and running, change your function to have `return pystache2.render_file('viewfiles', context)` instead of just printing the dictionary. Once you get this figured out, this starts looking like a real web app. Awesome!

## 7. Turn the files into links

Now, you need to be able to go deeper into Dropbox folders instead of just looking at the root folder. You should add a \<:path\> to the end of the viewfiles route so that it reads

    @bottle.route('/viewfiles/<path:path>')
    def viewfiles(path = '.'):
        ...

Now, you have a variable named path available within this function, which reprenents your current location in Dropbox. Change the function to use this path instead of the generic one, and you're one step closer! Sweet!

The final step to making all your files accessible is to turn each one into a link. Go back into the mustache template, and instead of just printing text, each file should turn into a link. Think for a moment about what it should link to. It should display the contents of that subdirectory, and you already have a URL route that displays the contents of a directory. Figure out what your desired result should be, then play with the available strings a bit to get that result.

It's worth mentioning two valuable tips here. An incredibly powerful statement in python is `import pdb;pdb.set_trace()`. When your server hits that line, the Python interpreter will stop, and you'll be dropped into an interpreter, where you can print out available variables, change the values of variables, do anything you can in normal Python (note that the web page will seem to be frozen in 'loading..' while you're in the debugger. The second tip is a trap that I ran into. The file links didn't work for me unless the URLs that they linked to were prefixed with `http://` - just something to be aware of if you run into the situation where your links don't seem to work for some mysterious reason.

## 8. View the contents of files

Now, all that's left to do is load in file data. You could make a new route for it - I chose to do an if statement in /viewfiles/ to see if we're viewing a dictionary or not, and then loading a different template based on that determination. I think either way would probably be fine, but I did find using a single route to be fairly convenient. Your next steps:

1. create that conditional behavior going in `/viewfiles` (maybe there's some metadata you already have that has the answer!).
2. Find the Dropbox API call to load in file data, and figure out how to use it correctly.
3. Create a template for file viewing. You'll add editing later. For now, just have an extremely simple template to view the contents of a file.

A short note about the last two points: the object that the Dropbox API returns when requesting a file can be a tad confusing. It's a dictionary, and it contains the key `fp`, which has a value as a file object. You'll need to call `.read()` on this object to get the actual file data out.

## 9. Turn your app into a full-fledged text editor

First, take a minute to enjoy how awesome your web app is. It's really awesome. Go tell the person next to you. Good job. Now, this next step should be pretty easy. Modify your template to display the file contents within an editable [\<textarea\>](http://www.w3schools.com/tags/tag_textarea.asp). Wrap it within a form and add a submit button. Add a reset button for good measure.

## 10. Add the save button

Now, make sure your updates are actually going to work. One thing to understand about Dropbox is that each path has an associated property called 'rev'. It helps Dropbox to resolve differences between files, and you'll need to use it to update files. Create hidden form inputs for both the file path and the rev in your template for the file viewer. That will make your form pass along those parameters, making your life a bit easier. Add a form action to your form as well, which will perform a `POST` to the URL `/submission`. This form is going to pass along any information contained within it's tags from textareas and inputs.

Create a route for `/submission`. Access the form data with the dictionary `bottle.request.params`. Check out the Dropbox library again for how to put an update to a file. Perform that function call within the function for `/submission`, and make sure you pass in the parent_rev parameter as the rev from the metadata of the file you're updating. Once you have all that figured out, breathe for a moment. You're done!

## 11. The really hard part

Celebrate! You're done! Tell your neighbors. Get in line to present. Eat some pizza and ice cream! Freakin awesome!

## 11. Where next?

Brainstorm what else you could do with this project, or what other things you could build. A few ideas to get you started:

- Your website looks like it's from 1990. Learn some more HTML and some CSS (there are some upcoming H@B events to teach this stuff!). Check out [Twitter Bootstrap](http://twitter.github.com/bootstrap/) for a way to make *beautiful* websites with almost zero work.
- Add more functionality: rename files, delete files, create files.
- Make the text editor much more feature-full: syntax highlighting, keyboard shortcuts, the works.
- Let your imagination run wild!

# Congratulations!

I hope you had a ton of fun. I'd love to hear how it went - send team@ an email, telling us how amazing your first hack was. Also, I'd genuinely appreciate your feedback for this tutorial. Let me know what works and what doesn't, and I'll try to make it better for future first time hackers!

# Happy Hacking!

