
# importing random module
import random

#declaring dictionary to count durations of completion dates
project_durations = {
    '30_35':0,
    '36_38':0,
    '39_42':0,
}

# defining a function wich accept number of iterations as a parameter
def montecarlo_simulation(num_iterations):
    # assigning number of iterations to a another variable to check the liklyhood later
    total_number = num_iterations

    # running a while loop for number of iterations
    while num_iterations >= 1:
        # assigning a random number between 8 and 12 to activity A
        activity_a_days = random.randint(8,12);
        # assigning a random number between 10 and 14 to activity B
        activity_b_days = random.randint(10,14);
        # assigning a random number between 12 and 16 to activity C
        activity_c_days = random.randint(12,16);

        # adding each activity's date to get the total duration to complete the project
        total_days = activity_a_days + activity_b_days + activity_c_days;

        # checking weather total days are in the optimistic range
        if(total_days >= 30 and total_days <= 35):
            # if so increasing optimistic range total count by 1
            project_durations['30_35'] = project_durations['30_35'] + 1;
        # checking weather total days are in the mostlikely range
        if(total_days >= 36 and total_days <= 38):
            # if so increasing mostlikely range total count by 1
            project_durations['36_38'] = project_durations['36_38'] + 1
        # checking weather total days are in the pesimistic range
        if(total_days >= 39 and total_days <= 42):
            # if so increasing pesimistic range total count by 1
            project_durations['39_42'] = project_durations['39_42'] + 1

        # decreasing number of iteration by 1 so while loop will be stopped after running for the given number
        num_iterations = num_iterations - 1

    # dividing total optimistic count by total number of times to get the likelyhood of finishing project in optimistic range
    likelihood_30_35 = project_durations['30_35']/total_number
    # dividing total mostlikely count by total number of times to get the likelyhood of finishing project in mostlikely range
    likelihood_36_38 = project_durations['36_38']/total_number
    # dividing total pesimistic count by total number of times to get the likelyhood of finishing project in pesimistic range
    likelihood_39_43 = project_durations['39_42']/total_number

    # printing the likely hood of each duration as percentage and rounded to 1 decimal point
    print(f"Likelyhood of project compliting in 30 - 35 days : {round(likelihood_30_35 * 100,2)}")
    print(f"Likelyhood of project compliting in 36 - 38 days : {round(likelihood_36_38 * 100,2)}")
    print(f"Likelyhood of project compliting in 39 - 42 days : {round(likelihood_39_43 * 100,2)}")




if __name__ == '__main__':
    # taking the number of iterations as a input from the user
    iteration_count = input("Enter how many iterations do you want to run?(Press enter to run with default 500 iterations)\n")
    # checking if user enterd a number or want to go with default iterations
    if iteration_count != "":
        # if user entered a number changing string data type to integer
        iteration_count = int(iteration_count)
    # calling the function by passing number of iterations as a parameter
    montecarlo_simulation(iteration_count or 500)
    input("Press enter to exit ")

