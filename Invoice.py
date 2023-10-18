
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import imageio
from tkinter import messagebox

template_messages = {
    1: """
Hello,
This side Sparsh from BROOMEES INDIA.

We are a young, new-age startup committed to bring you the perfect domestic-help for your home. Thank you for making a booking; we hope you have a pleasant experience with Broomees. 

As per our telephonic conversation, I am proceeding further with your booking. I will keep you posted on the booking status and will try to arrange a relevant helper profile for your requirements within the next 2-7 working days.

In case you have any queries, please feel free to reach me. I would be happy to assist you.

Best regards,
Sparsh
🌎https://broomees.com
☎: +91-8401-8401-42
📩: support@broomees.com
""",
    2: """
Hello,
This side Sparsh from BROOMEES INDIA.

We are a young, new-age startup committed to bring you the perfect domestic-help for your home. Thank you for making a booking; we hope you have a pleasant experience with Broomees. 

As per our telephonic conversation, I would request you to kindly pay the Subscription charges of Rs. Full Amount (with GST) for the services of a Service Name using the below mentioned payment options and share the payment screenshot with me for confirmation.

Once this is done, I will proceed further with your booking and will keep you posted on the booking status. I will also try to arrange a relevant helper profile as per your requirements within the next 2-7 working days.

In case you have any queries, please feel free to reach me. I would be happy to assist you.

Best regards,
Sparsh
🌎: https://broomees.com
☎: +91-8401-8401-42
📩: support@broomees.com
""",
    3: """
Hello,
This side Sparsh Kandpal from BROOMEES INDIA.

We have received your payment for the Subscription Amount : 7285.38.

As per our telephonic conversation, I am proceeding further with your booking. You will receive an Invoice and a Payment Receipt on your email. I will keep you posted on the booking status and will also try to arrange a relevant helper profile as per your requirements within the next 2-7 working days.

In case you have any queries, please feel free to reach me. I would be happy to assist you.

Best regards,
Sparsh Kandpal
🌎: https://broomees.com
☎: +91-8401-8401-42
📩: support@broomees.com
Terms and conditions: https://broomees.com/terms

""",
    4: """
Hello,
This is Sparsh from BROOMEES INDIA.

I am delighted to confirm your booking with Broomees. I've attempted to reach out to you regarding this matter but was unable to connect.

Could you please provide me with a suitable time for a call back, so that, I can proceed efficiently and finalize the details as soon as possible.

Thank you!

Best regards,
Sparsh
🌎: https://broomees.com
☎: +91-8401-8401-42
📩: support@broomees.com
""",
    5: """
Dear Valued Customer,

I hope this message finds you well. At Broomees, we are committed to providing top-notch domestic helper services, and your satisfaction is our utmost priority.

We are reaching out to you today to ask for a small favor. If you've been pleased with the services our domestic helpers have provided, we kindly request your help in spreading the word about Broomees. Your Personal Referral means the world to us and can make a significant difference in someone else's life.

Do you know of friends, family members, or colleagues who could benefit from the exceptional assistance and care that our domestic helpers offer? If so, we would be immensely grateful if you could refer them to Broomees. Your recommendation will not only help them find reliable help but also contribute to our mission of enhancing the lives of individuals and families.

Simply forward their Name, Contact Number, and Requirements to me. I will get in touch with them directly.

As a token of our appreciation, for every Successful Referral you make (i.e., if your Referral places a Booking and avails our services by paying for either 3/6/12 months' subscription)*, you'll receive a *Special Discount on your next service with Broomees.

Thank you for being a valued member of the Broomees family, and for helping us make a positive impact in our community. Your support means everything to us.

If you have any questions or need further information, please don't hesitate to reach out to me. I would be happy to assist you.

Regards,
Sparsh
🌎https://broomees.com
☎: +91-8401-8401-42
📩: support@broomees.com
""",
    6: """
Hi Sir/Ma'am, 
Hope you are doing well. 

I would like to share a final standpoint from our end. 

1. We have cancelled your booking upon your request. 

2. In case you wish to avail any other service, please feel free to place another booking on the website. 

3. An onboarding manager will call you and you will be required to pay a subscription fee again, because the last subscription that you availed has been cancelled. 

4. However, if you wish to resume the current subscription and we receive your approval on the same, we will start searching for a helper from that very date and follow the replacement policy of 10 days.

5. Also, our subscription cannot be paused or kept on hold at any moment during its tenure, so we will be providing you with the services for the number of days pending in the tenure on a pro-rata basis. 

In case you have any queries, please feel free to get in touch with me. I would be happy to help you.

Regards,
Sparsh
🌎https://broomees.com
☎: +91-8401-8401-42
📩: support@broomees.com
""",
    7: """
Hi Sir/Ma'am,
Thank you for your honest feedback.

I will make sure that the same is forwarded to the helper for her betterment.

However, in similar situations, our next steps of the process will be as follows:

1. We will forward this feedback to our trainer, and they will mediate it with the helper. They will also check if the current helper can be reassessed or not. If yes, we will do that and ask her to rejoin, because we believe in giving our helpers a Second Chance.

2. Since, it was just the first/second/third day of work, we would really appreciate it if you could allow the helper at least 3-5 days to adjust and adapt to the work at your location, because it might take a few more days for them to understand and respond accordingly in terms of work.

3. We will definitely inform her to follow all the basic hygiene measures. Please do not worry about this.

4. Despite this, in case she shows no signs of improvement, we will definitely provide you with a replacement helper within 10 days after this and make sure that the similar issues do not arise in the future.

This will be the basic protocol that we will be following. Please let us know if there is anything else that I can do to assist you better.

Regards,
Sparsh
🌎https://broomees.com
☎: +91-8401-8401-42
📩: support@broomees.com
""",
    8: """
Good afternoon Ma'am,
This side Sparsh from BROOMEES INDIA. I would like to connect and discuss with you over the All Rounder service you have selected, henceforth please let us know a suitable time when you will be available. I would be happy to assist you.

Best regards,
Sparsh
🌎https://broomees.com
☎: +91-8401-8401-42
📩: support@broomees.com
""",
    9: """
🔳🔳🔳🔳🔳🔳🔳🔳🔳🔳🔳🔳🔳

🔴Subscription Packages:

🔸FOR COOKS, BABYSITTERS & ALL-ROUNDERS: (For Home)

1. Basic Pack - 3 months: Rs. 4999 + 18% GST = Rs. 5898.82 (2 free replacements)

2. Best Seller Pack - 6 months: Rs. 6,499 + 18% GST = Rs. 7,668.82 (3 free replacements)

3. Super Saver Pack - 12 months: Rs. 9,919 + 18% GST = Rs. 11,704.42 (5 free replacements)

🔸FOR DOMESTIC HELPER: (For Home)

1. Basic Pack - 3 months: Rs. 3,599 + 18% GST = Rs. 4246.82 (2 free replacements)

2. Best Seller Pack - 6 months: Rs. 4,496 + 18% GST = Rs. 5305.28 (3 free replacements)

3. Super Saver Pack - 12 months: Rs. 5,920 + 18% GST = Rs. 6985.6 (5 free replacements)

🔸FOR JAPA: (For Home)

1. Part Time - 1 Kid - 1 month: Rs. 3,499 + 18% GST = Rs. 4128.82 (1 replacement)

2. Part Time - Twins - 1 month: Rs. 4,999 + 18% GST = Rs. 5898.82 (1 replacement)

3. Full Time - 1 Kid - 1 month: Rs. 4,979 + 18% GST = Rs. 5875.22 (1 replacement)

4. Full Time - Twins - 1 month: Rs. 7,499 + 18% GST = Rs. 8848.82 (1 replacement)

5. Full Time - 1 Kid - 2 months: Rs. 7,999 + 18% GST = Rs. 9438.82 (2 replacements)

6. Full Time - Twins - 2 months: Rs. 12,409 + 18% GST = Rs. 14,642.62 (2 replacements)

This needs to be paid to us before availing the services. After paying the subscription fee, our team will do all the verification and document work which can take approximately 2-7 working days to finalize it.

🔳🔳🔳🔳🔳🔳🔳🔳🔳🔳🔳🔳🔳

🔴Monthly Salary of the helper: Rs. (per month)

🔸FOR COOK, BABYSITTER, ALL-ROUNDER & DOMESTIC HELPER (Part Time) - You are requested to pay the salary directly to the helper before 1st of the upcoming month, and they can take 3 paid leaves in a month. If not taken, the per day salary for these 3 days needs to be paid in cash, along with the salary.

🔸FOR COOK, BABYSITTER, ALL-ROUNDER & DOMESTIC HELPER (Full Time) - You are requested to pay the salary to us on a separate salary invoice before 1st of the upcoming month, and they can take 2 paid leaves in a month. If not taken, the per day salary for these 2 days needs to be paid in cash, along with the salary.

🔸FOR JAPA (Part Time/Full Time) - You are requested to pay the salary in advance, along with the Subscription Fee on the same Invoice altogether.

🔳🔳🔳🔳🔳🔳🔳🔳🔳🔳🔳🔳🔳

🔴Payment details:

1) Payment Details for Bank Transfers:
Bank: ICICI SDA Branch
Bank Account: 182505000904
IFSC: ICIC0001825
Name: Broomees India Pvt Ltd
PAN: AAJCB6109K

2) UPI/Wallets:
Any UPI app: BROOMEESINDIAPRIVATELIMITED@ICICI (OR) 8401840142@OKBIZAXIS
GooglePay Number: 8401840142 (Broomees India Pvt Ltd)

🌎: https://broomees.com
☎: +91-8401-8401-42
📩: support@broomees.com
Terms & Conditions: www.broomees.com/terms
""",

 10: """
Good morning sir,
This side Sparsh from BROOMEES INDIA.

We are a young, new-age startup committed to bring you the perfect domestic-help for your home. Thank you for making a booking; we hope you have a pleasant experience with Broomees. 

I would be your onboarding manager for the booking of cook you have made, In case you have any queries, please feel free to reach me. I would be happy to assist you.

Best regards,
Sparsh
🌎: https://broomees.com
☎: +91-8401-8401-42
📩: support@broomees.com
Terms & Conditions: www.broomees.com/terms

"""



    # ... (existing templates here)
}

