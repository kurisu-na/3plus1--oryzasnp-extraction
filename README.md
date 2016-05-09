# 3+1 Research: OryzaSNP Data Extraction (Python)

This is a custom Python script used to convert copied text data from the website oryzasnp.org into a table of records containing the rice's phenotype data. The data was obtained by manually perusing the database and copy-pasting the shown values.

This script was made in part of my 3+1 Research project, to make a classifier using Indonesian rice phenotype data.

This script assumes all acquired data are in the form of a *loooooooooooong* vertical list, and then stores the end product in CSV format so you can view it as a neat table.

The frontend script is `runscriptrun.py`. **Run that one, please.**

The backend script is `convert.py`.

`runscriptrun.py` has predefined variables, denoted by the comment `# PREDEFINED`. Change those to `""` (blank) or `0` or other values if you're going to use it for different data. If you change them to `""` or `0`, you will be asked for input each time you run `runscriptrun.py`.

The files I used can be found in the `Files` folder.

That's it! :octocat:

--

**(kurisu_na, 7-10 March 2016, final revision on 8 April 2016.)**
Python version: 3.4.3
