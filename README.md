[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/iPRzcknB)
# Assignment: Playwright Action API
# uvicorn main:app --loop asyncio
## Objective

Build a REST API service that exposes Playwright browser automation actions (e.g., `click`, `hover`, `fill`, etc.) as real-time HTTP endpoints. The system must support multiple browser sessions and return a screenshot after each action.

---

### Tech Stack

You may use either of the following stacks:

- **Python** with **FastAPI**
- **JavaScript** with **Express.js**

All automation must use **[Playwright](https://playwright.dev/)**.

---

## Core Requirements

### 1. Session Management

Support multiple browser sessions via a `sessionId`. Each action must operate within its own session context.

- #### `POST /session/start`

  Start a new browser session.

  - **Sample Request:**

    ```json
    {
      "browser": "chromium",
      "headless": true,
      // add more config parameters
    }
    ```

  - **Sample Response:**

    ```json
    {
      "sessionId": "abc123"
    }
    ```


- ####  `POST /session/close`

  Close an active session.

  - **Request:**

    ```json
    {
      "sessionId": "abc123"
    }
    ```

---

### 2. Action Endpoints

Expose each Playwright action as a separate endpoint. Each endpoint should:

- Accept a `sessionId`
- Accept a `locator` (either string or structured format)
- Execute in real time
- Return a base64-encoded screenshot

Refer to the full list of actions and their usage here:  
📚 [Playwright Input Actions Documentation](https://playwright.dev/docs/input)

---

### 3. Locator Format

Endpoints must support both:

1.  **String selectors** (e.g., `"text=Submit"`, `"#email"`)

2.  **Structured locators** using role and name:
  

    ```json
    {
      "role": "button",
      "name": "Continue"
    }
    ```

---

## Response Format

Each action endpoint should return:

- **Success:**

  ```json
  {
    "status": "success",
    "screenshot": "base64_png_data"
  }
  ```

- **Error:**

  ```json
  {
    "status": "error",
    "error": "Element not found: text=Login"
  }
  ```

---

## What NOT to Build

- No frontend UI
- No authentication or rate limiting
- No persistent storage for sessions
- No saving of screenshots (return as base64 only)

---

## Bonus 

If you can find and integrate an open source session management library. (it's hard to find, but it exists!)


---