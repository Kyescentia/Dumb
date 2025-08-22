from utils.q1 import *

def main():
    print("A filename consists of a name and its extension (e.g., document.txt)")
    filename = input("Enter a filename: ")
    print() 

    try:
        with open(filename, 'r') as file:
            
            rect_number = 1 

            for line in file:
                cleaned_line = line.strip().replace('\t', ',')
                parts = cleaned_line.split(',')
                
                try:
                    width = float(parts[0])
                    height = float(parts[1])
                    
                    area = getArea(width, height)
                    perimeter = getPerimeter(width, height)
                    
                    print(f"Rectangle {rect_number}")
                    print(f"Width    : {width:.2f}")
                    print(f"Height   : {height:.2f}")
                    print(f"Area     : {area:.2f}")
                    print(f"Perimeter: {perimeter:.2f}")
                    print()
                    
                    rect_number += 1
                except:
                    pass

    except FileNotFoundError:
        print("Error: Something went wrong while opening the file!")
    except IOError:
        print("Error: Something went wrong while reading the file!")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()