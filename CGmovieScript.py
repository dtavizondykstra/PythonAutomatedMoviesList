"""
CinemaGoer Top Movies Emailer

This script fetches the top 10 trending movies of the week using the CinemaGoer library and sends an email with the movie details to a specified recipient. The email includes information such as the movie's title, plot, main actor, genre, and production company.

Requirements:
    - Python 3.x
    - imdb library (install using `pip install imdb`)
    - An email account (Gmail, Outlook, etc.) to send the email from

Usage:
    1. Configure the email settings in the `send_email` function.
    2. Run the script using Python.
    3. Check the recipient's email for the top 10 trending movies of the week.

"""


import imdb
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def get_top_10_movies():
    """
    Fetches the top 10 trending movies of the week using the CinemaGoer library.

    Returns:
        list: A list of movie objects representing the top 10 movies.
    """
    try:
        ia = imdb.Cinemagoer()
        all_popular_movies = ia.get_popular100_movies()
        top10_movies = all_popular_movies[:10]
        top10_movies_ids = [ia.get_movie(movie.movieID) for movie in top10_movies]
        return top10_movies_ids
    except imdb.IMDbError as e:
        print("An error occurred while retrieving movie information:", e)
        return []


def format_movie_info(movie):
    """
    Formats the movie information into a string.

    Args:
        movie (dict): A dictionary containing movie details.

    Returns:
        str: The formatted movie information.
    """
    title = movie["title"]
    plot = movie["plot"][0]
    main_actor = movie["cast"][0]
    genre = movie["genre"][0]
    production_company = movie["production companies"][0]
    return f"Title: {title}\nPlot: {plot}\nMain Actor: {main_actor}\nGenre: {genre}\nProduction Company: {production_company}\n\n"


def generate_email_content(movies):
    """
    Generates the content of the email to be sent.

    Args:
        movies (list): A list of movie objects.

    Returns:
        str: The content of the email.
    """
    content = "Top 10 Trending Movies This Week:\n\n"
    for movie in movies:
        content += format_movie_info(movie)
    return content


def send_email(subject, content, recipient):
    """
    Sends an email with the provided subject, content, and recipient.

    Args:
        subject (str): The subject of the email.
        content (str): The content of the email.
        recipient (str): The recipient's email address.
    """
    # Email configuration
    smtp_host = "smtp.mail.com"  # SMTP server address
    smtp_port = 587  # SMTP server port
    smtp_username = "your_email@example.com"  # SMTP server username
    smtp_password = "your_email_password"  # SMTP server password

    sender = "your_email@example.com"  # Sender's email address

    # Create message container
    message = MIMEMultipart()
    message["From"] = sender
    message["To"] = recipient
    message["Subject"] = subject

    # Add message content
    message.attach(MIMEText(content, "plain"))

    try:
        # Create SMTP session
        with smtplib.SMTP(smtp_host, smtp_port) as server:
            # Start TLS for security
            server.starttls()

            # Login to the SMTP server
            server.login(smtp_username, smtp_password)

            # Send email
            server.send_message(message)

        print("Email sent successfully!")

    except smtplib.SMTPException as e:
        print("An error occurred while sending the email:", e)


def main():
    """
    Main entry point of the script.
    """
    try:
        top10_movies = get_top_10_movies()
        if top10_movies:
            content = generate_email_content(top10_movies)
            send_email(
                "Top 10 Trending Movies This Week", content, "recipient@example.com"
            )
    except Exception as e:
        print("An error occurred:", e)


if __name__ == "__main__":
    main()
