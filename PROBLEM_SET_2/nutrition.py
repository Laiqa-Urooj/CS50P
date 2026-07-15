#Take input from user 
#user .lower to normalize input for mapping
#map the fruit name with calories 

fruit_dict = {
    "apple" : 130,
    "avocado" : 50,
    "banana" : 110,
    "cantaloupe" : 50,
    "grapefruit" : 60,
    "grapes" : 90,
    "honeydew melon" : 50,
    "kiwifruit" : 90,
    "lemon" : 15,
    "lime" : 20,
    "nectarine" : 60,
    "orange" : 80,
    "peach" : 60,
    "pear" : 100,
    "pineapple" : 50,
    "plums" : 70,
    "strawberries" : 50,
    "sweet cherries" : 100,
    "tangerine" : 50,
    "watermelon" : 80
}

def main() :
    fruit_name = input("Input : ")
    print(get_calories(fruit_name))
    
def get_calories(fruit_name) :
    fruit_name = fruit_name.lower()
    if fruit_name in fruit_dict :
        return fruit_dict[fruit_name]
            
main()