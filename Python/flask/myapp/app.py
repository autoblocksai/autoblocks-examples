import dotenv
from flask import Flask, request

from myapp.ai import augmented_generation

dotenv.load_dotenv(".env")

app = Flask(__name__)


@app.route("/", methods=["POST"])
def index():
    print('got here')
    return augmented_generation(
        user_input=request.json["user_input"],
        n=2,
    )


if __name__ == "__main__":
    app.run(port=8000)
