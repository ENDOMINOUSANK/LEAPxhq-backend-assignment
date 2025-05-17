import uuid
from playwright.async_api import async_playwright

class BrowserManager:
    sessions = {}

    @classmethod
    async def start_session(cls, browser_name, headless, url=None):
        if browser_name not in ["chromium", "firefox", "webkit"]:
            raise Exception("Invalid browser name. Supported browsers: chromium, firefox, webkit.")
        print(f"Starting {browser_name} session...")
        print(f"Headless mode: {headless}")
        playwright = await async_playwright().start()
        browser = await getattr(playwright, browser_name).launch(headless=headless)
        context = await browser.new_context()
        page = await context.new_page()
        if url:
            try:
                print(f"Navigating to: {url}")
                await page.goto(url, wait_until="load")
                print(f"Navigation to {url} complete. Current URL: {page.url}")
            except Exception as e:
                print(f"Navigation error: {e}")
        session_id = str(uuid.uuid4())
        cls.sessions[session_id] = {
            "playwright": playwright,
            "browser": browser,
            "context": context,
            "page": page
        }
        return session_id

    @classmethod
    async def get_page(cls, session_id):
        if session_id not in cls.sessions:
            raise Exception("Invalid sessionId")
        return cls.sessions[session_id]["page"]

    @classmethod
    async def close_session(cls, session_id):
        if session_id in cls.sessions:
            await cls.sessions[session_id]["browser"].close()
            await cls.sessions[session_id]["playwright"].stop()
            del cls.sessions[session_id]