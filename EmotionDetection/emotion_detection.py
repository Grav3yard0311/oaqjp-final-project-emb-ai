"""Emotion Detection module using the Watson NLP Emotion Predict API."""
import json
import requests


def emotion_detector(text_to_analyze):
    """Analyze the given text and return emotion scores with the dominant emotion.

    Args:
        text_to_analyze (str): The text to analyze for emotions.

    Returns:
        dict: Scores for anger, disgust, fear, joy, sadness and the dominant_emotion.
              Values are None when the API responds with a 400 status code.
    """
    url = ('https://sn-watson-emotion.labs.skills.network'
           '/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict')
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = {"raw_document": {"text": text_to_analyze}}
    response = requests.post(url, json=myobj, headers=header, timeout=30)

    if response.status_code == 400:
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }

    formatted_response = json.loads(response.text)
    emotion_scores = formatted_response['emotionPredictions'][0]['emotion']
    dominant_emotion = max(emotion_scores, key=emotion_scores.get)
    emotion_scores['dominant_emotion'] = dominant_emotion
    return emotion_scores
