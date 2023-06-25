# PythonAutomatedMoviesList
Automating Movie Recommendations with Python: Get the Top 10 Trending Movies Emailed to You Weekly

# CinemaGoer Top Movies Emailer

This script fetches the most popular movies weekly using the Cinemagoer Python library and sends an email containing a list of the top 10 movies. The email includes movie details such as title, plot, main actor, genre, and production company.

## Requirements

- Python 3.x
- `imdb` library (install using `pip install cinemagoer`)
- An email account (Gmail, Outlook, etc.) to send the email from
- Allow less secure apps access (for Gmail, see: https://support.google.com/accounts/answer/6010255)

## Usage

1. Configure the email settings in the script.
2. Run the script using Python: python cinema_goer_emailer.py
3. Check the recipient's email for the top 10 movies of the week.

## Configuration

To use this script, you need to configure the email settings in the `cinema_goer_emailer.py` file:

- Update the `smtp_host` variable with the SMTP server address.
- Update the `smtp_port` variable with the SMTP server port.
- Update the `smtp_username` variable with the SMTP server username (your email address).
- Update the `smtp_password` variable with the SMTP server password (your email password).
- Update the `sender` variable with your email address.
- Update the `recipient` variable with the recipient's email address.

## License

Feel free to customize and enhance the script according to your needs!


