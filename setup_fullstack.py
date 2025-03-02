#!/usr/bin/env python3
"""
Full-Stack Project Setup Script (Final Version with Database Setup)

This script:
  1) Prompts for a project name, a backend framework choice (FastAPI or Express),
     a database choice (SQL or MongoDB), and a database name.
  2) Creates a 'log' folder with setup.log, frontend.log, and backend.log.
  3) Generates the frontend folder structure with:
       - Top-level folders: public/ (empty), src/
       - Under src/, subfolders: assets/, components/, config/, lib/, pages/, store/
       - Top-level files: .gitignore, eslint.config.js, index.html, package.json,
         postcss.config.js, README.md, tailwind.config.js, vite.config.js
       - Files in src/: App.jsx, index.css, main.jsx,
         plus src/store/ThemeContext.jsx, src/lib/axios.js,
         and src/components/ToggleThemeButtons.jsx.
       - Also creates src/pages/HomePage.jsx which displays a welcome message including
         the project name and demonstrates dark mode styling.
  4) Generates the backend folder:
       - For FastAPI: creates backend/app with subfolders (models, schemas, routers, core),
         a main.py file, and a database setup file at backend/app/core/database.py.
       - For Express.js: creates backend with subdirectories (routes, models, controllers),
         an app.js file, a database setup file at backend/db.js, and a package.json updated
         with extra dependencies based on the database choice.
  
Make sure you have Python 3 installed. Run this script to generate your project.
"""

import sys
import datetime
from pathlib import Path

def log_message(log_file: Path, message: str):
    """Append a timestamped message to the given log file."""
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with log_file.open("a", encoding="utf-8") as f:
        f.write(f"[{timestamp}] {message}\n")

def get_user_inputs():
    """Prompt user for project name, backend choice, and database info."""
    project_name = input("Enter the project name: ").strip()
    if not project_name:
        print("No project name provided. Exiting.")
        sys.exit(1)

    print("\nChoose your backend framework:")
    print("  1. FastAPI (Python)")
    print("  2. Express.js (Node.js)")
    backend_choice = input("Enter 1 or 2: ").strip()
    if backend_choice not in ("1", "2"):
        print("Invalid backend choice. Exiting.")
        sys.exit(1)

    print("\nChoose your database:")
    print("  1. SQL")
    print("  2. MongoDB")
    db_choice = input("Enter 1 or 2: ").strip()
    if db_choice not in ("1", "2"):
        print("Invalid database choice. Exiting.")
        sys.exit(1)

    db_name = input("Enter the database name: ").strip()
    if not db_name:
        print("No database name provided. Exiting.")
        sys.exit(1)

    return project_name, backend_choice, db_choice, db_name

def create_log_files(project_dir: Path):
    """Creates a 'log' directory with setup.log, frontend.log, and backend.log."""
    log_dir = project_dir / "log"
    log_dir.mkdir(parents=True, exist_ok=True)
    (log_dir / "setup.log").write_text(f"Setup started at {datetime.datetime.now()}\n", encoding="utf-8")
    (log_dir / "frontend.log").write_text("", encoding="utf-8")
    (log_dir / "backend.log").write_text("", encoding="utf-8")
    return log_dir

