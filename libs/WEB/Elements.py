
### GENERIC SUITE INFO
browser = "Chrome"
chrome_file = "chromedriver.exe"
firefox_file = "geckodriver.exe"

browser_title = 'Technical Challenge for CDS'
url = "http://localhost:8080/"
swagger_url = "http://localhost:8080/swagger-ui.html"

### JAR PROCESS
chk_jar_process = "ps -eaf | grep -i OppenheimerProjectDev.jar | head -1 | awk {'print $2'}"

### UPLOAD CSV FILE
browse_file = '//*[contains(text(), "file")]'
browse_upload_file = "//input[@type='file']"
refresh_taxRelief_table = '//*[@id="contents"]/button[1]'
table_header_xpath = '//*[@id="contents"]/div[2]/table/thead/tr/th[1]'  #<th scope="col">NatId</th>


### XPATH FOR DISPENSE
dispense_now_icon = '//*[contains(text(), "Dispense Now")]'
#<a href="dispense" role="button" class="btn btn-danger btn-block" style="font-size: 5em;">Dispense Now</a>
cash_dispensed = '//*[contains(text(), "Cash dispensed")]'

### SYSTEM PATHS
win_utils_path = "\\utils\\"
lnx_utils_path = "/utils/"
