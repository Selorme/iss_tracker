# ISS Notification System

This Python script sends an email notification when the International Space Station (ISS) is directly overhead and it's dark outside. It checks the ISS's position and the local sunrise/sunset times using public APIs.

## Features

- Monitors the current position of the ISS.
- Checks if it is currently dark in the user's location.
- Sends an email notification when both conditions are met.

## Setup Instructions

### 1. Clone the GitHub Repository

To get started, clone the repository to your local machine:

```bash
git clone https://github.com/Selorme/iss_tracker.git
```

Navigate into the project directory:

```bash
cd iss-notification
```

### 2. Install Dependencies

Make sure you have Python 3.x installed. You can check your version using:

```bash
python --version
```

You will need the `requests` and `python-dotenv` libraries to run this script. You can install them using pip:

```bash
pip install requests python-dotenv
```

### 3. Set Up Environment Variables

Create a `.env` file in the project directory to store your environment variables. Add the following lines to your `.env` file:

```plaintext
MY_LAT=your_latitude
MY_LONG=your_longitude
MY_EMAIL=your_email@example.com
PASSWORD=your_email_password
```

Replace `your_latitude`, `your_longitude`, `your_email@example.com`, and `your_email_password` with your actual latitude, longitude, email address, and email password. Make sure to enable "Less secure app access" in your Google account settings if using Gmail.

### 4. Run the Script

Run the script using Python:

```bash
python iss_notification.py
```

The script will run continuously and check every 60 seconds if the ISS is within range and if it is dark outside. If both conditions are met, it will send you an email notification.

## Code Explanation

1. **Imports**: The script imports necessary libraries for making API requests, handling dates, sending emails, and loading environment variables.
2. **Environment Variables**: It loads latitude, longitude, email, and password from a `.env` file for secure access.
3. **ISS Position Check**: The function `right_iss_position()` checks the current latitude and longitude of the ISS.
4. **Darkness Check**: The function `it_is_dark()` retrieves sunrise and sunset times to determine if it is currently dark.
5. **Email Notification**: If the ISS is close and it’s dark, the script sends an email notification using the SMTP protocol.

## License

This project is licensed under the MIT License.