def create_frontend_files(project_dir: Path, log_dir: Path, project_name: str):
    """Creates the complete frontend structure and files."""
    frontend_dir = project_dir / "frontend"
    frontend_dir.mkdir(exist_ok=True)

    # Create top-level directories: public, src (do not create node_modules explicitly)
    for folder in ["public", "src"]:
        (frontend_dir / folder).mkdir(parents=True, exist_ok=True)

    # Create additional subdirectories under src (using 'components' in plural)
    for subfolder in ["assets", "components", "config", "lib", "pages", "store"]:
        (frontend_dir / "src" / subfolder).mkdir(parents=True, exist_ok=True)

    # Define top-level file contents (removed package-lock.json)
    files_and_content = {
        ".gitignore": (
            "# Logs\n"
            "logs\n"
            "*.log\n"
            "npm-debug.log*\n"
            "yarn-debug.log*\n"
            "yarn-error.log*\n"
            "pnpm-debug.log*\n"
            "lerna-debug.log*\n\n"
            "node_modules\n"
            "dist\n"
            "dist-ssr\n"
            "*.local\n\n"
            "# Editor directories and files\n"
            ".vscode/*\n"
            "!.vscode/extensions.json\n"
            ".idea\n"
            ".DS_Store\n"
            "*.suo\n"
            "*.ntvs*\n"
            "*.njsproj\n"
            "*.sln\n"
            "*.sw?\n"
        ),
        "eslint.config.js": (
            "import js from '@eslint/js'\n"
            "import globals from 'globals'\n"
            "import react from 'eslint-plugin-react'\n"
            "import reactHooks from 'eslint-plugin-react-hooks'\n"
            "import reactRefresh from 'eslint-plugin-react-refresh'\n\n"
            "export default [\n"
            "  { ignores: ['dist'] },\n"
            "  {\n"
            "    files: ['**/*.{js,ts,jsx,tsx}'],\n"
            "    languageOptions: {\n"
            "      ecmaVersion: 2020,\n"
            "      globals: globals.browser,\n"
            "      parserOptions: {\n"
            "        ecmaVersion: 'latest',\n"
            "        ecmaFeatures: { jsx: true },\n"
            "        sourceType: 'module',\n"
            "      },\n"
            "    },\n"
            "    settings: { react: { version: '18.3' } },\n"
            "    plugins: {\n"
            "      react,\n"
            "      'react-hooks': reactHooks,\n"
            "      'react-refresh': reactRefresh,\n"
            "    },\n"
            "    rules: {\n"
            "      ...js.configs.recommended.rules,\n"
            "      ...react.configs.recommended.rules,\n"
            "      ...react.configs['jsx-runtime'].rules,\n"
            "      ...reactHooks.configs.recommended.rules,\n"
            "      'react/jsx-no-target-blank': 'off',\n"
            "      'react-refresh/only-export-components': [\n"
            "        'warn', { allowConstantExport: true },\n"
            "      ],\n"
            "    },\n"
            "  },\n"
            "]\n"
        ),
        "index.html": (
            "<!doctype html>\n"
            "<html lang=\"en\">\n"
            "<head>\n"
            "  <meta charset=\"UTF-8\" />\n"
            "  <link rel=\"icon\" type=\"image/svg+xml\" href=\"logo.png\" />\n"
            "  <meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\" />\n"
            f"  <title>{project_name}</title>\n"
            "</head>\n"
            "<body>\n"
            "  <div id=\"root\"></div>\n"
            "  <script type=\"module\" src=\"/src/main.jsx\"></script>\n"
            "</body>\n"
            "</html>\n"
        ),
        "package.json": (
            "{\n"
            "  \"name\": \"frontend\",\n"
            "  \"private\": true,\n"
            "  \"version\": \"0.0.0\",\n"
            "  \"type\": \"module\",\n"
            "  \"scripts\": {\n"
            "    \"dev\": \"vite\",\n"
            "    \"build\": \"vite build\",\n"
            "    \"lint\": \"eslint .\",\n"
            "    \"preview\": \"vite preview\"\n"
            "  },\n"
            "  \"dependencies\": {\n"
            "    \"react-router-dom\": \"^7.0.2\",\n"
            "    \"tailwindcss\": \"^3.4.16\",\n"
            "    \"axios\": \"^1.4.0\",\n"
            "    \"react-hot-toast\": \"^2.4.1\"\n"
            "  },\n"
            "  \"devDependencies\": {\n"
            "    \"vite\": \"^6.0.1\",\n"
            "    \"@vitejs/plugin-react\": \"^4.3.4\",\n"
            "    \"autoprefixer\": \"^10.4.20\",\n"
            "    \"postcss\": \"^8.4.49\",\n"
            "    \"tailwindcss\": \"^3.4.16\"\n"
            "  }\n"
            "}\n"
        ),
        "postcss.config.js": (
            "import tailwindcss from 'tailwindcss'\n"
            "import autoprefixer from 'autoprefixer'\n\n"
            "export default {\n"
            "  plugins: [tailwindcss, autoprefixer]\n"
            "}\n"
        ),
        "README.md": "# My Frontend Project\n\nMinimal README content.\n",
        "tailwind.config.js": (
            "/** @type {import('tailwindcss').Config} */\n"
            "export default {\n"
            "  darkMode: 'class',\n"
            "  content: [\n"
            "    \"./index.html\",\n"
            "    \"./src/**/*.{js,ts,jsx,tsx}\"\n"
            "  ],\n"
            "  theme: {\n"
            "    extend: {\n"
            "      screens: { xs: '480px' },\n"
            "      aspectRatio: {\n"
            "        '1/5': '4 / 5',\n"
            "        '3/1': '3 / 1',\n"
            "        '12/7': '12 / 7'\n"
            "      },\n"
            "      keyframes: {\n"
            "        spin: {\n"
            "          '0%': { transform: 'rotate(0deg)' },\n"
            "          '100%': { transform: 'rotate(360deg)' }\n"
            "        },\n"
            "        alertShake: {\n"
            "          '0%, 100%': { transform: 'translateX(0)' },\n"
            "          '25%': { transform: 'translateX(-5px)' },\n"
            "          '50%': { transform: 'translateX(5px)' },\n"
            "          '75%': { transform: 'translateX(-5px)' }\n"
            "        },\n"
            "        alertBgRed: {\n"
            "          '0%, 100%': { backgroundColor: 'transparent' },\n"
            "          '50%': { backgroundColor: 'rgba(255, 0, 0, 0.7)' }\n"
            "        }\n"
            "      },\n"
            "      animation: {\n"
            "        'spin-slow': 'spin 0.8s linear infinite',\n"
            "        spin: 'spin 2s linear infinite',\n"
            "        pulse: 'pulse 1s ease-in-out infinite',\n"
            "        alert: 'alertShake 0.5s ease, alertBgRed 0.5s ease'\n"
            "      }\n"
            "    }\n"
            "  },\n"
            "  plugins: []\n"
            "}\n"
        ),
        "vite.config.js": (
            "import { defineConfig } from 'vite'\n"
            "import react from '@vitejs/plugin-react'\n\n"
            "// https://vite.dev/config/\n"
            "export default defineConfig({\n"
            "  plugins: [react()],\n"
            "})\n"
        )
    }

    for filename, content in files_and_content.items():
        (frontend_dir / filename).write_text(content, encoding="utf-8")

    # Files in src/ folder: App.jsx, index.css, main.jsx
    src_files = {
        "App.jsx": (
            "import React from 'react';\n"
            "import { Route, Routes } from 'react-router-dom';\n"
            "import { Toaster } from 'react-hot-toast';\n"
            "import HomePage from './pages/HomePage';\n"
            "import { ToggleThemeBtn } from './components/ToggleThemeButtons';\n\n"
            "const App = () => {\n"
            "  return (\n"
            "    <div className=\"relative dark:bg-[#1a1a1a] dark:text-white bg-white\">\n"
            "      <Routes>\n"
            "        <Route path=\"/\" element={<HomePage />} />\n"
            "      </Routes>\n"
            "      <Toaster position=\"top-right\" reverseOrder={false} />\n"
            "      <div className=\"fixed bottom-2 right-2\">\n"
            "        <ToggleThemeBtn size={10} />\n"
            "      </div>\n"
            "    </div>\n"
            "  );\n"
            "};\n\n"
            "export default App;\n"
        ),
        "index.css": (
            "@tailwind base;\n"
            "@tailwind components;\n"
            "@tailwind utilities;\n"
        ),
        "main.jsx": (
            "import { StrictMode } from 'react';\n"
            "import { createRoot } from 'react-dom/client';\n"
            "import './index.css';\n"
            "import App from './App.jsx';\n"
            "import { BrowserRouter } from 'react-router-dom';\n"
            "import { ThemeProvider } from './store/ThemeContext.jsx';\n\n"
            "createRoot(document.getElementById('root')).render(\n"
            "  <StrictMode>\n"
            "    <BrowserRouter>\n"
            "      <ThemeProvider>\n"
            "        <App />\n"
            "      </ThemeProvider>\n"
            "    </BrowserRouter>\n"
            "  </StrictMode>\n"
            ");\n"
        )
    }

    for filename, content in src_files.items():
        (frontend_dir / "src" / filename).write_text(content, encoding="utf-8")

    # Create src/pages/HomePage.jsx with a simple component that shows the project name and dark mode styling
    home_page_path = frontend_dir / "src" / "pages" / "HomePage.jsx"
    home_page_content = f"""import React from 'react';

const HomePage = () => {{
  return (
    <div className="p-4 dark:bg-gray-800 dark:text-white bg-white text-black">
      <h1 className="text-2xl font-bold">Welcome to the Project: {project_name}</h1>
      <p className="mt-2">This is the homepage. Toggle dark mode to see the effect.</p>
    </div>
  );
}};

export default HomePage;
"""
    home_page_path.write_text(home_page_content, encoding="utf-8")

    # Create src/store/ThemeContext.jsx
    theme_context_content = (
        "import { createContext, useState, useEffect } from 'react';\n\n"
        "export const ThemeContext = createContext();\n\n"
        "export const ThemeProvider = ({ children }) => {\n"
        "  // Function to get system theme preference\n"
        "  const getSystemTheme = () => {\n"
        "    return window.matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light';\n"
        "  };\n\n"
        "  // Initialize theme state\n"
        "  const [theme, setTheme] = useState(() => {\n"
        "    // Check localStorage for saved theme, otherwise use system preference\n"
        "    return localStorage.getItem('theme') || getSystemTheme();\n"
        "  });\n\n"
        "  // Apply theme to the root HTML element\n"
        "  useEffect(() => {\n"
        "    const root = window.document.documentElement;\n"
        "    root.classList.remove(theme === 'dark' ? 'light' : 'dark');\n"
        "    root.classList.add(theme);\n"
        "    localStorage.setItem('theme', theme);\n"
        "  }, [theme]);\n\n"
        "  // Toggle between light and dark themes\n"
        "  const toggleTheme = () => {\n"
        "    setTheme((prevTheme) => (prevTheme === 'light' ? 'dark' : 'light'));\n"
        "  };\n\n"
        "  // Optional: Listen for system theme changes\n"
        "  useEffect(() => {\n"
        "    const mediaQuery = window.matchMedia('(prefers-color-scheme: dark)');\n"
        "    const handleChange = (e) => {\n"
        "      if (!localStorage.getItem('theme')) {\n"
        "        setTheme(e.matches ? 'dark' : 'light');\n"
        "      }\n"
        "    };\n\n"
        "    mediaQuery.addEventListener('change', handleChange);\n"
        "    return () => mediaQuery.removeEventListener('change', handleChange);\n"
        "  }, []);\n\n"
        "  return (\n"
        "    <ThemeContext.Provider value={{ theme, toggleTheme }}>\n"
        "      {children}\n"
        "    </ThemeContext.Provider>\n"
        "  );\n"
        "};\n\n"
        "export default ThemeContext;\n"
    )
    (frontend_dir / "src" / "store" / "ThemeContext.jsx").write_text(theme_context_content, encoding="utf-8")

    # Create src/lib/axios.js
    axios_content = (
        "import axios from \"axios\";\n\n"
        "export const axiosInstance = axios.create({\n"
        "    baseURL: \"http://localhost:3000/api\",\n"
        "    withCredentials: true,\n"
        "});\n"
    )
    (frontend_dir / "src" / "lib" / "axios.js").write_text(axios_content, encoding="utf-8")

    # Create src/components/ToggleThemeButtons.jsx without the lucide-react import
    components_dir = frontend_dir / "src" / "components"
    components_dir.mkdir(parents=True, exist_ok=True)
    toggle_buttons_content = (
        "// Removed import { Moon, Sun } from 'lucide-react'; as per requirements\n"
        "import React, { useContext } from 'react';\n"
        "import { ThemeContext } from '../store/ThemeContext.jsx';\n\n"
        "// ✅ Simple Toggle Theme Button Component\n"
        "export const SimpleToggleThemeBtn = ({ size = 14 }) => {\n"
        "    const { theme, toggleTheme } = useContext(ThemeContext);\n\n"
        "    return (\n"
        "        <label htmlFor=\"dark-toggle\" className={`flex items-center cursor-pointer gap-${size / 2}`}>\n"
        "            <div className=\"relative\">\n"
        "                <input\n"
        "                    type=\"checkbox\"\n"
        "                    id=\"dark-toggle\"\n"
        "                    className=\"hidden\"\n"
        "                    checked={theme === 'dark'}\n"
        "                    onChange={toggleTheme}\n"
        "                />\n"
        "                <div className={`block border border-gray-800 dark:border-white w-${size} h-${size / 2} rounded-full`}></div>\n"
        "                <div className={`dot absolute left-1 top-1 w-${size / 3.5} h-${size / 3.5} rounded-full transition transform ${theme === 'dark' ? `translate-x-${size / 1.75} bg-white` : 'translate-x-0 bg-gray-800'}`}></div>\n"
        "            </div>\n"
        "        </label>\n"
        "    );\n"
        "};\n\n"
        "// ✅ Styled Toggle Theme Button Component\n"
        "export const DesignedToggleBtn = ({ size = 12 }) => {\n"
        "    const { theme, toggleTheme } = useContext(ThemeContext);\n\n"
        "    return (\n"
        "        <div className={`border border-gray-500 p-1 rounded-full flex justify-between w-${size * 3}`} onClick={toggleTheme}>\n"
        "            <button\n"
        "                type=\"button\"\n"
        "                className={`rounded-full py-1 px-2 text-sm font-semibold ${theme === 'light' ? 'bg-gray-500 text-white' : 'text-gray-400'}`}\n"
        "            >\n"
        "                Light\n"
        "            </button>\n\n"
        "            <button\n"
        "                type=\"button\"\n"
        "                className={`rounded-full py-1 px-2 text-sm font-semibold ${theme === 'dark' ? 'bg-gray-800 text-white' : 'text-gray-400'}`}\n"
        "            >\n"
        "                Dark\n"
        "            </button>\n"
        "        </div>\n"
        "    );\n"
        "};\n\n"
        "// ✅ Dynamic Size Toggle Theme Button Component\n"
        "export const ToggleThemeBtn = ({ size = 10 }) => {\n"
        "    const { theme, toggleTheme } = useContext(ThemeContext);\n"
        "    return (\n"
        "        <button\n"
        "            onClick={toggleTheme}\n"
        "            className={`relative w-${size * 2} h-${size} flex items-center justify-between rounded-full bg-gray-200 dark:bg-gray-600 p-1 transition-all duration-300`}\n"
        "            aria-label=\"Toggle Dark Mode\"\n"
        "        >\n"
        "            <span className={`absolute w-${size - 2} h-${size - 2} bg-white dark:bg-gray-800 rounded-full shadow-md transform transition-transform duration-300 ${theme === 'dark' ? `right-1` : 'left-1'}`}></span>\n"
        "        </button>\n"
        "    );\n"
        "};\n\n"
        "export const ImagesToggleBtn = ({ size = 12 }) => {\n"
        "    const { theme, toggleTheme } = useContext(ThemeContext);\n"
        "    return (\n"
        "        <button\n"
        "            onClick={toggleTheme}\n"
        "            className={`relative w-${size} h-${size} flex items-center justify-center rounded-full bg-gray-200 dark:bg-gray-800 shadow-md transition-all duration-300 focus:outline-none`}\n"
        "            aria-label=\"Toggle Dark Mode\"\n"
        "        >\n"
        "            {theme === 'dark' ? (\n"
        "                <svg\n"
        "                    xmlns=\"http://www.w3.org/2000/svg\"\n"
        "                    className={`w-${size / 1.5} h-${size / 1.5} text-yellow-400`}\n"
        "                    fill=\"none\"\n"
        "                    viewBox=\"0 0 24 24\"\n"
        "                    stroke=\"currentColor\"\n"
        "                    strokeWidth={2}\n"
        "                >\n"
        "                    <path strokeLinecap=\"round\" strokeLinejoin=\"round\" d=\"M12 3v2m0 14v2m9-9h-2M5 12H3m16.364-7.364l-1.414 1.414M7.05 16.95l-1.414 1.414m12.728 0l-1.414-1.414M7.05 7.05L5.636 5.636M12 8a4 4 0 100 8 4 4 0 000-8z\" />\n"
        "                </svg>\n"
        "            ) : (\n"
        "                <svg\n"
        "                    xmlns=\"http://www.w3.org/2000/svg\"\n"
        "                    className={`w-${size / 1.5} h-${size / 1.5} text-blue-500`}\n"
        "                    fill=\"none\"\n"
        "                    viewBox=\"0 0 24 24\"\n"
        "                    stroke=\"currentColor\"\n"
        "                    strokeWidth={2}\n"
        "                >\n"
        "                    <path strokeLinecap=\"round\" strokeLinejoin=\"round\" d=\"M20.354 15.354A9 9 0 118.646 3.646 7 7 0 0020.354 15.354z\" />\n"
        "                </svg>\n"
        "            )}\n"
        "        </button>\n"
        "    );\n"
        "};\n"
    )
    (components_dir / "ToggleThemeButtons.jsx").write_text(toggle_buttons_content, encoding="utf-8")

    log_message(log_dir / "frontend.log", "Frontend structure created successfully.")

