import os
import pandas as pd

def clean_data(file_path):
    file_name = os.path.splitext(os.path.basename(file_path))[0]
    df = pd.read_excel(file_path)

    # Drop columns that start with "Points" or "Feedback"
    df = df.drop(columns=[col for col in df.columns if col.startswith("Points") or col.startswith("Feedback")], errors='ignore')

    # Drop specific columns if they exist
    drop_cols = ['ID', 'Start time', 'Completion time', 'Email', 'Name', 'Total points', 'Quiz feedback']
    df = df.drop(columns=[col for col in drop_cols if col in df.columns], errors='ignore')

    # Rename column
    df.rename(columns={
        'Nomor Kelompok. Format: {Nama kelas}_{Nomor kelompok}. Contoh: B1_05 atau B3_12': 'Nomor_Kelompok'
    }, inplace=True)

    output_path = f'../data/interim/cleaned_data_{file_name}.csv'
    df.to_csv(output_path, index=False)
    print(f"Saved: {output_path}")

# Loop through all Excel files in the folder
folder_path = '../data/jawaban-pretest-posttest/'  # replace with your actual folder path

for file in os.listdir(folder_path):
    if file.endswith(".xlsx") or file.endswith(".xls"):
        file_path = os.path.join(folder_path, file)
        clean_data(file_path)
