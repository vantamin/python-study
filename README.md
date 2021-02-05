# python-study

python study

## 가상 환경 생성

```bash
$ python3 -m venv python-study
$ cd python-study
$ source bin/activate
(python-study) $ pip freeze > requirements.txt
(python-study) $ python -m pip install -r requirements.txt # 모든 필요한 패키지를 설치
```

[가상 환경 및 패키지](https://docs.python.org/ko/3/tutorial/venv.html)

## Project Initial

```bash
~/javascript-study $ yarn add --dev --exact prettier @prettier/plugin-python
~/javascript-study $ npx mrm lint-staged
```

## Package Install

```bash
~/javascript-study $ git config --local user.name "vantamin"
~/javascript-study $ git config --local user.email "vantablack.min@gmail.com"
~/javascript-study $ yarn install
```

## Sourcetree 실행

```bash
$ open /Applications/Sourcetree.app
```

## Selenium

### 1. Selenium 설치

```bash
(python-study) $ pip install selenium
(python-study) $ pip freeze > requirements.txt
```

[Selenium with Python](https://selenium-python.readthedocs.io/)

### 2. ChromeDriver 다운로드

[ChromeDriver](https://chromedriver.chromium.org/downloads)

## Face Crop

```bash
(python-study) $ pip install autocrop
(python-study) $ pip freeze > requirements.txt
```

[autocrop](https://pypi.org/project/autocrop/)
