# AI Road Damage Detection — Streamlit Frontend

Professional Streamlit frontend for the [AI Road Damage Detection System](https://github.com/WardaAhad/ai-road-damage-detection-system) backend (FastAPI + YOLOv11, deployed on Railway).

## Run Locally

```bash
pip install -r requirements.txt
cp .streamlit/secrets.toml.example .streamlit/secrets.toml
streamlit run app.py
```

## Deploy on Streamlit Community Cloud

1. Push this folder to a GitHub repo (e.g. `ai-road-damage-detection-frontend`).
2. Go to https://share.streamlit.io → **New app**.
3. Select the repo, branch `main`, main file `app.py`.
4. In **Advanced settings → Secrets**, add: