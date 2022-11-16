from create_app import create_app

flask_app = create_app()

@flask_app.route("/")
def index():
    return "<h1>This is the task inceptor endpoint</h1>"


if __name__ == "__main__":
    flask_app.run(debug=True)
