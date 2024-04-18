from selenium import webdriver

driver = webdriver.Chrome()

driver.get("https://magento.softwaretestingboard.com/")

xpaths = {
    "WhatsNew": "//*[@id="ui-id-3"]/span",
    "Women": "//*[@id="ui-id-4"]/span[2]",
    "Men": "//*[@id="ui-id-5"]/span[2]"
    "Gear": "//*[@id="ui-id-6"]/span[2]"
    "Training": "//*[@id="ui-id-7"]/span[2]"
    "Sale": "//*[@id="ui-id-8"]/span"
}

for key, value in xpaths.items():
    try:
        elemento = driver.find_element_by_xpath(value)
        if elemento.is_displayed():
            print(f"La validación para {key} pasó: elemento encontrado en la página.")
        else:
            print(f"La validación para {key} falló: elemento no visible en la página.")
    except:
        print(f"La validación para {key} falló: elemento no encontrado en la página.")

driver.quit()
