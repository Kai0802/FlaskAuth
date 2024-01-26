# this file will be run when we want to run our website
from website import create_app
app = create_app()

if __name__ == '__main__':  # Only if we runs this file it will run the line below, exporting the file won't run the line below
    # debug = True means that everytime we make a change to our python code -> it will automatically restart the server
    # turn this off when we have it run in production
    app.run(debug=True)
