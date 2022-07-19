# Name processor
# Jeremy Bargy
# 4/12/20

##Write a program which asks for the user's first and last name (in a single prompt).
##Then displays the name to the user in proper case. The format for proper case is the first letter of the user's
##first name and last name is capitalized and the remaining letters are lower case.
##For example, the user enters wENdy PAYne the program will display Wendy Payne.
##Remember the program will run as many times as the user wishes.


def main():
    another = 'y'

    welcome()

    while another == 'y' or another == 'Y':

        userName = getName()
        print('User name is obtained..')

        #copy string with all lower cased letters
        fullName = userName.lower()
        print('User name is being processed..')
        
        #find the space between the names using the index position of the space beween names
        position = fullName.find(' ')
        print('First name and last name found..')
        
        #create first name variable with the index position of the space between names
        firstName = fullName[0: position]
        #create last name variable with the index position of the space between names
        lastName = fullName[position: ]
        print('First name and last name being processed..')
        #strip the leading white space character left from the user name input on the last name variable
        lastName = lastName.lstrip()
        print('Processing names are complete..\n\n\n')
        
        print('Processed user name\n')
        print('--------------------\n')
        print(firstName.capitalize() , lastName.capitalize())

        # Determine whether the user wants to add
        # another record to the file.
        print('\nIs there another user?')
        another = input('Y = yes, anything else = no: \n')
        #validate input
        while another !='Y' and another !='y' and another!='N' and another !='n':
            print('Error: please enter Y for yes, anything else for no.')
            another = input('Y = yes, anything else = no: \n')

    print('Thanks for using our program.')
    print('Goodbye')
    
def welcome():

    beginSequence= 'y'       #str
    
    print('\n\t\t\t\tHello Users!\n\t\t\t\t---------------')
    print('Thank you for taking the time to use this program.')
    print('The program was made by Jeremy Bargy.')
    print('Last update April 2020')

    #Display description of program
    print('\n\t\t\t\tInstructions\n\t\t\t\t------------')
    print('The program being used is designed to ask a user for their name and display the name in a proper format of the first letters of their names\' capitalized.\n')
    print('For example, the user enters wENdy PAYne the program will display Wendy Payne.\n')
    print('The program will run as many times as the users needs.\n\n\n')

    #loop until user had read instructions
    beginSequence = input('Begin program?\nPlease enter Y for yes\n')
    while not(beginSequence == 'Y' or beginSequence == 'y') or beginSequence=='' or beginSequence== ' ':
        print('Error: please read the instructions and enter "Y" for yes to begin: \n')
        beginSequence= input('Begin program? \n')

def getName():      #define get name function
    # Get user name
    userName = input('Please enter in your full name, first and last: \n')
    #validate sting
    while userName.isdigit():
        print('Error: incorrect input:')
        userName =input('Please your full name: \n')
    return userName

main()
