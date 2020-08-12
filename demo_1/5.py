import requests,time
from selenium import  webdriver

a = 'china'
url = 'https://fanyi.baidu.com/translate?aldtype=16047&query=&keyfrom=baidu&smartresult=dict&lang=auto2zh#auto/zh/{}'.format(a)
driver = webdriver.Chrome('C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe')
driver.get(url)
clike_ = driver.find_element_by_xpath('/html/body/div[1]/div[3]/div/div/div[1]/div[2]/div[1]/div[1]/div/div[2]/div[2]').click()
time.sleep(5)

# test_txt = 'china'
# js = 'var txt = document.getElementById("baidu_translate_input"); txt.value="'+test_txt+'";'
#
# driver.execute_script(js)
time.sleep(10)
driver.find_element_by_id('translate-button').click()






data = driver.find_element_by_xpath('/html/body/div[1]/div[3]/div/div/div[1]/div[2]/div[1]/div[2]/div/div/div[1]/p[2]/span').text()
print(data)






