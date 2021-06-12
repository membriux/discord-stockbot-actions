from os import EX_UNAVAILABLE
from selenium import webdriver

GOOGLE_CHROME_PATH = '/app/.apt/usr/bin/google_chrome'
CHROMEDRIVER_PATH = '/app/.chromedriver/bin/chromedriver'

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument('--no-sandbox')
chrome_options.binary_location = GOOGLE_CHROME_PATH

insider_buying = "https://finviz.com/screener.ashx?v=111&s=it_latestbuys&f=cap_smallover,sh_avgvol_o750,sh_relvol_o1&ft=4"
squeeze = "https://finviz.com/screener.ashx?v=111&f=sh_relvol_o2,sh_short_o20"
top_gainer = "https://finviz.com/screener.ashx?v=111&s=ta_topgainers&f=cap_smallover,sh_avgvol_o500,sh_relvol_o2"
ma_50 = "https://finviz.com/screener.ashx?v=111&f=sh_opt_option,ta_beta_o2,ta_highlow52w_a50h,ta_sma50_pca&ft=4"
sleepign_monster = "https://finviz.com/screener.ashx?v=111&f=fa_curratio_o2,fa_salesqoq_o5,sh_avgvol_o200,sh_relvol_o1,ta_highlow52w_b0to5h,ta_sma20_pa,ta_sma200_sb50,ta_sma50_sb20&ft=4"
unusual_volume = "https://finviz.com/screener.ashx?v=111&s=ta_unusualvolume&f=cap_smallover,ind_stocksonly,sh_avgvol_o200,sh_relvol_o5,ta_beta_o1,ta_perf_dup&ft=4&o=perfytd"

browser = webdriver.Chrome(executable_path=CHROMEDRIVER_PATH, chrome_options=chrome_options)

browser.get(insider_buying)
links = browser.find_element_by_class_name("screener-link-primary")
print(links)

