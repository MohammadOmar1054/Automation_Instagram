import asyncio
from playwright.async_api import async_playwright
from credentials import username, password

async def send_instagram_message(username, password, recipients, message):
    async with async_playwright() as p:
        # Use persistent context to save login session
        context = await p.chromium.launch_persistent_context(
            user_data_dir="instagram_session",
            headless=False,
            viewport={"width": 1200, "height": 800}
        )
        page = context.pages[0]

        # Go to login page
        await page.goto('https://www.instagram.com/accounts/login/', timeout=60000)
        await page.wait_for_load_state('domcontentloaded', timeout=60000)

        # Check if already logged in
        try:
            await page.wait_for_selector('svg[aria-label="Home"]', timeout=5000)
            print("Already logged in!")
        except:
            # Fill credentials if not logged in
            await page.fill('input[name="username"]', username)
            await page.fill('input[name="password"]', password)
            await page.click('button[type="submit"]')
            await page.wait_for_load_state('domcontentloaded', timeout=60000)

        # Handle popups
        try:
            await page.wait_for_selector('button:has-text("Allow all cookies")', timeout=10000)
            await page.click('button:has-text("Allow all cookies")')
        except:
            pass

        try:
            await page.wait_for_selector('button:has-text("Not Now")', timeout=10000)
            await page.click('button:has-text("Not Now")')
        except:
            pass

        # Go to home
        await page.goto('https://www.instagram.com/', timeout=60000)
        await page.wait_for_load_state('domcontentloaded', timeout=60000)

        # Handle login challenges
        try:
            await page.wait_for_selector('button:has-text("Dismiss")', timeout=10000)
            await page.click('button:has-text("Dismiss")')
        except:
            pass

        # Try to find the DM icon
        try:
            await page.wait_for_selector('div:has-text("Messages")', timeout=60000)
            await page.click('div:has-text("Messages")')
        except Exception as e:
            print(f"Could not find DM icon: {e}")
            try:
                await page.wait_for_selector('div:has-text("Direct")', timeout=60000)
                await page.click('div:has-text("Direct")')
            except Exception as e2:
                print(f"Could not find DM icon with fallback selector: {e2}")
                await context.close()
                return

        await page.wait_for_load_state('domcontentloaded', timeout=60000)

        for recipient in recipients:
            try:
                await page.wait_for_selector('div[role="button"][aria-label="Write a message"]', timeout=60000)
                await page.click('div[role="button"][aria-label="Write a message"]')
            except Exception as e:
                print(f"Could not find new message button: {e}")
                continue

            try:
                await page.wait_for_selector('input[aria-label="Search"]', timeout=60000)
                await page.fill('input[aria-label="Search"]', recipient)
            except Exception as e:
                print(f"Could not find search input: {e}")
                continue

            try:
                await page.wait_for_selector(f'div[role="button"] >> text="{recipient}"', timeout=60000)
                await page.click(f'div[role="button"] >> text="{recipient}"')
            except Exception as e:
                print(f"Could not find recipient {recipient}: {e}")
                continue

            try:
                await page.wait_for_selector('div[role="textbox"]', timeout=60000)
                await page.fill('div[role="textbox"]', message)
                await page.keyboard.press('Enter')
            except Exception as e:
                print(f"Could not send message to {recipient}: {e}")
                continue

            await page.wait_for_timeout(2000)

        await context.close()

recipients = ['_.3rzxii']
message = 'Hello! This is a test message.'
asyncio.run(send_instagram_message(username, password, recipients, message))
