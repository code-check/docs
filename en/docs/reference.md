# How to use ChallengeViewer
See [Japanese version](challenge-viewer_ja.md)

## <a name="section1"> 1. How to use ChallengeViewer
### 1-1. Edit files
#### Type of files
![イメージ10](images/s10.png)  
You can see file tree on the left side of ChallengeViewer.  
And you can make sure which file is editable or not by seeing the type of file icon.  
Please follow challenge sentence and edit file which is supposed to be edited.

### 1-2. ChallengeViewer Settings
![イメージ9](images/s9.png)  

You can edit the settings of ChallengeViewer.
Click setting icon if you want to edit below settings:
* Color theme
* Tab key action
* Auto Preview
* Save Dialog


### 1-3. Run,Preview
#### Run test
You can run the test by clicking the run button at lower right side of ChallengeViewer.
- About test code
  - codecheck support to test by using test framework as like an Unit test.
  - "test" means not Exam or challenge but test code to verify whether program is correct or not.
  - applicants can try to run public test code.

#### Preview
Preview feature support applicants to see html view an application configured with HTML, CSS, and Javascript.  
you can see latest html view automatically without reload ChallengeViewer when the Auto Preview setting is checked.

### 1-4. How to save challenge
To click "SAVE" button to save files you edited  
![イメージ13](images/s13.png)  
Choose file which you want to save and click "OK" button to save files.

## <a name="section2"> 2. How to solve by using GitHub
You need to connect your GitHub account if you want to solve challenge by using GitHub.
Add your GitHub account at social account setting page before you start taking Exam.

### 2-1. How to solve with GitHub
#### Fork challenge
the modal appeirs when you click "Fork" button.
![イメージ11](images/s11.png)  
Fill out repository name and click "OK" button, then you are going to jump to the generated repository page.
Check "Private Repository" if you do not want to publish the repository.

#### Clone repository
![イメージ15](images/s15.png)   
The way to clone is same as GitHub like below

```
$ git clone {GIT_URL}
```
you can hack Challenges with your own environment (editor, server, etc) after clone it!

### 2-2. Save answer
Save your ansewr by pushing your bransh to remote master.

```
$ git push origin master
```
the answer is saved at same time on codecheck server too.
Please make sure whether the state of challenge became from "Inprogress" to "Saved" in exam detail page.

That's it!

## 3. Recommend Browser
Please choose mordan browser which is compatible with HTML5,CSS3, and Websocket.
Our recommend Browser is Google Chrome.

# contents list

## Category
### 1. Algorithm Challenge
* Languages: C,C++,C#,Java,Javascript,Scala,PHP,Perl,Python,Ruby,Go,Haskell,Groovy
* contents:FizzBuzz,Primary,etc.

### 2. Frameworks Challenge

|Language|Frameworks|
|---|---|
|Ruby|RubyOnRails,Sinatra|
|PHP|CakePHP,Larval,Wordpress|
|Python|django|
|Java|PlayFramework,Spring|
|Scala|PlayFramework|
|Javascript|Express,SailsJS,JQuery,Bootstrap,AnglarJS,ReactJS|
|SQL|SQLite|

### 3. APIs(Server) Challenge
### 4. HTML(Frontend) Challenge
### 5. Markdown Challenge
### 6. Mobile Challenge
* Cordova
* Android

### 7. Game Challenge
* Unity
* cocos2dx

|difficulty|Algorithms|Frameworks|APIs(Server)|HTML(Frontend)|Markdown|Mobile|Game|
|:-:|---|---|---|---|---|---|---|
|Very Hard|[Sudoku][sudoku]<br />[Rijndael][rijndael]|[EntityFramework][entity-framework]|[Event Application][eventapp]<br />[Login API][login-api]|||||
|Hard||||||||
|Normal|[Sudoku][sudoku-medium]<br />[Rijndael][rijndael-medium]|||||||
|Easy|[Sudoku][sudoku-easy]<br>[array(C#)][arrays]<br />[ROT13][rot13]||[SQL][sql]|||||
|Very Easy|[Fizzbuzz][fizzbuzz]<br />[Binary ToString][binary-tostring]||||||||

[fizzbuzz]: https://github.com/code-check/fizzbuzz
[sql]: https://github.com/code-check/challenge-sql
[arrays]: https://github.com/code-check/challenge-arrays
[eventapp]: https://github.com/code-check/challenge-eventapp
[login-api]: https://github.com/code-check/challenge-login-api
[entity-framework]: https://github.com/code-check/challenge-entity-framework
[sudoku-easy]: https://github.com/code-check/challenge-sudoku-easy
[sudoku-medium]: https://github.com/code-check/challenge-sudoku-medium
[sudoku]: https://github.com/code-check/challenge-sudoku
[rijndael-medium]: https://github.com/code-check/challenge-rijndael-medium
[rijndael]: https://github.com/code-check/challenge-rijndael
[binary-tostring]: https://github.com/code-check/challenge-binary-tostring
[rot13]: https://github.com/code-check/challenge-rot13


# Access Rights

||Owner|Admin|Regular|Supporter|
|---|:-:|:-:|:-:|:-:|
|See applicants,answer|◯|◯|◯|◯|
|Judge answer|◯|◯|◯|◯|
|Create Challenge|◯|◯|◯|◯|
|Modify Organization Challenge|◯|◯|◯|-|
|Create Exam|◯|◯|◯|-|
|Invite,Remove member|◯|◯|-|-|
|Change member's role|◯|◯|-|-|
|Edit company profile|◯|◯|-|-|
