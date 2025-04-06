# Python code for empty webpage.

Created: 2023-03-16 17:00:56
Last Updated: 2023-03-16 17:00:56

### User - 2023-03-16 17:00:56

Write python code that will display an empty webpage on localhost using current best practices.

### Assistant - 2023-03-16 17:01:08

To display an empty webpage on localhost using current best practices in Python, you can use the Flask web framework. Here's the code:

```python
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<html><body></body></html>'

if __name__ == '__main__':
    app.run(debug=True)
```

This code creates a Flask application object and defines a route for the root URL ('/'). When a user visits this URL, the `index` function is called, which returns an empty HTML page. Finally, the application is run using the `run()` method with the `debug` flag set to `True` to enable debugging.

To run this code, save it to a file (e.g. `app.py`) and execute it with the following command in a terminal:

```
$ python app.py
```

Then, visit `http://localhost:5000` in a web browser to see the empty page.

### User - 2023-03-16 17:02:06

Add "Hello world!" to the page and use CSS styling to make it a purple title.

### Assistant - 2023-03-16 17:02:21

To add "Hello world!" to the page and use CSS styling to make it a purple title in the Flask application, you can modify the `index` function as follows:

```python
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '''
        <html>
            <head>
                <title>Hello world!</title>
                <style>
                    h1 {
                        color: purple;
                    }
                </style>
            </head>
            <body>
                <h1>Hello world!</h1>
            </body>
        </html>
    '''

if __name__ == '__main__':
    app.run(debug=True)
```

In this code, we have added an HTML `title` element with the text "Hello world!" and a CSS `style` element that defines the color of the `h1` element to be purple. We have also wrapped the "Hello world!" text in an `h1` element to create a title.

When you run this code using the same command as before (`$ python app.py`) and visit `http://localhost:5000` in a web browser, you should see the "Hello world!" title displayed in purple text.

### User - 2023-03-16 17:05:05

Now add a second page called "Time" which shows the time when the page was loaded. Add a link to that page from the index.

### Assistant - 2023-03-16 17:05:31

To add a second page called "Time" which shows the time when the page was loaded and a link to that page from the index in the Flask application, you can modify the code as follows:

```python
from flask import Flask
import datetime

app = Flask(__name__)

@app.route('/')
def index():
    return '''
        <html>
            <head>
                <title>Hello world!</title>
                <style>
                    h1 {
                        color: purple;
                    }
                </style>
            </head>
            <body>
                <h1>Hello world!</h1>
                <p><a href="/time">Click here to see the current time.</a></p>
            </body>
        </html>
    '''

@app.route('/time')
def time():
    current_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    return '''
        <html>
            <head>
                <title>Current time</title>
            </head>
            <body>
                <h1>Current time:</h1>
                <p>{}</p>
                <p><a href="/">Go back to the index.</a></p>
            </body>
        </html>
    '''.format(current_time)

if __name__ == '__main__':
    app.run(debug=True)
```

In this code, we have added a new route for the "/time" URL, which returns an HTML page that displays the current time using the `datetime` module. We have also added a link to the "Time" page in the index page, and a link to the index page in the "Time" page.

When you run this code using the same command as before (`$ python app.py`) and visit `http://localhost:5000` in a web browser, you should see the "Hello world!" title displayed in purple text with a link to the "Time" page. Clicking on the link should take you to the "Time" page, which displays the current time and a link back to the index page.

### User - 2023-03-16 17:07:26

Update the time page to show a ❤️ if the current seconds are even and a 💙 if they are odd.

### Assistant - 2023-03-16 17:08:49

To update the time page to show a ❤️ if the current seconds are even and a 💙 if they are odd, you can modify the `time` function as follows:

```python
from flask import Flask
import datetime

app = Flask(__name__)

@app.route('/')
def index():
    return '''
        <html>
            <head>
                <title>Hello world!</title>
                <style>
                    h1 {
                        color: purple;
                    }
                </style>
            </head>
            <body>
                <h1>Hello world!</h1>
                <p><a href="/time">Click here to see the current time.</a></p>
            </body>
        </html>
    '''

@app.route('/time')
def time():
    current_time = datetime.datetime.now()
    if current_time.second % 2 == 0:
        heart_color = 'red'
        heart_text = '❤️'
    else:
        heart_color = 'blue'
        heart_text = '💙'
    current_time_str = current_time.strftime('%Y-%m-%d %H:%M:%S')
    return f'''
        <html>
            <head>
                <title>Current time</title>
            </head>
            <body>
                <h1>Current time:</h1>
                <p>{current_time_str} <span style="color: {heart_color};">{heart_text}</span></p>
                <p><a href="/">Go back to the index.</a></p>
            </body>
        </html>
    '''

if __name__ == '__main__':
    app.run(debug=True)
```

