import requests
import json

def emotion_detector(text_to_analyze):
    #URL of the emotion detection service
    URL = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    
    # Custom header specifying the model ID
    Headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}

    # Constructing the request payload in the expected format
    myobj = { "raw_document": { "text": text_to_analyze } }

    # Sending a POST request to the emotion detection service API
    response = requests.post(URL, json=myobj, headers=Headers)

    if response.status_code == 400:
        emotions = {}
        emotions['anger'] = None 
        emotions['disgust'] = None 
        emotions['fear'] = None
        emotions['joy'] = None  
        emotions['sadness'] = None 
        emotions['dominant_emotion'] = None
    else:    

        # Parsing the JSON response from the API
        formatted_response = json.loads(response.text)

        # extracting emotions dictionary
        emotions = formatted_response['emotionPredictions'][0]['emotion']
        
        # transform in a list and sort 
        elist = list(emotions.items())
        sorted_elist = sorted(elist, key=lambda t: t[1],reverse= True)
        
        # adding dominant_emotion to the dictionary
        emotions['dominant_emotion'] = sorted_elist[0][0]
    
    # return a dictionary 
    return emotions