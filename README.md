# Secret Santa File Creator

## Description
This Python script facilitates the creation of files for organizing a Secret Santa game. It allows users to input participant names and assigns each participant a gift recipient. Results are saved in individual text files indicating group membership and assigned recipients.

## Requirements
- Python 3.x (latest version recommended)
- Dependencies:
  - `random`
  - `argparse`

## Installation
No installation steps are necessary beyond ensuring Python 3.x is installed on your system.

## Usage
1. **Help Menu**: Display the help menu with different input options:
   ```sh
   python secret_santa.py -h
   This command provides detailed usage instructions.
2. **Menu Mode**: Access a menu for guided input options:
   ```sh
   python secret_santa.py -m
   This interactive mode guides users through inputting participant names.
3. **File Mode**: Import participant names from a specific file:
   ```sh
   python secret_santa.py -f participants.txt
   Replace participants.txt with your file containing participant names.
4. **Group Division**: Specify the number of groups to divide participants into:
   ```sh
   python secret_santa.py -g 3
   Divides participants into 3 groups.

## Error Handling
- If the specified group size is incompatible with the number of participants, an error message will be displayed.
## Output
Upon successful execution:

- Participants will be assigned gift recipients.
- Individual text files for each participant will be saved in the folder, indicating group membership and assigned recipient.

## Known Issues
None at the moment.

## Contributing
Contributions are welcome! Fork the repository and submit pull requests. Report any issues or suggestions in the Issues section.

## License
This project is licensed under the MIT License. See the LICENSE file for more details.


