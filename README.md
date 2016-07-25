# kulms-autodownloader
KULMS Auto file downloader for lazy TAs


## Preparation & Installation

First, you need to make config.py such as below

### config.py
```python
id = '<id>'
pw = '<password>'
login_url = 'https://kulms.korea.ac.kr/'
base_url = '<viewNeedsGrading page URL>'
file_path = '<file path for saving files>'
```

example of base_url) https://kulms.korea.ac.kr/webapps/gradebook/do/instructor/viewNeedsGrading?course_id=_64035_1&page_


### selenium
```sh
$ sudo apt-get install selenium
```

### just run crawling.py!
```sh
$ python crawling.py
```
