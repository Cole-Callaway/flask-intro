"""Greeting Flask app."""

from random import choice

from flask import Flask, request

# "__name__" is a special Python variable for the name of the current module
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

AWESOMENESS = [
    'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza',
    'oh-so-not-meh', 'brilliant', 'ducky', 'coolio', 'incredible',
    'wonderful', 'smashing', 'lovely']


@app.route('/')
def start_here():
    """Home page."""

    return "<!doctype html><html>Hi! This is the home page.<br><a href='/hello'>Go say hello</a><br><a href='/setup'>Go get a diss</a></html </html>"


@app.route('/hello')
def say_hello():
    """Say hello and prompt for user's name."""

    return """
    <!doctype html>
    <html>
      <head>
        <title>Hi There!</title>
      </head>
      <body>
        <h1>Hi There!</h1>
        <form action="/greet">
          What's your name? <input type="text" name="person">
          
          <br>
          <label for="compliment">Choose a compliment:</label>
          <select name="compliment">
            <option name="compliment" value="awesome">Awesome</option>
            <option name="compliment" value="terrific">Terrific</option>
            <option name="compliment" value="fantastic">Fantastic</option>
            <option name="compliment" value="neato">Neato</option>
            <option name="compliment" value="fantabulous">Fantabulous</option>
            <option name="compliment" value="wowza">Wowza</option>
            <input type="submit" value="Submit">
          </select>
        </form>
      </body>
    </html>
    """


@app.route('/greet')
def greet_person():
    """Get user by name."""
    
    player = request.args.get("person")
    
    compliment = request.args.get('compliment')

    return f"""
    <!doctype html>
    <html>
      <head>
        <title>A Compliment</title>
      </head>
      <body>
        Hi, {player}! I think you're {compliment}!
      </body>
    </html>
    """

@app.route('/setup')
def setup_diss():
    return """<!doctype html>
      <html>
        <head>
          <title>Hi There!</title>
        </head>
        <body>
          <h1>Hi There!</h1>
          <form action="/diss">
            What's your name? <input type="text" name="person">
            
            <br>
            <label for="diss">Choose a diss:</label>
            <select name="diss">
              <option name="diss" value="dumb">dumb</option>
              <option name="diss" value="stupid">stupid</option>
              <option name="diss" value="smelly">smelly</option>
              <option name="diss" value="lame">lame</option>
              <option name="diss" value="crazy">crazy</option>
              <option name="diss" value="odd">odd</option>
              <input type="submit" value="Submit">
            </select>
          </form>
        </body>
      </html>
      """
    
@app.route('/diss')
def diss():
    
    player = request.args.get('person')
    
    diss = request.args.get('diss')  
    
    return f"""
    <!doctype html>
    <html>
      <head>
        <title>A Compliment</title>
      </head>
      <body>
        Hi, {player}! I think you're {diss}!
      </body>
    </html>
    """
if __name__ == '__main__':
    # debug=True gives us error messages in the browser and also "reloads"
    # our web app if we change the code.
    app.run(debug=True, host="0.0.0.0")
