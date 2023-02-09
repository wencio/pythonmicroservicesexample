# Authentication Service
def authenticate_user(username, password):
    # Validate user credentials
    if valid_credentials(username, password):
        return generate_token(username)
    else:
        raise Exception("Invalid credentials")

# Payment Service
def process_payment(payment_details, token):
    # Validate token
    if not valid_token(token):
        raise Exception("Unauthorized")

    # Process payment
    if successful_payment(payment_details):
        return "Payment processed successfully"
    else:
        raise Exception("Payment failed")

# Main Application
def place_order(order_details, username, password):
    # Authenticate user
    token = authenticate_user(username, password)

    # Process payment
    payment_status = process_payment(order_details["payment"], token)

    # Return success message
    return "Order placed successfully. " + payment_status