def create_db_setup_files(project_dir: Path, backend_choice: str, db_choice: str, db_name: str, log_dir: Path):
    """Creates the database setup file based on backend and database choice."""
    if backend_choice == "1":
        # FastAPI: create backend/app/core/database.py
        core_dir = project_dir / "backend" / "app" / "core"
        db_file = core_dir / "database.py"
        if db_choice == "1":  # SQL (using SQLite as example)
            content = (
                "from sqlalchemy import create_engine\n"
                "from sqlalchemy.orm import sessionmaker\n\n"
                f"SQLALCHEMY_DATABASE_URL = \"sqlite:///./{db_name}.db\"\n"
                "engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={\"check_same_thread\": False})\n"
                "SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)\n"
            )
        else:  # MongoDB (using motor)
            content = (
                "from motor.motor_asyncio import AsyncIOMotorClient\n\n"
                "MONGODB_URL = \"mongodb://localhost:27017\"\n"
                f"client = AsyncIOMotorClient(MONGODB_URL)\n"
                f"db = client[\"{db_name}\"]\n"
            )
        db_file.write_text(content, encoding="utf-8")
    elif backend_choice == "2":
        # Express.js: create backend/db.js
        db_file = project_dir / "backend" / "db.js"
        if db_choice == "1":  # SQL (using sqlite3 as example)
            content = (
                "// SQL Database setup (example using sqlite3)\n"
                "const sqlite3 = require('sqlite3').verbose();\n"
                f"const db = new sqlite3.Database(`./{db_name}.db`, (err) => {{\n"
                "    if (err) {\n"
                "        console.error(err.message);\n"
                "    }\n"
                "    console.log('Connected to the SQLite database.');\n"
                "});\n"
                "module.exports = db;\n"
            )
        else:  # MongoDB (using mongoose)
            content = (
                "// MongoDB Database setup using mongoose\n"
                "const mongoose = require('mongoose');\n"
                f"mongoose.connect(`mongodb://localhost:27017/{db_name}`, {{ useNewUrlParser: true, useUnifiedTopology: true }})\n"
                "    .then(() => console.log('Connected to MongoDB'))\n"
                "    .catch((err) => console.error('MongoDB connection error:', err));\n"
                "module.exports = mongoose;\n"
            )
        db_file.write_text(content, encoding="utf-8")
    else:
        print("Invalid backend choice in DB setup. Exiting.")
        sys.exit(1)
    log_message(log_dir / "backend.log", f"Database setup file created for {'SQL' if db_choice == '1' else 'MongoDB'} with name '{db_name}'.")

