# kulms-autodownloader
KULMS Auto file downloader for lazy TAs


## Preparation & Installation

### Create config.py
```python
id = '<id>'
pw = '<password>'
login_url = 'https://kulms.korea.ac.kr/'
base_url = '<viewNeedsGrading page URL>'
file_path = '<file path for saving files>'
```

example of base_url) https://kulms.korea.ac.kr/webapps/gradebook/do/instructor/viewNeedsGrading?course_id=_64035_1&pageIndex=


### Install selenium
```sh
$ sudo apt-get install selenium
```

### Just run crawling.py!
```sh
$ python crawling.py
```
