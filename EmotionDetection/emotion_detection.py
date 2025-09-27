import requests, json  # Import the requests library to handle HTTP requests

def emotion_detector(text_to_analyse):  
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    inputJson = { "raw_document": { "text": text_to_analyse } }  # Create a dictionary with the text to be analyzed
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}  # Set the headers required for the API request
    response = requests.post(url, json = inputJson, headers=header)  # Send a POST request to the API with the text and headers
    
    # If the response status code is 200, extract the label and score from the response
    if response.status_code == 400:
        return { 
            'anger': None, 'disgust': None, 'fear': None, 'joy': None, 'sadness': None, 'dominant_emotion': None        
            }

    data = json.loads(response.text)
    emotion_map = data['emotionPredictions'][0]['emotion']
    dominant = max(emotion_map, key=emotion_map.get)
    emotion_map['dominant_emotion'] = dominant
    return emotion_map