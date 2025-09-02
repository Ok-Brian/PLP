def calculate_discount(price, discount_percent):
    """
    Calculate the final price after applying a discount.
    Apply the discount only if discount_percent is 20% or higher.
    """
    if discount_percent >= 20:
        discount_amount = (discount_percent / 100) * price
        return price - discount_amount
    else:
        return price  # no discount applied


# --- Main Program ---
try:
    # Prompt the user for input
    original_price = float(input("Enter the original price of the item: "))
    discount = float(input("Enter the discount percentage: "))

    # Call the function
    final_price = calculate_discount(original_price, discount)

    # Print result
    if discount >= 20:
        print(f"Final price after {discount}% discount: {final_price:.2f}")
    else:
        print(f"No discount applied. Price remains: {final_price:.2f}")

except ValueError:
    print("Please enter valid numeric values for price and discount.")
