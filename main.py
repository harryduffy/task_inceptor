from create_app import create_app

flask_app = create_app()

@flask_app.route("/")
def index():
    return "Hello World"


if __name__ == "__main__":
    flask_app.run(debug=True)
