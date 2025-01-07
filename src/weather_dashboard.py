import os
import json
import boto3
import requests
from datetime import datetime
from dotenv import load_dotenv

# Load environment variables from a .env file
load_dotenv()

class WeatherDashboard:
    def __init__(self):
        # Retrieve API key and bucket name from environment variables
        self.api_key = os.getenv('OPENWEATHER_API_KEY')
        self.bucket_name = os.getenv('AWS_BUCKET_NAME')
        # Initialize S3 client using boto3
        self.s3_client = boto3.client('s3')

    def create_bucket_if_not_exists(self):
        """
        Checks if the S3 bucket exists; if not, creates it.
        """
        try:
            # Check if the bucket exists
            self.s3_client.head_bucket(Bucket=self.bucket_name)
            print(f"Bucket {self.bucket_name} exists")
        except:
            # Bucket doesn't exist, so create it
            print(f"Creating bucket {self.bucket_name}")
            try:
                # Create bucket (simple creation for us-east-1 region)
                self.s3_client.create_bucket(Bucket=self.bucket_name)
                print(f"Successfully created bucket {self.bucket_name}")
            except Exception as e:
                print(f"Error creating bucket: {e}")

    def fetch_weather(self, city):
        """
        Fetches weather data from OpenWeather API for the given city.
        """
        base_url = "http://api.openweathermap.org/data/2.5/weather"
        params = {
            "q": city,  # City name
            "appid": self.api_key,  # API key for authentication
            "units": "imperial"  # Use Fahrenheit units
        }
        try:
            # Make a GET request to the OpenWeather API
            response = requests.get(base_url, params=params)
            response.raise_for_status()  # Raise an error for HTTP codes >= 400
            return response.json()  # Return the response JSON
        except requests.exceptions.RequestException as e:
            print(f"Error fetching weather data: {e}")
            return None

    def save_to_s3(self, weather_data, city):
        """
        Saves the fetched weather data as a JSON file in the S3 bucket.
        """
        if not weather_data:
            return False

        # Generate a timestamp and create a unique file name
        timestamp = datetime.now().strftime('%Y%m%d-%H%M%S')
        file_name = f"weather-data/{city}-{timestamp}.json"

        try:
            # Add a timestamp to the weather data
            weather_data['timestamp'] = timestamp
            # Save the JSON file to S3
            self.s3_client.put_object(
                Bucket=self.bucket_name,
                Key=file_name,
                Body=json.dumps(weather_data),  # Convert dict to JSON string
                ContentType='application/json'  # Set content type
            )
            print(f"Successfully saved data for {city} to S3")
            return True
        except Exception as e:
            print(f"Error saving to S3: {e}")
            return False

def main():
    # Initialize the WeatherDashboard class
    dashboard = WeatherDashboard()
    
    # Ensure the S3 bucket exists
    dashboard.create_bucket_if_not_exists()
    
    # List of cities to fetch weather data for
    cities = ["Philadelphia", "Seattle", "New York"]
    
    for city in cities:
        print(f"\nFetching weather for {city}...")
        # Fetch weather data for the city
        weather_data = dashboard.fetch_weather(city)
        
        if weather_data:
            # Extract and display weather details
            temp = weather_data['main']['temp']
            feels_like = weather_data['main']['feels_like']
            humidity = weather_data['main']['humidity']
            description = weather_data['weather'][0]['description']
            
            print(f"Temperature: {temp}°F")
            print(f"Feels like: {feels_like}°F")
            print(f"Humidity: {humidity}%")
            print(f"Conditions: {description}")
            
            # Save the weather data to S3
            success = dashboard.save_to_s3(weather_data, city)
            if success:
                print(f"Weather data for {city} saved to S3!")
        else:
            print(f"Failed to fetch weather data for {city}")

# Entry point of the script
if __name__ == "__main__":
    main()
