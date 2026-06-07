# My first Python file from Colab
print("Hello from Google Colab!")

def hello_world():
    return "Pushed to GitHub successfully!"

# Now push it
%cd /content/machine-learning
!git add first_file.py
!git commit -m "Initial commit: Add first Python file"
!git push origin main
