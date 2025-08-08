**backend/app/main.py**

**backend/app/routes/login.py**

**backend/app/security.py**

**frontend/src/index.js**

**frontend/src/App.jsx**

**frontend/src/components/NavBar.jsx**

**frontend/src/components/LoginForm.jsx**

**frontend/src/components/Dashboard.jsx**

**frontend/public/index.html**

**frontend/Dockerfile**

**backend/tests/test_main.py**

from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_read_main():
    response = client.get("/")
    assert