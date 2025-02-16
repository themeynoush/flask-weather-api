# Flask Weather API

## Overview

This is a simple **Flask-based Weather API** that fetches real-time weather data from a free weather API and exposes it via a RESTful endpoint. The project follows **SOLID principles** making it modular, maintainable, and scalable.

## Features

- Fetch real-time weather using a free external API (**WeatherAPI Free Tier**).
- **SOLID architecture**: Uses blueprints, services, and utility modules for clean separation of concerns.
- **Custom library (`weatherlib`)**: Handles weather data processing, making it reusable.
- **Dependency management**: Utilizes Poetry for clean installation and packaging.
- **CI/CD pipeline**: Uses GitHub Actions for automated testing, linting, and deployment.
- **GitHub Pages deployment**: Demonstrates continuous deployment by publishing documentation.

## Project Structure

```
flask-weather-api/
├── app/                     # Flask application package
│   ├── __init__.py          # Application factory and initialization
│   ├── config.py            # Configuration (uses environment variables)
│   └── weather_routes.py    # API routes (Blueprint)
├── weatherlib/              # Custom weather processing library
│   ├── __init__.py
│   ├── provider.py          # Handles fetching weather from external API
│   └── utils.py             # Utility functions (e.g., unit conversion, data formatting)
├── tests/                   # Unit tests
│   ├── __init__.py
│   ├── test_provider.py     # Tests for API fetching logic
│   └── test_utils.py        # Tests for weather utilities
├── docs/                    # Documentation files for MkDocs
│   └── index.md             # Main documentation page
├── .github/
│   └── workflows/
│       └── ci.yml           # GitHub Actions CI/CD pipeline
├── mkdocs.yml               # Configuration file for MkDocs site generation
├── pyproject.toml           # Poetry dependencies & project metadata
├── README.md                # Documentation
└── .gitignore               # Ignore unnecessary files



```

## Installation

### Prerequisites

- **Python (>= 3.9)**
- **Poetry (dependency manager)**
- **Flask (installed via Poetry)**
- **GitHub account (for CI/CD setup)**

### Setup Instructions

#### Clone the repository:
```sh
git clone https://github.com/yourusername/flask-weather-api.git
cd flask-weather-api
```

#### Install Poetry (if not already installed):
```sh
pip install poetry
```

#### Install dependencies:
```sh
poetry install
```

#### Set up environment variables (modify `.env` or set manually):
```sh
export FLASK_APP=app
export FLASK_ENV=development
export WEATHER_API_KEY=your_api_key_here
```

#### Run the Flask application:
```sh
poetry run flask run
```

#### Access the API:
Open a browser or use `curl`:
```sh
curl "http://127.0.0.1:5000/weather/current?city=Paris"
```

## API Endpoints

### **GET /weather/current?city=CityName**

Fetches the current weather for a given city.

#### **Request Parameters**
- `city` (string, required) – Name of the city.

#### **Example Request**
```sh
curl "http://127.0.0.1:5000/weather/current?city=Paris"
```

#### **Example Response**
```json
{
  "condition": "Sunny",
  "location": "Paris",
  "temperature_c": 5.3,
  "temperature_f": 41.54
}
```

#### **Error Responses**
- **`400 Bad Request`**: If no city is provided.
- **`500 Internal Server Error`**: If there is an issue fetching data from the external API.

## Running Tests

To ensure everything is working, we run the test suite using `unittest` in the CI pipeline:
```sh
poetry run python -m unittest discover -v
```
This runs all unit tests located in the `tests/` directory.

## Linting & Code Quality

To lint the code locally:
```sh
poetry run pylint app weatherlib
```

## CI/CD Pipeline

This project includes a **GitHub Actions** workflow that:

- Runs **unit tests** (using `unittest`).
- Deploys **documentation** to **GitHub Pages**.

To see the latest build status, check the **Actions** tab in the GitHub repository.

## Deployment

### **GitHub Pages Deployment**

Although Flask is a backend framework, this project deploys **documentation** to **GitHub Pages** as a demonstration of continuous deployment.

- **CI/CD automatically deploys docs** when changes are pushed to the `main` branch.
- The deployed site can be accessed via `https://yourusername.github.io/flask-weather-api/` (after enabling GitHub Pages in repo settings).

## Future Enhancements

- Add support for **multiple weather providers** (e.g., Open-Meteo, WeatherAPI, etc.).
- Implement **caching** to reduce API calls and improve performance.
- Support **unit selection** (Celsius/Fahrenheit) via query parameters.

## License

This project is licensed under the **MIT License**. Feel free to modify and distribute it.

