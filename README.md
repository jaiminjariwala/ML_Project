## End to End Machine Learning Project

## How to start?
1. Create a folder and open VS Code
2. Open terminal and create Environment:
    - ``` conda create -p venv python==3.11 ``` <br>
    - ``` conda activate given_file path ```
3. Create `README.md` file, `requirements.txt` file, `setup.py` file
4. Open Github repo, create new file, type `.gitignore` and select template `Python` and commit changes.

5. Come back to VS Code, create `src` folder and add `__init__.py`, `exception.py`, `logger.py`, `utils.py` file.
    - Also create 2 folders:
        - `components` folder that includes `__init__.py`, `data_ingestion.py`, `data_transformation.py`, `model_trainer.py` files
        - `pipeline_folder` folder that includes `__init__.py`, `predict_pipeline.py`, `train_pipeline.py` files.

6. Write code in `setup.py` file and add libraries required in `requirements.txt` file.
7. Save all files and run ```pip install -r requirements.txt``` in `terminal`.
8. Then run ```pip install -e .``` in `terminal`.

9. Later add `notebook` folder which inlcudes:
    - `data` folder that has `.csv` file and...
    - `EDA` and `MODEL TRAINING` file.
