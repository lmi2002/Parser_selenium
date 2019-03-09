from selenium.webdriver.chrome import service
from selenium import webdriver


opera_exe_path = r'C:\Users\anokhin\AppData\Local\Programs\Opera\launcher.exe'

opera_driver_exe_path = r'C:\Users\anokhin\PycharmProjects\Parser_site\drivers\operadriver.exe'

port = 6000


capabilities = {
    'operaOptions': {
        'binary': opera_exe_path
    }
}


webdriver_service = service.Service(opera_driver_exe_path)

remote = webdriver.Remote(webdriver_service, capabilities)
