from selenium import webdriver
from selenium.webdriver import ActionChains


driver=webdriver.Chrome(executable_path="C:/Users/Admin/Downloads/chromedriver.exe")
driver.get("https://jqueryui.com/droppable/")
framewar=driver.find_element_by_xpath("//iframe[@class='demo-frame']")
driver.switch_to_frame(framewar)
print("Switch to frame")

src_drag=driver.find_element_by_id("draggable")
print("Capturing the source value")

dest_drag=driver.find_element_by_id("droppable")
print("Capture the destination value")

a=ActionChains(driver)
a.drag_and_drop(src_drag,dest_drag).perform()
print("dragged and dropped to the required source")






