# import the necessary libraries
import json

# import the flask app from the app.py script
from app.app import app


def test_add():

    # pass a POST request to the Flask application
    response = app.test_client().post(
        "/my_sum",
        data=json.dumps({"data": ["1", "2", "3"]}),
        content_type="application/json",
    )

    # extract the response
    data = json.loads(response.get_data(as_text=True))

    # ensure that the returned values match
    assert response.status_code == 200
    assert data == 6
