import parser_data
from plot_data import plot_data

def segment_climbing_walking(data):
    """
    Segment the data to isolate only the climbing activity.

    While collecting data on stairs, there were times when walking (flat surface) was mixed in.
    This function removes parts of the data corresponding to walking and keeps only climbing data.

    Returns:
        A list of tuples (x, y, z) corresponding to climbing only.
    """

    print('Segmenting climbing from walking...')
    plot_data(data)

    # TODO: Write your algorithm here to separate climbing data from walking data
    # NOTE: Do not simply use timestamps to cut the data.
    #       Instead, detect climbing segments based on patterns in the accelerometer signals

    return data  # Currently returning unsegmented data

def count_steps(data):
    """
    Count the number of steps from the segmented climbing data.

    Args:
        data: A list of (x, y, z) accelerometer tuples.

    Returns:
        The number of steps detected.
    """
    print('Counting steps...')
    num_steps = 0

    # TODO: Write your step-counting logic here

    return num_steps

def main():
    """Main function to load, segment, and count steps from accelerometer data."""
    file_name = "test.csv"  # Change this to your actual data file
    data = parser_data.get_data(file_name)
    segmented_data = segment_climbing_walking(data)
    number_of_steps = count_steps(segmented_data)
    print("Number of steps counted: {0:d}".format(number_of_steps))

if __name__ == "__main__":
    main()
