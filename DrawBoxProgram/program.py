import drawableBox

def main():
    vyska = int(input("Zadejte vysku: "))
    delka = int(input("Zadejte delku krabice: "))
    print(drawableBox.drawBox(vyska, delka))


if __name__ == "__main__":
    main()