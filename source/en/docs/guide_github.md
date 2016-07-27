# Using GitHub
You need to connect your GitHub account if you want to solve challenge by using GitHub.
Add your GitHub account at social account setting page before you start taking Exam.

## How to solve with GitHub
### Fork challenge
the modal appears when you click "Fork" button.
![イメージ11](images/s11.png)  
Fill out repository name and click "OK" button, then you are going to jump to the generated repository page.
Check "Private Repository" if you do not want to publish the repository.

### Clone repository
![イメージ15](images/s15.png)   
The way to clone is same as GitHub like below

```
$ git clone {GIT_URL}
```
you can hack Challenges with your own environment (editor, server, etc) after clone it!

### Save answer
Save your answer by pushing your branch to remote master.

```
$ git push origin master
```
the answer is saved at same time on codecheck server too.
Please make sure whether the state of challenge became from "In Progress" to "Saved" in exam detail page.

That's it!
