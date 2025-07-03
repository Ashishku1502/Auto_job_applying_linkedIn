Here's a **step-by-step guide** to install, configure, and run the **Auto Job Applier for LinkedIn** from the `GodsScion/Auto_job_applier_linkedIn` GitHub repository. This walkthrough is especially tailored for **Windows users**, assuming you want to proceed manually and understand each step (without relying solely on `windows-setup.bat`).

---

## ✅ **Step 1: Install Python (3.10 or above)**

### 🔹 Option A: Official Python Website

1. Visit: [https://www.python.org/downloads/](https://www.python.org/downloads/)
2. Download the **Windows installer** (choose 64-bit).
3. During installation:

   * ✅ Check the box: **“Add Python to PATH”**
   * Click **Install Now**

### 🔹 Option B: Microsoft Store

1. Open the **Microsoft Store**
2. Search for **“Python 3.10” or later**
3. Click **Install**

---

## ✅ **Step 2: Install Required Python Packages**

Open **Command Prompt** or **PowerShell** and run:

```bash
pip install undetected-chromedriver pyautogui setuptools openai flask-cors flask
```

If pip is not recognized, close and reopen terminal or reinstall Python with PATH selected.

---

## ✅ **Step 3: Install Google Chrome (Latest)**

1. Download and install Google Chrome from: [https://www.google.com/chrome](https://www.google.com/chrome)

---

## ✅ **Step 4: Download the Repository**

### Option A: Using Git

```bash
git clone https://github.com/Ashishku1502/Auto_job_applying_linkedIn.git
cd Auto_job_applier_linkedIn
```

### Option B: Download ZIP

1. Go to [https://github.com/GodsScion/Auto\_job\_applier\_linkedIn](https://github.com/GodsScion/Auto_job_applier_linkedIn)
2. Click **“Code > Download ZIP”**
3. Extract the contents and open in VSCode or file explorer

---

## ✅ **Step 5: Install ChromeDriver**

### Option A: Manual

1. Go to: [https://googlechromelabs.github.io/chrome-for-testing/](https://googlechromelabs.github.io/chrome-for-testing/)
2. Find your installed **Chrome version**:

   * Open Chrome and visit `chrome://settings/help`
3. Download **matching ChromeDriver** version
4. Copy the extracted **chromedriver.exe** to your Chrome install directory (usually `C:\Program Files\Google\Chrome\Application\`)

### Option B: Automated (Windows only)

Run the script:

```bash
setup/windows-setup.bat
```

---

## ✅ **Step 6: Configure the Bot**

### 🔧 A. Fill in your details

Open these files in a code editor:

#### 1. `/config/personals.py`

Enter your name, phone, address, etc.

#### 2. `/config/questions.py`

Answer common application questions here.
Set options like:

```python
pause_before_submit = True
pause_on_unknown_question = True
```

#### 3. `/config/search.py`

Set job search preferences:

```python
search_location = "Bengaluru, Karnataka, India"
search_terms = ["Full Stack Developer"]
```

#### 4. `/config/secrets.py`

Provide your:

* LinkedIn email and password
* OpenAI API Key *(optional for AI-generated resumes)*

Leave blank for manual login if you don’t want to store credentials.

#### 5. `/config/settings.py`

Adjust bot behavior:

```python
stealth_mode = True
run_in_background = False
randomize_click_intervals = True
```

---

## ✅ **Step 7: Add Your Resume (Optional)**

Place your PDF resume at:

```
/all resumes/default/resume.pdf
```

Or set `default_resume_path` inside `questions.py`.

---

## ✅ **Step 8: Run the Bot**

Open terminal inside the repo folder and run:

```bash
python runAiBot.py
```

This will launch the browser, search for jobs, and begin applying automatically.

---

## ✅ **Step 9: View History UI (Optional)**

To view applied job history:

```bash
python app.py
```

Open browser at:
[http://localhost:5000](http://localhost:5000)

---

## 🔧 Developer Note

Follow the contributor coding style if you want to modify the code:

* Snake case for function names
* Camel case for local variables
* Snake case for global variables
* Type hints and docstrings

---

## ✅ **Discord Community**

Need help or want to chat?
Join the Discord server:
👉 [https://discord.gg/fFp7uUzWCY](https://discord.gg/fFp7uUzWCY)

---

Let me know if you'd like me to **automate** your resume generation or configure this on your PC remotely using a script.
