phone_book = {
    "Airtel": "016864.....",
    "Teletalk": "015345.....",
}

print("01.", phone_book.keys())
print("02.", phone_book.values())
print("03.", phone_book.get("Airtel"))
print("04.", phone_book["Airtel"])

phone_book["Teletalk2"] = "015345....."
print("05.", phone_book.keys())

del phone_book["Teletalk2"]
print("06.", phone_book.keys())

print("07.", phone_book)

phone_book.clear()
print("08.", phone_book)


