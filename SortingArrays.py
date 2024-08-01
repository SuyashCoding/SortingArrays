def main():
    n = int(input("Enter the number of names you want to input: "))
    
    names_input = input(f"Enter {n} names separated by commas: ")
    
    names = names_input.split(',')
    
    if len(names) != n:
        print(f"Please enter {n} names.")
        return
    
    print("Choose a sorting option:")
    print("1) Sort the names alphabetically")
    print("2) Sort the names by their length")
    print("3) Sort the names based on the sum of their ASCII values")
    
    option = input("Enter the number corresponding to your choice: ")
    
    if option == '1':
        sorted_names = sorted(names)
    elif option == '2':
        sorted_names = sorted(names, key=len)
    elif option == '3':
        sorted_names = sorted(names, key=lambda name: sum(ord(char) for char in name))
    else:
        print("Invalid option selected.")
        return
    
    print("Sorted names:", sorted_names)

main()
