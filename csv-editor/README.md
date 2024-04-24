# flask-csv-viewer
Flask WebApp - view csv files as table in a webapp

CSV Viewer Web App

## Description

CSV Viewer is a web application built with HTML, CSS, and JavaScript, allowing users to upload, view, and interact with CSV files in a tabular format. The app also utilizes jQuery for AJAX calls and Bootstrap for styling.

## Features

- [x]  Upload CSV files for viewing
- [x]  Download the current data set with a secret key
- [x]  Search for text within table cells
- [x]  Toggle columns on/off
- [x]  Dynamic column swapping
- [x]  Scrollable table with custom-styled scrollbar
- [x]  Dark Mode UI

## Technologies Used

- HTML5
- CSS3
- JavaScript
- jQuery 3.6.0
- Bootstrap 5.3.0-alpha1

## Installation and Setup

Requires: Python 3; Pip: Flask, pandas
Clone this repository or download the source code and run the main.py with

```python3
python3 main.py
```

## Usage

### Uploading CSV File

To upload a CSV file, click on the "Choose File" button and select the CSV file you wish to view. After selecting the file, click the "Submit" button to upload and view the file.

### Setting Secret Key

You can set a secret key for downloading the current data set by typing the secret into the "Set Secret" input box and clicking "Set and Download".

### Search Text in Cells

To search for specific text in the table cells, use the "Search Text in Cells" input box.

### Toggle Columns

To toggle the visibility of specific columns, use the checkboxes beside each column name.

### Column Drag and Drop

To swap the positions of two columns, simply click and drag one column header over another.

### Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.



