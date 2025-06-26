import subprocess

# Start uvicorn
process = subprocess.Popen(
    ["uvicorn", "Templt:app","--host","0.0.0.0", "--port", "8000"],
    # env=env
)

# uvicorn main:app --host 0.0.0.0 --port 8000 --reload