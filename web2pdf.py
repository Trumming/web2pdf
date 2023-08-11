from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import time

def scroll_down_to_botton(scroll_times=4):
    while scroll_times > 0:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
        print("scroll to page end,{}".format(scroll_times))
        time.sleep(5)
        scroll_times = scroll_times - 1

# 设置Chrome浏览器驱动程序路径
# chrome_driver_path = '/usr/bin/chromedriver'
# service = Service(executable_path=chrome_driver_path)
# 启动webdriver服务
webdriver_service = Service(ChromeDriverManager().install())

# 设置Chrome浏览器选项
chrome_options = Options()
# chrome_options.add_argument('--headless')  # 无界面模式
# chrome_options.add_argument('--disable-gpu')  # 无界面模式
# chrome_options.add_argument('--no-sandbox')
# chrome_options.add_argument('--disable-dev-shm-usage')
chrome_options.add_argument('--kiosk-printing')

chrome_options.add_experimental_option('prefs', {
    'download.default_directory': '~/Downloads'
})

# 创建Chrome浏览器实例
driver = webdriver.Chrome(service=webdriver_service,options=chrome_options)

with open('urls.txt', 'r') as file:
    urls = file.readlines()

for url in urls:
    url = url.strip()  # 去除行末的换行符

    # 打开网页
    driver.get(url)
    print("load the url [{}]".format(url))
    # 等待网页加载完成
    time.sleep(1)  # 可根据实际情况调整等待时间
    scroll_down_to_botton()  # 滚动到网页底部
    time.sleep(10)  # 可根据实际情况调整等待时间

    # 生成PDF文件名
    timestamp = time.strftime("%Y%m%d%H%M%S")
    filename = f"{timestamp}.pdf"

    # 调用浏览器的打印功能将网页保存为PDF
    # print_option = {'printBackground': True}
    # driver.execute_cdp_cmd('Page.printToPDF', print_option)
    # with open(filename, 'wb') as pdf_file:
    #     pdf_file.write(driver.page_source.encode('utf-8'))

    driver.execute_script('window.print();')

    time.sleep(10)  # 等待打印完成

    # 将截图转换为PDF
    # pdfkit.from_file('screenshot.png', filename)

    print(f"Saved {url} as {filename}")

# 关闭浏览器
driver.quit()
