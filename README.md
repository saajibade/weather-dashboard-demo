# 30DayDevOpsChallenge
A Python-based Weather Dashboard that integrates real-time weather data retrieval with cloud storage using Amazon S3. This project demonstrates the power of automation, API integrations, and cloud computing in building scalable, data-driven applications.

Here's a structured **README.md** file content for your GitHub repository:

---

# Weather Dashboard 🌦️

A Python-based Weather Dashboard that fetches real-time weather data from the OpenWeather API and securely stores it in an Amazon S3 bucket. This project demonstrates the seamless integration of cloud storage, Python scripting, and API automation to deliver a scalable and efficient solution.

---

## 📌 Features
- **Fetch Real-Time Weather Data**: Retrieves current weather data for multiple cities.
- **Secure Cloud Storage**: Automatically creates an S3 bucket (if it doesn’t already exist) and stores weather data in JSON format.
- **Detailed Logs**: Provides insights into temperature, humidity, and weather conditions for each city.
- **Automated Workflow**: Combines Python and AWS to streamline the process of fetching, storing, and logging weather data.

---



## 🛠️ Tech Stack
- **Python**: The core language for scripting and automation.
- **AWS S3**: Cloud storage solution for storing JSON weather data.
- **OpenWeather API**: Source for real-time weather information.
- **Libraries Used**:
  - `boto3`: To interact with AWS S3.
  - `requests`: For making API requests.
  - `dotenv`: For managing environment variables.

---

## 🚀 How to Get Started
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/username/weather-dashboard.git
   cd weather-dashboard
   ```

2. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Set Up Environment Variables**:
   - Create a `.env` file in the root directory and add the following:
     ```
     OPENWEATHER_API_KEY=your_openweather_api_key
     AWS_BUCKET_NAME=your_s3_bucket_name
     ```


     

4. **Run the Application**:
   ```bash
   python src/weather_dashboard.py
   ```

---

## 📊 Output Example
When you run the script, it will:
- Fetch weather data for the specified cities.
- Log details such as temperature, humidity, and weather conditions.
- Save the weather data as a JSON file in your specified S3 bucket.

Example output:
```plaintext
Fetching weather for New York...
Temperature: 75°F
Feels like: 73°F
Humidity: 60%
Conditions: clear sky

Weather data for New York saved to S3!
```

---

## 🌟 What I Learned
- **API Integrations**: Fetching real-time data using REST APIs.
- **Cloud Storage**: Automating S3 bucket creation and JSON uploads.
- **Python Automation**: Leveraging Python to build efficient workflows.
- **Error Handling**: Managing exceptions for robust and reliable scripts.

---

## 📚 Resources
- [OpenWeather API Documentation](https://openweathermap.org/api)
- [AWS S3 Documentation](https://aws.amazon.com/s3/)
- [Python Requests Library](https://docs.python-requests.org/en/latest/)
- [Boto3 Documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html)

![s3 image](https://github.com/saajibade/weather-dashboard-demo/blob/master/src/Assets/30DaychallengeDay1.JPG)
