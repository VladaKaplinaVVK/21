from classes import склад, магазин, Request
while True:
    user_text = input("Введите команду:\n")


    print(f"В склад хранится: {склад}")
    #print(f"В магазин хранится: {storage_2}")
    print(f"В магазин хранится: {магазин}")

    if user_text == "стоп":
        break
    else:
        req = Request(user_text)
        req.move()


