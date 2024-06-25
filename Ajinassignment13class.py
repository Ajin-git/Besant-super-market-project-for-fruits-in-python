Company_Name="Besant Himalayas Fruits"
width= 60
Address= "Anna Salai, The Island, Park Town, Chennai, Tamil Nadu 600003"
centered_text = Company_Name.center(width)
#centered_text = f"{Company_Name:^{width}}"
print(centered_text)
print(Address)

#Use Library Module
import datetime
x=datetime.datetime.now()
print(x)



store_items_text=("items---> \n 1kg apples=230  Oranges=160  1Kg Bannana=45 1kg Grapes=90 \n Pomegranate=235  mango=120  jackfruit=510 pineapple=125  ")
print(store_items_text)

import smtplib

def store_items():
    # Prices of items
    prices = {
        "apples": 230,
        "bananas": 45,
        "oranges": 100,
        "Grapes": 90,
        "Pomegranate": 235,
        "mango" : 120,
        "jackfruit": 510,
        "pineapple": 125
    }

    # Available store items
    store_items = list(prices.keys())

    # Initialize total purchase amount
    grand_total = 0

    while True:
        your_order = input("Enter the product name you want to buy (or 'done' to finish): ").strip().lower()
        if your_order == 'done':
            break

        if your_order in store_items:
            print(f"Yes, {your_order.capitalize()} is available in store.")
            how_many_items = int(input(f"How many {your_order.capitalize()} do you want? ").strip())
            total = prices[your_order] * how_many_items
            grand_total += total
            print(f"The price for one {your_order.capitalize()} is: {prices[your_order]}")
            print(f"Subtotal for {your_order.capitalize()}: {total}")
        else:
            print(f"Sorry, {your_order.capitalize()} is not available in store.")

    # Calculate GST
    print(f"Your total is {grand_total}")
    GST = (grand_total / 100) * 5
    print(f"GST (5%): {GST}")
    total_amount = grand_total + GST
    print(f"Your Grand Total is {total_amount:.2f}")

    # Send email with the bill
    email_sending(total_amount)

def email_sending(total_amount):
    print("\nGive your email address to send the bill.")
    customer_email = input("Enter your email id: ").strip()

    # SMTP Configuration
    smtp_server = "smtp.gmail.com"
    smtp_port = 587
    sender_email = "kamalamamala513@gmail.com"  # 
    sender_password = "gktr mipy pxqf rfcm"  # 

    # Email content
    subject = "Your Grocery Store Bill"
    body = (f"Thank you for shopping with {Company_Name}!\n\n"
            f"Your total bill amount is: {total_amount:.2f} INR\n\n"
            f"{Address}")


    # Try to send the email
    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, customer_email, f"Subject: {subject}\n\n{body}") #how to add company name in mail
        server.quit()
        print("Email sent successfully to", customer_email)
    except Exception as e:
        print("Error sending email:", str(e))

# Start the grocery store process
store_items()




