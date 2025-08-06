# Network TestLab Automation MVP

## Project Overview

This project is a Minimum Viable Product (MVP) prototype of a Network TestLab Automation tool designed to simplify and automate network device testing workflows. It simulates discovery of LANforge devices on a network, allows running simple network throughput tests on these devices, and presents results in a user-friendly web interface.

Intended as a final year IT student project, it demonstrates full-stack development skills, API design, and test automation concepts relevant to network performance testing.

---

## Features

- **Device Discovery:** Simulated discovery of LANforge devices returning a predefined list with IP addresses, names, and statuses.
- **Test Execution Simulation:** Run a "throughput" test on selected device IPs, returning dummy but realistic test metrics (throughput, latency, packet loss).
- **RESTful Backend API:** Built with Python Flask exposing `/discover` (GET) and `/run_test` (POST) endpoints.
- **Frontend Web Interface:** Simple HTML/CSS/JS UI allowing users to trigger discovery, run tests, and view formatted test results.
- **Embedded Documentation & Author Info:** Project details and personal contact information integrated into the frontend UI.

---

## Technology Stack

- **Backend:** Python 3.x, Flask, flask-cors  
- **Frontend:** HTML5, CSS3, Vanilla JavaScript  
- **Dev Environment:** Localhost Flask server at `http://localhost:5000`

---

## Project Structure

network-testlab-mvp/
├── backend/
│ └── app.py # Flask backend with API endpoints
├── discovery/
│ └── discover.py # Simulated device discovery function
├── frontend/
│ └── index.html # Frontend UI with embedded docs and controls
├── requirements.txt # Python dependencies: Flask, flask-cors
└── README.md # This file


---

## Getting Started

### Prerequisites

- Python 3.x installed  
- `pip` package manager  
- Modern web browser (Chrome, Firefox, Edge, etc.)

### Installation & Running

1. **Clone the repository or download the source files** to your local machine.

2. **Navigate to your project root directory** in the terminal or command prompt.

3. (Optional but recommended) **Create and activate a Python virtual environment:**

    On Linux/Mac:
    ```
    python3 -m venv env
    source env/bin/activate
    ```
    On Windows:
    ```
    python -m venv env
    env\Scripts\activate
    ```

4. **Install Python dependencies:**

    ```
    pip install -r requirements.txt
    ```

    If `requirements.txt` is not present, install manually:

    ```
    pip install Flask flask-cors
    ```

5. **Start the Flask backend server:**

    ```
    python backend/app.py
    ```

    The server runs by default at `http://localhost:5000`.

6. **Open the frontend UI:**

    Open `frontend/index.html` file in your preferred web browser by double-clicking it or serving it via a simple HTTP server if you prefer.

7. **Use the UI:**

    - Click **"Discover Devices"** to load the list of simulated LANforge devices.
    - Click **"Run Test"** next to a device to simulate a throughput test and view results.

---

## API Endpoints

| Endpoint      | Method | Description                                | Request Data                     | Response                  |
|---------------|--------|--------------------------------------------|---------------------------------|---------------------------|
| `/discover`   | GET    | Returns list of LANforge devices           | None                            | JSON array of devices      |
| `/run_test`   | POST   | Runs a simulated test on the given device  | JSON: `{ device_ip, test_type }` | JSON with test metrics     |

---

## Future Improvements

- Implement real LANforge device discovery using network protocols such as mDNS or ping scanning.
- Integrate with actual LANforge REST APIs to conduct real network tests.
- Persist test results in a database (e.g., MongoDB) for historical tracking.
- Enhance frontend with charts, historical data visualization, and richer dashboard features.
- Add user authentication and role management for production usage.
- Containerize using Docker for easier deployment and sharing.

---

## Author

**Avala Prabhash**  
Aspiring Software Engineering Intern | Full Stack Developer  
Vizianagaram, Andhra Pradesh, India  
Email: prabhasavala7@gmail.com  
Phone: +91 9390330367  
LinkedIn: [Your LinkedIn URL]  
GitHub: [Your GitHub URL]

---

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details (if added).

---

## Acknowledgments

- The project is inspired by network testing tools like LANforge by Candela Technologies.
- Uses Flask and modern JavaScript for the backend and frontend respectively.

---

Thank you for reviewing this Network TestLab Automation MVP project! Feel free to reach out with any questions or suggestions.

