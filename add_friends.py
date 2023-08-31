import asyncio
from playwright.async_api import async_playwright
import data


async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False, args=["--start-maximized"])
        context = await browser.new_context(no_viewport=True)
        page = await context.new_page()

        # open goodreads sign in page
        async def open_goodreads():
            # go to sign in page
            await page.goto(data.BASE_URL)

            await page.wait_for_load_state("networkidle")

            # click sign in button
            await page.get_by_text("Sign in with email").click()
            await page.wait_for_load_state("networkidle")

        await open_goodreads()

        # perform sign in
        async def perform_sign_in():
            await page.locator('input[type="email"]').type(data.EMAIL)
            await page.locator('input[type="password"]').type(data.PASS)
            await page.click("input#signInSubmit")
            await page.wait_for_load_state("networkidle")

        await perform_sign_in()

        # go to friend list url
        await page.wait_for_timeout(4000)
        await page.goto(data.FRIEND_URL)

        # perform add a friend loop
        async def add_friend_loop():
            # get an array of all 'Add as a Friend' button elements
            async def get_all_friend_links():
                # get all selectors for a page
                links = await page.query_selector_all(
                    'xpath=//a[text()="Add as a Friend"]'
                )
                print("total friends to add: ", len(links))

                # create a for loop to click each button
                for link in links:
                    await link.click()
                    print("friend added!")
                    await page.wait_for_timeout(500)

            await get_all_friend_links()

        # close browser
        async def closing_browser():
            await page.wait_for_timeout(3000)
            print("All's well that ends well! Closing browser.")
            await browser.close()

        await closing_browser()


# run script
asyncio.run(main())
