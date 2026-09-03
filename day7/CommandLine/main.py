import sys
import argument_module

print("\n===== 19. Command Line Arguments =====")

if len(sys.argv) >= 3:

    num1 = int(sys.argv[1])

    num2 = int(sys.argv[2])

    result = argument_module.add_numbers(num1, num2)

    print("Sum =", result)

else:

    print("Run like: python main.py 10 20")