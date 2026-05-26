# Weather App using Python

A simple command-line Weather App built using Python that fetches real-time weather information for a user-specified location using the OpenWeatherMap API.

## Features

- Search weather by city name
- Displays current temperature
- Displays humidity
- Displays weather condition
- Handles invalid city names with an error message

## Technologies Used

- Python
- Requests library
- OpenWeatherMap API

## Project Structure

```bash
weather-app/
│
├── weather_app.py
└── README.md
```

## Installation

1. Clone the repository

```bash
git clone <your-repository-link>
```

2. Install required library

```bash
pip install requests
```

3. Get your API key from OpenWeatherMap

:contentReference[oaicite:0]{index=0}

4. Add your API key in `weather_app.py`

```python
API_KEY = "YOUR_API_KEY"
```

## Run the Application

```bash
python weather_app.py
```

## Example Output

```bash
Enter city name: Chennai

Weather Details
----------------------
City: Chennai
Temperature: 33°C
Humidity: 72%
Condition: Clear sky
```

## Learning Outcomes

Through this project, I learned:

- Working with APIs in Python
- Sending HTTP requests using the requests library
- Parsing JSON data
- Handling user input
- Error handling in Python

## Future Improvements

- Add wind speed
- Add "feels like" temperature
- Search using ZIP/PIN code
- Support multiple searches without restarting the app

## Author

G.Manasa# Weather-app
