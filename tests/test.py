import requests
import json

# Test if `api/inference` endpoint return the expected prediction
def test_inference_endpoint():
    with open("../samples/SAP.txt", encoding="utf-8") as file:
        sample_text = file.read()

    response = requests.post(
                'http://localhost:9000/api/inference',
                json={'text': sample_text}
            )

    assert response.status_code == 200
    assert response.text == '10'

# Test if `api/save` endpoint save the data and return it back
def test_save_endpoint():
    with open("../samples/SAP.txt", encoding="utf-8") as file:
        sample_text = file.read()
        prediction = "SAP"

    response = requests.post(
                f'http://localhost:9000/api/save?prediction={prediction}',
                json={'text': sample_text}
            )

    all_resume = json.loads(response.text)
    last_index = len(all_resume) - 1
    assert response.status_code == 200
    assert all_resume[last_index]["resume"] == sample_text
    assert all_resume[last_index]["prediction"] == prediction
