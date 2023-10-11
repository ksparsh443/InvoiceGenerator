# InvoiceGenerator
This code is a Python program that creates a graphical user interface (GUI) using the Tkinter library. The program allows users to enter various pieces of information, and upon clicking a "Generate PDF" button, it creates a PDF document with the user-provided details. Here's a brief description of the functionality of the code:

1. The code imports necessary libraries and modules, such as re for regular expressions, tkinter for GUI, simpledialog and messagebox for user interaction, and reportlab for PDF generation.

2. It defines two functions for input validation: `validate_phone_number` to check if a phone number is in a valid format, and `validate_email` to check if an email address ends with one of the allowed domains (gmail.com, yahoo.com, or hotmail.com).

3. The code initializes a global variable `pdf_generated` to keep track of whether the PDF has been generated to prevent duplication.

4. The `create_pdf` function is called when the "Generate PDF" button is clicked. It retrieves user input, validates the input for phone number and email format, and then generates a PDF with the provided information. The PDF is saved with a filename based on the user's full name and booking ID.

5. The `reset_form` function is called when the "Reset Form" button is clicked. It clears the form's input fields and resets the `pdf_generated` flag.

6. The code sets up a Tkinter window, configures the form labels, and creates input fields for the user to enter information (e.g., full name, address, phone number, email, etc.).

7. The "Generate PDF" and "Reset Form" buttons are created and linked to their respective functions.

8. When the Tkinter window is launched using `root.mainloop()`, users can input their details. Once the "Generate PDF" button is clicked, a PDF is generated with the user's information, and a message is displayed to confirm the PDF creation.

9. The code uses a black background for the GUI, and it provides a simple and straightforward way for users to input their data, generate a PDF document, and reset the form if needed.

10. The program ensures that the PDF generation is a one-time operation to prevent overwriting existing PDFs with the same name by checking the `pdf_generated` flag.
![image](https://github.com/ksparsh443/InvoiceGenerator/assets/84833857/3da08d8e-77d9-4726-ac0b-e4d575128e3e)


YOU CAN CUSTOMISE THE INPUT AND UI BASED ON THE REQUIREMENTS AND NEEDS.
