# flake8: noqa
import yaml
import asyncio
from playwright.async_api import async_playwright, Page, Browser

with open('config.yaml', 'r') as config_file:
    config = yaml.load(config_file, Loader=yaml.FullLoader)
    
BASE_URL = config['BASE_URL']
EMAIL = config['EMAIL']
PASS = config['PASS']
FRIEND_URL = config['FRIEND_URL'][0]
FRIEND_MSG = config['FRIEND_MSG']

# open goodreads sign in page
async def open_goodreads(page: Page):
    # go to sign in page
    await page.goto(BASE_URL)

    await page.wait_for_load_state("networkidle")

    # click sign in button
    await page.get_by_text("Sign in with email").click()
    await page.wait_for_load_state("networkidle")
    
# perform sign in
async def perform_sign_in(page: Page):
    await page.locator('input[type="email"]').type(EMAIL)
    await page.locator('input[type="password"]').type(PASS)
    await page.click("input#signInSubmit")
    await page.wait_for_load_state("networkidle")
    
# go to friend list url
async def open_friend_list(page: Page):
    await page.wait_for_timeout(4000)
    print("friend url: ", FRIEND_URL)
    await page.goto(FRIEND_URL)         
# confirm friend page logic
async def confirm_friend(page: Page):
    print("confirm friend page opened! Send the default friend message.")
    # add FRIEND_MESSAGE to the text area
    await page.locator('textarea[name="message"]').fill(FRIEND_MSG)
    # click Add Friend button
    await page.locator('input[value="Add as a Friend"]').click()
    # wait for page to load
    await page.wait_for_load_state("networkidle")

# get all friend links
async def get_all_friend_links(page: Page):
    # get all selectors for a page
    links = await page.query_selector_all(
        'xpath=//a[text()="Add as a Friend"]'
    )
    print("total friends to add: ", len(links))

    # create a for loop to click each Add Friend button
    for link in links:
        await link.click()
        await page.wait_for_load_state("networkidle")
        print("current url is: ", page.url)
        
        # check url for /confirm_friend/ page. If url contains /add_as_friend/user_id then run confirm_friend()
        # if directed to confirm friend page, then run confirm_friend()
        if "add_as_friend" in page.url:
            print("URL contains add_as_friend")
            await page.wait_for_load_state("networkidle")
            await confirm_friend()
        else :
            print("URL does not contain add_as_friend")
        
        print("friend added!")
        await page.wait_for_timeout(500)  

# close browser
async def closing_browser(page: Page, browser: Browser):
    await page.wait_for_timeout(3000)
    print("All's well that ends well! Closing browser.")
    await browser.close()
                  
# main function
async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False, args=["--start-maximized"])
        context = await browser.new_context(no_viewport=True)
        page = await context.new_page()

        await open_goodreads(page)
        await perform_sign_in(page)
        await open_friend_list(page)
        await get_all_friend_links(page)                       
        await closing_browser(page, browser)

# Run the script
asyncio.run(main())
