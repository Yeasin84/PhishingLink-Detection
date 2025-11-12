from featureExtractor import featureExtraction
from pycaret.classification import load_model, predict_model

# Load the pre-trained phishing detection model
model = load_model('model/phishingdetection')

def predict(url):
    # Extract features from the URL
    data = featureExtraction(url)
    
    # Make a prediction with the loaded model
    result = predict_model(model, data=data)
    
    # Get prediction score and label
    prediction_score = result['prediction_score'][0]  
    prediction_label = result['prediction_label'][0]  
    
    return {
        'prediction_label': prediction_label,
        'prediction_score': prediction_score * 100,
    }

# Test URLs
if __name__ == "__main__": 
    test_urls = {
        'phishing_url_1': 'https://bafybeifqd2yktzvwjw5g42l2ghvxsxn76khhsgqpkaqfdhnqf3kiuiegw4.ipfs.dweb.link/',
        'phishing_url_2': 'http://about-ads-microsoft-com.o365.frc.skyfencenet.com',
        'real_url_1': 'https://chat.openai.com',
        'real_url_2': 'https://github.com/'
    }
    
    # Predict and display results
    for label, url in test_urls.items():
        prediction = predict(url)
        print(f"{label} ({url}):")
        print(f"  Prediction Label: {prediction['prediction_label']}")
        print(f"  Prediction Score: {prediction['prediction_score']:.2f}%\n")
