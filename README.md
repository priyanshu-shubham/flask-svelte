# Flask-Svelte Documentation

Welcome to Flask-Svelte, a python package that integrates [Svelte](https://svelte.dev/) with [Flask](https://flask.palletsprojects.com/en/1.1.x/). This integration brings together the best of both worlds: Svelte's reactive frontend capabilities and Flask's robust backend, providing a seamless experience for web application development.

Note: This package is still in development. The API is subject to change.

## Key Features
- **Svelte Integration with Flask**: Effortlessly serve Svelte templates as dynamic components within Flask applications.
- **Automatic Live Reloading**: Implement livereload for instant browser updates when templates are modified.
- **Simplified Project Management**: Utilize the CLI for effortless project setup and template handling.
- **Use Python data in Svelte**: The `render_template` function extends Flask's capability, allowing direct data integration into Svelte templates for dynamic content rendering.
- **Tailwind CSS Preinstalled**: Comes with Tailwind CSS, a utility-first CSS framework for rapid UI development, preconfigured and ready to use.

## Getting Started

### Installation and Project Setup
0. **Prerequisites**: Install [Node.js](https://nodejs.org/en/) and [Python](https://www.python.org/downloads/).
1. **Install Flask-Svelte**: 
   ```bash
   pip install flask-svelte
   ```
2. **Create a New Project**: 
   ```bash
   flask-svelte create <project_name>
   ```
3. **Navigate to the Project Directory**: 
   ```bash
   cd <project_name>
   ```
4. **Install JavaScript Dependencies**: 
   ```bash
   npm install
   ```

### Development Workflow
- **Start Development Server**: 
  ```bash
  npm run dev
  ```
- **Add New Svelte Templates**: 
  ```bash
  flask-svelte add-page <template_name>
  ```
  Generates Svelte files in `svelte/<template_name>`. Edit them and see the changes in the browser.
  Note: The `npm run dev` command must be restarted for new templates to be recognized.

### Important Usage Notes
1. **Production Build**: Use `npm run build` for deployment readiness. Post-build, the `svelte` directory is optional.
2. **Data Integration in Templates**: Replace `flask.render_template` with `flask_svelte.render_template` for enhanced data passing. Example:
   ```python
   from flask_svelte import render_template
   from app import app

   @app.route('/')
   def index():
       return render_template('index.html', name='World')
   ```
3. **Accessing Data in Svelte**: Retrieve Flask-passed data in Svelte with `{{ app.data["key"] }}`. Example:
   ```html
   <h1>Hello {{ app.data["name"] }}!</h1>
   ```

## Enhanced Documentation

### `render_template` Function
- **Purpose**: Replaces Flask's `render_template` for integrating Python and JavaScript.
- **Usage**: Passes variables and data from Flask to Svelte components for interactive web applications.

### `app.data` Object
- **Functionality**: Facilitates data transfer between Flask and Svelte.
- **Access in Svelte**: Retrieve Flask data in Svelte templates via `{{ app.data["key"] }}`.

### Command-Line Interface (CLI) Commands
- **Create a New Project**: 
  ```
  flask-svelte create <project_name>
  ```
  Sets up a new Flask-Svelte project environment.
  
- **Add a New Template**: 
  ```
  flask-svelte add-page <template_name>
  ```
  Adds a new Svelte template to your project, creating necessary files in `svelte/<template_name>`.