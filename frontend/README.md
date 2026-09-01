# AI Road Damage Detection — Standalone Streamlit App

Self-contained Streamlit app. Loads the YOLOv11 model (`models/best.pt`)
directly inside the app and runs detection locally — **no backend/API
required**.

## Run Locally

```bash
pip install -r requirements.txt
streamlit run app.py
```

## Deploy on Streamlit Community Cloud

1. Push this whole `frontend/` folder to a GitHub repo (e.g.
   `ai-road-damage-detection-frontend`), making sure `models/best.pt`
   is included (do NOT gitignore the `models/` folder).
2. Go to https://share.streamlit.io → **New app**.
3. Select the repo, branch `main`, main file `app.py`.
4. Deploy. No secrets needed — everything runs in the app itself.

## Notes

- `packages.txt` installs system libraries (`libgl1`, `libglib2.0-0`)
  needed by OpenCV/Torch on Streamlit Cloud's Debian environment.
- First load will be slower since `torch`/`ultralytics` need to
  initialize and the model needs to load — this is cached after the
  first run (`@st.cache_resource`).
- The old `backend/` (FastAPI) project and its Railway deployment are
  no longer needed for this app and can be deleted.
