# Running the Script

To execute the `app.py` script, run the following command in your terminal or command prompt:

```bash
python app.py -e "C:\Users\YourUser\Documents\data.xlsx" -s Sheet1 -t sales_data
```

## Arguments

The script accepts the following arguments:

- **`-e` / `--excel-file`** (Required)  
  Specifies the path to the Excel file.  
  **Example:** `"C:\Users\YourUser\Documents\data.xlsx"`

- **`-s` / `--sheet-name`** (Required)  
  Defines the name of the sheet within the Excel file.  
  **Example:** `Sheet1`

- **`-t` / `--table-name`** (Required)  
  Specifies the MySQL table where the data will be uploaded.  
  **Example:** `sales_data`

## Notes

- Ensure that the specified Excel file and sheet exist.
- Verify that the MySQL database is properly configured before running the script.
- If needed, install dependencies using `pip install -r requirements.txt`.

