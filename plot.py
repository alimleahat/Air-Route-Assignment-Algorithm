import matplotlib.pyplot as plt

def plot_time_series(x, y, title, xlabel, ylabel, stats=None):
    # Create a new figure
    plt.figure()
    
    # Plot the data
    plt.plot(x, y)
    
    # Add labels
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    
    # Add statistics box 
    if stats:
        mean = stats[0]
        std = stats[1]
        skew = stats[2]
        
        # Create text with stats
        stats_text = "Mean=" + str(round(mean, 1))
        stats_text += "\nStd=" + str(round(std, 1))
        stats_text += "\nSkew=" + str(round(skew, 1))
        
        # Position text in upper right corner
        plt.text(0.95, 0.95, stats_text,
                 horizontalalignment='right',
                 verticalalignment='top',
                 transform=plt.gca().transAxes)
    
    plt.tight_layout()
    
    # Display the plot
    plt.show()


def plot_bar(labels, values, title, xlabel, ylabel, stats=None):
    # Create a new figure
    plt.figure()
    
    # Create bar chart
    plt.bar(labels, values)
    
    # Add labels
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    
    # Add statistics box if provided
    if stats:
        mean = stats[0]
        std = stats[1]
        skew = stats[2]
        
        # Create text with stats
        stats_text = "Mean=" + str(round(mean, 1))
        stats_text += "\nStd=" + str(round(std, 1))
        stats_text += "\nSkew=" + str(round(skew, 1))
        
        # Position text in upper right corner
        plt.text(0.95, 0.95, stats_text,
                 horizontalalignment='right',
                 verticalalignment='top',
                 transform=plt.gca().transAxes)
    
    # Rotate x-axis labels so they don't overlap
    plt.xticks(rotation=90)
    
    plt.tight_layout()
    
    # Display the plot
    plt.show()