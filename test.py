import numpy as np  # Import numpy with common alias

import parser_data
from plot_data import plot_data

def main():
    data = parser_data.get_data("test.csv")
    plot_data(data)

if __name__ == "__main__":
    main()
