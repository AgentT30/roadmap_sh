Implementation for https://roadmap.sh/projects/unit-converter

# Unit Converter

A simple web page that has different sections for different units of measurement. The user can input a value to convert, select the units to convert from and to, and view the converted value. The app's UI is built using [Steamlit](https://streamlit.io/)

# Project Directory Structure

```
.
├── app.py
├── pages
│   ├── length.py
│   ├── temperature.py
│   └── weight.py
├── README.md
└── requirements.txt
```

The `app.py` is the entrypoint which redirects the user to different unit convertors. Each file in the `pages/` directory is for a specific type of unit.

# Installation

```
pip install -r requirements.txt
```

# Execution

```
streamlit run app.py
```

Head over to [localhost:8501](localhost:8501) to access the UI web interface