#### Clone repository
```sh
$ git clone https://github.com/dmitrysonder/AB.git
```
#### Install packages
```sh
$ pip install requirements.txt
```
#### Install allure cli
Debian:
```sh
$ sudo apt-add-repository ppa:yandex-qatools/allure-framework
$ sudo apt-get update 
$ sudo apt-get install allure-commandline
```
Mac OS:
```sh
$ brew tap qatools/formulas 
$ brew install allure-commandline
```
#### Start testing
Start pytest:
```sh
$ py.test --alluredir [path to allure report directory]
```
Generate html report:
```sh
$ allure generate [path to allure report directory]
```