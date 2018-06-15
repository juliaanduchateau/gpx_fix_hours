import sys
import re
import argparse


parser = argparse.ArgumentParser(description="Fix time difference in a gpx file.")
parser.add_argument("input_file", type=str, help="The gpx file to work on")
parser.add_argument("-o", "--output", type=str, default="output.gpx", help="Name of the output file (default: 'output.gpx')")
parser.add_argument("-t", "--time", type=int, default=1, help="Time difference in hours to add/substract (default: 1)")
args = parser.parse_args()

try:
    file                = args.input_file                              # Open non-optional argument as file
    new_file_name       = args.output                                  # Set output file name

    lines               = file.read().split("<trkpt")                   # Read in the text and split

    new_lines           = list()                                        # Create a list to store the edited lines
    new_lines.append(lines[0])                                          # Add the first line, this one does not need to be changed
    for i in range(1,len(lines)):                                       # Loop from second line to last
        string          = "<trkpt" + lines[i]                           # Prefix each line with data lost due splitting
        hour            = int(re.findall("T..:..:..", string)[0][1:3])  # Extract "Thh:mm:ss", slice it to "hh" and convert to integer
        hour            += args.time                                    # Add time difference
        hour_string     = "T" + str(hour) + ":"                         # Prefix with "T" and suffix with ":" to replace "Thh:" below
        string          = re.sub("T..:", hour_string, string)           # Substitute old hour with new hour
        new_lines.append(string)                                        # Append the line to the list
    
    new_file            = open(new_file_name,'w')                       # Create new file to write to
    for line in new_lines:
        _               = new_file.write(line)                          # Write every line
    new_file.close()                                                    # Close the file
    print("Done")
    print("Output is saved in {}".format(new_file_name))
except:
    print("There was an error")
