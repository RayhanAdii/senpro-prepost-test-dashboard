import streamlit as st
import pandas as pd
import os
import glob

def load_csv_files(folder_path):
    """Load all CSV files matching the pattern from the specified folder"""
    pattern = os.path.join(folder_path, "cleaned_data_*.csv")
    csv_files = glob.glob(pattern)
    return csv_files

def get_file_display_name(file_path):
    """Extract display name from file path"""
    filename = os.path.basename(file_path)
    # Remove .csv extension and cleaned_data_ prefix
    display_name = filename.replace("cleaned_data_", "").replace(".csv", "")
    return display_name

def load_data(file_path):
    """Load and return DataFrame from CSV file"""
    try:
        df = pd.read_csv(file_path)
        return df
    except Exception as e:
        st.error(f"Error loading file: {e}")
        return None

def main():
    st.set_page_config(
        page_title="Student Data Viewer",
        page_icon="📊",
        layout="wide"
    )
    
    st.title("📊 Dashboard Pre-Post-Test Senpro TIF 2025")
    st.markdown("---")
    
    # Folder selection
    st.sidebar.header("📁 Folder Configuration")
    folder_path = st.sidebar.text_input(
        "Enter folder path containing CSV files:",
        value=".",
        help="Enter the path to the folder containing your cleaned_data_*.csv files"
    )
    
    if not os.path.exists(folder_path):
        st.error(f"Folder path '{folder_path}' does not exist. Please enter a valid path.")
        return
    
    # Load CSV files
    csv_files = load_csv_files(folder_path)
    
    if not csv_files:
        st.warning(f"No CSV files matching pattern 'cleaned_data_*.csv' found in '{folder_path}'")
        st.info("Expected file format: cleaned_data_[Pre-test/Post-test]-[number].csv")
        return
    
    # File selection
    st.sidebar.header("📄 File Selection")
    file_options = {get_file_display_name(file): file for file in csv_files}
    
    selected_display_name = st.sidebar.selectbox(
        "Select CSV file:",
        options=list(file_options.keys()),
        help="Choose which CSV file to analyze"
    )
    
    selected_file = file_options[selected_display_name]
    
    # Load selected data
    with st.spinner("Loading data..."):
        df = load_data(selected_file)
    
    if df is None:
        return
    
    # Display file info
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("📋 Selected File", selected_display_name)
    with col2:
        st.metric("👥 Total Students", len(df))
    with col3:
        st.metric("📊 Total Columns", len(df.columns))
    
    st.markdown("---")
    
    # Check required columns
    required_columns = ['Nama', 'NIM', 'Kelas', 'Nomor_Kelompok']
    missing_columns = [col for col in required_columns if col not in df.columns]
    
    if missing_columns:
        st.error(f"Missing required columns: {', '.join(missing_columns)}")
        st.info("Required columns: Nama, NIM, Kelas, Nomor_Kelompok")
        return
    
    # Student selection
    st.header("🎯 Student Selection")
    
    # Get unique names and sort them
    names = sorted(df['Nama'].dropna().unique())
    
    if len(names) == 0:
        st.warning("No student names found in the data.")
        return
    
    selected_name = st.selectbox(
        "Select student name:",
        options=names,
        help="Choose a student to view their information"
    )
    
    # Filter data for selected student
    student_data = df[df['Nama'] == selected_name]
    
    if len(student_data) == 0:
        st.warning(f"No data found for student: {selected_name}")
        return
    
    # Display student information
    st.markdown("---")
    st.header(f"📋 Information for: **{selected_name}**")
    
    # Basic information
    student_info = student_data.iloc[0]  # Get first row if multiple entries
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.info(f"**NIM:** {student_info['NIM']}")
    with col2:
        st.info(f"**Kelas:** {student_info['Kelas']}")
    with col3:
        st.info(f"**Nomor Kelompok:** {student_info['Nomor_Kelompok']}")
    
    # Question responses
    st.subheader("📝 Question Responses")
    
    # Get question columns (exclude basic info columns)
    question_cols = [col for col in df.columns if col not in required_columns]
    
    if question_cols:
        # Display format options
        col1, col2 = st.columns([2, 1])
        with col1:
            display_mode = st.radio(
                "Display format:",
                ["Card View", "Table View"],
                horizontal=True,
                help="Choose how to display the questions and responses"
            )
        with col2:
            if len(question_cols) > 6:
                questions_per_page = st.selectbox(
                    "Questions per page:",
                    [6, 10, 15, 20],
                    index=0
                )
            else:
                questions_per_page = len(question_cols)
        
        # Pagination
        if len(question_cols) > questions_per_page:
            total_pages = (len(question_cols) + questions_per_page - 1) // questions_per_page
            page = st.select_slider(
                f"Page (showing {questions_per_page} questions per page):",
                options=list(range(1, total_pages + 1)),
                value=1,
                format_func=lambda x: f"Page {x} of {total_pages}"
            )
            
            start_idx = (page - 1) * questions_per_page
            end_idx = min(start_idx + questions_per_page, len(question_cols))
            current_questions = question_cols[start_idx:end_idx]
        else:
            current_questions = question_cols
        
        # Display questions based on selected mode
        if display_mode == "Card View":
            # Card view - easier to read
            for i, col in enumerate(current_questions):
                response = student_info[col]
                
                # Create a nice card for each question
                with st.container():
                    # Make question number and title more readable
                    question_num = (start_idx if len(question_cols) > questions_per_page else 0) + i + 1
                    
                    # Show full question
                    display_question = col
                    
                    st.markdown(f"**Q{question_num}: {display_question}**")
                    
                    # Display response with appropriate styling
                    if pd.isna(response) or response == "":
                        st.markdown("*No response*")
                    else:
                        # Handle different types of responses
                        if isinstance(response, (int, float)):
                            st.markdown(f"**Answer:** `{response}`")
                        else:
                            response_str = str(response)
                            # Show full response by default
                            st.markdown(f"**Answer:** {response_str}")
                    
                    # Add some spacing between questions
                    st.markdown("---")
        
        else:
            # Table view - compact
            question_data = {}
            for col in current_questions:
                # Shorten question names for table
                display_name = col if len(col) <= 30 else col[:27] + "..."
                response = student_info[col]
                
                if pd.isna(response) or response == "":
                    question_data[display_name] = "No response"
                else:
                    response_str = str(response)
                    # Truncate long responses in table view
                    if len(response_str) > 50:
                        question_data[display_name] = response_str[:47] + "..."
                    else:
                        question_data[display_name] = response_str
            
            question_df = pd.DataFrame([question_data]).T
            question_df.columns = ['Response']
            question_df.index.name = 'Question'
            
            st.dataframe(
                question_df,
                use_container_width=True,
                height=min(400, len(current_questions) * 35 + 100)
            )
            
            # Show note about truncated content
            if any(len(str(student_info[col])) > 50 for col in current_questions):
                st.info("💡 Some responses are truncated in table view. Switch to Card View to see full responses.")
    
    else:
        st.info("No question columns found in the data.")
    
    # Raw data view (optional)
    with st.expander("🔍 View Raw Data for Selected Student"):
        st.dataframe(student_data, use_container_width=True)
    
    # Statistics (optional)
    with st.expander("📈 Dataset Statistics"):
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader("Basic Info")
            st.write(f"**Total students:** {len(df)}")
            st.write(f"**Unique classes:** {df['Kelas'].nunique()}")
            st.write(f"**Unique groups:** {df['Nomor_Kelompok'].nunique()}")
            
        with col2:
            st.subheader("Data Quality")
            missing_data = df.isnull().sum()
            if missing_data.sum() > 0:
                st.write("**Missing values:**")
                for col, missing in missing_data.items():
                    if missing > 0:
                        st.write(f"- {col}: {missing}")
            else:
                st.success("No missing values found!")

if __name__ == "__main__":
    main()