def create_backend_files(project_dir: Path, backend_choice: str, db_choice: str, log_dir: Path):
    """Creates the backend folder structure with minimal sample files, including updated package dependencies."""
    backend_dir = project_dir / "backend"
    backend_dir.mkdir(exist_ok=True)

    if backend_choice == "1":
        # FastAPI backend
        app_dir = backend_dir / "app"
        subdirs = ["models", "schemas", "routers", "core"]
        for sub in subdirs:
            (app_dir / sub).mkdir(parents=True, exist_ok=True)
        main_py = (
            "from fastapi import FastAPI\n"
            "app = FastAPI()\n\n"
            "@app.get('/')\n"
            "def read_root():\n"
            "    return {'Hello': 'FastAPI'}\n"
        )
        (app_dir / "main.py").write_text(main_py, encoding="utf-8")
        for sub in subdirs:
            (app_dir / sub / "__init__.py").write_text(f"# {sub} init\n", encoding="utf-8")
        (app_dir / "models" / "user.py").write_text("# user model placeholder\n", encoding="utf-8")
        (app_dir / "schemas" / "user.py").write_text("# user schema placeholder\n", encoding="utf-8")
        (app_dir / "routers" / "user.py").write_text("# user router placeholder\n", encoding="utf-8")
        (app_dir / "core" / "config.py").write_text("# config placeholder\n", encoding="utf-8")
        (app_dir / "__init__.py").write_text("# backend app init\n", encoding="utf-8")
        # Update requirements.txt with additional packages
        req_content = "fastapi>=0.68.0\nuvicorn>=0.18.0\n"
        if db_choice == "1":
            req_content += "SQLAlchemy>=1.4.0\n"
        else:
            req_content += "motor>=3.0.0\n"
        (backend_dir / "requirements.txt").write_text(req_content, encoding="utf-8")
        readme_content = "# Backend (FastAPI)\nThis is the FastAPI backend for the project.\n"
        (backend_dir / "README.md").write_text(readme_content, encoding="utf-8")
        log_message(log_dir / "backend.log", "FastAPI backend created.")
    elif backend_choice == "2":
        # Express.js backend
        subdirs = ["routes", "models", "controllers"]
        for sub in subdirs:
            (backend_dir / sub).mkdir(parents=True, exist_ok=True)
        app_js = (
            "const express = require('express');\n"
            "const app = express();\n"
            "const indexRouter = require('./routes/index');\n"
            "app.use('/', indexRouter);\n"
            "const PORT = process.env.PORT || 3000;\n"
            "app.listen(PORT, () => {\n"
            "  console.log(`Server running on port ${PORT}`);\n"
            "});\n"
        )
        (backend_dir / "app.js").write_text(app_js, encoding="utf-8")
        index_js = (
            "// routes index.js\n"
            "const express = require('express');\n"
            "const router = express.Router();\n"
            "router.get('/', (req, res) => {\n"
            "  res.send('Hello from Express.js');\n"
            "});\n"
            "module.exports = router;\n"
        )
        (backend_dir / "routes" / "index.js").write_text(index_js, encoding="utf-8")
        (backend_dir / "routes" / "users.js").write_text("// placeholder for user route\n", encoding="utf-8")
        (backend_dir / "models" / "user.js").write_text("// placeholder for user model\n", encoding="utf-8")
        (backend_dir / "controllers" / "userController.js").write_text("// placeholder for user controller\n", encoding="utf-8")
        # Update package.json with additional dependencies for Express.js
        if db_choice == "1":
            extra_deps = '"sqlite3": "^5.1.2"'
        else:
            extra_deps = '"mongoose": "^7.0.0"'
        package_json = (
            "{\n"
            '  "name": "backend",\n'
            '  "version": "1.0.0",\n'
            '  "main": "app.js",\n'
            '  "scripts": {\n'
            '    "start": "node app.js"\n'
            "  },\n"
            '  "dependencies": {\n'
            '    "express": "^4.17.1",\n'
            f"    {extra_deps}\n"
            "  }\n"
            "}\n"
        )
        (backend_dir / "package.json").write_text(package_json, encoding="utf-8")
        readme_content = "# Backend (Express.js)\nThis is the Express.js backend for the project.\n"
        (backend_dir / "README.md").write_text(readme_content, encoding="utf-8")
        log_message(log_dir / "backend.log", "Express.js backend created.")
    else:
        log_message(log_dir / "backend.log", "Invalid backend choice.")
        print("Invalid backend option. Exiting.")
        sys.exit(1)