def copy_template():
    selected_template = template_number_var.get()
    if selected_template in template_messages:
        user_name = user_name_var.get()
        template_text = template_messages[selected_template].replace('Sparsh', user_name)
        root.clipboard_clear()
        root.clipboard_append(template_text)
        root.update()
        message = f"Template {selected_template}:\n\n{template_text}\n\nMessage copied to clipboard."
        messagebox.showinfo("Template Copied", message)
    else:
        messagebox.showerror("Invalid Template", "Please select a valid template number.")

# Function to reset the template selection
def reset_template():
    template_number_var.set(1)
    user_name_var.set('')

# Create the main window
root = tk.Tk()
root.title("Template Selector")
root.geometry("800x600")

# Load and set the background image
bg_image_path = "D:\\PERSONAL\\DOwnloads\\its-a-gaming-champ-too-it-adds-fun-and-challenge-upscaled.png"
bg_image = Image.open(bg_image_path)
bg_image = bg_image.resize((800, 600), Image.LANCZOS)
background_image = ImageTk.PhotoImage(bg_image)
background_label = tk.Label(root, image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

# Set the default template number to 1
template_number_var = tk.IntVar()
template_number_var.set(1)

# Create a label for template selection
template_label = tk.Label(root, text="Select a Template Number:", bg='black', fg='white', font=("Helvetica", 14))
template_label.place(relx=0.5, rely=0.1, anchor="center")

# Create a template selection dropdown
template_dropdown = tk.OptionMenu(root, template_number_var, *template_messages.keys())
template_dropdown.configure(bg='black', fg='white', font=("Helvetica", 14), highlightthickness=0, bd=0)
template_dropdown.place(relx=0.5, rely=0.15, anchor="center")

# Create a label for user's name
user_name_label = tk.Label(root, text="Enter your name:", bg='black', fg='white', font=("Helvetica", 14))
user_name_label.place(relx=0.5, rely=0.25, anchor="center")

# Create an entry for user's name
user_name_var = tk.StringVar()
user_name_entry = tk.Entry(root, textvariable=user_name_var, font=("Helvetica", 14), highlightthickness=0, bd=0)
user_name_entry.place(relx=0.5, rely=0.3, anchor="center")

# Create a copy button
copy_button = tk.Button(root, text="Copy Template", command=copy_template, bg='black', fg='white', font=("Helvetica", 14), highlightthickness=0, bd=0)
copy_button.place(relx=0.5, rely=0.4, anchor="center")

# Create a reset button
reset_button = tk.Button(root, text="Reset", command=reset_template, bg='black', fg='white', font=("Helvetica", 14), highlightthickness=0, bd=0)
reset_button.place(relx=0.5, rely=0.45, anchor="center")

# Start the GUI main loop
root.mainloop()
