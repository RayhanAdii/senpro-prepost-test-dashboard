# 📊 TIF Senpro Pre-Post-Test Data Viewer

A Streamlit web application for viewing and analyzing student pre and post test from CSV files with a clean, user-friendly interface.


## 🚀 How to Run

<!-- 1. **Install Python** (3.7 or higher) -->

1. Download Cleaned Dataset (minta rehan) and put it in data/interim directory

2. **Install required packages:**
   ```bash
   pip install -r requirements.txt
   ```



## ▶️ How to Run

1. **Open terminal/command prompt**

2. **Navigate to the folder containing `student_viewer.py`**

3. **Run the app:**
   ```bash
   streamlit run main.py
   ```

4. **Open your browser** - Streamlit will automatically open the app (usually at `http://localhost:8501`)

## 📖 How to Use

### Step 1: Set Folder Path
- In the sidebar, enter the path to the folder containing your CSV files
- Default is "./data/interim" (current directory)

### Step 2: Select CSV File
- Choose which CSV file to analyze from the dropdown
- Files are displayed with friendly names (e.g., "Pre-test-1", "Post-test-2")

### Step 3: Choose Student
- Select a student name from the dropdown
- Names are sorted alphabetically for easy finding

### Step 4: View Information
The app will display:
- **Basic Info**: NIM, Kelas, Nomor_Kelompok in colored boxes
- **Question Responses**: All question columns and their answers
<!-- 
## 🎨 Display Options

### Card View (Recommended)
- Shows each question and response in a clean card format
- Full questions and responses are visible
- Easy to read and scroll through
- Questions are numbered (Q1, Q2, Q3...)

### Table View
- Compact table format for quick scanning
- Good for when you have many short responses
- Truncates long content for better table fit

### Pagination
- Choose how many questions to show per page (6, 10, 15, or 20)
- Navigate between pages using the slider
- Automatic pagination when you have many questions

## 🔧 Features

- **📁 Smart File Detection**: Automatically finds all matching CSV files
- **✅ Data Validation**: Checks for required columns and shows helpful errors
- **📊 Statistics**: View dataset overview and data quality information
- **🔍 Raw Data View**: Optional expandable section to see all raw data
- **📱 Responsive Design**: Works on different screen sizes
- **⚡ Fast Loading**: Efficient data processing with loading indicators

## 🚨 Troubleshooting

### "No CSV files found"
- Check that your files follow the naming pattern: `cleaned_data_*.csv`
- Verify the folder path is correct
- Make sure files are in the specified directory

### "Missing required columns"
- Ensure your CSV has columns: `Nama`, `NIM`, `Kelas`, `Nomor_Kelompok`
- Check for typos in column names (case-sensitive)

### "No student names found"
- Check that the `Nama` column has data
- Verify there are no encoding issues with the CSV file

### App won't start
- Make sure you have Python 3.7+ installed
- Install required packages: `pip install streamlit pandas`
- Check that the file `student_viewer.py` is in your current directory

## 💡 Tips

1. **Large datasets**: Use pagination to avoid overwhelming display
2. **Long responses**: Card View is better for reading full responses
3. **Quick scanning**: Table View is faster for short answers
4. **File organization**: Keep all CSV files in one folder for easier management
5. **Performance**: The app loads data on-demand, so switching between students is fast

## 📝 Example Usage

1. Put your CSV files in a folder (e.g., `student_data/`)
2. Run the app: `streamlit run student_viewer.py`
3. Enter folder path: `student_data`
4. Select file: "Pre-test-1"
5. Choose student: "Ahmad Rizki"
6. View their complete information and responses

## 🆘 Support

If you encounter issues:
1. Check the error messages in the app - they're designed to be helpful
2. Verify your CSV file format matches the requirements
3. Ensure all required Python packages are installed
4. Check that file paths are correct and accessible

## 🔄 Updates

The app automatically handles:
- Different numbers of questions across files
- Missing data (shows "No response")
- Various response types (numbers, text, etc.)
- Dynamic content sizing based on your data

---

**Happy analyzing! 📊✨** -->