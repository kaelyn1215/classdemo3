# Parking Fines Calculator

minutes = int(input("Enter the number of minutes over the time limit: "))
handicapped = input("Is the vehicle parked in a handicapped parking space? (yes/no): ")
# Calculate the parking fine
if minutes < 0:
    print("Invalid input. Minutes cannot be negative.")
else:
    if minutes == 0:
        fine = 0
    elif minutes <= 15:
        fine = 10
    elif minutes <= 30:
        fine = 20
    elif minutes <= 60:
        fine = 40
    else:
        fine = 75

    # Add handicapped parking fine
    if handicapped.lower() == "yes":
        fine += 150

    # Display the input and fine
    print("Minutes over the time limit:", minutes)
    print("Handicapped parking space:", handicapped)
    print(f"Fine due: ${fine:.2f}")
