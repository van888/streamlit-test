## STEP 1 deactivate local environment
>If local virtual environment is activated, deactivate it
`deactivate`

STEP 2: activate conda env 
>Because of M1 chip lack of support run in conda env
`conda activate st`

---

STEP 3: run streamlit

`streamlit run streamlit.py`

---

# basic terminal command:
- conda activate [env]
- conda deactivate 
- conda update conda
- conda install PACKAGENAME
- conda update PACKAGENAME

# Using environments:
- conda create --name ENVNAME python=3.9
- conda info --envs
- conda env list
- conda create --clone ENVNAME --name ENVNAME_NEW
- conda list --explicit > requirements.txt
- conda env create --file requirements.txt 
- conda env remove --name ENVNAME