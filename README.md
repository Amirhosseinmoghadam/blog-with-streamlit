# Personal Blog using Streamlit

This is a simple personal blog application built with Streamlit and SQLite. Users can read articles and submit their own articles with images.

## Features

- Display a list of articles with titles, authors, and images.
- Submit new articles with a title, content, author name, and an optional image.
- Articles are stored in an SQLite database.
- Responsive design with RTL support for Persian text.

### Installation Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/Amirhosseinmoghadam/Protected-Exam.git
   
   ```
2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate   # For Linux/macOS
   venv\Scripts\activate      # For Windows
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Running the Application
   ```bash
    streamlit run blog.py
   ```


## Project Structure
    📂 blog_project
    ├── 📄 blog.py           # Main application file
    ├── 📄 requirements.txt  # Required dependencies
    ├── 📂 uploads           # Folder for storing uploaded images
    └── 📄 README.md         # Project documentation


## License
This project is licensed under [MIT License](LICENSE).

## Contact Us
For questions or feedback, please contact [Amirhosseinbavafa32@gmail.com].
