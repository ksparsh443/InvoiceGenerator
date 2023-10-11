import re
import tkinter as tk
from tkinter import simpledialog
from tkinter import messagebox
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

# Function to validate phone number format
def validate_phone_number(phone_number):
    return re.match(r'^\d{10}$', phone_number)

# Function to validate email address format
def validate_email(email):
    return re.match(r'^[A-Za-z0-9._%+-]+@(gmail\.com|yahoo\.com|hotmail\.com)$', email)

# Flag to track whether PDF has been generated
pdf_generated = False

# Function to create a PDF from user input
def create_pdf():
    global pdf_generated
    if pdf_generated:
        messagebox.showinfo("PDF Already Generated", "PDF has already been generated. Please do not duplicate.")
        return

    full_name_booking_id = full_name_booking_id_entry.get()
    complete_address = complete_address_entry.get()
    primary_contact_number = primary_contact_number_entry.get()

    while not validate_phone_number(primary_contact_number):
        primary_contact_number = simpledialog.askstring("Invalid Input", "Invalid phone number format. Please enter a 10-digit numeric phone number:")

    secondary_contact_number = secondary_contact_number_entry.get()
    email_id = email_id_entry.get()

    while not validate_email(email_id):
        email_id = simpledialog.askstring("Invalid Input", "Invalid email address format. Please enter an address ending with @gmail.com, @yahoo.com, or @hotmail.com:")

    joining_date = joining_date_entry.get()
    package_description = package_description_entry.get()
    area = area_entry.get()

    # Create a PDF file with proper indentation
    pdf_file_name = f"{full_name_booking_id.split()[0]}_details.pdf"

    # Create a canvas
    c = canvas.Canvas(pdf_file_name, pagesize=letter)
    text_origin_x = 100
    text_origin_y = 700
    c.setFont("Helvetica-Bold", 12)
    c.setFillColorRGB(1, 1, 1)  # Text color: white
    c.setFillColorRGB(0, 0, 0)  # Background color: black

    # Define the message with proper indentation
    message = f"Full Name & Booking ID : {full_name_booking_id}\n" \
              f"Complete Address : {complete_address}\n" \
              f"Primary contact number (for sms, WhatsApp and calls) : {primary_contact_number}\n" \
              f"Secondary contact number (if any) : {secondary_contact_number}\n" \
              f"Email ID : {email_id}\n" \
              f"Joining date : {joining_date}\n" \
              f"Package Description : {package_description}\n" \
              f"Area : {area}"

    # Split the message into lines
    lines = message.split("\n")
    line_height = 14  # Adjust this value for proper line spacing

    # Draw each line with indentation
    for line in lines:
        c.drawString(text_origin_x, text_origin_y, line)
        text_origin_y -= line_height  # Move down to the next line

    c.save()

    pdf_generated = True
    messagebox.showinfo("PDF Generated", f"PDF file '{pdf_file_name}' created with user details.")

# Function to reset the form
def reset_form():
    global pdf_generated
    pdf_generated = False
    full_name_booking_id_entry.delete(0, 'end')
    complete_address_entry.delete(0, 'end')
    primary_contact_number_entry.delete(0, 'end')
    secondary_contact_number_entry.delete(0, 'end')
    email_id_entry.delete(0, 'end')
    joining_date_entry.delete(0, 'end')
    package_description_entry.delete(0, 'end')
    area_entry.delete(0, 'end')

# Create a Tkinter window
root = tk.Tk()
root.title("User Information to PDF")
root.configure(bg="black")  # Background color: black

# Create and configure form labels
font_style = ("Helvetica", 12, "bold")
label_color = "white"
label_bg = "black"

labels = ["Full Name & Booking ID:", "Complete Address:", "Primary contact number:",
          "Secondary contact number:", "Email ID:", "Joining date:", "Package Description:", "Area:"]

# Create a frame for the form and center-align it
form_frame = tk.Frame(root, bg="black")
form_frame.pack(padx=20, pady=20)

for i, label_text in enumerate(labels):
    label = tk.Label(form_frame, text=label_text, font=font_style, fg=label_color, bg=label_bg, anchor="w")
    label.grid(row=i, column=0, sticky="w", padx=(0, 10), pady=10)

# Create and configure form entry fields
entry_bg = "white"

full_name_booking_id_entry = tk.Entry(form_frame, font=font_style, bg=entry_bg)
full_name_booking_id_entry.grid(row=0, column=1, padx=(0, 10), pady=10, sticky="ew")

complete_address_entry = tk.Entry(form_frame, font=font_style, bg=entry_bg)
complete_address_entry.grid(row=1, column=1, padx=(0, 10), pady=10, sticky="ew")

primary_contact_number_entry = tk.Entry(form_frame, font=font_style, bg=entry_bg)
primary_contact_number_entry.grid(row=2, column=1, padx=(0, 10), pady=10, sticky="ew")

secondary_contact_number_entry = tk.Entry(form_frame, font=font_style, bg=entry_bg)
secondary_contact_number_entry.grid(row=3, column=1, padx=(0, 10), pady=10, sticky="ew")

email_id_entry = tk.Entry(form_frame, font=font_style, bg=entry_bg)
email_id_entry.grid(row=4, column=1, padx=(0, 10), pady=10, sticky="ew")

joining_date_entry = tk.Entry(form_frame, font=font_style, bg=entry_bg)
joining_date_entry.grid(row=5, column=1, padx=(0, 10), pady=10, sticky="ew")

package_description_entry = tk.Entry(form_frame, font=font_style, bg=entry_bg)
package_description_entry.grid(row=6, column=1, padx=(0, 10), pady=10, sticky="ew")

area_entry = tk.Entry(form_frame, font=font_style, bg=entry_bg)
area_entry.grid(row=7, column=1, padx=(0, 10), pady=10, sticky="ew")

# Create buttons to trigger the PDF generation and reset the form
generate_pdf_button = tk.Button(form_frame, text="Generate PDF", font=font_style, command=create_pdf)
generate_pdf_button.grid(row=8, column=0, columnspan=2, pady=10, sticky="ew")

reset_button = tk.Button(form_frame, text="Reset Form", font=font_style, command=reset_form)
reset_button.grid(row=9, column=0, columnspan=2, pady=10, sticky="ew")

root.mainloop()
