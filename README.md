# Password Strength Checker Web App
This project is a web-based password strength checker built using Python and Flask. Users can enter a password, check its strength on a scale of 1 to 5, and receive feedback on how secure the password is. The app uses visual cues and a responsive design for an elegant and user-friendly experience.

# Features
1. Password Strength Evaluation: Calculates password strength based on character types (uppercase, lowercase, numbers, special characters).
2. Visual Feedback: Displays a strength bar that changes color according to the strength level.
3. User-Friendly Interface: Simple and elegant design with smooth animations and visual feedback.

# Technologies Used
1. Backend: Python, Flask
2. Frontend: HTML, CSS
3. Libraries: string, Flask
   
# Project Structure

password_checker/
├── app.py               # Main Flask application
├── templates/
│   └── index.html       # HTML template for the password checker page
├── static/
│   └── style.css        # CSS styling for the webpage
└── README.md            # Project documentation


# Setup Instructions

1. Clone the Repository

$ git clone https://github.com/your-username/password-checker.git
$ cd password-checker


2. Create a Virtual Environment (Optional)

$ python3 -m venv venv
$ source venv/bin/activate   # On Windows, use: venv\Scripts\activate

3. Install Dependencies

$ pip install flask

4. Run the Flask Application

$ python app.py

5. Access the Web Application

Open your web browser and navigate to http://127.0.0.1:5000 to access the password strength checker.

# Usage
1. Enter your desired password in the input field.
2. Click the Check Strength button to submit the password.
3. View the password strength on a scale of 1 to 5, along with feedback on the strength level.
