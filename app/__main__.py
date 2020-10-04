"""Run Flask application in debug mode."""
from app import main


main.app.debug = True
main.app.run()
