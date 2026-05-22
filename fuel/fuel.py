def main():

    while True:
        try:
            fraction = input("Fraction: ")
            x, y = fraction.split("/")
            x = int(x)
            y = int(y)

            if y == 0 or x > y or x < 0 or y < 0 :
                continue

            z =round(((x/y)*100))


            if z <= 1:
                print("E")
                break

            elif z >= 99:
                print('F')
                break
            else:
                print(f"{z}%")
                break


        except ValueError:
            pass
        except ZeroDivisionError:
            pass






main()
