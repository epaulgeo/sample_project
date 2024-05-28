# *Project Site* Water Levels Dashboard

A project to visualize water level data at the *Project Site*. 

Input: Data reviewed (QC'd) by project manager.   
Output: No-code, web-free interactive data visualization .html file that can be shared with stakeholders.

Project No.: 12345678   
Project Manager: EAP   
Dev: EAP   


## How to Use or Update the Dashboard

1. Follow the **Setup and Installation** instructions to run the code locally.
   
2. If needed, add folders to the directory to match the functional form for the code, per **Directory Structure** below. Include underscores ( _ ) in folder names.
   
3. Retrieve the data source files (see **Data Source Files**) and store in the `my_data_source` folder.
   
4. Run all notebooks in the `my_notebooks` folder. This will create a new folder called `my_data_intermediate`.
   
5. From the command line (and with the virtual environment activated), run the dashboard script with
   ```
   python my_source_code\my_dashboard.py
   ```

6. A browser window will open with the interactive dashboard and an `.html` file for sharing will be created and saved to the `my_data_outputs` folder.
   
7. Manually save the .html file to the Sharepoint `Water Levels` folder. Distribute via email or alert pertinent stakeholders.
   
8. Update the Azure DevOps repository with `git push`.
   
9. Recommended to delete your local project directory and repeat this process next time the dashboard is updated. Alternatively, skip steps 1 and 2 of **Setup and Installation** and run `git pull` to ensure your local version stays current with the source repo.

## Setup and Installation

To run the scripts on your own machine, either use the **clone in VSCode** button, or from the command terminal:
1. Create and navigate into project directory
   ```
   cd my_project_directory
   ```
2. Clone the repository to your project directory:
   ```
   git clone https://github.com/epaulgeo/sample_project_python.git
   ```
3. Install depencies using Pipenv:
   ```
   pipenv install
   ```
4. Activate the virtual environment:
   ```
   pipenv shell
   ```  
5. You will know you are in your virtual environment if your prompt looks something like the following, with the (VirtualEnvName in parenthesis) suffix:
   ```
   (NameOfVirtualEnvironmnent) C:\Users\YourUserName\my_project_directory>
   ```

   
## Directory Structure

After cloning the repository, add any subdirectories to match the directory structure below. Some subdirectories will populate only once the `.ipynb` or `.py` files are run.
```
my_project_directory
|
├── my_data_intermediate
|   |
|   └── contents: outputs from .ipynb cleaning files to be used for plotting
|   
├── my_data_outputs 
|   |
|   └── contents:
|
├── my_data_source 
|   |  
|   └── contents: files described under Data Source Files  
| 
├── my_notebooks   
|   |
|   └── contents: .ipynb notebooks for preparing data for plotting 
|
├── my_source_code  
|   | 
|   └── contents: .py files for functions, visualization app, etc.  
| 
├── .gitignore
├── CHANGELOG.md
├── Pipfile   
├── Pipfile.lock   
└── README.md
```

## Data Source Files

These files should be stored in the `my_data_source` subdirectory. Add the subdirectory as shown in **Directory Structure** if needed. Retrieve these files from SharePoint.

- *ProjectSite*_WaterLevels.xlsx ([Link that leads to nowhere]())

## Tested on:

- Windows 11 Pro, Microsoft Edge browser, VSCode
