# Phishing URL Detection with Machine Learning

This project is a web application that detects phishing URLs using a machine learning model. A user can paste a URL into the web interface, and the application will analyze its features in real-time to classify it as either **"Secure"** or **"Not Secure"**.

This project was developed as part of a Cybersecurity course.

## 🚀 Project Demonstration

A short video demonstrating the live application and its functionality is available here:

* **[Watch the Project Demo on Google Drive](https://drive.google.com/file/d/1z6UvxrRtyi9hmanjZVRCHepFOqCVXO_-/view?usp=sharing)**

### 📸 Screenshot

*(**Note:** You should add a screenshot of your application here. Name it `screenshot.png` and upload it to your repository.)*

![Application Screenshot](screenshot.png)

## ✨ Key Features

* **Real-Time Detection:** Classifies URLs instantly upon submission.
* **Simple Web Interface:** A clean and easy-to-use UI built with Flask and Bootstrap.
* **Machine Learning Model:** Uses a pre-trained PyCaret classification model to predict the legitimacy of a URL.
* **Comprehensive Feature Extraction:** Analyzes dozens of features, including:
    * **Address-Based:** URL length, depth, presence of symbols (`@`, `-`, IP addresses), and URL shortening services.
    * **Domain-Based:** Domain age, expiration date (via `whois`), and presence of sensitive words (e.g., "login", "paypal").
    * **HTML & JS-Based:** Checks for `<iframe>` usage, `onMouseOver` events, and forwarding (via `httpx`).

## ⚙️ How It Works (Architecture)

The application follows a simple data-flow pipeline:

1.  **Frontend:** A user submits a URL via the Bootstrap web page (`index.html`).
2.  **Backend (Flask):** The Flask server (`app.py`) receives the POST request.
3.  **Feature Extraction (`featureExtractor.py`):**
    * The application immediately parses the URL for structural features using `extractorFunctions.py` (e.g., URL length, depth, special characters).
    * It performs a `whois` lookup to get domain registration and expiration dates.
    * It uses `httpx` to fetch the page's HTML content and check for suspicious elements like `<iframe>`s or JavaScript redirects.
    * Finally, it uses a pre-trained PCA model (`model/pca_model.pkl`) to transform some features.
4.  **Prediction:**
    * The resulting set of features is formatted into a pandas DataFrame.
    * This DataFrame is fed into the pre-trained PyCaret classification model (`model/phishingdetection`).
5.  **Result:** The model returns a prediction ("Secure" or "Not Secure"), which is rendered back to the user on the `index.html` page.

## 🛠️ Technology Stack

* **Backend:** Flask
* **Machine Learning:** PyCaret, Pandas, Scikit-learn
* **Feature Extraction:** `whois` (for domain info), `httpx` (for HTML content)
* **Frontend:** HTML, Bootstrap 5

## 📁 Project Structure
 phishing-detection-app/ 
 ├── model/ 
 │ ├── phishingdetection # PyCaret model file 
 │ └── pca_model.pkl # PCA model for feature transformation 
 ├── templates/ 
 │ └── index.html # Main HTML page 
 ├── app.py # Main Flask application 
 ├── featureExtractor.py # Feature extraction pipeline 
 ├── extractorFunctions.py # Helper functions for feature extraction 
 ├── main.py # Standalone script for testing 
 └── requirements.txt # Python dependencies


## Setting Up and Running Locally

To run this project on your local machine, follow these steps:

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/YOUR_USERNAME/YOUR_REPOSITORY_NAME.git](https://github.com/YOUR_USERNAME/YOUR_REPOSITORY_NAME.git)
    cd YOUR_REPOSITORY_NAME
    ```

2.  **Create a Python virtual environment:**
    ```bash
    python -m venv venv
    ```

3.  **Activate the virtual environment:**
    * **On Windows:**
        ```bash
        .\venv\Scripts\activate
        ```
    * **On macOS/Linux:**
        ```bash
        source venv/bin/activate
        ```

4.  **Install the required dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

5.  **Run the application:**
    ```bash
    python app.py
    ```

6.  **Access the application:**
    Open your web browser and go to `http://127.0.0.1:5000`.

## 📄 License

This project is licensed under the MIT License.

## Acknowledgements

* This project was created for my Cybersecurity course.
* Special thanks to the creators of PyCaret and Flask for their powerful and easy-to-use tools.