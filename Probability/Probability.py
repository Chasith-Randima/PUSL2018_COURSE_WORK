
# importing random module
import random

# defining a variable to count situations all three childs are girls
all_girls_count = 0
# defining a variable to count atleast one child is a girl
least_onegirl_count = 0

# defining a function which accept number of iterations as a parameter
def probability_check(num_iterations):
    # making variables outside the functions available to use and manipulate inside the function
    global all_girls_count,least_onegirl_count
    # assigning number of iterations to a another variable to check the probability later
    total_iterations = num_iterations
    # running a while loop for given number of iterations
    while num_iterations >= 1:
        # assigning random number between 0 and 1 to child_one variable
        child_one = random.randint(0,1)
        # assigning random number between 0 and 1 to child_two variable
        child_two = random.randint(0,1)
        # assigning random number between 0 and 1 to child_three variable
        child_three = random.randint(0,1)

        # here on wards all the checks are done assuming 0 IS A GIRL and 1 IS A BOY

        # checking weather all three childs are girls (assigned random number equals to 0)
        if(child_one == 0 and child_two == 0 and child_three == 0):
            # if so increasing all_girs_count by 1
            all_girls_count = all_girls_count + 1
        # if above case is false checing weather at least one child is a girl (assinged random number equals to 0)
        elif(child_one == 0 or child_two == 0 or child_three == 0):
            # if so increasing least_onegirl_count by 1
            least_onegirl_count = least_onegirl_count + 1

        # decreasing number of iterations by 1 so while loop will be stopped after running for given number of iterations
        num_iterations = num_iterations - 1

    # dividing all three are girls count by total iterations count to get the probability of all three are childs
    all_three_probability = all_girls_count/total_iterations
    # dividing at least one child is a girl count by total iterations count to get the probability of at least one child is a girl
    least_one_probability = least_onegirl_count/total_iterations

    # printing the probability of all three childs are girls rounded to one decimal number
    print(f"Probability of all three childs are girls : {round(all_three_probability,2)}")
    # printing the probability of at least one child is girl rounded to one decimal number
    print(f"Probability of at least one child is  girl : {round(least_one_probability,2)}")



if __name__ == '__main__':
    # taking the number of iterations as a input from the user
    iteration_num = input("Enter how many iterations you want?(Press enter to go with default 1000 iterations)\n")
    # checking if user enterd a number or want to go with default iterations
    if(iteration_num != ""):
        # if user entered a number changing string data type to integer
        iteration_num = int(iteration_num)
    # calling the function by passing number of iterations as a parameter
    probability_check(iteration_num or 1000)
    input("Press enter to exit ")

