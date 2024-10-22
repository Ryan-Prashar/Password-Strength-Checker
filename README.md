# Password-Strength-Checker

A password strength checker using Python is a program designed to evaluate the security level of a password based on specific criteria. This type of program helps users create stronger, more secure passwords by providing feedback on the composition of their passwords.

# Key Features:
1. User Input: The user enters a password, which is then analyzed for strength. The password is typically checked for various attributes like the presence of uppercase letters, lowercase letters, numbers, whitespace characters, and special symbols.
  
2. Strength Calculation: The program assigns a strength score based on the diversity of characters used in the password:
    i. Lowercase letters
    ii. Uppercase letters
    iii. Digits (numbers)
    iv. Whitespace (spaces)
    v. Special symbols (like @, #, $, etc.)

3. Feedback on Password Strength:
   1. The strength score ranges from 1 (very weak) to 5 (very strong).
   2. Based on the score, the program provides a remark:
       2.1 Score 1: Very bad password, needs immediate change.
       2.2 Score 2: Weak password, should be improved.
       2.3 Score 3: Okay, but could be stronger.
       2.4 Score 4: Hard to guess, but can still be better.
       2.5 Score 5: Strong password, highly secure.
   
4. Detailed Breakdown: The program counts and displays the number of each type of character in the password (lowercase, uppercase, numbers, etc.), helping the user understand what is missing or could be improved.
   
5. Interactive Loop: The program allows users to check multiple passwords in a single session by asking if they want to check another password after evaluating the first one.

# Example Workflow:
1. The user runs the program and is prompted to input a password.
2. The password is analyzed for its composition, and a score is generated based on how many different types of characters it contains.
3. The program then displays:
   3.1 A breakdown of character types used in the password.
   3.2 A password strength score (ranging from 0.0 to 1.0).
   3.3 Feedback on the quality of the password.
4. The user can choose to check another password or exit the program.