def main():
    project_name, backend_choice, db_choice, db_name = get_user_inputs()
    project_dir = Path(project_name)
    project_dir.mkdir(exist_ok=True)

    # Create log directory and log files
    log_dir = create_log_files(project_dir)
    log_message(log_dir / "setup.log", "Created log directory and log files.")

    # Create frontend structure with updated files and new component files
    try:
        create_frontend_files(project_dir, log_dir, project_name)
    except Exception as e:
        log_message(log_dir / "frontend.log", f"Error creating frontend: {e}")
        raise

    # Create backend structure (with DB-dependent package updates)
    try:
        create_backend_files(project_dir, backend_choice, db_choice, log_dir)
    except Exception as e:
        log_message(log_dir / "backend.log", f"Error creating backend: {e}")
        raise

    # Create database setup file based on user's DB choice
    try:
        create_db_setup_files(project_dir, backend_choice, db_choice, db_name, log_dir)
    except Exception as e:
        log_message(log_dir / "backend.log", f"Error creating database setup: {e}")
        raise

    log_message(log_dir / "setup.log", "Setup completed successfully.")
    print(f"\nFull-stack project '{project_name}' created successfully!")
    print("Check the 'log' folder for setup.log, frontend.log, and backend.log for details.\n")

if __name__ == "__main__":
    main()
