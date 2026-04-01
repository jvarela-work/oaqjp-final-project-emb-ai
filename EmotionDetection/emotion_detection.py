import requests
import json

def emotion_detector(text_to_analyse):
    '''Function to analyse text emotions.'''
    PARAMS = {
        'URL': 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict',
        'Headers': {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"},
        'Input json': { "raw_document": { "text": text_to_analyse } }
    }
    url = PARAMS['URL']
    header = PARAMS['Headers']
    myobj = PARAMS['Input json']
    response = requests.post(url, json=myobj, headers=header)
    formatted_response = json.loads(response.text)
    final_response = {}
    if response.status_code == 400:
        for emotion in ['anger', 'disgust', 'fear', 'joy', 'sadness', 'dominant_emotion']:
            final_response[emotion] = None
    else:    
        dominant_emotion = 'anger'
        for emotion in ['anger', 'disgust', 'fear', 'joy', 'sadness']:
            final_response[emotion] = formatted_response['emotionPredictions'][0]['emotion'][emotion]
            if emotion != 'anger' and final_response[emotion] > final_response[dominant_emotion]:
                dominant_emotion = emotion
        final_response['dominant_emotion'] = dominant_emotion
    
    return final_response

