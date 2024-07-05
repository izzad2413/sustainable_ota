from playwright.sync_api import Playwright, sync_playwright    # web automation
import pandas as pd                                            # data manipulation & storage
import time                                                     
import random
import os
import re

# Define a function for waiting with retry of a webpage
def wait_for_page_load_with_retry(page, max_retries=20, retry_interval=5, reload_interval=5):
    for retry in range(max_retries):
        page_state = page.evaluate('(document.readyState)')
        if page_state == 'complete':
            return  # Page has fully loaded
        else:
            print(f"Page is not fully loaded. Retrying in {retry_interval} seconds======>Retrying Attempt {retry + 1}/{max_retries}")
            time.sleep(retry_interval)  # Sleep for a specified interval before retrying

        # Check if it's time to reload the page (every 5 attempts)
        if (retry + 1) % 5 == 0:
            print(f"Reloading page after {retry + 1} attempts...")
            page.reload()
            time.sleep(reload_interval)

    raise Exception(f"Page is not fully loaded after {max_retries} retries.")

# creating the web scraping function
def main():
    # list to store scraped data
    scraped_data = [] 
    
    with sync_playwright() as p:
        
        page_url = 'url'
        city_name = page_url.split('ss=')[1].split('%2C')[0] # getting the city name from page_url

        # open chrome browser
        print('===[Connecting]===')
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()

        # chrome browser to navigate to the page
        page.set_extra_http_headers({"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"})
        page.goto(page_url, timeout=60000)

        # to scrape the total number of pages defined
        for page_num in range(1,51): # defining the number of pages needed to scrape # default at 50 pages
            print(f"Scraping================================================>page {page_num}")

            # wait for a while
            time.sleep(random.uniform(5,7))

            # Check if the pop-up exists and dismiss it if present
            try:
                dismiss_button = page.query_selector('button[aria-label="Dismiss sign in information."]')
                dismiss_button.click()
                time.sleep(2)  # Wait for the pop-up to be dismissed
                print('===[Close popup]===')
            except:
                pass
                print('===[No popup]===')

            # path at the overview section
            properties_path = 'div[data-testid="property-card"]'
            title_path = 'a[data-testid="title-link"]' 
            availability_path = 'a[data-testid="availability-cta-btn"]'

            # to count the number of hotels available that can be scraped at the current webpage
            properties = page.locator(properties_path).all()
            print(f'There are: {len(properties)} properties listed.')
            print('===>Begin Scraping<===')

            for property in properties:
                # click each property at the listed property
                # it will open a new tab
                with page.expect_popup(timeout=90000) as popup_info:
                    page.wait_for_selector(availability_path, state='visible', timeout=90000)
                    property.locator(availability_path).click(timeout=90000)
                property = popup_info.value

                if "Expected Popup Title" not in property.title():
                # Handle unexpected popup here or raise an error
                     pass
                time.sleep(8)
                wait_for_page_load_with_retry(property) # to wait for the webpage to be fully loaded

                # identified path
                name_path = 'h2.pp-header__title'
                address_path = '[data-node_tt_id="location_score_tooltip"]'
                coordinate_path = 'a#hotel_address[data-atlas-latlng]'
                star_rating_path = '//*[@data-testid="rating-stars"]//span[@class="fcd9eec8fb d31eda6efc c25361c37f"]'
                quality_rating_path = '//*[@data-testid="rating-squares"]//span[@class="fcd9eec8fb d31eda6efc c25361c37f"]'
                preferred_partner_path = '//div[@data-tooltip-text]'
                preferred_plus_partner_path = 'img.pp-icon-valign--initial[data-tooltip-text]'
                uploaded_pics_path = 'span.bh-photo-grid-thumb-more-inner-2'
                description_path = 'div[data-capla-component-boundary="b-property-web-property-page/PropertyDescriptionDesktop"] > p'
                count_room_types_path = '//span[@class="hprt-roomtype-icon-link "]'
                prices_range_path = 'span.prco-valign-middle-helper'
                overall_reviews_path = '(//div[@class="a3b8729ab1 d86cee9b25"])[last()]'
                count_reviews_path = 'span.a3b8729ab1.f45d8e4c32.d935416c47'
                review_titles_path = '//div[@data-testid="PropertyReviewsRegionBlock"]//span[@class="d6d4671780"]'
                review_scores_path = '//div[@data-testid="PropertyReviewsRegionBlock"]//div[@class="ccb65902b2 efcd70b4c4"]'
                score_status_path = '(//div[@class="abf093bdfe ae7544114a"])[last()]'
                host_score_review_path = '//span[@data-testid="host-review-score"]'
                host_count_reviews_path = '//span[@class="a53cbfa6de f45d8e4c32"]'
                count_qna_path = '//span[contains(text(), "See other questions")]'
                count_reviewer_by_cat_path = '(//ul[@class="bui-dropdown-menu__items"])[1]/li'
                count_reviewer_by_scores_path = '(//ul[@class="bui-dropdown-menu__items"])[2]/li'
                count_reviewer_by_lan_path = '(//ul[@class="bui-dropdown-menu__items"])[3]/li'
                count_landmarks_path = '(//ul[@data-location-block-list="true"])[1]/li'
                count_topattractions_path = '(//ul[@data-location-block-list="true"])[3]/li'
                count_publictransport_path = '(//ul[@data-location-block-list="true"])[4]/li'
                count_closestairports_path = '(//ul[@data-location-block-list="true"])[5]/li'
                count_restaurantscafes_path = '(//ul[@data-location-block-list="true"])[2]/li'
                all_landmarks_distances_path = '(//ul[@data-location-block-list="true"])[1]//div[@class="a53cbfa6de f45d8e4c32"]'
                all_topattractions_distances_path = '(//ul[@data-location-block-list="true"])[3]//div[@class="a53cbfa6de f45d8e4c32"]'
                all_publictransport_distances_path = '(//ul[@data-location-block-list="true"])[4]//div[@class="a53cbfa6de f45d8e4c32"]'
                all_closestairports_distances_path = '(//ul[@data-location-block-list="true"])[5]//div[@class="a53cbfa6de f45d8e4c32"]'
                all_restaurantscafes_distances_path = '(//ul[@data-location-block-list="true"])[2]//div[@class="a53cbfa6de f45d8e4c32"]'
                facilities_path = 'div.e50d7535fa div.a432050e3a'
                sub_facilities_path = '//div[@data-testid="property-section--content" and contains(@class, "a53cbfa6de")]//div[@class="e50d7535fa"]//span[@class="db312485ba"]'
                sustainable_level_path = 'span.abf093bdfe.d068504c75.be09c104ad'
                sustainable_steps_open_1_button_path = '//button[contains(., "See all steps")]' # 'See all steps' button link
                sustainable_steps_open_2_button_path = '//div[@data-testid="sustainability-banner-container"]//button[contains(., "Learn more")]' # 'Learn more' button link
                sustainable_steps_close_1_button_path = '//button[@class="a83ed08757 c21c56c305 a4c1805887 f671049264 deab83296e c082d89982 d268b35b0b"]'
                sustainable_steps_close_2_button_path = '//button[@class="a83ed08757 c21c56c305 f38b6daa18 d691166b09 ab98298258 deab83296e f4552b6561"]'
                sustainable_steps_title_path = '//div[@class="d20c7d4f05"]//span[@class="a51f4b5adb"]'
                sustainable_steps_taken_path = '//div[@class="d20c7d4f05"]//li/div'


                # create a dictionary with default values
                scraped_dict = {
                    'name':'',
                    'address':'',
                    'coordinate':'',
                    'star_rating':'',
                    'quality_rating':'',
                    'preferred_partner':'',
                    'count_uploaded_pics':'',
                    'description':'',
                    'count_room_types':'',
                    'prices_range':'',
                    'overall_reviews':'',
                    'count_reviews':'',
                    'review_titles':'',
                    'review_overall_scores':'',
                    'score_status':'',
                    'host_score_review':'',
                    'host_count_reviews':'',
                    'count_qna':'',
                    'count_reviewer_by_cat':'',
                    'count_reviewer_by_scores':'',
                    'count_reviewer_by_lan':'',
                    'count_landmarks':'',
                    'count_topattractions':'',
                    'count_publictransport':'',
                    'count_closestairports':'',
                    'count_restaurantscafes':'',
                    'all_landmarks_distances':'',
                    'all_topattractions_distances':'',
                    'all_publictransports_distances':'',
                    'all_closestairports_distances':'',
                    'all_restaurantscafes_distances':'',
                    'count_facilities':'',
                    'count_sub_facilities':'',
                    'facilities':'',
                    'sub_facilities':'',
                    'count_sustainable_steps_title':'',
                    'sustainable_steps_title':'',
                    'count_sustainable_steps_taken':'',
                    'sustainable_steps_taken':'',
                    'sustainable_level':''
                }

                # extracting data, if path existed return data else null
                name = property.locator(name_path).all()
                if name:
                    scraped_dict['name'] = name[0].inner_text()
                else:
                    scraped_dict['name'] = ''

                address = property.locator(address_path).all()
                if address:
                    scraped_dict['address'] = address[0].inner_text()
                else:
                    scraped_dict['address'] = ''

                coordinate = property.locator(coordinate_path).all()
                if coordinate:
                    scraped_dict['coordinate'] = coordinate[0].get_attribute('data-atlas-latlng')
                else:
                    scraped_dict['coordinate'] = ''

                star_rating = property.query_selector_all(star_rating_path)
                if star_rating:
                    scraped_dict['star_rating'] = len(star_rating)
                else:
                    scraped_dict['star_rating'] = ''

                quality_rating = property.query_selector_all(quality_rating_path)
                if quality_rating:
                    scraped_dict['quality_rating'] = len(quality_rating)
                else:
                    scraped_dict['quality_rating'] = ''

                preferred_partner = property.locator(preferred_partner_path).all()
                preferred_plus_partner = property.locator(preferred_plus_partner_path).all()
                if preferred_partner or preferred_plus_partner:
                    scraped_dict['preferred_partner'] = 1
                else:
                    scraped_dict['preferred_partner'] = 0

                count_uploaded_pics = property.query_selector_all(uploaded_pics_path)
                if count_uploaded_pics:
                    scraped_dict['count_uploaded_pics'] = int(count_uploaded_pics[0].inner_text().split()[0])
                else:
                    scraped_dict['count_uploaded_pics'] = ''

                description = property.query_selector_all(description_path)
                if description:
                    scraped_dict['description'] = ''.join(description[0].inner_text().split('\n'))
                else:
                    scraped_dict['description'] = ''

                count_room_types = property.query_selector_all(count_room_types_path)
                if count_room_types:
                    scraped_dict['count_room_types'] = len(count_room_types)
                else:
                    scraped_dict['count_room_types'] = ''

                prices_range = property.query_selector_all(prices_range_path)
                if prices_range:
                    scraped_dict['prices_range'] = ', '.join([element.inner_text().strip().replace('\n', '').replace('MYR', '').strip() for element in prices_range])
                else:
                    scraped_dict['prices_range'] = ''

                time.sleep(random.uniform(3,5))

                overall_reviews = property.query_selector_all(overall_reviews_path)
                if overall_reviews:
                    scraped_dict['overall_reviews'] = float(overall_reviews[0].inner_text())
                else:
                    scraped_dict['overall_reviews'] = ''

                count_reviews = property.query_selector_all(count_reviews_path)
                if count_reviews:
                    count_reviews_num = re.search(r'\d+', count_reviews[0].inner_text())
                    if count_reviews_num:
                        scraped_dict['count_reviews'] = int(count_reviews_num.group())
                    else:
                        scraped_dict['count_reviews'] = ''
                else:
                    scraped_dict['count_reviews'] = ''

                review_titles = property.query_selector_all(review_titles_path)
                if review_titles:
                    scraped_dict['review_titles'] = ', '.join([element.inner_text() for element in  review_titles])
                else:
                    scraped_dict['review_titles'] = ''

                review_scores = property.query_selector_all(review_scores_path)
                if review_scores:
                    scraped_dict['review_overall_scores'] = ', '.join([element.inner_text() for element in  review_scores])
                else:
                    scraped_dict['review_overall_scores'] = ''

                score_status = property.query_selector_all(score_status_path)
                if score_status:
                    scraped_dict['score_status'] = score_status[0].inner_text()
                else:
                    scraped_dict['score_status'] = ''

                host_score_review = property.query_selector_all(host_score_review_path)
                if host_score_review:
                    host_score_review_num = re.search(r'\d+\.\d+', host_score_review[0].inner_text())
                    if host_score_review_num:
                        scraped_dict['host_score_review'] = float(host_score_review_num.group())
                    else:
                        scraped_dict['host_score_review'] = ''
                else:
                    scraped_dict['host_score_review'] = ''

                host_count_reviews = property.query_selector_all(host_count_reviews_path)
                if host_count_reviews:
                    scraped_dict['host_count_reviews'] = host_count_reviews[0].inner_text()
                else:
                    scraped_dict['host_count_reviews'] = ''

                count_qna = property.query_selector_all(count_qna_path)
                if count_qna:
                    scraped_dict['count_qna'] = count_qna[0].inner_text()
                else:
                    scraped_dict['count_qna'] = ''

                count_reviewer_by_cat = property.query_selector_all(count_reviewer_by_cat_path)
                if count_reviewer_by_cat:
                    scraped_dict['count_reviewer_by_cat'] = ', '.join([element.inner_text().strip() for element in count_reviewer_by_cat])
                else:
                    scraped_dict['count_reviewer_by_cat'] = ''

                count_reviewer_by_scores = property.query_selector_all(count_reviewer_by_scores_path)
                if count_reviewer_by_scores:
                    scraped_dict['count_reviewer_by_scores'] = ', '.join([element.inner_text().strip() for element in count_reviewer_by_scores])
                else:
                    scraped_dict['count_reviewer_by_scores'] = ''

                count_reviewer_by_lan = property.query_selector_all(count_reviewer_by_lan_path)
                if count_reviewer_by_lan:
                    scraped_dict['count_reviewer_by_lan'] = ', '.join([element.inner_text().strip() for element in count_reviewer_by_lan])
                else:
                    scraped_dict['count_reviewer_by_lan'] = ''

                time.sleep(random.uniform(3,5))

                count_landmarks = property.query_selector_all(count_landmarks_path)
                if count_landmarks:
                    scraped_dict['count_landmarks'] = len(count_landmarks)
                else:
                    scraped_dict['count_landmarks'] = ''

                count_topattractions = property.query_selector_all(count_topattractions_path)
                if count_topattractions:
                    scraped_dict['count_topattractions'] = len(count_topattractions)
                else:
                    scraped_dict['count_topattractions'] = ''

                count_publictransport = property.query_selector_all(count_publictransport_path)
                if count_publictransport:
                    scraped_dict['count_publictransport'] = len(count_publictransport)
                else:
                    scraped_dict['count_publictransport'] = ''

                count_closestairports = property.query_selector_all(count_closestairports_path)
                if count_closestairports:
                    scraped_dict['count_closestairports'] = len(count_closestairports)
                else:
                    scraped_dict['count_closestairports'] = ''

                count_restaurantscafes = property.query_selector_all(count_restaurantscafes_path)
                if count_restaurantscafes:
                    scraped_dict['count_restaurantscafes'] = len(count_restaurantscafes)
                else:
                    scraped_dict['count_restaurantscafes'] = ''

                all_landmarks_distances = property.query_selector_all(all_landmarks_distances_path)
                if all_landmarks_distances:
                    scraped_dict['all_landmarks_distances'] = ', '.join([element.inner_text().strip() for element in all_landmarks_distances])
                else:
                    scraped_dict['all_landmarks_distances'] = ''
                
                all_topattractions_distances = property.query_selector_all(all_topattractions_distances_path)
                if all_topattractions_distances:
                    scraped_dict['all_topattractions_distances'] = ', '.join([element.inner_text().strip() for element in all_topattractions_distances])
                else:
                    scraped_dict['all_topattractions_distances'] = ''

                all_publictransport_distances = property.query_selector_all(all_publictransport_distances_path)
                if all_publictransport_distances:
                    scraped_dict['all_publictransports_distances'] = ', '.join([element.inner_text().strip() for element in all_publictransport_distances])
                else:
                    scraped_dict['all_publictransports_distances'] = ''

                all_closestairports_distances = property.query_selector_all(all_closestairports_distances_path)
                if all_closestairports_distances:
                    scraped_dict['all_closestairports_distances'] = ', '.join([element.inner_text().strip() for element in all_closestairports_distances])
                else:
                    scraped_dict['all_closestairports_distances'] = ''

                all_restaurantscafes_distances = property.query_selector_all(all_restaurantscafes_distances_path)
                if all_restaurantscafes_distances:
                    scraped_dict['all_restaurantscafes_distances'] = ', '.join([element.inner_text().strip() for element in all_restaurantscafes_distances])
                else:
                    scraped_dict['all_restaurantscafes_distances'] = ''

                count_facilities = property.query_selector_all(facilities_path)
                if count_facilities:
                    scraped_dict['count_facilities'] = len(count_facilities)
                else:
                    scraped_dict['count_facilities'] = ''

                count_sub_facilities = property.query_selector_all(sub_facilities_path)
                if count_sub_facilities:
                    scraped_dict['count_sub_facilities'] = len(count_sub_facilities)
                else:
                    scraped_dict['count_sub_facilities'] = ''

                facilities = property.query_selector_all(facilities_path)
                if facilities:
                    scraped_dict['facilities'] = ', '.join([element.inner_text().strip() for element in facilities])
                else:
                    scraped_dict['facilities'] = ''

                sub_facilities = property.query_selector_all(sub_facilities_path)
                if sub_facilities:
                    scraped_dict['sub_facilities'] = ', '.join([element.inner_text().strip() for element in sub_facilities])
                else:
                    scraped_dict['sub_facilities'] = ''

                # if the page contains sustainable information
                if property.locator(sustainable_steps_open_1_button_path).is_visible():
                    property.locator(sustainable_steps_open_1_button_path).click()
                    property.wait_for_selector(sustainable_steps_title_path, timeout=90000)
                    if property.wait_for_selector(sustainable_steps_title_path, timeout=3000):
                        sustainable_steps_title_elements = property.query_selector_all(sustainable_steps_title_path)
                        scraped_dict['count_sustainable_steps_title'] = len(sustainable_steps_title_elements)
                        scraped_dict['sustainable_steps_title'] = ', '.join([element.inner_text() for element in sustainable_steps_title_elements])

                        sustainable_steps_title_taken_elements = property.query_selector_all(sustainable_steps_taken_path)
                        scraped_dict['count_sustainable_steps_taken'] = len(sustainable_steps_title_taken_elements)
                        scraped_dict['sustainable_steps_taken'] = ', '.join([element.inner_text() for element in  sustainable_steps_title_taken_elements])

                        if property.locator(sustainable_steps_close_1_button_path).is_visible():
                            property.locator(sustainable_steps_close_1_button_path).click(timeout=30000)
                        else:
                            property.locator(sustainable_steps_close_2_button_path).click(timeout=30000)
                        time.sleep(random.uniform(3,5))
                        
                elif property.locator(sustainable_steps_open_2_button_path).is_visible():
                    property.locator(sustainable_steps_open_2_button_path).click()
                    property.wait_for_selector(sustainable_steps_title_path, timeout=90000)
                    if property.wait_for_selector(sustainable_steps_title_path, timeout=3000):
                        sustainable_steps_title_elements = property.query_selector_all(sustainable_steps_title_path)
                        scraped_dict['count_sustainable_steps_title'] = len(sustainable_steps_title_elements)
                        scraped_dict['sustainable_steps_title'] = ', '.join([element.inner_text() for element in sustainable_steps_title_elements])

                        sustainable_steps_title_taken_elements = property.query_selector_all(sustainable_steps_taken_path)
                        scraped_dict['count_sustainable_steps_taken'] = len(sustainable_steps_title_taken_elements)
                        scraped_dict['sustainable_steps_taken'] = ', '.join([element.inner_text() for element in  sustainable_steps_title_taken_elements])

                        if property.locator(sustainable_steps_close_1_button_path).is_visible():
                            property.locator(sustainable_steps_close_1_button_path).click(timeout=30000)
                        else:
                            property.locator(sustainable_steps_close_2_button_path).click(timeout=30000)
                        time.sleep(random.uniform(3,5))
                    
                else:
                    scraped_dict['count_sustainable_steps_title'] = ''
                    scraped_dict['sustainable_steps_title'] = ''
                    scraped_dict['count_sustainable_steps_taken'] = ''
                    scraped_dict['sustainable_steps_taken'] = ''

                sustainable_level = property.query_selector_all(sustainable_level_path)
                if sustainable_level:
                    scraped_dict['sustainable_level'] = sustainable_level[0].inner_text()
                else:
                    scraped_dict['sustainable_level'] = ''

                # listed data move into the define dictionary
                scraped_data.append(scraped_dict)

                # Calculate the numerator (total len features that were able to be scraped)
                scraped_count = sum(1 for value in scraped_dict.values() if value)

                # Calculate the denominator (total len features that needed to be scraped)
                total_count = len(scraped_dict)

                # To check scraped status
                print(f':::>Scraped status: {scraped_count}/{total_count}')
                time.sleep(random.uniform(5,8))

                # Get all open tabs/pages in the current context
                all_pages = context.pages

                # Check if there is a new tab (property link open a new tab)
                if len(all_pages) > 1:
                    # Switch to the new tab
                    new_tab = all_pages[-1]  # Assuming the new tab is the last one in the list

                    # Close the new tab
                    new_tab.close()

                    # Return to the main page (switch back to the first tab)
                    context.pages[0].bring_to_front()

            # Moving to the next page
            time.sleep(3)
            # locate the next page button
            next_button_path = 'div.b16a89683f.cab1524053 button[aria-label="Next page"]'
            
            page.wait_for_selector(next_button_path, timeout=90000)
            next_page = page.query_selector(next_button_path)
            if next_page and next_page.is_enabled(): # check if the button is clickable
                next_page.click()
            else:
                print('===[No "Next page" button found. Exiting scraping]===')
                break

            # Delay web scraping process to avoid being blocked by website admin
            time.sleep(random.uniform(5,8))

            # Wait for the page to load
            page.wait_for_load_state('networkidle', timeout=180000) 

        print('===[Scraping Succesful]===')
        browser.close()

    # Convert scraped data to a pandas DataFrame
    df = pd.DataFrame(scraped_data)

    # Define path to save data
    save_directory = './../data/raw'

    # Create the directory if it doesn't exist
    os.makedirs(save_directory, exist_ok=True)

    # Initialize a counter
    counter = 1

    # Construct the initial file name
    base_file_name = city_name

    # Check if the file already exists, and if it does, increment the counter
    while os.path.exists(os.path.join(save_directory, f'{base_file_name}.csv')):
        counter += 1
        base_file_name = f'{city_name}_{counter}'

    # Save the DataFrame as a CSV file in the specified path
    csv_file_path = os.path.join(save_directory, f'{base_file_name}.csv')
    df.to_csv(csv_file_path, index=False)
    print(f'Scraped data saved to: {csv_file_path}')

# Checks whether the current module is being executed as the main program           
if __name__ == '__main__':
    main()