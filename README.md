# Student Management System
A simple system to manage student information including adding, viewing, updating, and deleting students, with support for saving and loading data from a file.

## Description
The Student Management System allows users to manage student records. It enables functionalities to add new students, view all students, update student information, delete students, and save the data to a file for future use. The system ensures that the student data is stored persistently in a file (`students.txt`) using a JSON-like format. Additionally, the system includes unit tests to validate the core features such as adding and deleting students, updating information, and saving/loading data from the file.

### Getting Started

### Dependencies
- Python 3.12 or higher
- `unittest` (for testing, comes with Python)
- `flake8` (for linting, optional)
- A code editor like VS Code, Sublime Text, or similar

### Installing
1. **Clone the repository in gitbash**:
   git clone https://github.com/AleksandraP98/student_management.git
   cd student_management
   
2. **Install flake8 (optional)**:
   pip install flake8

3. **Install any additional dependencies (if applicable, though none required at this time)**:
   pip install -r requirements.txt  # If you have a requirements.txt file

#### Executing the Program
To run the Student Management System:
1. Start the system:
   python student_management.py
   
2. You will be prompted with a menu that lets you:
* Add a new student
* View all students
* Update a student's information
* Delete a student by ID
* Save and exit the program

Example steps:
To add a student, choose option 1, then provide the student's details.
To view all students, choose option 2.
To update a student, choose option 3, enter the student ID, and then the attribute to update (e.g., name, age).
To delete a student, choose option 4, then enter the student ID.

##### Testing the Program Locally
1. **Unit Tests**: The system includes unit tests to validate the core features. These tests are located in the student_management_test.py file.

2. **Running the tests**: You can run the tests locally using Python’s built-in unittest framework:
   python -m unittest student_management_test.py
   
   This will execute all the tests defined in the student_management_test.py file and report any failures or successes.

###### Git Workflow for Merging Branches
**This project follows a standard Git workflow for development and testing. Below is the workflow for merging between branches**:

**Development (dev) Branch**:
All new features and changes should be made in the dev branch.
This is where you should push your changes after creating a new feature or fixing bugs.

**Testing (test) Branch**:
Once you've developed a feature on the dev branch, create a pull request to merge the changes into the test branch.
On the test branch, all new features will undergo automated testing via GitHub Actions (configured in .github/workflows/test.yml).

**Main (main) Branch**:
Once all tests on the test branch pass successfully, create a pull request to merge the changes into the main branch.
The main branch should always contain stable and tested code.

**Example Workflow**:
1. Create a new branch for a feature (from dev):
git checkout -b feature/new-feature dev

2. Work on the feature and commit changes:
   git add .
   git commit -m "Added new feature"

3. Push the feature branch to GitHub:
   git push origin feature/new-feature

4. Merge into the test branch:
   * Create a pull request from feature/new-feature to test.
   * Ensure all tests pass before merging.

5. Merge test into dev after successful tests:
   git checkout dev
   git pull origin dev
   git merge test
   git push origin dev

6. Merge dev into main after testing and validation:
   git checkout main
   git pull origin main
   git merge dev
   git push origin main


###### Help
If you encounter any issues, ensure that:

* Python 3.12+ is installed correctly.
* The required dependencies are installed (if using optional tools like flake8).
* Make sure your students.txt file is in the correct format if it's being loaded, or create a new one when running for the first time.
  
If you need help, you can view the program’s help message or check for common issues in the GitHub repository's issues section.

**Command to run if program contains helper info**:
python student_management.py --help

**Authors**
Aleksandra P

**Version history**
* 0.2: Various bug fixes and optimizations
* See commit change or release history for details.
* 0.1: Initial Release

**License**
MIT License

Copyright (c) [2024] [Aleksandra P]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.


## Acknowledgments

- **YouTube Tutorials**: A special thanks to various YouTube tutorials that helped me understand key concepts in Python, object-oriented programming, and version control. Specific tutorials like those from *Bro Code* and *Programing with Mosh* were incredibly helpful in learning Python best practices and understanding Git workflows.
  
- **Python Documentation**: The official [Python documentation](https://docs.python.org) was invaluable for understanding how to work with libraries, file handling, error handling, and testing. It provided detailed explanations and examples that made it easier to write clean and functional code.

- **Git Bash**: Thanks to [Git Bash](https://git-scm.com/) for making Git version control simple and intuitive. It was essential for managing the project repository and understanding Git commands, especially during the development and testing process.

- **Stack Overflow**: A big thank you to the [Stack Overflow](https://stackoverflow.com/) community. Many of the coding challenges I encountered were solved by browsing existing questions and answers on the platform.

- **GitHub**: Thanks to [GitHub](https://github.com/) for hosting my project and providing tools for version control, collaboration, and automated testing with GitHub Actions.

- **Open-Source Community**: Finally, a heartfelt thank you to the open-source community. Your contributions to various libraries and tools, as well as the shared knowledge in forums and documentation, have been an indispensable resource throughout this project.






