# django-final

Clone a Django Project from GitHub and Run


###Install the virtualenv

Step 1: Install the virtual environment by running the following command.
---------------------------------------------

Step 2: If you are using Unix/Linux/macOS run the following command in the terminal.

python3 -m pip install --user virtualenv
Step 3: If you are using windows the following command in the command prompt.

py -m pip install --user virtualenv
----------------------------------------------

Step 4: Create a virtual environment.

 Unix/Linux/macOS users run the following command 
python3 -m venv env
Windows users run the following command
py -m venv env
----------------------------------------------
Step 5: Activate the virtual environment and verify it

 Unix/Linux/macOS users run the following command 
source env/bin/activate
Windows users run the following command
.\env\Scripts\activate
If you have trouble in creating or activating the virtual environment refer to this article.

###Clone a GitHub Repository 
Copy the URL of the GitHub repository if you want to clone it in the tutorial we are using this repository. Run the git clone command in the terminal or git bash to clone the repository.

Syntax: git clone "URL of GitHub repository"
git clone "https://github.com/Hardik-Kushwaha/Face-Detection-Minor1"


###Deploy Django Project from GitHub
After the repository is cloned successfully change the directory to the recent clone repository in which the Django project is kept.

cd Face-Detection-Minor1
Install the requirements (if any). Most of the projects have requirements.txt file which specifies the requirements of that project, so let’s install the requirements of it from the file.

pip install -r requirements.txt

Run the Django server by running the below command.

python3 manage.py runserver
