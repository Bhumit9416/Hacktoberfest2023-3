import pyjokes

def get_random_joke():
    joke = pyjokes.get_joke()
    return joke

if __name__ == "__main__":
    print("Here's a random joke for you:")
    joke = get_random_joke()
    print(joke)
