from plot_data import plot_data
import parser_data

def count_steps(data):
    """Plot accelerometer data and count the number of steps."""
    print("Accelerometer data graph:")
    plot_data(data)

    num_steps = 0

    # TODO: Add your step-counting logic here
    # Example idea (not implemented): Detect peaks in vertical acceleration

    return num_steps

def main():
    """Main function to load data, count steps, and display the result."""
    file_name = "test.csv"  # Change this to your actual file name
    data = parser_data.get_data(file_name)
    number_of_steps = count_steps(data)
    print("Number of steps counted: {0:d}".format(number_of_steps))

if __name__ == "__main__":
    main()
