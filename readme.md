# Full-Stack Project Setup Script

## Overview

This Full-Stack Project Setup Script is an internal automation tool designed to create a complete project skeleton for modern web development. It generates a preconfigured environment for both the frontend and backend portions of your project, including integrated logging and database setup based on your choices.

The script creates:
- A modern React-based frontend using Vite.
- A backend using either FastAPI (Python) or Express.js (Node.js).
- Database configuration (SQL via SQLite or MongoDB) according to your selection.
- Detailed log files tracking every step of the setup process.

## What This Script Offers

- **Automated Project Structure Creation:**  
  The script automatically generates a complete, consistent directory layout so you can focus on developing features rather than manual setup.

- **Frontend Setup:**
  - Uses React and Vite for a fast, modern development experience.
  - Generates essential configuration files:
    - **.gitignore:** Ignores logs, build files, and editor-specific files.
    - **eslint.config.js:** Configured with recommended rules for JavaScript and React.
    - **tailwind.config.js** and **postcss.config.js:** Configure Tailwind CSS styling.  
      > **Note:** The `postcss.config.js` file now uses ES module syntax (with `import`/`export`) to work with `"type": "module"` in package.json.
    - **vite.config.js:** Imports and uses the React plugin, enabling Vite to process React files.
    - **package.json:** Contains scripts for development, building, linting, and previewing.  
      The dependencies have been updated, for example:
      - `"@vitejs/plugin-react": "^4.3.4"`
      - `"autoprefixer": "^10.4.20"`, `"postcss": "^8.4.49"`, and an extra `"tailwindcss": "^3.4.16"` are now in devDependencies.
  - Creates a structured **src/** folder with the following subdirectories:
    - **assets/** – For static assets.
    - **components/** – Contains all custom React components (e.g., theme toggler buttons).
    - **config/** – For configuration files.
    - **lib/** – Contains the `axios.js` file with a preconfigured Axios instance.
    - **pages/** – Contains page components; a **HomePage.jsx** is generated here.
    - **store/** – Contains the `ThemeContext.jsx` file for managing the theme.
  - Generates core source files:
    - **App.jsx:** The main React component that sets up routes, includes a toast notification system, and displays a fixed-position theme toggler at the bottom-right.
    - **index.css:** Contains Tailwind CSS directives.
    - **main.jsx:** The React entry point that renders the application, now wrapped in `<ThemeProvider>` to provide the context.
    - **HomePage.jsx:** A sample homepage component under **src/pages/** that displays a welcome message (including the project name) and demonstrates dark mode styling.
  - **Note:** The script does not explicitly create a `node_modules` folder or a `package-lock.json` file—npm will generate these automatically.

- **Backend Setup:**
  - Offers a choice between **FastAPI (Python)** and **Express.js (Node.js)**.
  - **FastAPI Setup:**
    - Creates a structured backend folder under **backend/app/** with subdirectories:
      - **models/** – For ORM models.
      - **schemas/** – For Pydantic data schemas.
      - **routers/** – For grouping API routes.
      - **core/** – For configuration files including database setup.
    - Generates a basic **main.py** file to initialize the FastAPI application.
    - Creates a database setup file at **backend/app/core/database.py** that configures a connection using:
      - SQL (via SQLAlchemy with SQLite) or
      - MongoDB (using motor).
    - Updates **requirements.txt** with essential dependencies (`fastapi`, `uvicorn`, plus either `SQLAlchemy` or `motor`).
  - **Express.js Setup:**
    - Generates an **app.js** file as the entry point for the Express.js server.
    - Creates subdirectories under **backend/**:
      - **routes/** – Contains a basic **index.js** and a placeholder **users.js**.
      - **models/** – Placeholder for data models.
      - **controllers/** – Placeholder for controller logic.
    - Creates a database setup file at **backend/db.js** that configures a connection using:
      - SQL (via sqlite3) or
      - MongoDB (using mongoose).
    - Updates **backend/package.json** with dependencies (`express` plus either `sqlite3` or `mongoose`).

- **Database Setup:**
  - When you run the script, you are prompted for:
    - The database type (SQL or MongoDB).
    - The database name.
  - Based on your selection:
    - **FastAPI:** The file **backend/app/core/database.py** is created to set up the connection.
    - **Express.js:** The file **backend/db.js** is created to set up the connection.

- **Logging:**
  - A **log/** folder is created at the project root with three log files:
    - **setup.log:** Records overall setup steps.
    - **frontend.log:** Logs detailed actions during the frontend creation process.
    - **backend.log:** Logs detailed actions during backend and database setup.
  - Each log entry is timestamped to aid troubleshooting.

## Prerequisites

- **Python 3** must be installed.
- **Node.js & npm** are required to install and run frontend dependencies.
- **Database Engine (Optional):**
  - For SQL: The script uses SQLite by default.
  - For MongoDB: Ensure MongoDB is installed and running locally.

## How to Run the Script

1. **Download the Script:**  
   Save the `setup_fullstack.py` file to a directory of your choice.

2. **Open a Terminal:**  
   Navigate to the directory containing the script.

3. **Execute the Script:**
   ```bash
   python setup_fullstack.py
   ```

4. **Provide the Required Information:**  
   When prompted, enter:
   - Your project name.
   - Your backend framework choice (Enter **1** for FastAPI or **2** for Express.js).
   - Your database type (Enter **1** for SQL or **2** for MongoDB).
   - The desired database name.

5. **Wait for the Script to Complete:**  
   The script will generate the complete project structure and log every step in the **log/** folder.

## Project Structure Overview

After running the script, your project folder (named as provided) will have the following structure:

```
<project-name>/
├── backend/
│   ├── app/                   (For FastAPI)
│   │   ├── main.py            (FastAPI entry point)
│   │   ├── models/            (Placeholder ORM models)
│   │   ├── schemas/           (Pydantic schemas)
│   │   ├── routers/           (API routes)
│   │   └── core/              (Contains database.py for DB setup)
│   ├── requirements.txt       (For FastAPI) OR
│   ├── package.json           (For Express.js)
│   ├── README.md
│   └── db.js                  (Express.js database setup)
├── frontend/
│   ├── public/                (Empty folder for static files)
│   ├── src/
│   │   ├── assets/
│   │   ├── components/        (Contains custom React components)
│   │   ├── config/
│   │   ├── lib/               (Contains axios.js)
│   │   ├── pages/             (Contains HomePage.jsx)
│   │   ├── store/             (Contains ThemeContext.jsx)
│   │   ├── App.jsx            (Main React component with routing and theme toggler)
│   │   ├── index.css          (Tailwind CSS directives)
│   │   └── main.jsx           (Entry point for the React app, wrapped in ThemeProvider)
│   ├── .gitignore
│   ├── eslint.config.js
│   ├── index.html
│   ├── package.json
│   ├── postcss.config.js      (ES module syntax for PostCSS)
│   ├── README.md
│   ├── tailwind.config.js
│   └── vite.config.js         (Configured with React plugin)
└── log/
    ├── setup.log
    ├── frontend.log
    └── backend.log
```

## Detailed Explanation: Frontend

- **.gitignore:**  
  Lists files and directories (e.g., logs, build directories, and editor files) that Git should ignore.

- **eslint.config.js:**  
  Configured with recommended settings for JavaScript and React to ensure consistent code quality.

- **index.html:**  
  The HTML entry point that dynamically sets the title to the project name.

- **package.json:**  
  Contains scripts for development (`npm run dev`), building (`npm run build`), linting (`npm run lint`), and previewing (`npm run preview`).  
  The dependencies and devDependencies are now updated to include:
  - `"@vitejs/plugin-react": "^4.3.4"`
  - `"autoprefixer": "^10.4.20"`, `"postcss": "^8.4.49"`, and an extra `"tailwindcss": "^3.4.16"`.

- **postcss.config.js:**  
  Now uses ES module syntax:
  ```js
  import tailwindcss from 'tailwindcss'
  import autoprefixer from 'autoprefixer'

  export default {
    plugins: [tailwindcss, autoprefixer]
  }
  ```

- **tailwind.config.js:**  
  Configures Tailwind CSS to use dark mode (via `darkMode: 'class'`) and scans the appropriate files for class names.

- **vite.config.js:**  
  Imports and uses the React plugin, enabling Vite to process React files:
  ```js
  import { defineConfig } from 'vite'
  import react from '@vitejs/plugin-react'

  // https://vite.dev/config/
  export default defineConfig({
    plugins: [react()],
  })
  ```

- **src/App.jsx:**  
  The main React component that:
  - Defines application routes using `react-router-dom`.
  - Includes the **Toaster** component for notifications.
  - Renders the **ToggleThemeBtn** (from **src/components/ToggleThemeButtons.jsx**) in a fixed container at the bottom-right.
  
- **src/main.jsx:**  
  The entry point that renders the React application, now wrapped in `<ThemeProvider>` from **src/store/ThemeContext.jsx** to ensure context is available.

- **src/store/ThemeContext.jsx:**  
  Implements a React Context for managing the light/dark theme with a toggle function and optional system preference listener.

- **src/lib/axios.js:**  
  Exports an Axios instance preconfigured for API calls.

- **src/components/ToggleThemeButtons.jsx:**  
  Contains multiple React components for theme toggling. The file no longer imports `{ Moon, Sun }` from 'lucide-react' per your update.

- **src/pages/HomePage.jsx:**  
  A sample homepage component that:
  - Displays a welcome message including the project name.
  - Uses Tailwind’s `dark:` classes to demonstrate dark mode styling.

## Detailed Explanation: Backend

### FastAPI Backend

- **backend/app/main.py:**  
  Initializes the FastAPI application and sets up a basic GET endpoint.

- **backend/app/models/:**  
  Directory for ORM models (contains placeholder files, e.g., `user.py`).

- **backend/app/schemas/:**  
  Contains Pydantic schemas for data validation (placeholder files included).

- **backend/app/routers/:**  
  Groups API routes (placeholder files included).

- **backend/app/core/config.py:**  
  Placeholder file for configuration settings.

- **backend/app/core/database.py:**  
  Sets up the database connection:
  - **SQL Option:** Uses SQLAlchemy with SQLite (database file named `<database_name>.db`).
  - **MongoDB Option:** Uses motor for an asynchronous connection.
  
- **backend/requirements.txt:**  
  Lists Python dependencies for FastAPI:
  - `fastapi`
  - `uvicorn`
  - `SQLAlchemy` (if SQL) or `motor` (if MongoDB)

- **backend/README.md:**  
  Provides basic documentation for the FastAPI backend.

### Express.js Backend

- **backend/app.js:**  
  The entry point for the Express.js server. Sets up the server and imports routes.

- **backend/routes/index.js:**  
  Defines a basic GET route that returns a greeting.

- **backend/routes/users.js:**  
  A placeholder file for user-related routes.

- **backend/models/user.js:**  
  Placeholder file for data models.

- **backend/controllers/userController.js:**  
  Placeholder file for controller logic.

- **backend/db.js:**  
  Sets up the database connection:
  - **SQL Option:** Uses sqlite3 to connect to an SQLite database file named `<database_name>.db`.
  - **MongoDB Option:** Uses mongoose to connect to a local MongoDB instance with the provided database name.

- **backend/package.json:**  
  Manages Node.js dependencies for Express.js:
  - Includes `express`.
  - Adds `sqlite3` (if SQL) or `mongoose` (if MongoDB) as an extra dependency.

- **backend/README.md:**  
  Provides basic documentation for the Express.js backend.

## Database Setup

When you run the script, you will be prompted for:
- The database type (SQL or MongoDB).
- The database name.

Based on your selection:
- **FastAPI:**  
  The file **backend/app/core/database.py** is created to set up the database connection.
- **Express.js:**  
  The file **backend/db.js** is created to set up the connection.

## Logging and Debugging

The script creates a **log/** folder at the project root containing:
- **setup.log:** Records the overall steps of the project setup.
- **frontend.log:** Logs detailed actions during the frontend creation process.
- **backend.log:** Logs detailed actions during backend and database setup.

Each log entry is timestamped to aid troubleshooting.

## Installation Guide

### Frontend

1. **Navigate to the Frontend Directory:**
   ```bash
   cd <project-name>/frontend
   ```
2. **Install Dependencies:**
   ```bash
   npm install
   ```
3. **Start the Development Server:**
   ```bash
   npm run dev
   ```

### Backend

#### For FastAPI

1. **Navigate to the Backend Directory:**
   ```bash
   cd <project-name>/backend
   ```
2. **Create a Virtual Environment and Activate It:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
4. **Run the Server:**
   ```bash
   uvicorn app.main:app --reload
   ```

#### For Express.js

1. **Navigate to the Backend Directory:**
   ```bash
   cd <project-name>/backend
   ```
2. **Install Dependencies:**
   ```bash
   npm install
   ```
3. **Start the Server:**
   ```bash
   npm start
   ```

## Usage and Maintenance

- **Frontend:**  
  Develop your React application within the **src/** folder. Customize components, styles, and configuration files as needed. Use the Vite development server for live reloading.

- **Backend:**  
  Expand the FastAPI or Express.js structure by adding routes, models, and controllers as your project evolves. Update the database configuration if necessary.

- **Logging:**  
  Review the log files in the **log/** folder for details about the setup process and for troubleshooting.

## Environment Configuration

- **Python Environment:** Ensure Python 3 is installed.
- **Node Environment:** Install Node.js and npm.
- **Database:**  
  - SQL: The default is SQLite.
  - MongoDB: Ensure MongoDB is installed and running locally.

## Security Recommendations

- Regularly update all dependencies.
- Use HTTPS in production environments.
- Sanitize all user inputs on both the frontend and backend.
- Consider using environment variables for sensitive configuration data.

## Testing and Quality Assurance

- **Frontend:**  
  Consider using Jest and React Testing Library for testing your components.
- **Backend (FastAPI):**  
  Use pytest for testing endpoints and functionality.
- **Backend (Express.js):**  
  Consider using Mocha, Chai, or Jest for testing.
- Automated testing is recommended to ensure application stability.

## Continuous Integration / Continuous Deployment (CI/CD)

- Integrate with CI/CD tools like GitHub Actions, Travis CI, or Jenkins.
- Automate testing, building, and deployment processes for both the frontend and backend.

## Customization and Extensions

- **Frontend Customization:**  
  - Modify React components, styling, and configurations within the **src/** folder.
  - Extend the **ThemeContext.jsx** in **src/store/** to support additional themes.
  - Update the Axios instance in **src/lib/axios.js** if needed.
  - Customize toggle button components in **src/components/ToggleThemeButtons.jsx**.
  - The **HomePage.jsx** component in **src/pages/** is a starting point that displays your project name and demonstrates dark mode styling.
  
- **Backend Customization:**  
  - For FastAPI, add more models, schemas, and routers under **backend/app/**.
  - For Express.js, expand routes, models, and controllers in the **backend/** folder.
  - Modify the database setup files (**backend/app/core/database.py** for FastAPI or **backend/db.js** for Express.js) as required.

## References

For further guidance and to learn more about the technologies used, refer to these official resources:
- **Python Documentation:** [https://docs.python.org/3/](https://docs.python.org/3/)
- **FastAPI Documentation:** [https://fastapi.tiangolo.com/](https://fastapi.tiangolo.com/)
- **Express.js Documentation:** [https://expressjs.com/](https://expressjs.com/)
- **React Documentation:** [https://reactjs.org/](https://reactjs.org/)
- **Vite Documentation:** [https://vitejs.dev/](https://vitejs.dev/)
- **Tailwind CSS Documentation:** [https://tailwindcss.com/](https://tailwindcss.com/)
- **Axios Documentation:** [https://axios-http.com/](https://axios-http.com/)
- **React Hot Toast Documentation:** [https://react-hot-toast.com/](https://react-hot-toast.com/)
- **SQLAlchemy Documentation:** [https://docs.sqlalchemy.org/](https://docs.sqlalchemy.org/)
- **Motor (MongoDB) Documentation:** [https://motor.readthedocs.io/](https://motor.readthedocs.io/)
- **sqlite3 Documentation:** [https://docs.python.org/3/library/sqlite3.html](https://docs.python.org/3/library/sqlite3.html)
- **Mongoose Documentation:** [https://mongoosejs.com/](https://mongoosejs.com/)
- **Node.js Documentation:** [https://nodejs.org/en/docs/](https://nodejs.org/en/docs/)
- **npm Documentation:** [https://docs.npmjs.com/](https://docs.npmjs.com/)

## Final Notes

This setup script is designed to streamline the creation of a full-stack project environment for internal use. It automates the generation of a robust project structure, integrates logging and database configuration, and provides a solid starting point for both frontend and backend development.

For any issues during the setup process, review the log files in the **log/** folder. Customize and extend the generated files as needed to suit your specific project requirements.

*End of README*

---