In this code, we have updated the `time` function to check if the current seconds are even or odd using the modulo operator (`%`). If the seconds are even, we set the `heart_color` variable to 'red' and the `heart_text` variable to '❤️'. Otherwise, we set them to 'blue' and '💙', respectively. We have also modified the HTML page to include a `span` element with the `style` attribute set to the appropriate color and the `heart_text` variable as its content.

When you run this code using the same command as before (`$ python app.py`) and visit `http://localhost:5000/time` in a web browser, you should see the current time displayed with a heart or a blue heart, depending on whether the seconds are even or odd.

### User - 2023-03-16 17:08:52

Modify the time page to add a button which updates the time. The button should be dark grey with white text. 

### Assistant - 2023-03-16 17:09:29

To modify the time page to add a button which updates the time, you can modify the `time` function as follows:

```python
from flask import Flask, render_template
import datetime

app = Flask(__name__)

@app.route('/')
def index():
    return '''
        <html>
            <head>
                <title>Hello world!</title>
                <style>
                    h1 {
                        color: purple;
                    }
                </style>
            </head>
            <body>
                <h1>Hello world!</h1>
                <p><a href="/time">Click here to see the current time.</a></p>
            </body>
        </html>
    '''

@app.route('/time')
def time():
    current_time = datetime.datetime.now()
    if current_time.second % 2 == 0:
        heart_color = 'red'
        heart_text = '❤️'
    else:
        heart_color = 'blue'
        heart_text = '💙'
    current_time_str = current_time.strftime('%Y-%m-%d %H:%M:%S')
    return render_template('time.html', current_time=current_time_str, heart_color=heart_color, heart_text=heart_text)

if __name__ == '__main__':
    app.run(debug=True)
```

Then, you can create a new file called `time.html` in the same directory as `app.py` with the following contents:

```html
<html>
    <head>
        <title>Current time</title>
        <style>
            h1 {
                color: black;
            }
            button {
                background-color: darkgrey;
                color: white;
                border: none;
                padding: 10px 20px;
                font-size: 16px;
                border-radius: 5px;
                cursor: pointer;
            }
        </style>
    </head>
    <body>
        <h1>Current time:</h1>
        <p>{{ current_time }} <span style="color: {{ heart_color }};">{{ heart_text }}</span></p>
        <form method="get">
            <button type="submit">Update time</button>
        </form>
        <p><a href="/">Go back to the index.</a></p>
    </body>
</html>
```

In this code, we have created a new HTML page called `time.html` which includes a button with the style specified in the `style` element. We have also added a `form` element with a `submit` button which will allow the user to update the time when clicked. The `{{ current_time }}`, `{{ heart_color }}`, and `{{ heart_text }}` placeholders will be replaced with the appropriate values when the page is rendered.

When you run this code using the same command as before (`$ python app.py`) and visit `http://localhost:5000/time` in a web browser, you should see the current time displayed with a heart or a blue heart, depending on whether the seconds are even or odd. Clicking on the "Update time" button should reload the page and display the updated time.

### User - 2023-03-16 17:14:12

FYI, the time.html file needs to go in a templates/ directory, not the same directory as app.py

### Assistant - 2023-03-16 17:14:45

Yes, you are correct! Thank you for pointing that out.

When using Flask, the `render_template` function looks for HTML files in a directory named `templates` in the same directory as the application script. So, the `time.html` file should be moved to a directory named `templates`.

Here is the updated code for `app.py`:

```python
from flask import Flask, render_template
import datetime

app = Flask(__name__)

@app.route('/')
def index():
    return '''
        <html>
            <head>
                <title>Hello world!</title>
                <style>
                    h1 {
                        color: purple;
                    }
                </style>
            </head>
            <body>
                <h1>Hello world!</h1>
                <p><a href="/time">Click here to see the current time.</a></p>
            </body>
        </html>
    '''

@app.route('/time')
def time():
    current_time = datetime.datetime.now()
    if current_time.second % 2 == 0:
        heart_color = 'red'
        heart_text = '❤️'
    else:
        heart_color = 'blue'
        heart_text = '💙'
    current_time_str = current_time.strftime('%Y-%m-%d %H:%M:%S')
    return render_template('time.html', current_time=current_time_str, heart_color=heart_color, heart_text=heart_text)

if __name__ == '__main__':
    app.run(debug=True)
```

And the updated `time.html` file should be placed in a directory named `templates` in the same directory as `app.py`:

```html
<html>
    <head>
        <title>Current time</title>
        <style>
            h1 {
                color: black;
            }
            button {
                background-color: darkgrey;
                color: white;
                border: none;
                padding: 10px 20px;
                font-size: 16px;
                border-radius: 5px;
                cursor: pointer;
            }
        </style>
    </head>
    <body>
        <h1>Current time:</h1>
        <p>{{ current_time }} <span style="color: {{ heart_color }};">{{ heart_text }}</span></p>
        <form method="get">
            <button type="submit">Update time</button>
        </form>
        <p><a href="/">Go back to the index.</a></p>
    </body>
</html>
```

Thank you for bringing this to my attention!

