# Step 1 - To import FLASK
from flask import Flask, render_template, request
import re
# Step 2 - Create the object with a parameter __name__
app = Flask(__name__)

# Step 3 - Create an END POINT using routes and bind them with a functionality

@app.route('/',methods = ['GET','POST'])
def regx_matcher():
    if request.method == 'POST':
        #Get the input i.e test string and regex
        test_string = request.form['test_string']
        regex = request.form['regex']

        #Finding all the matches in input
        matches = re.findall(regex,test_string)

        #render the result with matches
        return render_template('results.html',matches = matches)

    #If request method is get render the template
    return render_template('form.html')


# Step 4 - Run the app
if __name__ == '__main__':
    app.run(debug=True)
