import parser_data
from plot_data import plot_data

def clean_data(data):
    """Clean the input data by removing garbage entries and saving the cleaned data."""
    print("Starting to clean the data...")

    # TODO: Write code here to remove garbage data


    file_name_clean = "walking_steps_clean.csv"
    print(f"Saving cleaned data to '{file_name_clean}'...")
    # TODO: Save cleaned_data to file_name_clean

def main():
    """Main function to load, clean, and process the data."""
    file_name = "walking_steps.csv"  # Adjusted path to suggest better file organization
    data = parser_data.get_data(file_name)  # Assuming data is something like [time, X, Y, Z]
    clean_data(data)

if __name__ == "__main__":
    main()