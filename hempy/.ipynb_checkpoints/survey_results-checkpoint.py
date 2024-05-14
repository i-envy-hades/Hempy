import matplotlib.pyplot as plt

def plot_consumption_percentage():
    """
    Plots a bar chart of consumption percentage against different consumption frequencies.

    Parameters:
    percentage (list): A list of percentages.
    consummation (list): A list of consummation frequencies corresponding to the percentages.

    Returns:
    Displays a bar chart.
    """
    percentage = [9.3, 20.9, 4.7, 14.0, 18.6, 32.6]
    consummation = ["everyday", "1-4 times per week", "once a month", "once every 2-4 months", "rarely", "never"]
    # Create a figure and a set of subplots
    fig, ax = plt.subplots()
    
    # Create a bar chart
    ax.bar(consummation, percentage, color='green')
    
    # Set title and labels
    ax.set_title('Consumption Percentage')
    ax.set_xlabel('Consummation')
    ax.set_ylabel('Percentage')
    
    # Rotate labels for better readability if needed
    plt.xticks(rotation=45, ha='right')
    
    # Show the plot
    plt.show()

plot_consumption_percentage()

def plot_time_vs_age():
    """
    Plots a line graph of the time of effect as a function of age.

    Parameters:
    age (list): A list of ages.
    time (list): A list of times corresponding to each age.

    Returns:
    Displays a line graph.
    """
    age = [19, 20, 21, 22, 23, 24, 26]
    time = [1, 5, 10, 15, 30, 120, 60]
    # Create a figure and a set of subplots
    fig, ax = plt.subplots()
    
    # Plot the age vs time data
    ax.plot(age, time, marker='o', linestyle='-', color='b')
    
    # Set title and labels for the axes
    ax.set_title('Time of the Effect in function of Age')
    ax.set_xlabel('Age')
    ax.set_ylabel('Time (in minutes)')
    
    # Enable grid
    ax.grid(True)
    
    # Show the plot
    plt.show()

plot_effect_time_in function_of_age()
