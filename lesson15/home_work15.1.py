from loguru import logger
import argparse

def my_func(first, last, middle=""):
    try:
        if middle == True:
            result = f"{last.title()} {first.title()} {middle.title()}"
        else:
            result = f"{last.title()} {first.title()}"

        logger.info(f"Function executed successfully: {result}")
        return result

    except Exception as e:
        logger.error(f"Error in my_func: {e}")
        raise

def main():
    parser = argparse.ArgumentParser(description='Process some names.')
    parser.add_argument('first', type=str, help='First name')
    parser.add_argument('last', type=str, help='Last name')
    parser.add_argument('--middle', action='store_true', help='Include middle name')

    args = parser.parse_args()

    try:
        my_func_result = my_func(args.first, args.last, args.middle)
        print("Result:", my_func_result)
    except Exception as e:
        print("An error occurred:", e)

if __name__ == "__main__":
    main()


print(my_func("николай","глазков"))