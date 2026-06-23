"""
Random User Generator - Main Application
This application fetches and displays random user profiles from the Random User API.
"""

import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import requests
from io import BytesIO
import json
import webbrowser

class RandomUserGenerator:
    def __init__(self, root):
        self.root = root
        self.root.title("Random User Generator")
        self.root.geometry("500x700")
        self.root.resizable(False, False)
        self.root.configure(bg='#f0f0f0')
        
        # API URL
        self.api_url = "https://randomuser.me/api/"
        
        # Current user data
        self.current_user = None
        self.current_image = None
        
        # Setup UI
        self.setup_ui()
        
        # Load first user
        self.fetch_random_user()
    
    def setup_ui(self):
        """Setup the user interface"""
        # Main frame
        main_frame = tk.Frame(self.root, bg='#f0f0f0', padx=20, pady=20)
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Title
        title_label = tk.Label(
            main_frame, 
            text="Random User Generator", 
            font=('Arial', 20, 'bold'),
            bg='#f0f0f0',
            fg='#2c3e50'
        )
        title_label.pack(pady=(0, 20))
        
        # Profile frame (for avatar and info)
        self.profile_frame = tk.Frame(
            main_frame, 
            bg='white', 
            relief=tk.RAISED, 
            bd=2,
            padx=20,
            pady=20
        )
        self.profile_frame.pack(fill=tk.BOTH, expand=True, pady=(0, 20))
        
        # Avatar image
        self.avatar_label = tk.Label(
            self.profile_frame, 
            bg='white',
            relief=tk.SUNKEN,
            bd=1
        )
        self.avatar_label.pack(pady=(0, 15))
        
        # User info frame
        info_frame = tk.Frame(self.profile_frame, bg='white')
        info_frame.pack(fill=tk.BOTH, expand=True)
        
        # Name
        self.name_label = tk.Label(
            info_frame,
            text="Name: ",
            font=('Arial', 14, 'bold'),
            bg='white',
            fg='#2c3e50'
        )
        self.name_label.pack(anchor='w', pady=2)
        
        # Gender
        self.gender_label = tk.Label(
            info_frame,
            text="Gender: ",
            font=('Arial', 12),
            bg='white',
            fg='#34495e'
        )
        self.gender_label.pack(anchor='w', pady=2)
        
        # Email
        self.email_label = tk.Label(
            info_frame,
            text="Email: ",
            font=('Arial', 12),
            bg='white',
            fg='#34495e',
            wraplength=350
        )
        self.email_label.pack(anchor='w', pady=2)
        
        # Phone
        self.phone_label = tk.Label(
            info_frame,
            text="Phone: ",
            font=('Arial', 12),
            bg='white',
            fg='#34495e'
        )
        self.phone_label.pack(anchor='w', pady=2)
        
        # Location
        self.location_label = tk.Label(
            info_frame,
            text="Location: ",
            font=('Arial', 12),
            bg='white',
            fg='#34495e',
            wraplength=350
        )
        self.location_label.pack(anchor='w', pady=2)
        
        # Age/DOB
        self.dob_label = tk.Label(
            info_frame,
            text="Date of Birth: ",
            font=('Arial', 12),
            bg='white',
            fg='#34495e'
        )
        self.dob_label.pack(anchor='w', pady=2)
        
        # Nationality
        self.nat_label = tk.Label(
            info_frame,
            text="Nationality: ",
            font=('Arial', 12),
            bg='white',
            fg='#34495e'
        )
        self.nat_label.pack(anchor='w', pady=2)
        
        # Buttons frame
        button_frame = tk.Frame(main_frame, bg='#f0f0f0')
        button_frame.pack(fill=tk.X, pady=(0, 10))
        
        # Generate button
        generate_btn = tk.Button(
            button_frame,
            text="Generate New User",
            command=self.fetch_random_user,
            font=('Arial', 12, 'bold'),
            bg='#3498db',
            fg='white',
            padx=20,
            pady=10,
            relief=tk.RAISED,
            bd=2,
            cursor='hand2'
        )
        generate_btn.pack(side=tk.LEFT, padx=5, fill=tk.X, expand=True)
        
        # Save button
        save_btn = tk.Button(
            button_frame,
            text="Save User Info",
            command=self.save_user_info,
            font=('Arial', 12, 'bold'),
            bg='#2ecc71',
            fg='white',
            padx=20,
            pady=10,
            relief=tk.RAISED,
            bd=2,
            cursor='hand2'
        )
        save_btn.pack(side=tk.RIGHT, padx=5, fill=tk.X, expand=True)
        
        # Bottom info
        info_label = tk.Label(
            main_frame,
            text="Powered by randomuser.me API",
            font=('Arial', 9),
            bg='#f0f0f0',
            fg='#7f8c8d'
        )
        info_label.pack()
    
    def fetch_random_user(self):
        """Fetch a random user from the API"""
        try:
            # Show loading state
            self.avatar_label.config(text="Loading...", image='')
            self.root.update()
            
            # Make API request
            response = requests.get(self.api_url, timeout=10)
            response.raise_for_status()
            
            data = response.json()
            user = data['results'][0]
            self.current_user = user
            
            # Display user info
            self.display_user_info(user)
            
            # Load and display avatar
            self.load_avatar(user['picture']['large'])
            
        except requests.exceptions.RequestException as e:
            messagebox.showerror(
                "Error",
                f"Failed to fetch user data.\nError: {str(e)}"
            )
            self.avatar_label.config(text="⚠ Error loading")
        except Exception as e:
            messagebox.showerror(
                "Error",
                f"An unexpected error occurred.\nError: {str(e)}"
            )
    
    def load_avatar(self, url):
        """Load and display avatar image from URL"""
        try:
            response = requests.get(url, timeout=10)
            response.raise_for_status()
            
            img_data = response.content
            img = Image.open(BytesIO(img_data))
            img = img.resize((150, 150), Image.Resampling.LANCZOS)
            
            self.current_image = ImageTk.PhotoImage(img)
            self.avatar_label.config(image=self.current_image, text='')
            
        except Exception as e:
            self.avatar_label.config(
                text="⚠ Failed to load image",
                image=''
            )
            print(f"Error loading avatar: {e}")
    
    def display_user_info(self, user):
        """Display user information in the UI"""
        name = f"{user['name']['title']}. {user['name']['first']} {user['name']['last']}"
        gender = user['gender'].capitalize()
        email = user['email']
        phone = user['phone']
        location = f"{user['location']['city']}, {user['location']['state']}, {user['location']['country']}"
        dob = f"{user['dob']['date'][:10]} (Age: {user['dob']['age']})"
        nationality = user['nat']
        
        self.name_label.config(text=f"Name: {name}")
        self.gender_label.config(text=f"Gender: {gender}")
        self.email_label.config(text=f"Email: {email}")
        self.phone_label.config(text=f"Phone: {phone}")
        self.location_label.config(text=f"Location: {location}")
        self.dob_label.config(text=f"Date of Birth: {dob}")
        self.nat_label.config(text=f"Nationality: {nationality}")
    
    def save_user_info(self):
        """Save the current user information to a JSON file"""
        if not self.current_user:
            messagebox.showwarning("Warning", "No user data to save!")
            return
        
        try:
            # Generate filename with user's name
            name = self.current_user['name']
            filename = f"user_{name['first']}_{name['last']}.json".lower()
            
            # Save to file
            with open(filename, 'w') as f:
                json.dump(self.current_user, f, indent=2)
            
            messagebox.showinfo(
                "Success",
                f"User information saved to:\n{filename}"
            )
            
        except Exception as e:
            messagebox.showerror(
                "Error",
                f"Failed to save user data.\nError: {str(e)}"
            )

def main():
    """Main entry point of the application"""
    root = tk.Tk()
    app = RandomUserGenerator(root)
    root.mainloop()

if __name__ == "__main__":
    main()
