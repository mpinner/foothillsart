## install
- [vscode](https://code.visualstudio.com/download) : a text editor
- [miniconda](https://conda.io/projects/conda/en/latest/user-guide/install/download.html) : a python env and package manager
- install pillow : `conda install pillow`
- install pandas : `conda install pandas`

## run
- run "Anaconda Prompt (miniconda3") from window prgrams under "Anaconda3 (64-bit)"
    - from that terminal go into dev-foothills: `cd dev-foothills`
    - and launch vscode: `code .` : this gives a vs code env with conda 

# setup
- open `create final show foldeers.py`
- set `show_title` for the generated filenames
- set `folder` and `output_folder` and `output_juror_folder`
- run file with play button in upper right
- note this will delete the entire `output_folder` and recreate
- should see file list, then attributes printed for each file until complete

# issues
- filename needs to be correctly formatted with all attributes and '_' as field delimitor
    - like so : `Francis,Kenda_ZigZagJag_Other Media_8x11_$950.jpg`
    - there is no validation on this
- if you are using the `output_folder` or viewing an image there, program console will show PermissionDenied Error
