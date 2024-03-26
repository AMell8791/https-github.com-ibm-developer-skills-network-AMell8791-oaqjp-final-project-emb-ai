import requests

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NIpService/Emot'
    headers = {"grpc-metadata-mm-model-id": "emotion aggregated-workflow_lang_en_stock"}
    input_json = {"raw_document": {"text": text_to_analyze}}
    
    response = requests.post(url, json=input_json, headers=headers)
    
    if response.status_code == 200:
        return response.json()['text']
    else:
        return "Error: Failed to analyze emotion."

# Test the function with the provided text
text_to_analyze = "I love this new technology."
print(emotion_detector(text_to_analyze))
