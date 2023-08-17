# Workout Log

The Workout Log is a Python script that helps you log your workouts by utilizing natural language processing (NLP) through the Nutritionx API to understand your exercise descriptions and then adds the workout details to a new row in a Google Sheet through Sheety API.

## Setup

1. Create accounts and obtain API credentials for the following services:
   - [Nutritionix API](https://www.nutritionix.com/business/api)
   - [Sheety API](https://sheety.co/)

2. Replace the placeholders in the script:
   - Replace `APP_ID` and `API_KEY` with your Nutritionix API credentials.
   - Replace `AUTHORIZATION` with your Sheety API token.
   - Customize `USERNAME`, `PROJECT_NAME`, and `SHEET_NAME` to match your Google Sheet.

## Usage

1. Run the script

2. The script will prompt you for the exercise you did today. Enter your exercise description in natural language.

3. The script will then analyze the exercise using the Nutritionix API and add the workout data to a new row in your Google Sheet using the Sheety API.

## Notes

- Ensure that your Google Sheet has the required columns (`date`, `time`, `exercise`, `duration`, `calories`) to store the workout data.
- Make sure you have the necessary permissions and access to modify the Google Sheet.

## Example input/output


![input](https://github.com/davidmakoyo/Workout-Log/assets/110312975/adb7099e-5d93-41d5-a828-d5f10905166f)

![output](https://github.com/davidmakoyo/Workout-Log/assets/110312975/791f08ef-8840-4824-ba8c-11dde770d56f)

