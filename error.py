def Calc_square_root(n):
    from math import sqrt
    if n < 0:
        raise ValueError("Cannot use a negetive")
    answer = sqrt(n)
    return answer

def main():
    try:
        print(Calc_square_root(-9))
    except ModuleNotFoundError:
        print("function nto found")
    except ValueError:
        print("Cannot use negetive number")
    except:
        print("Something else went wrong")
    print("End")



if __name__ == "__main__":
    main()


"""
Exceptions Raised
NameError
IndexError
IndentationError
TypeError
ModuleNotFound
"""